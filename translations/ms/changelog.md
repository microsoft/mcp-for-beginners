# Changelog: Kurikulum MCP untuk Pemula

Dokumen ini berfungsi sebagai rekod semua perubahan penting yang dibuat pada kurikulum Model Context Protocol (MCP) untuk Pemula. Perubahan didokumentasikan dalam susunan kronologi terbalik (perubahan terbaru dahulu).

## 9 September, 2026

### Penyelarasan Spesifikasi Akhir MCP 2026-07-28

Dikemaskini kurikulum Inggeris dari panduan calon pelepasan dan `2025-11-25`
garis dasar kepada spesifikasi MCP akhir `2026-07-28`.

- **Dikemaskini**: Rujukan versi semasa, pautan spesifikasi, panduan permintaan tanpa status,
  `server/discover`, pengepala HTTP Boleh alir, dan kitar hayat peluasan Tugas
  merentas 38 fail dokumentasi Inggeris.
- **Dibetulkan**: Elicitation kini menggunakan `elicitation/create`, Sampling menggunakan
  `sampling/createMessage`, dan `InputRequiredResult.resultType` menggunakan
  `"input_required"`.
- **Digantikan**: Pelajaran keadaan-perbualan Root Context yang tidak tepat dengan
  pelajaran Roots yang tepat protokol merangkumi petunjuk sistem fail informatif, aliran
  pelbagai perjalanan pusingan semasa, sempadan keselamatan, dan pilihan migrasi.
- **Dijelaskan**: Roots, Sampling, Logging, dan Pendaftaran Klien Dinamik adalah
  usang dalam `2026-07-28`, dengan penggantian yang disyorkan dan tarikh
  penghapusan awal didokumentasikan.
- **Dilabelkan**: Sampel yang masih bergantung pada MCP `2025-11-25`, HTTP+SSE,
  jabat tangan inisialisasi, atau sesi protokol dikekalkan sebagai contoh
  keserasian warisan dan bukan sebagai pelaksanaan semasa.
- **Panduan keselamatan**: Dikemaskini panduan keselamatan berdiri sendiri untuk menggunakan
  kebenaran setiap permintaan dan pemegang status aplikasi yang jelas dan bukannya
  ID sesi protokol yang dihapuskan. Dokumen Meta Data ID Klien kini menjadi
  jalan pendaftaran pilihan, dengan DCR didokumentasikan sebagai keserasian sahaja.
- **Bahan sokongan**: Dikemaskini panduan belajar, senarai semak penyumbang,
  kajian kes Publora, dan kajian kes APIM. Jalan pandu APIM kini mengesyorkan
  titik akhir HTTP Boleh alir `/mcp` semasa dan bukannya `/sse` yang usang.
- **Pautan kanonik**: Menggantikan URL spesifikasi yang sudah bersara dan draf dalam
  sumber Markdown bahasa Inggeris dengan pautan berjenama versi `2026-07-28`,
  sambil mengekalkan pautan jelas ke versi lama di mana sampel masih terikat pada alat lama.
- **Nama fail stabil**: Menamakan semula panduan spesifikasi akhir dan dua panduan
  keselamatan untuk mengalih keluar calon keluaran dan akhiran tahun,
  kemudian mengemas kini semua pautan Inggeris ke laluan stabil mereka.
- **Sampel kebenaran baharu**: Menambah
  [pelayan sumber TypeScript MCP `2026-07-28`](./02-Security/samples/cimd-dcr-auth/README.md)
  yang diuji yang membandingkan Dokumen Meta Data ID Klien pilihan dengan pendaftaran
  Klien Dinamik usang sebagai pelengkap. Sampel termasuk penemuan RFC 9728,
  pengesahan JWKS, skop untuk alat, dua belas ujian, dan panduan penyediaan Auth0.
- **Skop terjemahan**: Hanya fail sumber bahasa Inggeris yang disunting; terjemahan
  terhasil dan imej terjemahan kekal tidak berubah kerana ini diterjemah secara automatik.

## 29 Julai, 2026

### Modul Pendamping Baru 08: Sidecar Kebolehpercayaan dan Cubaan Semula Selamat

Menambah pelajaran pendamping neutral vendor untuk alat MCP yang mencipta kesan dunia sebenar,
selaras dengan spesifikasi akhir `2026-07-28`.

- **Baru**: [pelajaran pendamping sidecar kebolehpercayaan][reliability-sidecar]
  menggunakan satu cerita tiket sokongan, dua rajah Mermaid, dan aliran keputusan
  cubaan semula untuk menerangkan kekunci operasi stabil, kemasukan pendua atomik,
  penyelarasan, bukti, dan sempadan peluasan Tugas.
- **Baru**: Latihan suntikan kegagalan Python dan SQLite perpustakaan standard
  menggunakan stor operasi dan tiket berasingan untuk menunjukkan respons yang hilang
  selepas kesan luaran disahihkan. Enam ujian deterministik merangkumi penduaan naif,
  pemulihan semula dilindungi, konflik muatan, keputusan di-cache,
  tuntutan aktif, dan kemasukan pendua serentak.
- **Dikemaskini**: Modul 08 kini memautkan pelajaran pendamping, mengenal pasti model
  permintaan tanpa status `2026-07-28` akhir, membezakan pemerhatian OpenTelemetry
  daripada ciri log MCP yang usang, dan mengehadkan contoh cubaan semula generik kepada operasi
  hanya baca.
- **Pilihan**: Pelajaran memetakan konsep mudah alihnya ke satu pelaksanaan komuniti berlabel tanpa
  menjadikan perkhidmatan hos atau panggilan rangkaian sebahagian daripada
  latihan.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 Julai, 2026

### Pelajaran Baru: Calon Pelepasan Spesifikasi MCP 2026-07-28

Menambah liputan calon pelepasan spesifikasi MCP `2026-07-28` yang akan datang (diisytiharkan pada 21 Mei, 2026; pelepasan akhir dijadualkan pada 28 Julai, 2026), diringkaskan daripada [catatan blog pengumuman rasmi](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Garis dasar kurikulum kekal sebagai **Spesifikasi MCP 2025-11-25** sehingga versi baru dihantar, jadi ia dipersembahkan sebagai panduan ke hadapan dan bukan penulisan semula pelajaran sedia ada.

- **Baru**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — satu pelajaran penuh merangkumi protokol teras tanpa status (penghapusan jabat tangan `initialize` dan `Mcp-Session-Id`), pengepala penalaan laluan baru `Mcp-Method`/`Mcp-Name`, metadata cache `ttlMs`/`cacheScope`, Konteks Jejak W3C dalam `_meta`, rangka kerja Peluasan formal (Aplikasi MCP dan peluasan Tugas baru), enam SEP pengerasan kebenaran, penghapusan Roots/Sampling/Logging, dan peralihan ke JSON Schema 2020-12 penuh untuk skema alat.
- **Dikemaskini** dengan panggilan hadapan yang memaut ke pelajaran baru:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): nota versi protokol, bahagian Sampling/Roots/Logging/Tasks, dan "Apa yang seterusnya"
  - [02-Security/README.md](./02-Security/README.md): panggilan pengerasan kebenaran
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): panggilan pengangkutan tanpa status
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): panggilan penghapusan Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): penghapusan Logging dan peluasan Tugas
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): panggilan pengangkutan tanpa status/sesi
  - [README.md](./README.md): nota "Melihat ke hadapan" dalam bahagian spesifikasi dan entri baru `1.1` dalam jadual modul kurikulum
  - [study_guide.md](./study_guide.md): butir hadapan di bawah gambaran Kes Core Concepts dan nota tambahan bertarikh
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): panggilan pada peta pengangkutan `mcp-session-id` di hadapan model permintaan tanpa status
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): panggilan gambaran modul pada penghapusan Root Contexts/Sampling dan peluasan Tugas
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): panggilan pengerasan kebenaran

## 24 Jun, 2026

### Pelajaran Baru: Menggunakan MCP dalam aplikasi Copilot

- [Bahagian Alat](./12-tooling/README.md) Menambah bahagian alat.
- [MCP dalam aplikasi Copilot](./12-tooling/01-copilot-app/README.md)

## 16 Jun, 2026

### Penyelarasan Spesifikasi MCP & Pengesahan Sampel

Mengesahkan kurikulum terhadap **Spesifikasi MCP 2025-11-25** terkini dan SDK rasmi terkini, kemudian membetulkan rujukan spesifikasi lama yang masih ada dan mengesahkan sampel teras masih boleh dibina dan dijalankan.

#### Pembetulan Versi Spesifikasi (2025-06-18 / 2025-03-26 → 2025-11-25)

Dikemaskini kandungan bahasa Inggeris di mana ia masih mendakwa semakan spesifikasi lama adalah piawaian *terkini/terbaru*, dan mengubah pautan kepada laluan spesifikasi kanonik `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Dikemaskini sepanduk "Piawaian Semasa", pengenalan, tajuk prinsip keselamatan teras, tajuk keperluan wajib, seksyen Microsoft Entra ID, pautan Rujukan & Sumber, dan notis keselamatan penutup (8 rujukan) kepada 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Dikemaskini pautan Sumber Tambahan spesifikasi dan sepanduk "Piawaian Semasa" kepada 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Menggantikan pautan keselamatan-dan-kepercayaan `2025-03-26` yang usang dengan halaman amalan terbaik keselamatan 2025-11-25 terkini
- **03-GettingStarted/14-sampling/README.md**: Dikemaskini pautan dokumen sampel rasmi kepada 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Dikemaskini rujukan "spesifikasi MCP semasa" dalam masa kini dan pautan spesifikasi Sumber Tambahan kepada 2025-11-25 (nota penyingkiran SSE sejarah dibiarkan utuh untuk ketepatan)

#### Pengesahan Sampel Terhadap SDK Semasa

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` menyelesaikan `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` lulus tanpa ralat jenis — API sedia ada `McpServer`/`StdioServerTransport` kekal sah
- **Python (03-GettingStarted/01-first-server/solution/python)**: Disahkan dalam `.venv` terasing dengan `mcp[cli]` (1.27.2); `py_compile` lulus dan `FastMCP.list_tools()` mengembalikan alat `add` dan `subtract` dengan betul
- Mengesahkan semua julat versi sampel `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) menyelesaikan dengan bersih ke versi terkini `1.29.0` tanpa perubahan API yang memecahkan

#### Penyesuaian Pin Kebergantungan (menutup jurang versi)

Meningkatkan pin SDK usang supaya setiap sampel menjejak pelepasan MCP semasa, mematuhi konvensyen repo secara keseluruhan:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Meningkatkan `@modelcontextprotocol/sdk` dari `^1.8.0` → `>=1.26.0` dan mengemas kini deskripsi pakej usang `"dikemaskini untuk MCP 2025-06-18"` kepada `"selaras dengan Spesifikasi MCP 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** dan **lab4/code/github_mcp_server/pyproject.toml**: Meningkatkan pin tepat `mcp==1.23.0` → `mcp>=1.26.0`; menjana semula kedua-dua fail `uv.lock` (`uv lock`) supaya fail kunci menyelesaikan kepada `mcp 1.27.2` semasa dan kekal selaras dengan manifes

#### Analisis Jurang Kurikulum — Liputan Ciri Spesifikasi Terkini

Mengesahkan kurikulum sudah merangkumi semua primitif yang diperkenalkan/dikembangkan dalam MCP 2025-11-25, jadi tiada jurang kandungan yang tinggal:
- **Sampling**: Pelajaran 03-GettingStarted/14-sampling dan 05-AdvancedTopics/mcp-sampling
- **Elicitation (termasuk mod URL)**: Didokumentasikan dalam 01-CoreConcepts dan 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Didokumentasikan dalam 00-Introduction, 01-CoreConcepts, dan 05-AdvancedTopics/mcp-root-contexts
- **Tugas (eksperimen, operasi jangka panjang)**: Didokumentasikan dalam 01-CoreConcepts dan 05-AdvancedTopics/mcp-protocol-features
- **Anotasi Alat** (`readOnlyHint` / `destructiveHint`): Didokumentasikan dalam 01-CoreConcepts dan 05-AdvancedTopics/mcp-protocol-features

### Pengerasan Keselamatan & Pemulihan Kerentanan Kebergantungan

Menjalankan pemeriksaan keselamatan penuh merentas setiap manifes kebergantungan dan kod sumber sampel, kemudian membaiki semua nasihat npm yang dilaporkan dan satu penemuan tahap kod. Selepas pembaikan, `npm audit` melaporkan **0 kerentanan** di setiap direktori yang diaudit.

#### Kerentanan Kebergantungan npm (transitif) — Dibaiki

Mengaudit semua 15 fail `package-lock.json` yang dikomit. Kerentanan terhad kepada kebergantungan transitif yang diambil oleh alat pembangunan MCP Inspector, klien OpenAI, dan SDK MCP; semuanya kini diselesaikan tanpa memecahkan sampel:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** dan **lab3/code/weather_mcp/inspector**: Dikemaskini `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), yang telah membersihkan nasihat `ajv`, `brace-expansion`, `diff`, `path-to-regexp` dan `ws` yang disertakan. Ditambahkan entri npm `overrides` yang memaksa `shell-quote@1.8.4` yang berlapik untuk menghapuskan nasihat kritikal yang tinggal dibawa oleh `concurrently`; kedua-dua fail kunci digenerate semula (kini 0 kerentanan)
- **03-GettingStarted/samples/typescript**: `npm audit fix` mengemaskini `qs` transitif (sederhana) kepada keluaran berlapik
- **03-GettingStarted/samples/javascript**: `npm audit fix` mengemaskini `hono` transitif (sederhana) kepada keluaran berlapik
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` mengemaskini `form-data` transitif (tinggi) kepada keluaran berlapik
- **03-GettingStarted/11-simple-auth/solution/typescript**: Menghasilkan `package-lock.json` yang hilang supaya projek ini dapat dihasilkan semula dan diaudit (0 kerentanan)

#### Pembaikan Tahap Kod Keselamatan (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Dibuang `shell=True` dari alat `open_in_vscode`. Sebelumnya `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` membenarkan metakarakter shell dalam laluan folder ditafsir oleh `cmd.exe` (vektor suntikan arahan). Kini ia melancarkan `Code.exe` yang diselesaikan secara langsung dengan folder sebagai argumen — tanpa shell — yang berfungsi setara dan selamat

#### Audit Pergantungan Python

- Mengaudit semua set keperluan Python dengan `pip-audit`. `05-AdvancedTopics` dan `03-GettingStarted/samples/python` melaporkan **tiada kerentanan yang diketahui** (julatan `mcp` / `httpx` / `pydantic` / `python-dotenv` mereka menyelesaikan kepada keluaran berlapik terkini)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` menandakan kebergantungan transitif **`werkzeug` 3.1.1** dengan tiga nasihat DoS nama peranti Windows `safe_join` — `CVE-2025-66221`, `CVE-2026-21860`, dan `CVE-2026-27199` (semua diperbaiki dalam 3.1.6). Ditambahkan pin keselamatan `werkzeug>=3.1.6` yang eksplisit supaya keluaran berlapik dapat diselesaikan; disahkan kekangan menyelesaikan dengan bersih dengan timbunan `chainlit` / `mcp` / `semantic-kernel`

### Penjenamaan Semula Nama Produk

Dikemaskini semua kandungan kurikulum untuk mencerminkan penjenamaan semula produk Microsoft:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Dikemaskini pautan komuniti Discord
- **AGENTS.md**: Dikemaskini rujukan pelayan Discord
- **README.md**: Dikemaskini rujukan ekosistem teknologi
- **study_guide.md**: Dikemaskini rujukan kajian kes
- **05-AdvancedTopics/README.md**: Dikemaskini tajuk dan penerangan Modul 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Dikemaskini tajuk seksyen dan penerangan
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Dikemaskini tajuk modul penuh dan kandungan
- **05-AdvancedTopics/mcp-security-entra/README.md**: Dikemaskini pautan rujukan silang
- **07-LessonsfromEarlyAdoption/README.md**: Dikemaskini rujukan kajian kes
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Dikemaskini tajuk Seksyen 9, lencana, dan kemampuan
- **08-BestPractices/README.md**: Dikemaskini pautan komuniti Discord
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Dikemaskini rujukan saluran Discord
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Dikemaskini rujukan penyebaran model
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Dikemaskini jadual Perkhidmatan AI
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Dikemaskini rujukan sumber

#### AI Toolkit / AITK → Sambungan Alat Microsoft Foundry untuk VS Code
- **README.md**: Dikemaskini rujukan utama kurikulum
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Dikemaskini tajuk modul, gambaran keseluruhan, dan semua tajuk modul
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Dikemaskini tajuk, objektif pembelajaran, arahan penyediaan, dan sumber
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Dikemaskini tajuk, objektif pembelajaran, jadual hos MCP, dan rujukan silang
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Dikemaskini tajuk, lencana, prasyarat, dan sumber
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Dikemaskini rujukan Pembina Ejen dan pautan maklum balas
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Dikemaskini prasyarat dan rujukan sambungan

---

## 11 April, 2026

### Pelajaran Baru, Pembaikan Dokumentasi, dan Kemas Kini Pergantungan

#### Kandungan Kurikulum Baru Ditambah

**Modul 05 - Topik Lanjutan**
- **Pelajaran 5.17: Pemikiran Pelbagai Ejen Adversarial dengan MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Panduan komprehensif baharu yang merangkumi corak debat adversarial untuk sistem pelbagai ejen
  - Rajah seni bina Mermaid: dua ejen → pelayan MCP dikongsi → transkrip debat → hakim → keputusan
  - Pelayan alat MCP bersama (`web_search` + `run_python`) dilaksanakan dalam Python dan TypeScript
  - Arahan sistem bertentangan (UNTUK / MENENTANG / Hakim) dengan keperluan penggunaan alat yang jelas
  - Pengatur lisan debat dalam Python, TypeScript, dan C# mengurus pusingan dan penyaluran hujah
  - Pengkabelan `ClientSession` MCP untuk pengatur lisan ke panggilan alat sebenar
  - Jadual kes penggunaan (pengesanan halusinasi, pemodelan ancaman, semakan reka bentuk API, pengesahan fakta, pemilihan teknologi)
  - Pertimbangan keselamatan: pelaksanaan dalam sandbox, pengesahan panggilan alat, had kadar, log audit
  - Latihan berstruktur dengan tiga senario praktikal (semakan kod, keputusan seni bina, pengawal seliaan kandungan)

#### Pembaikan Dokumentasi

**Modul 03 - Memulakan**
- **05-stdio-server/README.md**: Memperbaiki contoh pelayan stdio TypeScript yang tidak lengkap — menambahkan instansiasi pengangkutan yang hilang (`new StdioServerTransport()`) dan panggilan `server.connect(transport)` untuk menyesuaikan contoh Python dan .NET dalam seksyen yang sama
- **14-sampling/README.md**: Memperbaiki kesilapan taip — membetulkan `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Kemas Kini Kurikulum

**README.md Utama**
- Ditambahkan entri 5.17 (Pemikiran Pelbagai Ejen Adversarial dengan MCP) ke jadual kurikulum dengan pautan langsung ke pelajaran baru

**05-AdvancedTopics/README.md**
- Ditambahkan baris Pelajaran 5.17 ke jadual pelajaran

**study_guide.md**
- Ditambahkan topik Pemikiran Pelbagai Ejen Adversarial ke peta minda dan penerangan prosa Topik Lanjutan

#### Pembaikan Kod dan Keselamatan

**Modul 05 - Ejen Adversarial (`mcp-adversarial-agents`)**
- **Pembaikan keselamatan — suntikan arahan**: Menggantikan interpolasi shell `execSync` dengan `execFile` + `promisify` dalam alat TypeScript `run_python`, menghapuskan permukaan suntikan arahan (kod yang dikawal LLM kini dihantar sebagai elemen argv literal tanpa penglibatan shell)
- **Pengkabelan gelung alat MCP**: Mengemas kini pengatur lisan debat Python untuk menggunakan klien `AsyncAnthropic` (menggantikan `Anthropic` sebenar yang menyekat secara segerak), menghantar `ClientSession` hidup terus ke setiap giliran ejen, mengambil definisi alat melalui `session.list_tools()` setiap giliran, dan mengedar blok `tool_use` melalui `session.call_tool()` dalam gelung sehingga model mengemukakan tindak balas teks akhir

#### Kemas Kini Pergantungan

- Dinaik taraf `hono` kepada 4.12.12 merentas pelbagai pakej (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Dinaik taraf `@hono/node-server` dari 1.19.11 ke 1.19.13 dalam pakej TypeScript
- Dinaik taraf `cryptography` dari 46.0.5 ke 46.0.7 dalam pakej Python (makmal 3 dan 4 10-StreamliningAIWorkflows)
- Dinaik taraf `lodash` dari 4.17.23 ke 4.18.1 dalam pemeriksa 10-StreamliningAIWorkflows

#### Terjemahan

- Menyegerakkan terjemahan untuk 48+ bahasa dengan perubahan sumber terkini (kemaskini i18n)

---

## 5 Februari, 2026

### Penambahbaikan Pengesahan dan Navigasi Keseluruhan Repositori

#### Kandungan Kurikulum Baru Ditambah

**Modul 03 - Memulakan**
- **12-mcp-hosts/README.md**: Panduan komprehensif baru untuk menyediakan hos MCP
  - Contoh konfigurasi Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Templat konfigurasi JSON untuk semua hos utama
  - Jadual perbandingan jenis pengangkutan (stdio, SSE/HTTP, WebSocket)
  - Penyelesaian masalah isu sambungan biasa
  - Amalan keselamatan terbaik untuk konfigurasi hos

- **13-mcp-inspector/README.md**: Panduan penyahpepijatan baru untuk Pemeriksa MCP
  - Kaedah pemasangan (npx, npm global, dari sumber)
  - Penyambungan ke pelayan melalui stdio dan HTTP/SSE
  - Alatan ujian, sumber, dan aliran kerja prompt
  - Integrasi VS Code dengan Pemeriksa MCP
  - Senario penyahpepijatan biasa dengan penyelesaian

**Modul 04 - Pelaksanaan Praktikal**
- **pagination/README.md**: Panduan pelaksanaan pagination baru
  - Corak pagination berasaskan kursor dalam Python, TypeScript, Java
  - Pengendalian pagination sisi klien
  - Strategi reka bentuk kursor (tidak telus vs. berstruktur)
  - Cadangan pengoptimuman prestasi

**Modul 05 - Topik Lanjutan**
- **mcp-protocol-features/README.md**: Penyelaman ciri protokol baru
  - Pelaksanaan notifikasi kemajuan
  - Corak pembatalan permintaan
  - Templat sumber dengan corak URI
  - Pengurusan kitar hayat pelayan
  - Kawalan tahap log
  - Corak pengendalian ralat dengan kod JSON-RPC

#### Pembaikan Navigasi (24+ fail dikemaskini)

**README Modul Utama**
 Kini pautan ke pelajaran pertama DAN modul seterusnya

**Fail Subsistem Keselamatan 02**
- Semua 5 dokumen keselamatan sokongan kini mempunyai navigasi "Apa Seterusnya":

**Fail Kajian Kes 09**
- Semua fail kajian kes kini mempunyai navigasi berurutan:

**Makmal 10-StreamliningAI**
Ditambahkan seksyen Apa Seterusnya ke gambaran keseluruhan Modul 10 dan Modul 11

#### Pembaikan Kod dan Kandungan

**Kemas Kini SDK dan Pergantungan**
Memperbaiki versi openai kosong kepada `^4.95.0`
Dikemaskini SDK dari `^1.8.0` ke `>=1.26.0`
Dikemaskini pin versi mcp ke `>=1.26.0`

**Pembaikan Kod**
Memperbaiki model tidak sah `gpt-4o-mini` ke `gpt-4.1-mini`

**Pembaikan Kandungan**
Memperbaiki pautan rosak `READMEmd` → `README.md`, membetulkan tajuk kurikulum `Module 1-3` → `Module 0-3`, membetulkan laluan yang peka kes
Membuang kandungan duplikat Kajian Kes 5 yang rosak

**Penambahbaikan Panduan Pemula**
Menambah pengenalan yang betul, objektif pembelajaran, dan prasyarat untuk pemula

#### Kemas Kini Kurikulum

**README.md Utama**
- Ditambahkan entri 3.12 (Hos MCP), 3.13 (Pemeriksa MCP), 4.1 (Pagination), 5.16 (Ciri Protokol) ke jadual kurikulum

**README Modul**
Ditambahkan pelajaran 12 dan 13 ke senarai pelajaran
Ditambahkan seksyen Panduan Praktikal dengan pautan pagination
Ditambahkan pelajaran 5.15 (Pengangkutan Custom) dan 5.16 (Ciri Protokol)

**study_guide.md**
- Dikemaskini peta minda dengan semua topik baru: Persediaan Hos MCP, Pemeriksa MCP, Strategi Pagination, Penyelaman Ciri Protokol

## 28 Januari, 2026

### Semakan Pematuhan Spesifikasi MCP 2025-11-25

#### Peningkatan Konsep Teras (01-CoreConcepts/)
- **Primitif Pelanggan Baru - Roots**: Ditambahkan dokumentasi komprehensif tentang primitif pelanggan Roots, membolehkan pelayan memahami sempadan sistem fail dan kebenaran akses
- **Anotasi Alat**: Ditambahkan dokumentasi tentang anotasi tingkah laku alat (`readOnlyHint`, `destructiveHint`) untuk keputusan pelaksanaan alat yang lebih baik
- **Panggilan Alat dalam Sampling**: Dikemaskini dokumentasi Sampling untuk menyertakan parameter `tools` dan `toolChoice` untuk pemanggilan alat yang dipacu model semasa permintaan sampling
- **Pemohonan Mod URL**: Ditambahkan dokumentasi tentang pemohonan berasaskan URL untuk interaksi web luaran yang dimulakan pelayan
- **Tugas (Eksperimen)**: Ditambahkan seksyen baru yang mendokumentasikan ciri Tugas eksperimen untuk pembalut pelaksanaan tahan lama dan pengambilan hasil tertunda

- **Sokongan Ikon**: Diperhatikan bahawa alat, sumber, templat sumber, dan arahan kini boleh termasuk ikon sebagai metadata tambahan

#### Kemas Kini Dokumentasi
- **README.md**: Ditambah rujukan versi Spesifikasi MCP 2025-11-25 dan penjelasan versi berdasarkan tarikh
- **study_guide.md**: Dikemas kini peta kurikulum untuk memasukkan Tugas dan Anotasi Alat dalam bahagian Konsep Teras; dikemas kini cap masa dokumen

#### Pengesahan Pematuhan Spesifikasi
- **Versi Protokol**: Disahkan semua rujukan dokumentasi menggunakan Spesifikasi MCP 2025-11-25 terkini
- **Penyelarasan Seni Bina**: Disahkan ketepatan dokumentasi seni bina dua lapisan (Lapisan Data + Lapisan Pengangkutan)
- **Dokumentasi Primitif**: Disahkan primitif pelayan (Sumber, Arahan, Alat) dan primitif klien (Pensampelan, Pengeluar, Perakam, Akar)
- **Mekanisme Pengangkutan**: Disahkan ketepatan dokumentasi pengangkutan STDIO dan HTTP Boleh Alir
- **Panduan Keselamatan**: Disahkan penyelarasan dengan dokumentasi Amalan Terbaik Keselamatan MCP terkini

#### Ciri Utama MCP 2025-11-25 Yang Didokumentasikan
- **Penemuan OpenID Connect**: Penemuan pelayan pengesahan melalui OIDC
- **Dokumen Metadata ID Pelanggan OAuth**: Mekanisme pendaftaran pelanggan yang disyorkan
- **JSON Schema 2020-12**: Dialek lalai untuk definisi skema MCP
- **Sistem Tahap SDK**: Formalkan keperluan sokongan ciri SDK dan penyelenggaraan
- **Struktur Tadbir Urus**: Formalkan Kumpulan Kerja dan Kumpulan Minat dalam tadbir urus MCP

### Kemas Kini Utama Dokumentasi Keselamatan (02-Security/)

#### Integrasi Bengkel Sidang Kemuncak Keselamatan MCP (Sherpa)
- **Sumber Latihan Amali Baru**: Ditambah integrasi menyeluruh dengan [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) dalam semua dokumentasi keselamatan
- **Liputan Laluan Ekspedisi**: Didokumentasikan perjalanan lengkap dari Kem Asas ke Kemuncak
- **Penyelarasan OWASP**: Semua panduan keselamatan kini dipadankan dengan risiko Panduan Keselamatan Azure MCP OWASP

#### Integrasi OWASP MCP Top 10
- **Bahagian Baru**: Ditambah jadual Risiko Keselamatan OWASP MCP Top 10 dengan mitigasi Azure dalam README Keselamatan utama
- **Dokumentasi Berasaskan Risiko**: Dikemas kini mcp-security-controls-2025.md dengan rujukan risiko OWASP MCP untuk setiap domain keselamatan
- **Seni Bina Rujukan**: Dipaut ke seni bina rujukan dan corak pelaksanaan Panduan Keselamatan Azure OWASP MCP

#### Fail Keselamatan Dikemas Kini
- **README.md**: Ditambah gambaran keseluruhan Bengkel Sherpa, jadual laluan ekspedisi, ringkasan risiko OWASP MCP Top 10, dan bahagian latihan amali
- **mcp-security-controls-2025.md**: Dikemas kini header ke Februari 2026, ditambah rujukan risiko OWASP (MCP01-MCP08), membetulkan ketidakselarasan versi spesifikasi
- **mcp-security-best-practices-2025.md**: Ditambah bahagian sumber Sherpa dan OWASP, dikemas kini cap masa
- **mcp-best-practices.md**: Ditambah bahagian latihan amali dengan pautan Sherpa dan OWASP
- **azure-content-safety-implementation.md**: Ditambah rujukan MCP06 OWASP, penyelarasan Camp 3 Sherpa, dan bahagian sumber tambahan

#### Pautan Sumber Baru Ditambah
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Halaman risiko OWASP MCP individu (MCP01-MCP10)

### Penyelarasan Spesifikasi MCP 2025-11-25 Seluruh Kurikulum

#### Modul 03 - Bermula
- **Dokumentasi SDK**: Ditambah Go SDK ke senarai SDK rasmi; dikemas kini semua rujukan SDK untuk selaras dengan Spesifikasi MCP 2025-11-25
- **Penjelasan Pengangkutan**: Dikemas kini huraian pengangkutan STDIO dan HTTP Streaming dengan rujukan spesifikasi yang jelas

#### Modul 04 - Pelaksanaan Praktikal
- **Kemas Kini SDK**: Ditambah Go SDK; dikemas kini senarai SDK dengan rujukan versi spesifikasi
- **Spesifikasi Kebenaran**: Dikemas kini pautan spesifikasi Kebenaran MCP ke versi 2025-11-25 terkini

#### Modul 05 - Topik Lanjutan
- **Ciri Baru**: Ditambah nota mengenai ciri baru Spesifikasi MCP 2025-11-25 (Tugas, Anotasi Alat, Elicitation Mod URL, Akar)
- **Sumber Keselamatan**: Ditambah pautan OWASP MCP Top 10 dan bengkel Sherpa ke rujukan tambahan

#### Modul 06 - Sumbangan Komuniti
- **Senarai SDK**: Ditambah Swift dan Rust SDK; dikemas kini pautan spesifikasi ke 2025-11-25
- **Rujukan Spesifikasi**: Dikemas kini pautan Spesifikasi MCP ke URL spesifikasi langsung

#### Modul 07 - Pengajaran dari Penggunaan Awal
- **Kemas Kini Sumber**: Ditambah pautan Spesifikasi MCP 2025-11-25 dan OWASP MCP Top 10 ke sumber tambahan

#### Modul 08 - Amalan Terbaik
- **Versi Spesifikasi**: Dikemas kini rujukan Spesifikasi MCP ke 2025-11-25
- **Sumber Keselamatan**: Ditambah OWASP MCP Top 10 dan bengkel Sherpa ke rujukan tambahan

#### Modul 10 - Memperkemaskan Aliran Kerja AI
- **Kemas Kini Lencana**: Ditukar lencana versi MCP dari versi SDK (1.9.3) ke versi spesifikasi (2025-11-25)
- **Pautan Sumber**: Dikemas kini pautan Spesifikasi MCP; ditambah OWASP MCP Top 10

#### Modul 11 - Makmal Amali MCP Server
- **Rujukan Spesifikasi**: Dikemas kini pautan Spesifikasi MCP ke versi 2025-11-25
- **Sumber Keselamatan**: Ditambah OWASP MCP Top 10 ke sumber rasmi

## 18 Disember, 2025

### Kemas Kini Dokumentasi Keselamatan - Spesifikasi MCP 2025-11-25

#### Amalan Terbaik Keselamatan MCP (02-Security/mcp-best-practices.md) - Kemas Kini Versi Spesifikasi
- **Kemas Kini Versi Protokol**: Dikemas kini untuk merujuk Spesifikasi MCP terkini 2025-11-25 (dikeluarkan 25 November 2025)
 - Dikemas kini semua rujukan versi spesifikasi daripada 2025-06-18 ke 2025-11-25
 - Dikemas kini rujukan tarikh dokumen daripada 18 Ogos 2025 ke 18 Disember 2025
 - Disahkan semua URL spesifikasi menunjuk ke dokumentasi terkini
- **Pengesahan Kandungan**: Pengesahan menyeluruh amalan terbaik keselamatan terhadap piawaian terkini
 - **Penyelesaian Keselamatan Microsoft**: Disahkan istilah dan pautan terkini untuk Perisai Arahan (sebelumnya "pengesanan risiko Jailbreak"), Keselamatan Kandungan Azure, Microsoft Entra ID, dan Azure Key Vault
 - **Keselamatan OAuth 2.1**: Disahkan penyelarasan dengan amalan terbaik keselamatan OAuth terkini
 - **Piawaian OWASP**: Disahkan rujukan OWASP Top 10 untuk LLM kekal terkini
 - **Perkhidmatan Azure**: Disahkan semua pautan dokumentasi Microsoft Azure dan amalan terbaik
- **Penyelarasan Piawaian**: Semua piawaian keselamatan yang dirujuk disahkan terkini
 - Rangka Kerja Pengurusan Risiko AI NIST
 - ISO 27001:2022
 - Amalan Terbaik Keselamatan OAuth 2.1
 - Rangka kerja keselamatan dan pematuhan Azure
- **Sumber Pelaksanaan**: Disahkan semua pautan dan sumber panduan pelaksanaan
 - Corak pengesahan Azure API Management
 - Panduan integrasi Microsoft Entra ID
 - Pengurusan rahsia Azure Key Vault
 - Saluran dan penyelesaian pemantauan DevSecOps

### Jaminan Kualiti Dokumentasi
- **Pematuhan Spesifikasi**: Memastikan semua keperluan keselamatan MCP wajib (MESTI/TIDAK MESTI) sejajar dengan spesifikasi terkini
- **Ketepatan Sumber**: Memastikan semua pautan luaran kepada dokumentasi Microsoft, piawaian keselamatan, dan panduan pelaksanaan adalah tepat
- **Liputan Amalan Terbaik**: Disahkan liputan menyeluruh pengesahan, kebenaran, ancaman khusus AI, keselamatan rantaian bekalan, dan corak perusahaan

## 6 Oktober, 2025

### Perluasan Bahagian Bermula – Penggunaan Pelayan Lanjutan & Pengesahan Mudah

#### Penggunaan Pelayan Lanjutan (03-GettingStarted/10-advanced)
- **Bab Baru Ditambah**: Memperkenalkan panduan menyeluruh untuk penggunaan pelayan MCP lanjutan, merangkumi seni bina pelayan biasa dan tahap rendah.
 - **Pelayan Biasa vs. Tahap Rendah**: Perbandingan terperinci dan contoh kod dalam Python dan TypeScript untuk kedua-dua pendekatan.
 - **Reka Bentuk Berasaskan Pengendali**: Penjelasan pengurusan alat/sumber/arahan berasaskan pengendali untuk pelaksanaan pelayan yang skala dan fleksibel.
 - **Corak Praktikal**: Senario dunia sebenar di mana corak pelayan tahap rendah bermanfaat untuk ciri dan seni bina lanjutan.

#### Pengesahan Mudah (03-GettingStarted/11-simple-auth)
- **Bab Baru Ditambah**: Panduan langkah demi langkah untuk melaksanakan pengesahan mudah dalam pelayan MCP.
 - **Konsep Pengesahan**: Penjelasan jelas mengenai pengesahan berbanding kebenaran, dan pengendalian kelayakan.
 - **Pelaksanaan Auth Asas**: Corak pengesahan berasaskan middleware dalam Python (Starlette) dan TypeScript (Express), dengan contoh kod.
 - **Kemajuan ke Keselamatan Lanjutan**: Panduan memulakan dengan auth mudah dan berkembang ke OAuth 2.1 dan RBAC, dengan rujukan modul keselamatan lanjutan.

Penambahan ini menyediakan panduan praktikal dan amali untuk membina pelaksanaan pelayan MCP yang lebih kukuh, selamat, dan fleksibel, menghubungkan konsep asas dengan corak pengeluaran lanjutan.

## 29 September, 2025

### Makmal Integrasi Pangkalan Data MCP Server - Laluan Pembelajaran Amali Menyeluruh

#### 11-MCPServerHandsOnLabs - Kurikulum Integrasi Pangkalan Data Lengkap Baru
- **Laluan Pembelajaran 13-Makmal Lengkap**: Ditambah kurikulum amali menyeluruh untuk membina pelayan MCP sedia produksi dengan integrasi pangkalan data PostgreSQL
 - **Pelaksanaan Dunia Sebenar**: Kes penggunaan analitik Zava Retail yang menunjukkan corak gred perusahaan
 - **Progresi Pembelajaran Berstruktur**:
   - **Makmal 00-03: Asas** - Pengenalan, Seni Bina Teras, Keselamatan & Multi-Tenancy, Persediaan Persekitaran
   - **Makmal 04-06: Membina Pelayan MCP** - Reka Bentuk & Skema Pangkalan Data, Pelaksanaan Pelayan MCP, Pembangunan Alat  
   - **Makmal 07-09: Ciri Lanjutan** - Integrasi Carian Semantik, Ujian & Debugging, Integrasi VS Code
   - **Makmal 10-12: Pengeluaran & Amalan Terbaik** - Strategi Penempatan, Pemantauan & Kebolehlihatan, Amalan Terbaik & Pengoptimuman
 - **Teknologi Perusahaan**: Rangka kerja FastMCP, PostgreSQL dengan pgvector, penanaman Azure OpenAI, Azure Container Apps, Application Insights
 - **Ciri Lanjutan**: Keselamatan Tahap Baris (RLS), carian semantik, akses data berbilang penyewa, penanaman vektor, pemantauan masa nyata

#### Standardisasi Terminologi - Penukaran Modul ke Makmal
- **Kemas Kini Dokumentasi Menyeluruh**: Dikemas kini secara sistematik semua fail README dalam 11-MCPServerHandsOnLabs untuk menggunakan terminologi "Makmal" menggantikan "Modul"
 - **Tajuk Bahagian**: Dikemas kini "What This Module Covers" kepada "What This Lab Covers" di semua 13 makmal
 - **Penerangan Kandungan**: Ditukar "This module provides..." kepada "This lab provides..." dalam keseluruhan dokumentasi
 - **Objektif Pembelajaran**: Dikemas kini "By the end of this module..." kepada "By the end of this lab..." 
 - **Pautan Navigasi**: Tukar semua rujukan "Modul XX:" kepada "Makmal XX:" dalam rujukan silang dan navigasi
 - **Penjejakan Penyelesaian**: Dikemas kini "After completing this module..." kepada "After completing this lab..."
 - **Pengekalan Rujukan Teknikal**: Mengekalkan rujukan modul Python dalam fail konfigurasi (contoh, `"module": "mcp_server.main"`)

#### Peningkatan Panduan Kajian (study_guide.md)
- **Peta Kurikulum Visual**: Ditambah bahagian baru "11. Database Integration Labs" dengan visualisasi struktur makmal menyeluruh
- **Struktur Repositori**: Dikemas kini daripada sepuluh ke sebelas bahagian utama dengan keterangan terperinci 11-MCPServerHandsOnLabs
- **Panduan Laluan Pembelajaran**: Diperbaiki arahan navigasi untuk merangkumi bahagian 00-11
- **Liputan Teknologi**: Ditambah perincian integrasi FastMCP, PostgreSQL, perkhidmatan Azure
- **Hasil Pembelajaran**: Ditekankan pembangunan pelayan sedia produksi, corak integrasi pangkalan data, dan keselamatan perusahaan

#### Peningkatan Struktur README Utama
- **Terminologi Berasaskan Makmal**: Dikemas kini README.md utama dalam 11-MCPServerHandsOnLabs untuk konsisten menggunakan struktur "Makmal"
- **Organisasi Laluan Pembelajaran**: Progresi jelas daripada konsep asas melalui pelaksanaan lanjutan di hingga penempatan produksi
- **Fokus Dunia Sebenar**: Penekanan pada pembelajaran praktikal dan amali dengan corak dan teknologi gred perusahaan

### Peningkatan Kualiti & Konsistensi Dokumentasi
- **Penekanan Pembelajaran Amali**: Memperkuat pendekatan berasaskan makmal sepanjang dokumentasi
- **Fokus Corak Perusahaan**: Menonjolkan pelaksanaan sedia produksi dan pertimbangan keselamatan perusahaan
- **Integrasi Teknologi**: Liputan menyeluruh perkhidmatan Azure moden dan corak integrasi AI
- **Progresi Pembelajaran**: Laluan jelas dan berstruktur daripada konsep asas ke penempatan produksi

## 26 September, 2025

### Peningkatan Kajian Kes - Integrasi Daftar MCP GitHub

#### Kajian Kes (09-CaseStudy/) - Fokus Pembangunan Ekosistem
- **README.md**: Perluasan besar dengan kajian kes Daftar MCP GitHub yang menyeluruh
 - **Kajian Kes Daftar MCP GitHub**: Kajian kes baru yang menyeluruh membincangkan pelancaran Daftar MCP GitHub pada September 2025
   - **Analisis Masalah**: Pemeriksaan terperinci cabaran penemuan dan penempatan pelayan MCP yang terpecah-belah
   - **Seni Bina Penyelesaian**: Pendekatan daftar berpusat GitHub dengan pemasangan satu klik VS Code
   - **Impak Perniagaan**: Peningkatan terukur dalam pendaftaran pemaju dan produktiviti
   - **Nilai Strategik**: Fokus pada penempatan ejen modular dan kebolehsinambungan merentas alat
   - **Pembangunan Ekosistem**: Kedudukan sebagai platform asas untuk integrasi agen
 - **Struktur Kajian Kes Dipertingkatkan**: Dikemas kini semua tujuh kajian kes dengan format konsisten dan penerangan menyeluruh
   - Ejen Pelancongan AI Azure: Penekanan orkestrasi pelbagai ejen
   - Integrasi Azure DevOps: Fokus automasi aliran kerja
   - Pengambilan Dokumentasi Masa Nyata: Pelaksanaan klien konsol Python
   - Penjana Pelan Kajian Interaktif: Aplikasi web perbualan Chainlit

    - Dokumentasi Dalam Penyunting: Integrasi VS Code dan GitHub Copilot
    - Pengurusan API Azure: Corak integrasi API perusahaan
    - Daftar MCP GitHub: Pembangunan ekosistem dan platform komuniti
  - **Kesimpulan Menyeluruh**: Bahagian kesimpulan yang ditulis semula menyorot tujuh kajian kes merangkumi pelbagai dimensi pelaksanaan MCP
    - Integrasi Perusahaan, Orkestrasi Multi-Ejen, Produktiviti Pembangun
    - Pembangunan Ekosistem, pengelasan Aplikasi Pendidikan
    - Penambahbaikan dalam wawasan corak seni bina, strategi pelaksanaan, dan amalan terbaik
    - Penekanan pada MCP sebagai protokol matang dan sedia produksi

#### Kemas Kini Panduan Kajian (study_guide.md)
- **Peta Kurikulum Visual**: Peta minda dikemaskini untuk memasukkan Daftar MCP GitHub dalam bahagian Kajian Kes
- **Penerangan Kajian Kes**: Diperbaiki daripada penerangan umum kepada pecahan terperinci tujuh kajian kes menyeluruh
- **Struktur Repositori**: Seksyen 10 dikemas kini untuk mencerminkan liputan kajian kes komprehensif dengan butiran pelaksanaan khusus
- **Integrasi Changelog**: Tambahan entri 26 September 2025 yang mendokumentasikan penambahan Daftar MCP GitHub dan penambahbaikan kajian kes
- **Kemas Kini Tarikh**: Tanda masa footer dikemas kini untuk mencerminkan semakan terkini (26 September 2025)

### Penambahbaikan Kualiti Dokumentasi
- **Penambahbaikan Konsistensi**: Menyeragamkan format dan struktur kajian kes di semua tujuh contoh
- **Liputan Menyeluruh**: Kajian kes kini merangkumi senario perusahaan, produktiviti pembangun, dan pembangunan ekosistem
- **Penempatan Strategik**: Fokus yang dipertingkatkan pada MCP sebagai platform asas untuk penyebaran sistem ejen
- **Integrasi Sumber**: Sumber tambahan dikemas kini untuk memasukkan pautan Daftar MCP GitHub

## 15 September 2025

### Pengembangan Topik Lanjutan - Pengangkut Tersuai & Kejuruteraan Konteks

#### Pengangkut Tersuai MCP (05-AdvancedTopics/mcp-transport/) - Panduan Pelaksanaan Lanjutan Baru
- **README.md**: Panduan pelaksanaan lengkap untuk mekanisme pengangkutan MCP tersuai
  - **Pengangkut Azure Event Grid**: Pelaksanaan pengangkutan berasaskan acara tanpa server yang menyeluruh
    - Contoh C#, TypeScript, dan Python dengan integrasi Azure Functions
    - Corak seni bina berasaskan acara untuk penyelesaian MCP yang boleh diskala
    - Penerima webhook dan pengendalian mesej berasaskan push
  - **Pengangkut Azure Event Hubs**: Pelaksanaan pengangkutan streaming berkelajuan tinggi
    - Keupayaan streaming masa nyata untuk senario latensi rendah
    - Strategi partisi dan pengurusan checkpoint
    - Penggugusan mesej dan pengoptimuman prestasi
  - **Corak Integrasi Perusahaan**: Contoh seni bina sedia produksi
    - Pemprosesan MCP diedarkan merentasi pelbagai Azure Functions
    - Seni bina pengangkutan hibrid menggabungkan pelbagai jenis pengangkutan
    - Ketahanan mesej, kebolehpercayaan, dan strategi pengendalian ralat
  - **Keselamatan & Pemantauan**: Integrasi Azure Key Vault dan corak kebolehlihatan
    - Pengesahan identiti terurus dan akses keistimewaan minimum
    - Telemetri Application Insights dan pemantauan prestasi
    - Pemutus litar dan corak ketahanan ralat
  - **Rangka Kerja Ujian**: Strategi ujian menyeluruh untuk pengangkut tersuai
    - Ujian unit dengan palsu ujian dan rangka kerja pra-konfig
    - Ujian integrasi dengan Azure Test Containers
    - Pertimbangan ujian prestasi dan beban

#### Kejuruteraan Konteks (05-AdvancedTopics/mcp-contextengineering/) - Disiplin AI Berkembang
- **README.md**: Eksplorasi menyeluruh tentang kejuruteraan konteks sebagai bidang yang muncul
  - **Prinsip Teras**: Perkongsian konteks lengkap, kesedaran keputusan tindakan, dan pengurusan tetingkap konteks
  - **Penjajaran Protokol MCP**: Bagaimana reka bentuk MCP menangani cabaran kejuruteraan konteks
    - Had tetingkap konteks dan strategi pemuatan progresif
    - Penentuan relevansi dan pengambilan konteks dinamik
    - Pengendalian konteks berbilang mod dan pertimbangan keselamatan
  - **Pendekatan Pelaksanaan**: Seni bina bersatu benang vs berbilang ejen
    - Teknik penggumpalan dan keutamaan konteks
    - Pemuatan progresif konteks dan strategi pemampatan
    - Pendekatan berlapis pada konteks dan pengoptimuman pengambilan
  - **Rangka Kerja Pengukuran**: Metrik baru untuk penilaian keberkesanan konteks
    - Kecekapan input, prestasi, kualiti, dan pertimbangan pengalaman pengguna
    - Pendekatan eksperimen untuk pengoptimuman konteks
    - Analisis kegagalan dan metodologi penambahbaikan

#### Kemas Kini Navigasi Kurikulum (README.md)
- **Struktur Modul Dipertingkat**: Jadual kurikulum dikemas kini untuk memasukkan topik lanjutan baru
  - Menambah Kejuruteraan Konteks (5.14) dan Pengangkut Tersuai (5.15)
  - Format dan pautan navigasi konsisten di semua modul
  - Penerangan dikemas kini untuk mencerminkan skop kandungan terkini

### Penambahbaikan Struktur Direktori
- **Penyeragaman Penamaan**: Menamakan semula "mcp transport" ke "mcp-transport" untuk keseragaman dengan folder topik lanjutan lain
- **Pengurusan Kandungan**: Semua folder 05-AdvancedTopics kini mengikut corak penamaan konsisten (mcp-[topik])

### Penambahbaikan Kualiti Dokumentasi
- **Penjajaran Spesifikasi MCP**: Semua kandungan baru merujuk Spesifikasi MCP 2025-06-18 terkini
- **Contoh Berbilang Bahasa**: Contoh kod menyeluruh dalam C#, TypeScript, dan Python
- **Fokus Perusahaan**: Corak sedia produksi dan integrasi awan Azure merentas seluruh dokumen
- **Dokumentasi Visual**: Rajah Mermaid untuk visualisasi seni bina dan aliran

## 18 Ogos 2025

### Kemas Kini Menyeluruh Dokumentasi - Standard MCP 2025-06-18

#### Amalan Terbaik Keselamatan MCP (02-Security/) - Pengubahsuaian Lengkap
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Penulisan semula lengkap selaras dengan Spesifikasi MCP 2025-06-18
  - **Keperluan Wajib**: Penambahan keperluan MUST/MUST NOT eksplisit dari spesifikasi rasmi dengan penunjuk visual jelas
  - **12 Amalan Keselamatan Teras**: Disusun semula daripada senarai 15 item kepada domain keselamatan menyeluruh
    - Keselamatan Token & Pengesahan dengan integrasi penyedia identiti luaran
    - Pengurusan Sesi & Keselamatan Pengangkutan dengan keperluan kriptografi
    - Perlindungan Ancaman Khusus AI dengan integrasi Microsoft Prompt Shields
    - Kawalan Akses & Kebenaran dengan prinsip keistimewaan minimum
    - Keselamatan Kandungan & Pemantauan dengan integrasi Azure Content Safety
    - Keselamatan Rantaian Bekalan dengan pengesahan komponen menyeluruh
    - Keselamatan OAuth & Pencegahan "Confused Deputy" dengan pelaksanaan PKCE
    - Respons & Pemulihan Insiden dengan keupayaan automatik
    - Pematuhan & Tadbir Urus dengan penjajaran peraturan
    - Kawalan Keselamatan Lanjutan dengan seni bina kepercayaan sifar
    - Integrasi Ekosistem Keselamatan Microsoft dengan penyelesaian menyeluruh
    - Evolusi Keselamatan Berterusan dengan amalan adaptif
  - **Penyelesaian Keselamatan Microsoft**: Panduan integrasi dipertingkat untuk Prompt Shields, Azure Content Safety, Entra ID, dan GitHub Advanced Security
  - **Sumber Pelaksanaan**: Pautan sumber dikategorikan mengikut Dokumentasi MCP Rasmi, Penyelesaian Keselamatan Microsoft, Standard Keselamatan, dan Panduan Pelaksanaan

#### Kawalan Keselamatan Lanjutan (02-Security/) - Pelaksanaan Perusahaan
- **MCP-SECURITY-CONTROLS-2025.md**: Penstrukturan semula penuh dengan rangka kerja keselamatan peringkat perusahaan
  - **9 Domain Keselamatan Menyeluruh**: Diperluaskan daripada kawalan asas kepada rangka kerja perusahaan terperinci
    - Pengesahan & Kebenaran Lanjutan dengan integrasi Microsoft Entra ID
    - Keselamatan Token & Kawalan Anti-Passthrough dengan pengesahan menyeluruh
    - Kawalan Keselamatan Sesi dengan pencegahan pengambilalihan
    - Kawalan Keselamatan Khusus AI dengan pencegahan suntikan prompt dan keracunan alat
    - Pencegahan Serangan "Confused Deputy" dengan keselamatan proksi OAuth
    - Keselamatan Pelaksanaan Alat dengan sandboxing dan pengasingan
    - Kawalan Keselamatan Rantaian Bekalan dengan pengesahan pergantungan
    - Kawalan Pemantauan & Pengesanan dengan integrasi SIEM
    - Respons & Pemulihan Insiden dengan keupayaan automatik
  - **Contoh Pelaksanaan**: Ditambah blok konfigurasi YAML terperinci dan contoh kod
  - **Integrasi Penyelesaian Microsoft**: Liputan menyeluruh perkhidmatan keselamatan Azure, GitHub Advanced Security, dan pengurusan identiti perusahaan

#### Keselamatan Topik Lanjutan (05-AdvancedTopics/mcp-security/) - Pelaksanaan Sedia Produksi
- **README.md**: Penulisan semula lengkap untuk pelaksanaan keselamatan perusahaan
  - **Penjajaran Spesifikasi Terkini**: Dikemas kini kepada Spesifikasi MCP 2025-06-18 dengan keperluan keselamatan wajib
  - **Pengesahan Dipertingkat**: Integrasi Microsoft Entra ID dengan contoh .NET dan Java Spring Security menyeluruh
  - **Integrasi Keselamatan AI**: Pelaksanaan Microsoft Prompt Shields dan Azure Content Safety dengan contoh Python terperinci
  - **Mitigasi Ancaman Lanjutan**: Contoh pelaksanaan menyeluruh untuk
    - Pencegahan Serangan "Confused Deputy" dengan PKCE dan pengesahan kebenaran pengguna
    - Pencegahan Passthrough Token dengan pengesahan audiens dan pengurusan token selamat
    - Pencegahan Pengambilalihan Sesi dengan pengikatan kriptografi dan analisis tingkah laku
  - **Integrasi Keselamatan Perusahaan**: Pemantauan Azure Application Insights, saluran pengesanan ancaman, dan keselamatan rantaian bekalan
  - **Senarai Semak Pelaksanaan**: Kawalan keselamatan wajib vs disyorkan dengan manfaat ekosistem keselamatan Microsoft

### Kualiti Dokumentasi & Penjajaran Standard
- **Rujukan Spesifikasi**: Dikemas kini semua rujukan kepada Spesifikasi MCP 2025-06-18 terkini
- **Ekosistem Keselamatan Microsoft**: Panduan integrasi dipertingkat merentas semua dokumentasi keselamatan
- **Pelaksanaan Praktikal**: Ditambah contoh kod terperinci dalam .NET, Java, dan Python dengan corak perusahaan
- **Pengurusan Sumber**: Pengkategorian menyeluruh dokumentasi rasmi, standard keselamatan, dan panduan pelaksanaan
- **Penunjuk Visual**: Penandaan jelas keperluan wajib vs amalan disyorkan


#### Konsep Teras (01-CoreConcepts/) - Pengubahsuaian Lengkap
- **Kemas Kini Versi Protokol**: Dikemas kini merujuk Spesifikasi MCP 2025-06-18 terkini dengan penomboran berasaskan tarikh (format YYYY-MM-DD)
- **Penambahbaikan Seni Bina**: Penerangan dipertingkat tentang Hos, Klien, dan Server untuk mencerminkan corak seni bina MCP kini
  - Hos kini jelas didefinisikan sebagai aplikasi AI yang menyelaras banyak sambungan klien MCP
  - Klien digambarkan sebagai penyambung protokol yang mengekalkan hubungan satu-ke-satu dengan server
  - Server dipertingkat dengan senario penyebaran tempatan vs jauh
- **Penstrukturan Semula Primitif**: Penstrukturan penuh semula primitif server dan klien
  - Primitif Server: Sumber (pangkalan data), Prompt (templat), Alat (fungsi boleh laksana) dengan penjelasan dan contoh terperinci
  - Primitif Klien: Pensampelan (penyelesaian LLM), Elicitasi (input pengguna), Log (penghuraian/pemantauan)
  - Dikemas kini dengan corak kaedah penemuan (`*/list`), pengambilan (`*/get`), dan pelaksanaan (`*/call`)
- **Seni Bina Protokol**: Memperkenalkan model seni bina dua lapisan
  - Lapisan Data: Asas JSON-RPC 2.0 dengan pengurusan kitar hayat dan primitif
  - Lapisan Pengangkutan: STDIO (tempatan) dan HTTP Boleh Alir dengan SSE (jarak jauh) mekanisme pengangkutan
- **Rangka Kerja Keselamatan**: Prinsip keselamatan menyeluruh termasuk persetujuan pengguna eksplisit, perlindungan privasi data, keselamatan pelaksanaan alat, dan keselamatan lapisan pengangkutan
- **Corak Komunikasi**: Mesej protokol dikemas kini untuk menunjukkan inisialisasi, penemuan, pelaksanaan, dan aliran pemberitahuan
- **Contoh Kod**: Contoh berbilang bahasa diperbaharui (.NET, Java, Python, JavaScript) untuk mencerminkan corak SDK MCP terkini

#### Keselamatan (02-Security/) - Penstrukturan Semula Keselamatan Menyeluruh  
- **Penjajaran Standard**: Penjajaran penuh dengan keperluan keselamatan Spesifikasi MCP 2025-06-18
- **Evolusi Pengesahan**: Didokumenkan evolusi daripada pelayan OAuth tersuai kepada delegasi penyedia identiti luaran (Microsoft Entra ID)
- **Analisis Ancaman Khusus AI**: Liputan dipertingkat mengenai vektor serangan AI moden
  - Senario serangan suntikan prompt terperinci dengan contoh dunia nyata
  - Mekanisme keracunan alat dan corak serangan "tarik permaidani"
  - Keracunan tetingkap konteks dan serangan kekeliruan model
- **Penyelesaian Keselamatan AI Microsoft**: Liputan menyeluruh ekosistem keselamatan Microsoft
  - AI Prompt Shields dengan pengesanan lanjutan, penyorotan, dan teknik pembatas
  - Corak integrasi Azure Content Safety
  - GitHub Advanced Security untuk perlindungan rantaian bekalan
- **Mitigasi Ancaman Lanjutan**: Kawalan keselamatan terperinci untuk
  - Pengambilalihan sesi dengan senario serangan khusus MCP dan keperluan ID sesi kriptografi
  - Masalah "Confused deputy" dalam senario proksi MCP dengan keperluan persetujuan eksplisit
  - Kerentanan passthrough token dengan kawalan pengesahan wajib
- **Keselamatan Rantaian Bekalan**: Liputan diperluas rantaian bekalan AI termasuk model asas, perkhidmatan embedding, penyedia konteks, dan API pihak ketiga
- **Keselamatan Asas**: Integrasi dipertingkat dengan corak keselamatan perusahaan termasuk seni bina kepercayaan sifar dan ekosistem keselamatan Microsoft
- **Pengurusan Sumber**: Pautan sumber komprehensif dikategorikan mengikut jenis (Dokumentasi Rasmi, Standard, Penyelidikan, Penyelesaian Microsoft, Panduan Pelaksanaan)

### Penambahbaikan Kualiti Dokumentasi
- **Objektif Pembelajaran Berstruktur**: Objektif pembelajaran diperkuat dengan hasil spesifik dan boleh dilaksanakan 
- **Rujukan Silang**: Ditambah pautan antara topik keselamatan dan konsep teras yang berkaitan
- **Maklumat Terkini**: Dikemas kini semua rujukan tarikh dan pautan spesifikasi kepada standard terkini
- **Panduan Pelaksanaan**: Ditambah panduan pelaksanaan spesifik dan boleh dilaksanakan merentas kedua-dua seksyen

## 16 Julai 2025

### Penambahbaikan README dan Navigasi
- Reka bentuk semula sepenuhnya navigasi kurikulum dalam README.md
- Menggantikan tag `<details>` dengan format jadual yang lebih mudah diakses
- Mewujudkan pilihan susun atur alternatif dalam folder "alternative_layouts" baru
- Menambah contoh navigasi gaya kad, tab, dan akordion
- Mengemas kini bahagian struktur repositori untuk memasukkan semua fail terkini
- Mempertingkatkan bahagian "Cara Menggunakan Kurikulum Ini" dengan cadangan jelas
- Mengemaskini pautan spesifikasi MCP untuk menunjuk ke URL yang betul
- Menambah bahagian Kejuruteraan Konteks (5.14) ke struktur kurikulum

### Kemas Kini Panduan Kajian
- Panduan kajian disemak semula sepenuhnya selaras dengan struktur repositori terkini
- Menambah seksyen baru untuk Klien MCP dan Alat, serta Server MCP Popular
- Mengupdate Peta Kurikulum Visual untuk mencerminkan semua topik dengan tepat
- Mempertingkatkan penerangan Topik Lanjutan untuk merangkumi semua bidang khusus
- Mengemas kini bahagian Kajian Kes untuk mencerminkan contoh sebenar
- Menambah changelog komprehensif ini

### Sumbangan Komuniti (06-CommunityContributions/)
- Menambah maklumat terperinci tentang server MCP untuk penjanaan imej
- Menambah seksyen komprehensif tentang penggunaan Claude di VSCode
- Menambah arahan penyediaan dan penggunaan klien terminal Cline
- Mengemas kini seksyen klien MCP untuk memasukkan semua pilihan klien popular
- Mempertingkatkan contoh sumbangan dengan sampel kod yang lebih tepat

### Topik Lanjutan (05-AdvancedTopics/)
- Mengatur semua folder topik khusus dengan penamaan konsisten
- Menambah bahan dan contoh kejuruteraan konteks
- Menambah dokumentasi integrasi agen Foundry
- Mempertingkatkan dokumentasi integrasi keselamatan Entra ID

## 11 Jun 2025

### Penciptaan Awal
- Mengeluarkan versi pertama kurikulum MCP untuk Pemula

- Membina struktur asas untuk semua 10 seksyen utama
- Melaksanakan Peta Kurikulum Visual untuk navigasi
- Menambah projek contoh awal dalam pelbagai bahasa pengaturcaraan

### Bermula (03-GettingStarted/)
- Membuat contoh pelaksanaan pelayan pertama
- Menambah panduan pembangunan klien
- Termasuk arahan integrasi klien LLM
- Menambah dokumentasi integrasi VS Code
- Melaksanakan contoh pelayan Server-Sent Events (SSE)

### Konsep Teras (01-CoreConcepts/)
- Menambah penjelasan terperinci tentang seni bina klien-pelayan
- Membuat dokumentasi komponen protokol utama
- Mendedahkan corak pemesejan dalam MCP

## 23 Mei, 2025

### Struktur Repositori
- Memulakan repositori dengan struktur folder asas
- Membuat fail README untuk setiap seksyen utama
- Menyediakan infrastruktur terjemahan
- Menambah aset imej dan rajah

### Dokumentasi
- Membuat README.md awal dengan gambaran keseluruhan kurikulum
- Menambah CODE_OF_CONDUCT.md dan SECURITY.md
- Menyediakan SUPPORT.md dengan panduan mendapatkan bantuan
- Membuat struktur panduan belajar awal

## 15 April, 2025

### Perancangan dan Kerangka Kerja
- Perancangan awal untuk kurikulum MCP untuk Pemula
- Menetapkan objektif pembelajaran dan audiens sasaran
- Menggariskan struktur 10 seksyen kurikulum
- Membangunkan kerangka konseptual untuk contoh dan kajian kes
- Membuat contoh prototaip awal untuk konsep utama

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->