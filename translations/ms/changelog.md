# Changelog: Kurikulum MCP untuk Pemula

Dokumen ini berfungsi sebagai rekod semua perubahan penting yang dibuat pada kurikulum Model Context Protocol (MCP) untuk Pemula. Perubahan didokumentasikan dalam susunan kronologi terbalik (perubahan terbaru dahulu).

## 18 Disember, 2025

### Kemas Kini Dokumentasi Keselamatan - Spesifikasi MCP 2025-11-25

#### Amalan Terbaik Keselamatan MCP (02-Security/mcp-best-practices.md) - Kemas Kini Versi Spesifikasi
- **Kemas Kini Versi Protokol**: Dikemas kini untuk merujuk Spesifikasi MCP terkini 2025-11-25 (dikeluarkan 25 November, 2025)
  - Dikemas kini semua rujukan versi spesifikasi dari 2025-06-18 ke 2025-11-25
  - Dikemas kini rujukan tarikh dokumen dari 18 Ogos, 2025 ke 18 Disember, 2025
  - Disahkan semua URL spesifikasi menunjuk ke dokumentasi terkini
- **Pengesahan Kandungan**: Pengesahan menyeluruh amalan terbaik keselamatan mengikut piawaian terkini
  - **Penyelesaian Keselamatan Microsoft**: Disahkan istilah dan pautan terkini untuk Prompt Shields (sebelumnya "Pengesanan risiko Jailbreak"), Azure Content Safety, Microsoft Entra ID, dan Azure Key Vault
  - **Keselamatan OAuth 2.1**: Disahkan kesesuaian dengan amalan terbaik keselamatan OAuth terkini
  - **Piawaian OWASP**: Disahkan rujukan OWASP Top 10 untuk LLM kekal terkini
  - **Perkhidmatan Azure**: Disahkan semua pautan dokumentasi Microsoft Azure dan amalan terbaik
- **Pematuhan Piawaian**: Semua piawaian keselamatan yang dirujuk disahkan terkini
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
- **Kesegaran Sumber**: Disahkan semua pautan luaran ke dokumentasi Microsoft, piawaian keselamatan, dan panduan pelaksanaan
- **Liputan Amalan Terbaik**: Disahkan liputan menyeluruh pengesahan, kebenaran, ancaman khusus AI, keselamatan rantaian bekalan, dan corak perusahaan

## 6 Oktober, 2025

### Perluasan Bahagian Memulakan – Penggunaan Pelayan Lanjutan & Pengesahan Mudah

#### Penggunaan Pelayan Lanjutan (03-GettingStarted/10-advanced)
- **Bab Baru Ditambah**: Memperkenalkan panduan menyeluruh untuk penggunaan pelayan MCP lanjutan, merangkumi seni bina pelayan biasa dan tahap rendah.
  - **Pelayan Biasa vs. Tahap Rendah**: Perbandingan terperinci dan contoh kod dalam Python dan TypeScript untuk kedua-dua pendekatan.
  - **Reka Bentuk Berasaskan Pengendali**: Penjelasan pengurusan alat/sumber/prompt berasaskan pengendali untuk pelaksanaan pelayan yang boleh diskala dan fleksibel.
  - **Corak Praktikal**: Senario dunia sebenar di mana corak pelayan tahap rendah bermanfaat untuk ciri dan seni bina lanjutan.

#### Pengesahan Mudah (03-GettingStarted/11-simple-auth)
- **Bab Baru Ditambah**: Panduan langkah demi langkah untuk melaksanakan pengesahan mudah dalam pelayan MCP.
  - **Konsep Auth**: Penjelasan jelas tentang pengesahan vs. kebenaran, dan pengendalian kelayakan.
  - **Pelaksanaan Auth Asas**: Corak pengesahan berasaskan middleware dalam Python (Starlette) dan TypeScript (Express), dengan contoh kod.
  - **Perkembangan ke Keselamatan Lanjutan**: Panduan memulakan dengan auth mudah dan berkembang ke OAuth 2.1 dan RBAC, dengan rujukan modul keselamatan lanjutan.

Penambahan ini menyediakan panduan praktikal dan langsung untuk membina pelaksanaan pelayan MCP yang lebih kukuh, selamat, dan fleksibel, menghubungkan konsep asas dengan corak pengeluaran lanjutan.

## 29 September, 2025

### Makmal Integrasi Pangkalan Data Pelayan MCP - Laluan Pembelajaran Praktikal Menyeluruh

#### 11-MCPServerHandsOnLabs - Kurikulum Integrasi Pangkalan Data Lengkap Baru
- **Laluan Pembelajaran 13-Makmal Lengkap**: Ditambah kurikulum praktikal menyeluruh untuk membina pelayan MCP sedia produksi dengan integrasi pangkalan data PostgreSQL
  - **Pelaksanaan Dunia Sebenar**: Kes penggunaan analitik Zava Retail yang menunjukkan corak gred perusahaan
  - **Progresi Pembelajaran Berstruktur**:
    - **Makmal 00-03: Asas** - Pengenalan, Seni Bina Teras, Keselamatan & Multi-Tenancy, Persediaan Persekitaran
    - **Makmal 04-06: Membina Pelayan MCP** - Reka Bentuk & Skema Pangkalan Data, Pelaksanaan Pelayan MCP, Pembangunan Alat  
    - **Makmal 07-09: Ciri Lanjutan** - Integrasi Carian Semantik, Ujian & Penyahpepijatan, Integrasi VS Code
    - **Makmal 10-12: Pengeluaran & Amalan Terbaik** - Strategi Pengeluaran, Pemantauan & Kebolehlihatan, Amalan Terbaik & Pengoptimuman
  - **Teknologi Perusahaan**: Rangka kerja FastMCP, PostgreSQL dengan pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Ciri Lanjutan**: Keselamatan Tahap Baris (RLS), carian semantik, akses data berbilang penyewa, vektor embeddings, pemantauan masa nyata

#### Penyeragaman Terminologi - Penukaran Modul ke Makmal
- **Kemas Kini Dokumentasi Menyeluruh**: Dikemas kini secara sistematik semua fail README dalam 11-MCPServerHandsOnLabs untuk menggunakan terminologi "Makmal" menggantikan "Modul"
  - **Tajuk Seksyen**: Dikemas kini "Apa Yang Modul Ini Liputi" ke "Apa Yang Makmal Ini Liputi" di semua 13 makmal
  - **Penerangan Kandungan**: Ditukar "Modul ini menyediakan..." ke "Makmal ini menyediakan..." di seluruh dokumentasi
  - **Objektif Pembelajaran**: Dikemas kini "Menjelang akhir modul ini..." ke "Menjelang akhir makmal ini..."
  - **Pautan Navigasi**: Ditukar semua rujukan "Modul XX:" ke "Makmal XX:" dalam rujukan silang dan navigasi
  - **Penjejakan Penyelesaian**: Dikemas kini "Selepas menyelesaikan modul ini..." ke "Selepas menyelesaikan makmal ini..."
  - **Rujukan Teknikal Dikekalkan**: Mengekalkan rujukan modul Python dalam fail konfigurasi (contoh, `"module": "mcp_server.main"`)

#### Penambahbaikan Panduan Kajian (study_guide.md)
- **Peta Kurikulum Visual**: Ditambah bahagian baru "11. Makmal Integrasi Pangkalan Data" dengan visualisasi struktur makmal menyeluruh
- **Struktur Repositori**: Dikemas kini dari sepuluh ke sebelas bahagian utama dengan penerangan terperinci 11-MCPServerHandsOnLabs
- **Panduan Laluan Pembelajaran**: Dipertingkatkan arahan navigasi untuk merangkumi bahagian 00-11
- **Liputan Teknologi**: Ditambah butiran integrasi FastMCP, PostgreSQL, perkhidmatan Azure
- **Hasil Pembelajaran**: Menekankan pembangunan pelayan sedia produksi, corak integrasi pangkalan data, dan keselamatan perusahaan

#### Penambahbaikan Struktur README Utama
- **Terminologi Berasaskan Makmal**: Dikemas kini README.md utama dalam 11-MCPServerHandsOnLabs untuk konsisten menggunakan struktur "Makmal"
- **Organisasi Laluan Pembelajaran**: Progresi jelas dari konsep asas melalui pelaksanaan lanjutan ke pengeluaran
- **Fokus Dunia Sebenar**: Penekanan pada pembelajaran praktikal dengan corak dan teknologi gred perusahaan

### Penambahbaikan Kualiti & Konsistensi Dokumentasi
- **Penekanan Pembelajaran Praktikal**: Memperkuat pendekatan berasaskan makmal di seluruh dokumentasi
- **Fokus Corak Perusahaan**: Menonjolkan pelaksanaan sedia produksi dan pertimbangan keselamatan perusahaan
- **Integrasi Teknologi**: Liputan menyeluruh perkhidmatan Azure moden dan corak integrasi AI
- **Progresi Pembelajaran**: Laluan terstruktur jelas dari konsep asas ke pengeluaran

## 26 September, 2025

### Penambahbaikan Kajian Kes - Integrasi Daftar MCP GitHub

#### Kajian Kes (09-CaseStudy/) - Fokus Pembangunan Ekosistem
- **README.md**: Perluasan besar dengan kajian kes Daftar MCP GitHub yang menyeluruh
  - **Kajian Kes Daftar MCP GitHub**: Kajian kes menyeluruh baru yang mengkaji pelancaran Daftar MCP GitHub pada September 2025
    - **Analisis Masalah**: Pemeriksaan terperinci cabaran penemuan dan pengeluaran pelayan MCP yang terpecah-pecah
    - **Reka Bentuk Penyelesaian**: Pendekatan daftar berpusat GitHub dengan pemasangan VS Code satu klik
    - **Impak Perniagaan**: Peningkatan terukur dalam onboarding dan produktiviti pembangun
    - **Nilai Strategik**: Fokus pada pengeluaran agen modular dan interoperabiliti merentas alat
    - **Pembangunan Ekosistem**: Penempatan sebagai platform asas untuk integrasi agenik
  - **Struktur Kajian Kes Dipertingkatkan**: Dikemas kini semua tujuh kajian kes dengan format konsisten dan penerangan menyeluruh
    - Ejen Perjalanan AI Azure: Penekanan orkestrasi multi-ejen
    - Integrasi Azure DevOps: Fokus automasi aliran kerja
    - Pengambilan Dokumentasi Masa Nyata: Pelaksanaan klien konsol Python
    - Penjana Pelan Kajian Interaktif: Aplikasi web perbualan Chainlit
    - Dokumentasi Dalam Editor: Integrasi VS Code dan GitHub Copilot
    - Pengurusan API Azure: Corak integrasi API perusahaan
    - Daftar MCP GitHub: Pembangunan ekosistem dan platform komuniti
  - **Kesimpulan Menyeluruh**: Bahagian kesimpulan ditulis semula menyorot tujuh kajian kes merangkumi pelbagai dimensi pelaksanaan MCP
    - Integrasi Perusahaan, Orkestrasi Multi-Ejen, Produktiviti Pembangun
    - Pembangunan Ekosistem, Kategori Aplikasi Pendidikan
    - Wawasan dipertingkatkan ke corak seni bina, strategi pelaksanaan, dan amalan terbaik
    - Penekanan pada MCP sebagai protokol matang dan sedia produksi

#### Kemas Kini Panduan Kajian (study_guide.md)
- **Peta Kurikulum Visual**: Dikemas kini mindmap untuk memasukkan Daftar MCP GitHub dalam bahagian Kajian Kes
- **Penerangan Kajian Kes**: Dipertingkatkan dari penerangan generik ke pecahan terperinci tujuh kajian kes menyeluruh
- **Struktur Repositori**: Dikemas kini bahagian 10 untuk mencerminkan liputan kajian kes menyeluruh dengan butiran pelaksanaan khusus
- **Integrasi Changelog**: Ditambah entri 26 September, 2025 yang mendokumentasikan penambahan Daftar MCP GitHub dan penambahbaikan kajian kes
- **Kemas Kini Tarikh**: Dikemas kini cap masa footer untuk mencerminkan semakan terkini (26 September, 2025)

### Penambahbaikan Kualiti Dokumentasi
- **Peningkatan Konsistensi**: Memperkemas format dan struktur kajian kes di semua tujuh contoh
- **Liputan Menyeluruh**: Kajian kes kini merangkumi perusahaan, produktiviti pembangun, dan senario pembangunan ekosistem
- **Penempatan Strategik**: Fokus dipertingkatkan pada MCP sebagai platform asas untuk pengeluaran sistem agenik
- **Integrasi Sumber**: Dikemas kini sumber tambahan untuk memasukkan pautan Daftar MCP GitHub

## 15 September, 2025

### Perluasan Topik Lanjutan - Pengangkutan Tersuai & Kejuruteraan Konteks

#### Pengangkutan Tersuai MCP (05-AdvancedTopics/mcp-transport/) - Panduan Pelaksanaan Lanjutan Baru
- **README.md**: Panduan pelaksanaan lengkap untuk mekanisme pengangkutan MCP tersuai
  - **Pengangkutan Azure Event Grid**: Pelaksanaan pengangkutan berasaskan acara tanpa pelayan yang menyeluruh
    - Contoh C#, TypeScript, dan Python dengan integrasi Azure Functions
    - Corak seni bina berasaskan acara untuk penyelesaian MCP yang boleh diskala
    - Penerima webhook dan pengendalian mesej berasaskan push
  - **Pengangkutan Azure Event Hubs**: Pelaksanaan pengangkutan penstriman berkelajuan tinggi
    - Keupayaan penstriman masa nyata untuk senario latensi rendah
    - Strategi pembahagian dan pengurusan checkpoint
    - Pengumpulan mesej dan pengoptimuman prestasi
  - **Corak Integrasi Perusahaan**: Contoh seni bina sedia produksi
    - Pemprosesan MCP diedarkan merentas pelbagai Azure Functions
    - Seni bina pengangkutan hibrid menggabungkan pelbagai jenis pengangkutan
    - Ketahanan mesej, kebolehpercayaan, dan strategi pengendalian ralat
  - **Keselamatan & Pemantauan**: Integrasi Azure Key Vault dan corak kebolehlihatan
    - Pengesahan identiti terurus dan akses keistimewaan minimum
    - Telemetri Application Insights dan pemantauan prestasi
    - Pemutus litar dan corak ketahanan ralat
  - **Rangka Kerja Ujian**: Strategi ujian menyeluruh untuk pengangkutan tersuai
    - Ujian unit dengan test doubles dan rangka kerja mocking
    - Ujian integrasi dengan Azure Test Containers
    - Pertimbangan ujian prestasi dan beban

#### Kejuruteraan Konteks (05-AdvancedTopics/mcp-contextengineering/) - Disiplin AI Berkembang
- **README.md**: Eksplorasi menyeluruh kejuruteraan konteks sebagai bidang yang sedang berkembang
  - **Prinsip Teras**: Perkongsian konteks lengkap, kesedaran keputusan tindakan, dan pengurusan tetingkap konteks
  - **Penyelarasan Protokol MCP**: Bagaimana reka bentuk MCP menangani cabaran kejuruteraan konteks
    - Had tetingkap konteks dan strategi pemuatan progresif
    - Penentuan relevan dan pengambilan konteks dinamik
    - Pengendalian konteks berbilang mod dan pertimbangan keselamatan
  - **Pendekatan Pelaksanaan**: Seni bina berbenang tunggal vs. multi-ejen
    - Teknik pemecahan dan keutamaan konteks
    - Pemuatan progresif konteks dan strategi pemampatan
    - Pendekatan berlapis konteks dan pengoptimuman pengambilan
  - **Rangka Kerja Pengukuran**: Metrik baru untuk penilaian keberkesanan konteks
    - Kecekapan input, prestasi, kualiti, dan pertimbangan pengalaman pengguna
    - Pendekatan eksperimen untuk pengoptimuman konteks
    - Analisis kegagalan dan metodologi penambahbaikan

#### Kemas Kini Navigasi Kurikulum (README.md)
- **Struktur Modul Dipertingkatkan**: Dikemas kini jadual kurikulum untuk memasukkan topik lanjutan baru
  - Ditambah entri Kejuruteraan Konteks (5.14) dan Pengangkutan Tersuai (5.15)
  - Format konsisten dan pautan navigasi di semua modul
  - Dikemas kini penerangan untuk mencerminkan skop kandungan semasa

### Penambahbaikan Struktur Direktori
- **Penyeragaman Penamaan**: Ditukar nama "mcp transport" ke "mcp-transport" untuk konsistensi dengan folder topik lanjutan lain
- **Pengurusan Kandungan**: Semua folder 05-AdvancedTopics kini mengikuti corak penamaan konsisten (mcp-[topik])

### Penambahbaikan Kualiti Dokumentasi
- **Penyelarasan Spesifikasi MCP**: Semua kandungan baru merujuk Spesifikasi MCP 2025-06-18 terkini
- **Contoh Pelbagai Bahasa**: Contoh kod menyeluruh dalam C#, TypeScript, dan Python
- **Fokus Perusahaan**: Corak sedia produksi dan integrasi awan Azure sepanjang dokumen
- **Dokumentasi Visual**: Diagram Mermaid untuk seni bina dan visualisasi aliran

## 18 Ogos, 2025

### Kemas Kini Menyeluruh Dokumentasi - Piawaian MCP 2025-06-18

#### Amalan Terbaik Keselamatan MCP (02-Security/) - Pemodenan Lengkap
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Penulisan semula lengkap selaras dengan Spesifikasi MCP 2025-06-18
  - **Keperluan Wajib**: Ditambah keperluan MUST/MUST NOT yang jelas dari spesifikasi rasmi dengan penunjuk visual yang jelas
  - **12 Amalan Keselamatan Teras**: Disusun semula dari senarai 15 item kepada domain keselamatan yang komprehensif
    - Keselamatan Token & Pengesahan dengan integrasi pembekal identiti luaran
    - Pengurusan Sesi & Keselamatan Pengangkutan dengan keperluan kriptografi
    - Perlindungan Ancaman Khusus AI dengan integrasi Microsoft Prompt Shields
    - Kawalan Akses & Kebenaran dengan prinsip keistimewaan paling minimum
    - Keselamatan & Pemantauan Kandungan dengan integrasi Azure Content Safety
    - Keselamatan Rantaian Bekalan dengan pengesahan komponen yang komprehensif
    - Keselamatan OAuth & Pencegahan Confused Deputy dengan pelaksanaan PKCE
    - Respons Insiden & Pemulihan dengan keupayaan automatik
    - Pematuhan & Tadbir Urus dengan penjajaran peraturan
    - Kawalan Keselamatan Lanjutan dengan seni bina zero trust
    - Integrasi Ekosistem Keselamatan Microsoft dengan penyelesaian komprehensif
    - Evolusi Keselamatan Berterusan dengan amalan adaptif
  - **Penyelesaian Keselamatan Microsoft**: Panduan integrasi dipertingkatkan untuk Prompt Shields, Azure Content Safety, Entra ID, dan GitHub Advanced Security
  - **Sumber Pelaksanaan**: Pautan sumber komprehensif dikategorikan mengikut Dokumentasi MCP Rasmi, Penyelesaian Keselamatan Microsoft, Standard Keselamatan, dan Panduan Pelaksanaan

#### Kawalan Keselamatan Lanjutan (02-Security/) - Pelaksanaan Perusahaan
- **MCP-SECURITY-CONTROLS-2025.md**: Penstrukturan semula lengkap dengan rangka kerja keselamatan tahap perusahaan
  - **9 Domain Keselamatan Komprehensif**: Diperluas dari kawalan asas kepada rangka kerja perusahaan terperinci
    - Pengesahan & Pemberian Kuasa Lanjutan dengan integrasi Microsoft Entra ID
    - Keselamatan Token & Kawalan Anti-Passthrough dengan pengesahan komprehensif
    - Kawalan Keselamatan Sesi dengan pencegahan pengambilalihan
    - Kawalan Keselamatan Khusus AI dengan pencegahan suntikan prompt dan keracunan alat
    - Pencegahan Serangan Confused Deputy dengan keselamatan proksi OAuth
    - Keselamatan Pelaksanaan Alat dengan sandboxing dan pengasingan
    - Kawalan Keselamatan Rantaian Bekalan dengan pengesahan kebergantungan
    - Kawalan Pemantauan & Pengesanan dengan integrasi SIEM
    - Respons Insiden & Pemulihan dengan keupayaan automatik
  - **Contoh Pelaksanaan**: Ditambah blok konfigurasi YAML terperinci dan contoh kod
  - **Integrasi Penyelesaian Microsoft**: Liputan komprehensif perkhidmatan keselamatan Azure, GitHub Advanced Security, dan pengurusan identiti perusahaan

#### Topik Lanjutan Keselamatan (05-AdvancedTopics/mcp-security/) - Pelaksanaan Sedia Produksi
- **README.md**: Penulisan semula lengkap untuk pelaksanaan keselamatan perusahaan
  - **Penjajaran Spesifikasi Semasa**: Dikemas kini kepada Spesifikasi MCP 2025-06-18 dengan keperluan keselamatan wajib
  - **Pengesahan Dipertingkatkan**: Integrasi Microsoft Entra ID dengan contoh .NET dan Java Spring Security yang komprehensif
  - **Integrasi Keselamatan AI**: Pelaksanaan Microsoft Prompt Shields dan Azure Content Safety dengan contoh Python terperinci
  - **Mitigasi Ancaman Lanjutan**: Contoh pelaksanaan komprehensif untuk
    - Pencegahan Serangan Confused Deputy dengan PKCE dan pengesahan persetujuan pengguna
    - Pencegahan Passthrough Token dengan pengesahan audiens dan pengurusan token selamat
    - Pencegahan Pengambilalihan Sesi dengan pengikatan kriptografi dan analisis tingkah laku
  - **Integrasi Keselamatan Perusahaan**: Pemantauan Azure Application Insights, saluran pengesanan ancaman, dan keselamatan rantaian bekalan
  - **Senarai Semak Pelaksanaan**: Kawalan keselamatan wajib vs. disyorkan dengan manfaat ekosistem keselamatan Microsoft

### Kualiti Dokumentasi & Penjajaran Standard
- **Rujukan Spesifikasi**: Dikemas kini semua rujukan kepada Spesifikasi MCP semasa 2025-06-18
- **Ekosistem Keselamatan Microsoft**: Panduan integrasi dipertingkatkan di seluruh dokumentasi keselamatan
- **Pelaksanaan Praktikal**: Ditambah contoh kod terperinci dalam .NET, Java, dan Python dengan corak perusahaan
- **Pengurusan Sumber**: Pengkategorian komprehensif dokumentasi rasmi, standard keselamatan, dan panduan pelaksanaan
- **Penunjuk Visual**: Penandaan jelas keperluan wajib vs. amalan disyorkan


#### Konsep Teras (01-CoreConcepts/) - Pemodenan Lengkap
- **Kemas Kini Versi Protokol**: Dikemas kini untuk merujuk Spesifikasi MCP semasa 2025-06-18 dengan penomboran versi berasaskan tarikh (format YYYY-MM-DD)
- **Penambahbaikan Seni Bina**: Penerangan dipertingkatkan tentang Hos, Klien, dan Pelayan untuk mencerminkan corak seni bina MCP semasa
  - Hos kini jelas ditakrifkan sebagai aplikasi AI yang menyelaraskan pelbagai sambungan klien MCP
  - Klien diterangkan sebagai penyambung protokol yang mengekalkan hubungan satu-ke-satu dengan pelayan
  - Pelayan dipertingkatkan dengan senario penyebaran tempatan vs. jauh
- **Penstrukturan Semula Primitif**: Penstrukturan semula lengkap primitif pelayan dan klien
  - Primitif Pelayan: Sumber (punca data), Prompt (templat), Alat (fungsi boleh dilaksanakan) dengan penerangan dan contoh terperinci
  - Primitif Klien: Persampelan (penyempurnaan LLM), Elicitation (input pengguna), Logging (debugging/pemantauan)
  - Dikemas kini dengan corak kaedah penemuan (`*/list`), pengambilan (`*/get`), dan pelaksanaan (`*/call`) semasa
- **Seni Bina Protokol**: Memperkenalkan model seni bina dua lapisan
  - Lapisan Data: Asas JSON-RPC 2.0 dengan pengurusan kitar hayat dan primitif
  - Lapisan Pengangkutan: STDIO (tempatan) dan HTTP Boleh Alir dengan SSE (jauh) mekanisme pengangkutan
- **Rangka Kerja Keselamatan**: Prinsip keselamatan komprehensif termasuk persetujuan pengguna yang jelas, perlindungan privasi data, keselamatan pelaksanaan alat, dan keselamatan lapisan pengangkutan
- **Corak Komunikasi**: Dikemas kini mesej protokol untuk menunjukkan inisialisasi, penemuan, pelaksanaan, dan aliran pemberitahuan
- **Contoh Kod**: Contoh pelbagai bahasa (.NET, Java, Python, JavaScript) disegarkan untuk mencerminkan corak SDK MCP semasa

#### Keselamatan (02-Security/) - Penstrukturan Semula Keselamatan Komprehensif  
- **Penjajaran Standard**: Penjajaran penuh dengan keperluan keselamatan Spesifikasi MCP 2025-06-18
- **Evolusi Pengesahan**: Didokumentasikan evolusi dari pelayan OAuth tersuai kepada delegasi pembekal identiti luaran (Microsoft Entra ID)
- **Analisis Ancaman Khusus AI**: Liputan dipertingkatkan vektor serangan AI moden
  - Senario serangan suntikan prompt terperinci dengan contoh dunia sebenar
  - Mekanisme keracunan alat dan corak serangan "rug pull"
  - Keracunan tetingkap konteks dan serangan kekeliruan model
- **Penyelesaian Keselamatan AI Microsoft**: Liputan komprehensif ekosistem keselamatan Microsoft
  - AI Prompt Shields dengan pengesanan lanjutan, spotlighting, dan teknik delimiter
  - Corak integrasi Azure Content Safety
  - GitHub Advanced Security untuk perlindungan rantaian bekalan
- **Mitigasi Ancaman Lanjutan**: Kawalan keselamatan terperinci untuk
  - Pengambilalihan sesi dengan senario serangan khusus MCP dan keperluan ID sesi kriptografi
  - Masalah confused deputy dalam senario proksi MCP dengan keperluan persetujuan eksplisit
  - Kerentanan passthrough token dengan kawalan pengesahan wajib
- **Keselamatan Rantaian Bekalan**: Liputan rantaian bekalan AI diperluas termasuk model asas, perkhidmatan embeddings, penyedia konteks, dan API pihak ketiga
- **Keselamatan Asas**: Integrasi dipertingkatkan dengan corak keselamatan perusahaan termasuk seni bina zero trust dan ekosistem keselamatan Microsoft
- **Pengurusan Sumber**: Pautan sumber komprehensif dikategorikan mengikut jenis (Dokumen Rasmi, Standard, Penyelidikan, Penyelesaian Microsoft, Panduan Pelaksanaan)

### Penambahbaikan Kualiti Dokumentasi
- **Objektif Pembelajaran Berstruktur**: Objektif pembelajaran dipertingkatkan dengan hasil khusus dan boleh dilaksanakan
- **Rujukan Silang**: Ditambah pautan antara topik keselamatan dan konsep teras yang berkaitan
- **Maklumat Semasa**: Dikemas kini semua rujukan tarikh dan pautan spesifikasi kepada standard semasa
- **Panduan Pelaksanaan**: Ditambah garis panduan pelaksanaan khusus dan boleh dilaksanakan di kedua-dua bahagian

## 16 Julai 2025

### Penambahbaikan README dan Navigasi
- Reka bentuk semula lengkap navigasi kurikulum dalam README.md
- Menggantikan tag `<details>` dengan format jadual yang lebih mudah diakses
- Mewujudkan pilihan susun atur alternatif dalam folder "alternative_layouts" baru
- Menambah contoh navigasi berasaskan kad, gaya tab, dan gaya akordion
- Dikemas kini bahagian struktur repositori untuk memasukkan semua fail terkini
- Mempertingkatkan bahagian "Cara Menggunakan Kurikulum Ini" dengan cadangan jelas
- Dikemas kini pautan spesifikasi MCP untuk menunjuk ke URL yang betul
- Ditambah bahagian Kejuruteraan Konteks (5.14) ke struktur kurikulum

### Kemas Kini Panduan Kajian
- Disemak semula sepenuhnya panduan kajian untuk penjajaran dengan struktur repositori semasa
- Ditambah bahagian baru untuk Klien MCP dan Alat, serta Pelayan MCP Popular
- Dikemas kini Peta Kurikulum Visual untuk mencerminkan semua topik dengan tepat
- Mempertingkatkan penerangan Topik Lanjutan untuk merangkumi semua bidang khusus
- Dikemas kini bahagian Kajian Kes untuk mencerminkan contoh sebenar
- Ditambah log perubahan komprehensif ini

### Sumbangan Komuniti (06-CommunityContributions/)
- Ditambah maklumat terperinci tentang pelayan MCP untuk penjanaan imej
- Ditambah bahagian komprehensif mengenai penggunaan Claude dalam VSCode
- Ditambah arahan penyediaan dan penggunaan klien terminal Cline
- Dikemas kini bahagian klien MCP untuk memasukkan semua pilihan klien popular
- Mempertingkatkan contoh sumbangan dengan sampel kod yang lebih tepat

### Topik Lanjutan (05-AdvancedTopics/)
- Mengatur semua folder topik khusus dengan penamaan konsisten
- Ditambah bahan dan contoh kejuruteraan konteks
- Ditambah dokumentasi integrasi agen Foundry
- Mempertingkatkan dokumentasi integrasi keselamatan Entra ID

## 11 Jun 2025

### Penciptaan Awal
- Menerbitkan versi pertama kurikulum MCP untuk Pemula
- Mewujudkan struktur asas untuk semua 10 bahagian utama
- Melaksanakan Peta Kurikulum Visual untuk navigasi
- Ditambah projek contoh awal dalam pelbagai bahasa pengaturcaraan

### Memulakan (03-GettingStarted/)
- Mewujudkan contoh pelaksanaan pelayan pertama
- Ditambah panduan pembangunan klien
- Termasuk arahan integrasi klien LLM
- Ditambah dokumentasi integrasi VS Code
- Melaksanakan contoh pelayan Server-Sent Events (SSE)

### Konsep Teras (01-CoreConcepts/)
- Ditambah penerangan terperinci tentang seni bina klien-pelayan
- Mewujudkan dokumentasi komponen protokol utama
- Mendokumentasikan corak mesej dalam MCP

## 23 Mei 2025

### Struktur Repositori
- Memulakan repositori dengan struktur folder asas
- Mewujudkan fail README untuk setiap bahagian utama
- Menyediakan infrastruktur terjemahan
- Ditambah aset imej dan diagram

### Dokumentasi
- Mewujudkan README.md awal dengan gambaran keseluruhan kurikulum
- Ditambah CODE_OF_CONDUCT.md dan SECURITY.md
- Menyediakan SUPPORT.md dengan panduan mendapatkan bantuan
- Mewujudkan struktur panduan kajian awal

## 15 April 2025

### Perancangan dan Rangka Kerja
- Perancangan awal untuk kurikulum MCP untuk Pemula
- Menentukan objektif pembelajaran dan audiens sasaran
- Merangka struktur 10 bahagian kurikulum
- Membangunkan rangka kerja konseptual untuk contoh dan kajian kes
- Mewujudkan contoh prototaip awal untuk konsep utama

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->