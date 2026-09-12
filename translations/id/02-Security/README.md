# Keamanan MCP: Perlindungan Komprehensif untuk Sistem AI

[![Praktik Terbaik Keamanan MCP](../../../translated_images/id/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Klik gambar di atas untuk menonton video pelajaran ini)_

Keamanan adalah dasar dari desain sistem AI, itulah sebabnya kami memprioritaskannya sebagai bagian kedua kami. Ini selaras dengan prinsip **Secure by Design** Microsoft dari [Inisiatif Masa Depan Aman](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) menghadirkan kemampuan baru yang kuat untuk aplikasi yang digerakkan oleh AI sekaligus memperkenalkan tantangan keamanan unik yang melampaui risiko perangkat lunak tradisional. Sistem MCP menghadapi kekhawatiran keamanan yang sudah mapan (pengkodean aman, hak akses minimum, keamanan rantai pasokan) serta ancaman baru spesifik AI termasuk injeksi prompt, pemusnahan alat, pembajakan sesi, serangan delegasi bingung, kerentanan token passthrough, dan modifikasi kemampuan dinamis.

Pelajaran ini mengeksplorasi risiko keamanan paling kritis dalam implementasi MCP—meliputi autentikasi, otorisasi, izin berlebihan, injeksi prompt tidak langsung, keamanan sesi, masalah delegasi bingung, manajemen token, dan kerentanan rantai pasokan. Anda akan mempelajari kontrol dan praktik terbaik yang dapat dilakukan untuk mengurangi risiko ini sambil memanfaatkan solusi Microsoft seperti Prompt Shields, Azure Content Safety, dan GitHub Advanced Security untuk memperkuat penggunaan MCP Anda.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- **Mengidentifikasi Ancaman Spesifik MCP**: Mengenali risiko keamanan unik dalam sistem MCP termasuk injeksi prompt, pemusnahan alat, izin berlebihan, pembajakan sesi, masalah delegasi bingung, kerentanan token passthrough, dan risiko rantai pasokan
- **Menerapkan Kontrol Keamanan**: Mengimplementasikan mitigasi efektif termasuk autentikasi kuat, akses hak minimal, manajemen token aman, kontrol keamanan sesi, dan verifikasi rantai pasokan
- **Memanfaatkan Solusi Keamanan Microsoft**: Memahami dan menerapkan Microsoft Prompt Shields, Azure Content Safety, dan GitHub Advanced Security untuk perlindungan beban kerja MCP
- **Memvalidasi Keamanan Alat**: Mengenali pentingnya validasi metadata alat, pemantauan perubahan dinamis, dan pertahanan terhadap serangan injeksi prompt tidak langsung
- **Mengintegrasikan Praktik Terbaik**: Menggabungkan fondasi keamanan yang sudah mapan (pengkodean aman, penguatan server, kepercayaan nol) dengan kontrol spesifik MCP untuk perlindungan komprehensif

# Arsitektur & Kontrol Keamanan MCP

Implementasi MCP modern membutuhkan pendekatan keamanan berlapis yang menangani keamanan perangkat lunak tradisional sekaligus ancaman spesifik AI. Spesifikasi MCP yang terus berkembang dengan cepat terus mematangkan kontrol keamanannya, memungkinkan integrasi lebih baik dengan arsitektur keamanan perusahaan dan praktik terbaik yang sudah mapan.

Penelitian dari [Microsoft Digital Defense Report](https://aka.ms/mddr) menunjukkan bahwa **98% pelanggaran yang dilaporkan dapat dicegah dengan kebersihan keamanan yang kuat**. Strategi perlindungan paling efektif menggabungkan praktik keamanan dasar dengan kontrol spesifik MCP—langkah keamanan dasar yang terbukti tetap paling berdampak dalam mengurangi risiko keamanan secara keseluruhan.

## Lanskap Keamanan Saat Ini

> **Catatan:** Bab ini menggabungkan kontrol keamanan MCP yang sudah mapan dengan
> pedoman otorisasi **Spesifikasi MCP 2026-07-28** saat ini. Selalu merujuk
> pada [Spesifikasi MCP](https://modelcontextprotocol.io/specification/2026-07-28/) saat ini,
> [repositori MCP GitHub](https://github.com/modelcontextprotocol), dan
> [dokumentasi praktik terbaik keamanan](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> saat mengimplementasikan kode yang sensitif terhadap keamanan.

> **Pembaharuan Otorisasi:** MCP `2026-07-28` mengharuskan klien memvalidasi
> parameter `iss` pada respons otorisasi (RFC 9207) dan mengikat kredensial
> terdaftar ke server otorisasi yang mengeluarkan. Pendaftaran Klien Dinamis
> sudah tidak digunakan; implementasi baru harus menggunakan Dokumen Metadata ID Klien.
> Lihat [Apa yang Berubah di MCP: Spesifikasi 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> untuk daftar lengkap perubahan otorisasi.

## 🏔️ Lokakarya Puncak Keamanan MCP (Sherpa)

Untuk **pelatihan keamanan praktis**, kami sangat merekomendasikan **Lokakarya Puncak Keamanan MCP** (Sherpa) - ekspedisi terpandu yang komprehensif untuk mengamankan server MCP di Microsoft Azure.

### Gambaran Lokakarya

[Lokakarya Puncak Keamanan MCP](https://azure-samples.github.io/sherpa/) menyediakan pelatihan keamanan praktis dan dapat dilakukan melalui metodologi yang sudah terbukti "rentan → eksploitasi → perbaikan → validasi". Anda akan:

- **Belajar dengan Memecahkan Masalah**: Mengalami kerentanan secara langsung dengan mengeksploitasi server yang sengaja tidak aman
- **Menggunakan Keamanan Asli Azure**: Memanfaatkan Azure Entra ID, Key Vault, API Management, dan AI Content Safety
- **Mengikuti Prinsip Pertahanan Berlapis**: Lanjutkan melalui berbagai kamp membangun lapisan keamanan komprehensif
- **Menerapkan Standar OWASP**: Setiap teknik sesuai dengan [Panduan Keamanan MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/)
- **Mendapatkan Kode Produksi**: Mendapatkan implementasi yang berfungsi dan telah diuji

### Rute Ekspedisi

| Kamp | Fokus | Risiko OWASP yang Dicakup |
|------|-------|---------------------------|
| **Base Camp** | Dasar MCP & kerentanan autentikasi | MCP01, MCP07 |
| **Kamp 1: Identitas** | OAuth 2.1, Identitas Terkelola Azure, Key Vault | MCP01, MCP02, MCP07 |
| **Kamp 2: Gateway** | Manajemen API, Endpoint Privat, tata kelola | MCP02, MCP06, MCP07, MCP09 |
| **Kamp 3: Keamanan I/O** | Injeksi prompt, perlindungan PII, keamanan konten | MCP03, MCP05, MCP06, MCP10 |
| **Kamp 4: Pemantauan** | Log Analytics, dasbor, deteksi ancaman | MCP04, MCP08 |
| **Puncak** | Tes integrasi Tim Merah / Tim Biru | Semua |

**Mulai**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## 10 Risiko Keamanan Teratas MCP OWASP

[Panduan Keamanan MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/) merinci sepuluh risiko keamanan paling kritis untuk implementasi MCP:

| Risiko | Deskripsi | Mitigasi Azure |
|------|-------------|------------------|
| **MCP01** | Manajemen Token & Paparan Rahasia yang Buruk | Azure Key Vault, Identitas Terkelola |
| **MCP02** | Eskalasi Hak Akses melalui Scope Creep | RBAC, Akses Bersyarat |
| **MCP03** | Pemusnahan Alat | Validasi alat, verifikasi integritas |
| **MCP04** | Serangan Rantai Pasokan Perangkat Lunak & Pemalsuan Dependensi | GitHub Advanced Security, pemindaian dependensi |
| **MCP05** | Injeksi Perintah & Eksekusi | Validasi input, sandboxing |
| **MCP06** | Penyalahgunaan Alur Niat | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Autentikasi & Otorisasi yang Tidak Memadai | Azure Entra ID, OAuth 2.1 dengan PKCE |
| **MCP08** | Kurangnya Audit dan Telemetri | Azure Monitor, Application Insights |
| **MCP09** | Server MCP Bayangan | Tata kelola API Center, isolasi jaringan |
| **MCP10** | Injeksi Konteks & Pembagian Berlebihan | Klasifikasi data, eksposur minimal |

### Evolusi Autentikasi MCP

Spesifikasi MCP telah berkembang secara signifikan dalam pendekatannya terhadap autentikasi dan otorisasi:

- **Pendekatan Awal**: Spesifikasi awal mengharuskan pengembang mengimplementasikan server autentikasi khusus, dengan server MCP bertindak sebagai Server Otorisasi OAuth 2.0 yang mengelola autentikasi pengguna secara langsung
- **Standar Saat Ini (`2026-07-28`)**: Server MCP dapat mendelegasikan autentikasi
  ke penyedia identitas eksternal seperti Microsoft Entra ID. Klien juga harus
  menerapkan persyaratan validasi penerbit dan pengikatan kredensial saat ini.
- **Keamanan Lapisan Transport**: Dukungan yang diperkuat untuk mekanisme transportasi aman dengan pola autentikasi yang tepat untuk koneksi lokal (STDIO) dan jarak jauh (Streamable HTTP)

## Keamanan Autentikasi & Otorisasi

### Tantangan Keamanan Saat Ini

Implementasi MCP modern menghadapi beberapa tantangan autentikasi dan otorisasi:

### Risiko & Vektor Ancaman

- **Logika Otorisasi yang Salah Konfigurasi**: Implementasi otorisasi yang cacat dalam server MCP dapat mengekspos data sensitif dan salah menerapkan kontrol akses
- **Kompromi Token OAuth**: Pencurian token server MCP lokal memungkinkan penyerang menyamar sebagai server dan mengakses layanan hilir
- **Kerentanan Token Passthrough**: Penanganan token yang tidak tepat menciptakan pengabaian kontrol keamanan dan celah akuntabilitas
- **Izin Berlebihan**: Server MCP yang memiliki hak berlebihan melanggar prinsip hak akses minimum dan memperluas permukaan serangan

#### Token Passthrough: Anti-Polanya yang Kritis

**Token passthrough secara eksplisit dilarang** dalam spesifikasi otorisasi MCP saat ini karena implikasi keamanannya yang parah:

##### Penghindaran Kontrol Keamanan
- Server MCP dan API hilir menerapkan kontrol keamanan penting (pembatasan laju, validasi permintaan, pemantauan lalu lintas) yang bergantung pada validasi token yang tepat
- Penggunaan token langsung dari klien ke API melewati perlindungan esensial ini, merusak arsitektur keamanan

##### Tantangan Akuntabilitas & Audit  
- Server MCP tidak dapat membedakan antara klien yang menggunakan token yang diterbitkan dari hulu, memutuskan jejak audit
- Log server sumber daya hilir menunjukkan asal permintaan yang menyesatkan daripada perantara server MCP yang sebenarnya
- Investigasi insiden dan audit kepatuhan menjadi jauh lebih sulit

##### Risiko Eksfiltrasi Data
- Klaim token yang tidak divalidasi memungkinkan aktor jahat dengan token curian menggunakan server MCP sebagai proxy untuk eksfiltrasi data
- Pelanggaran batas kepercayaan memungkinkan pola akses tidak sah yang melewati kontrol keamanan yang dimaksudkan

##### Vektor Serangan Multi-Layanan
- Token yang dikompromikan yang diterima oleh beberapa layanan memungkinkan pergerakan lateral di sistem yang terhubung
- Asumsi kepercayaan antara layanan dapat dilanggar ketika asal token tidak dapat diverifikasi

### Kontrol & Mitigasi Keamanan

**Persyaratan Keamanan Kritis:**

> **WAJIB**: Server MCP **TIDAK BOLEH** menerima token apapun yang tidak secara eksplisit diterbitkan untuk server MCP

#### Kontrol Autentikasi & Otorisasi

- **Tinjauan Otorisasi yang Ketat**: Lakukan audit komprehensif atas logika otorisasi server MCP untuk memastikan hanya pengguna dan klien yang dimaksudkan yang dapat mengakses sumber daya sensitif
  - **Panduan Implementasi**: [Azure API Management sebagai Gateway Autentikasi untuk Server MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integrasi Identitas**: [Menggunakan Microsoft Entra ID untuk Autentikasi Server MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Manajemen Token Aman**: Terapkan [praktik terbaik validasi token dan siklus hidup Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validasi klaim audiens token sesuai dengan identitas server MCP
  - Terapkan rotasi dan kebijakan kedaluwarsa token yang tepat
  - Cegah serangan pengulangan token dan penggunaan tanpa izin

- **Penyimpanan Token yang Dilindungi**: Amankan penyimpanan token dengan enkripsi baik saat diam maupun saat transmisi
  - **Praktik Terbaik**: [Pedoman Penyimpanan Token Aman dan Enkripsi](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementasi Kontrol Akses

- **Prinsip Hak Akses Minimum**: Berikan server MCP hanya izin minimum yang diperlukan untuk fungsi yang dimaksudkan
  - Tinjau dan perbarui izin secara berkala untuk mencegah hak akses yang meluas
  - **Dokumentasi Microsoft**: [Akses Dengan Hak Minimum yang Aman](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Kontrol Akses Berbasis Peran (RBAC)**: Terapkan penetapan peran yang sangat terperinci
  - Fokuskan peran secara ketat pada sumber daya dan tindakan tertentu
  - Hindari izin yang luas atau tidak perlu yang memperluas permukaan serangan

- **Pemantauan Izin Berkelanjutan**: Terapkan audit dan pemantauan akses yang berkelanjutan
  - Pantau pola penggunaan izin untuk anomali
  - Segera perbaiki hak akses yang berlebihan atau tidak digunakan

## Ancaman Keamanan Khusus AI

### Serangan Injeksi Prompt & Manipulasi Alat

Implementasi MCP modern menghadapi vektor serangan AI spesifik yang canggih yang tidak sepenuhnya dapat diatasi oleh langkah keamanan tradisional:

#### **Injeksi Prompt Tidak Langsung (Injeksi Prompt Lintas Domain)**

**Injeksi Prompt Tidak Langsung** merupakan salah satu kerentanan paling kritis dalam sistem AI yang diaktifkan MCP. Penyerang menyisipkan instruksi berbahaya dalam konten eksternal—dokumen, halaman web, email, atau sumber data—yang kemudian diproses oleh sistem AI sebagai perintah sah.

**Skenario Serangan:**
- **Injeksi Berbasis Dokumen**: Instruksi berbahaya tersembunyi dalam dokumen yang diproses yang memicu tindakan AI yang tidak diinginkan
- **Eksploitasi Konten Web**: Halaman web yang dikompromikan berisi prompt tertanam yang memanipulasi perilaku AI saat dikumpulkan
- **Serangan Berbasis Email**: Prompt berbahaya dalam email yang menyebabkan asisten AI membocorkan informasi atau melakukan tindakan tanpa izin
- **Kontaminasi Sumber Data**: Basis data atau API yang dikompromikan menyajikan konten tercemar ke sistem AI

**Dampak Dunia Nyata**: Serangan ini dapat mengakibatkan eksfiltrasi data, pelanggaran privasi, pembuatan konten berbahaya, dan manipulasi interaksi pengguna. Untuk analisis mendalam, lihat [Injeksi Prompt di MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Diagram Serangan Injeksi Prompt](../../../translated_images/id/prompt-injection.ed9fbfde297ca877.webp)

#### **Serangan Pemusnahan Alat**

**Pemusnahan Alat** menargetkan metadata yang mendefinisikan alat MCP, mengeksploitasi bagaimana LLM menafsirkan deskripsi alat dan parameter untuk membuat keputusan eksekusi.

**Mekanisme Serangan:**
- **Manipulasi Metadata**: Penyerang menyisipkan instruksi berbahaya ke dalam deskripsi alat, definisi parameter, atau contoh penggunaan
- **Instruksi Tak Terlihat**: Prompt tersembunyi dalam metadata alat yang diproses oleh model AI namun tidak terlihat oleh pengguna manusia
- **Modifikasi Alat Dinamis ("Rug Pulls")**: Alat yang disetujui pengguna kemudian diubah untuk melakukan tindakan berbahaya tanpa sepengetahuan pengguna
- **Injeksi Parameter**: Konten berbahaya tertanam dalam skema parameter alat yang memengaruhi perilaku model


**Risiko Server Tuan Rumah**: Server MCP jarak jauh menghadirkan risiko yang lebih tinggi karena definisi alat dapat diperbarui setelah persetujuan awal pengguna, menciptakan skenario di mana alat yang sebelumnya aman menjadi berbahaya. Untuk analisis menyeluruh, lihat [Serangan Keracunan Alat (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Diagram Serangan Injeksi Alat](../../../translated_images/id/tool-injection.3b0b4a6b24de6bef.webp)

#### **Vektor Serangan AI Tambahan**

- **Injeksi Prompt Lintas-Domain (XPIA)**: Serangan canggih yang memanfaatkan konten dari berbagai domain untuk melewati kontrol keamanan
- **Modifikasi Kapabilitas Dinamis**: Perubahan waktu nyata pada kapabilitas alat yang lolos dari penilaian keamanan awal
- **Keracunan Jendela Konteks**: Serangan yang memanipulasi jendela konteks besar untuk menyembunyikan instruksi berbahaya
- **Serangan Kebingungan Model**: Mengeksploitasi keterbatasan model untuk menciptakan perilaku yang tidak terduga atau tidak aman


### Dampak Risiko Keamanan AI

**Konsekuensi Berdampak Tinggi:**
- **Eksfiltrasi Data**: Akses dan pencurian data sensitif perusahaan atau pribadi tanpa izin
- **Pelanggaran Privasi**: Paparan informasi pribadi yang dapat diidentifikasi (PII) dan data bisnis rahasia  
- **Manipulasi Sistem**: Modifikasi yang tidak disengaja pada sistem dan alur kerja kritis
- **Pencurian Kredensial**: Kompromi token autentikasi dan kredensial layanan
- **Perpindahan Lateral**: Penggunaan sistem AI yang dikompromikan sebagai titik tumpu untuk serangan jaringan yang lebih luas

### Solusi Keamanan AI Microsoft

#### **Perisai Prompt AI: Perlindungan Lanjutan Terhadap Serangan Injeksi**

Microsoft **Perisai Prompt AI** menyediakan pertahanan komprehensif terhadap serangan injeksi prompt langsung maupun tidak langsung melalui beberapa lapisan keamanan:

##### **Mekanisme Perlindungan Inti:**

1. **Deteksi & Penyaringan Lanjutan**
   - Algoritma pembelajaran mesin dan teknik NLP mendeteksi instruksi berbahaya dalam konten eksternal
   - Analisis waktu nyata terhadap dokumen, halaman web, email, dan sumber data untuk ancaman tersembunyi
   - Pemahaman kontekstual pola prompt yang sah vs. berbahaya

2. **Teknik Penyinaran**  
   - Membedakan antara instruksi sistem tepercaya dan input eksternal yang berpotensi dikompromikan
   - Metode transformasi teks yang meningkatkan relevansi model sekaligus mengisolasi konten berbahaya
   - Membantu sistem AI menjaga hierarki instruksi yang benar dan mengabaikan perintah yang disuntikkan

3. **Sistem Pembatas & Penandaan Data**
   - Definisi batas eksplisit antara pesan sistem tepercaya dan teks input eksternal
   - Penanda khusus menyoroti batas antara sumber data tepercaya dan tidak tepercaya
   - Pemisahan yang jelas mencegah kebingungan instruksi dan eksekusi perintah tanpa izin

4. **Intelijen Ancaman Berkelanjutan**
   - Microsoft secara terus menerus memantau pola serangan yang muncul dan memperbarui pertahanan
   - Perburuan ancaman proaktif untuk teknik injeksi dan vektor serangan baru
   - Pembaruan rutin model keamanan untuk mempertahankan efektivitas terhadap ancaman yang berevolusi

5. **Integrasi Azure Content Safety**
   - Bagian dari suite lengkap Azure AI Content Safety
   - Deteksi tambahan untuk upaya jailbreak, konten berbahaya, dan pelanggaran kebijakan keamanan
   - Kontrol keamanan terpadu di seluruh komponen aplikasi AI

**Sumber Daya Implementasi**: [Dokumentasi Perisai Prompt Microsoft](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Perlindungan Perisai Prompt Microsoft](../../../translated_images/id/prompt-shield.ff5b95be76e9c78c.webp)


## Ancaman Keamanan MCP Lanjutan

### Kerentanan Pembajakan Sesi

**Pembajakan sesi** merupakan vektor serangan kritis dalam implementasi MCP berstatus di mana pihak tidak berwenang memperoleh dan menyalahgunakan pengenal sesi yang sah untuk menyamar sebagai klien dan melakukan tindakan tanpa otorisasi.

#### **Skenario & Risiko Serangan**

- **Injeksi Prompt Pembajakan Sesi**: Penyerang dengan ID sesi yang dicuri menyuntikkan peristiwa berbahaya ke server yang berbagi status sesi, berpotensi memicu tindakan merugikan atau mengakses data sensitif
- **Penyamaran Langsung**: ID sesi yang dicuri memungkinkan panggilan langsung ke server MCP yang melewati autentikasi, memperlakukan penyerang sebagai pengguna sah
- **Aliran Dapat Dilanjutkan yang Dikompromikan**: Penyerang dapat mengakhiri permintaan secara prematur, menyebabkan klien sah melanjutkan dengan konten yang berpotensi berbahaya

#### **Kontrol Keamanan untuk Manajemen Sesi**

**Persyaratan Kritis:**
- **Verifikasi Otorisasi**: Server MCP yang menerapkan otorisasi **HARUS** memverifikasi SEMUA permintaan masuk dan **TIDAK BOLEH** mengandalkan sesi untuk autentikasi
- **Pembuatan Sesi yang Aman**: Gunakan ID sesi yang aman secara kriptografis dan tidak deterministik yang dihasilkan dengan generator bilangan acak yang aman
- **Pengikatan Khusus Pengguna**: Kaitkan ID sesi dengan informasi khusus pengguna menggunakan format seperti `<user_id>:<session_id>` untuk mencegah penyalahgunaan sesi lintas pengguna
- **Manajemen Siklus Hidup Sesi**: Terapkan masa berlaku, rotasi, dan invalidasi yang tepat untuk membatasi jendela kerentanan
- **Keamanan Transportasi**: HTTPS wajib untuk semua komunikasi guna mencegah penyadapan ID sesi

### Masalah Deputi Bingung

**Masalah deputi bingung** terjadi ketika server MCP bertindak sebagai proxy autentikasi antara klien dan layanan pihak ketiga, menciptakan peluang untuk melewati otorisasi melalui eksploitasi ID klien statis.

#### **Mekanisme & Risiko Serangan**

- **Bypass Persetujuan Berbasis Cookie**: Autentikasi pengguna sebelumnya membuat cookie persetujuan yang dieksploitasi penyerang melalui permintaan otorisasi berbahaya dengan URI pengalihan yang dibuat khusus
- **Pencurian Kode Otorisasi**: Cookie persetujuan yang ada dapat menyebabkan server otorisasi melewati layar persetujuan, mengarahkan kode ke titik akhir yang dikendalikan penyerang  
- **Akses API Tanpa Izin**: Kode otorisasi yang dicuri memungkinkan pertukaran token dan penyamaran pengguna tanpa persetujuan eksplisit

#### **Strategi Mitigasi**

**Kontrol Wajib:**
- **Persyaratan Persetujuan Eksplisit**: Server proxy MCP yang menggunakan ID klien statis **HARUS** memperoleh persetujuan pengguna untuk setiap klien yang terdaftar secara dinamis
- **Implementasi Keamanan OAuth 2.1**: Ikuti praktik terbaik keamanan OAuth terkini termasuk PKCE (Proof Key for Code Exchange) untuk semua permintaan otorisasi
- **Validasi Klien Ketat**: Terapkan validasi ketat terhadap URI pengalihan dan pengenal klien untuk mencegah eksploitasi

### Kerentanan Token Passthrough  

**Token passthrough** merupakan pola anti eksplisit di mana server MCP menerima token klien tanpa validasi yang tepat dan meneruskannya ke API hilir, melanggar spesifikasi otorisasi MCP.

#### **Implikasi Keamanan**

- **Pengelakan Kontrol**: Penggunaan token langsung dari klien ke API melewati pembatasan laju, validasi, dan kontrol pemantauan yang penting
- **Kerusakan Jejak Audit**: Token yang diterbitkan hulu membuat identifikasi klien menjadi tidak mungkin, merusak kemampuan investigasi insiden
- **Eksfiltrasi Data Berbasis Proxy**: Token yang tidak tervalidasi memungkinkan aktor berbahaya menggunakan server sebagai proxy untuk akses data tidak sah
- **Pelanggaran Batas Kepercayaan**: Asumsi kepercayaan layanan hilir dapat dilanggar ketika asal token tidak dapat diverifikasi
- **Perluasan Serangan Multi-layanan**: Token yang dikompromikan yang diterima di beberapa layanan memungkinkan perpindahan lateral

#### **Kontrol Keamanan yang Dibutuhkan**

**Persyaratan Tidak Bisa Ditawar:**
- **Validasi Token**: Server MCP **TIDAK BOLEH** menerima token yang tidak diterbitkan secara eksplisit untuk server MCP
- **Verifikasi Audiens**: Selalu validasi klaim audiens token sesuai dengan identitas server MCP
- **Siklus Hidup Token yang Tepat**: Terapkan token akses berumur pendek dengan praktik rotasi yang aman


## Keamanan Rantai Pasok untuk Sistem AI

Keamanan rantai pasok telah berkembang melampaui ketergantungan perangkat lunak tradisional untuk mencakup seluruh ekosistem AI. Implementasi MCP modern harus secara ketat memverifikasi dan memantau semua komponen terkait AI, karena masing-masing memperkenalkan potensi kerentanan yang dapat mengkompromikan integritas sistem.

### Komponen Rantai Pasok AI yang Diperluas

**Ketergantungan Perangkat Lunak Tradisional:**
- Perpustakaan dan kerangka kerja sumber terbuka
- Gambar kontainer dan sistem dasar  
- Alat pengembangan dan jalur pembangunan
- Komponen dan layanan infrastruktur

**Elemen Rantai Pasok Khusus AI:**
- **Model Dasar**: Model yang sudah dilatih dari berbagai penyedia yang memerlukan verifikasi asal usul
- **Layanan Embedding**: Layanan vektorisasi dan pencarian semantik eksternal
- **Penyedia Konteks**: Sumber data, basis pengetahuan, dan repositori dokumen  
- **API Pihak Ketiga**: Layanan AI eksternal, jalur ML, dan titik akhir pemrosesan data
- **Artefak Model**: Bobot, konfigurasi, dan varian model yang disesuaikan
- **Sumber Data Pelatihan**: Dataset yang digunakan untuk pelatihan dan penyempurnaan model

### Strategi Keamanan Rantai Pasok Menyeluruh

#### **Verifikasi & Kepercayaan Komponen**
- **Validasi Asal Usul**: Verifikasi asal, lisensi, dan integritas semua komponen AI sebelum integrasi
- **Penilaian Keamanan**: Lakukan pemindaian kerentanan dan tinjauan keamanan untuk model, sumber data, dan layanan AI
- **Analisis Reputasi**: Evaluasi rekam jejak keamanan dan praktik penyedia layanan AI
- **Verifikasi Kepatuhan**: Pastikan semua komponen memenuhi persyaratan keamanan dan regulasi organisasi

#### **Jalur Penyebaran yang Aman**  
- **Keamanan CI/CD Otomatis**: Integrasikan pemindaian keamanan sepanjang jalur penyebaran otomatis
- **Integritas Artefak**: Terapkan verifikasi kriptografi untuk semua artefak yang disebarkan (kode, model, konfigurasi)
- **Penyebaran Bertahap**: Gunakan strategi penyebaran progresif dengan validasi keamanan di setiap tahap
- **Repositori Artefak Tepercaya**: Sebarkan hanya dari registri dan repositori artefak yang diverifikasi dan aman

#### **Pemantauan & Respons Berkelanjutan**
- **Pemindaian Ketergantungan**: Pemantauan kerentanan berkelanjutan untuk semua ketergantungan perangkat lunak dan komponen AI
- **Pemantauan Model**: Penilaian berkelanjutan terhadap perilaku model, drift performa, dan anomali keamanan
- **Pelacakan Kesehatan Layanan**: Pantau layanan AI eksternal untuk ketersediaan, insiden keamanan, dan perubahan kebijakan
- **Integrasi Intelijen Ancaman**: Gabungkan feed ancaman khusus ke risiko keamanan AI dan ML

#### **Kontrol Akses & Privilege Minimum**
- **Izin Tingkat Komponen**: Batasi akses ke model, data, dan layanan berdasarkan kebutuhan bisnis
- **Manajemen Akun Layanan**: Terapkan akun layanan khusus dengan izin minimal yang diperlukan
- **Segmentasi Jaringan**: Isolasi komponen AI dan batasi akses jaringan antar layanan
- **Kontrol Gateway API**: Gunakan gateway API terpusat untuk mengendalikan dan memantau akses ke layanan AI eksternal

#### **Respons & Pemulihan Insiden**
- **Prosedur Respons Cepat**: Proses yang ditetapkan untuk patch atau mengganti komponen AI yang dikompromikan
- **Rotasi Kredensial**: Sistem otomatis untuk merotasi rahasia, kunci API, dan kredensial layanan
- **Kemampuan Rollback**: Kemampuan untuk dengan cepat mengembalikan ke versi komponen AI yang dikenal baik sebelumnya
- **Pemulihan Pelanggaran Rantai Pasok**: Prosedur khusus untuk merespons kompromi layanan AI hulu

### Alat & Integrasi Keamanan Microsoft

**GitHub Advanced Security** menyediakan perlindungan rantai pasok komprehensif termasuk:
- **Pemindaian Rahasia**: Deteksi otomatis kredensial, kunci API, dan token dalam repositori
- **Pemindaian Ketergantungan**: Penilaian kerentanan untuk ketergantungan dan perpustakaan sumber terbuka
- **Analisis CodeQL**: Analisis kode statis untuk kerentanan keamanan dan masalah pengkodean
- **Wawasan Rantai Pasok**: Visibilitas ke kesehatan ketergantungan dan status keamanan

**Integrasi Azure DevOps & Azure Repos:**
- Integrasi pemindaian keamanan yang mulus di seluruh platform pengembangan Microsoft
- Pemeriksaan keamanan otomatis di Azure Pipelines untuk beban kerja AI
- Penegakan kebijakan untuk penyebaran komponen AI yang aman

**Praktik Internal Microsoft:**
Microsoft menerapkan praktik keamanan rantai pasok yang luas di semua produk. Pelajari pendekatan yang telah terbukti di [Perjalanan untuk Mengamankan Rantai Pasok Perangkat Lunak di Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Praktik Terbaik Keamanan Dasar

Implementasi MCP mewarisi dan membangun di atas sikap keamanan organisasi Anda yang ada. Memperkuat praktik keamanan dasar secara signifikan meningkatkan keamanan keseluruhan sistem AI dan penyebaran MCP.

### Fundamental Keamanan Inti

#### **Praktik Pengembangan Aman**
- **Kepatuhan OWASP**: Lindungi dari kerentanan aplikasi web [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- **Perlindungan Khusus AI**: Terapkan kontrol untuk [OWASP Top 10 untuk LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Manajemen Rahasia yang Aman**: Gunakan vault khusus untuk token, kunci API, dan data konfigurasi sensitif
- **Enkripsi End-to-End**: Terapkan komunikasi aman di seluruh komponen aplikasi dan aliran data
- **Validasi Input**: Validasi ketat semua input pengguna, parameter API, dan sumber data

#### **Penguatan Infrastruktur**
- **Autentikasi Multi-Faktor**: MFA wajib untuk semua akun administratif dan layanan
- **Manajemen Patch**: Patch otomatis dan tepat waktu untuk sistem operasi, kerangka kerja, dan ketergantungan  
- **Integrasi Penyedia Identitas**: Manajemen identitas terpusat melalui penyedia identitas perusahaan (Microsoft Entra ID, Active Directory)
- **Segmentasi Jaringan**: Isolasi logis komponen MCP untuk membatasi potensi perpindahan lateral
- **Prinsip Privilege Minimum**: Izin minimal yang diperlukan untuk semua komponen dan akun sistem

#### **Pemantauan & Deteksi Keamanan**
- **Pencatatan Komprehensif**: Pencatatan terperinci aktivitas aplikasi AI, termasuk interaksi klien-server MCP
- **Integrasi SIEM**: Manajemen informasi dan kejadian keamanan terpusat untuk deteksi anomali
- **Analitik Perilaku**: Pemantauan bertenaga AI untuk mendeteksi pola tidak biasa dalam sistem dan perilaku pengguna
- **Intelijen Ancaman**: Integrasi feed ancaman eksternal dan indikator kompromi (IOC)
- **Respons Insiden**: Prosedur yang terdefinisi baik untuk deteksi, respons, dan pemulihan insiden keamanan

#### **Arsitektur Zero Trust**
- **Jangan Pernah Percaya, Selalu Verifikasi**: Verifikasi berkelanjutan pengguna, perangkat, dan koneksi jaringan
- **Mikro-Segmentasi**: Kontrol jaringan granular yang mengisolasi beban kerja dan layanan individual
- **Keamanan Berbasis Identitas**: Kebijakan keamanan berdasarkan identitas terverifikasi daripada lokasi jaringan
- **Penilaian Risiko Berkelanjutan**: Evaluasi sikap keamanan dinamis berdasarkan konteks dan perilaku saat ini
- **Akses Kondisional**: Kontrol akses yang menyesuaikan berdasarkan faktor risiko, lokasi, dan kepercayaan perangkat

### Pola Integrasi Perusahaan

#### **Integrasi Ekosistem Keamanan Microsoft**
- **Microsoft Defender for Cloud**: Manajemen sikap keamanan cloud komprehensif
- **Azure Sentinel**: SIEM dan SOAR asli cloud untuk perlindungan beban kerja AI
- **Microsoft Entra ID**: Manajemen identitas dan akses perusahaan dengan kebijakan akses kondisional
- **Azure Key Vault**: Manajemen rahasia terpusat dengan perlindungan modul keamanan perangkat keras (HSM)
- **Microsoft Purview**: Tata kelola data dan kepatuhan untuk sumber data dan alur kerja AI

#### **Kepatuhan & Tata Kelola**
- **Keselarasan Regulasi**: Pastikan implementasi MCP memenuhi persyaratan kepatuhan spesifik industri (GDPR, HIPAA, SOC 2)

- **Klasifikasi Data**: Kategori dan penanganan yang tepat untuk data sensitif yang diproses oleh sistem AI
- **Jejak Audit**: Pencatatan komprehensif untuk kepatuhan regulasi dan investigasi forensik
- **Kontrol Privasi**: Implementasi prinsip privasi-dengan-desain dalam arsitektur sistem AI
- **Manajemen Perubahan**: Proses formal untuk tinjauan keamanan pada modifikasi sistem AI

Praktik dasar ini menciptakan dasar keamanan yang kokoh yang meningkatkan efektivitas kontrol keamanan spesifik MCP dan memberikan perlindungan menyeluruh untuk aplikasi yang digerakkan oleh AI.

## Poin Penting Keamanan

- **Pendekatan Keamanan Berlapis**: Gabungkan praktik keamanan dasar (pemrograman aman, hak istimewa paling sedikit, verifikasi rantai pasokan, pemantauan berkelanjutan) dengan kontrol spesifik AI untuk perlindungan menyeluruh

- **Lanskap Ancaman Khusus AI**: Sistem MCP menghadapi risiko unik seperti injeksi prompt, keracunan alat, pembajakan sesi, masalah confused deputy, kerentanan token passthrough, dan izin berlebihan yang memerlukan mitigasi khusus

- **Keunggulan Otentikasi & Otorisasi**: Terapkan otentikasi yang kuat menggunakan penyedia identitas eksternal (Microsoft Entra ID), lakukan validasi token yang tepat, dan jangan pernah menerima token yang tidak secara eksplisit diterbitkan untuk server MCP Anda

- **Pencegahan Serangan AI**: Gunakan Microsoft Prompt Shields dan Azure Content Safety untuk melindungi dari serangan injeksi prompt tidak langsung dan keracunan alat, sambil memvalidasi metadata alat dan memantau perubahan dinamis

- **Keamanan Sesi & Transportasi**: Gunakan ID sesi kriptografi yang aman dan non-deterministik yang terikat pada identitas pengguna, terapkan manajemen siklus hidup sesi yang tepat, dan jangan pernah menggunakan sesi untuk otentikasi

- **Praktik Terbaik Keamanan OAuth**: Cegah serangan confused deputy melalui persetujuan pengguna eksplisit untuk klien yang terdaftar secara dinamis, implementasi OAuth 2.1 dengan PKCE yang tepat, dan validasi URI pengalihan yang ketat  

- **Prinsip Keamanan Token**: Hindari pola anti token passthrough, validasi klaim audiens token, terapkan token yang berumur pendek dengan rotasi aman, dan pertahankan batas kepercayaan yang jelas

- **Keamanan Rantai Pasokan Menyeluruh**: Perlakukan semua komponen ekosistem AI (model, embeddings, penyedia konteks, API eksternal) dengan tingkat keamanan yang sama seperti ketergantungan perangkat lunak tradisional

- **Evolusi Berkelanjutan**: Tetap terkini dengan spesifikasi MCP yang berkembang pesat, kontribusikan standar komunitas keamanan, dan pertahankan sikap keamanan adaptif saat protokol matang

- **Integrasi Keamanan Microsoft**: Manfaatkan ekosistem keamanan Microsoft yang komprehensif (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) untuk perlindungan penerapan MCP yang ditingkatkan

## Sumber Daya Lengkap

### **Dokumentasi Keamanan Resmi MCP**
- [Spesifikasi MCP (Saat Ini: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Praktik Terbaik Keamanan MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Spesifikasi Otorisasi MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [Repositori GitHub MCP](https://github.com/modelcontextprotocol)

### **Sumber Daya Keamanan OWASP MCP**
- [Panduan Keamanan OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - OWASP MCP Top 10 yang komprehensif dengan panduan implementasi Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Risiko keamanan resmi OWASP MCP
- [Lokakarya MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Pelatihan keamanan praktis untuk MCP di Azure

### **Standar & Praktik Terbaik Keamanan**
- [Praktik Terbaik Keamanan OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Keamanan Aplikasi Web](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 untuk Model Bahasa Besar](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Laporan Pertahanan Digital Microsoft](https://aka.ms/mddr)

### **Riset & Analisis Keamanan AI**
- [Injeksi Prompt dalam MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Serangan Keracunan Alat (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Briefing Riset Keamanan MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Solusi Keamanan Microsoft**
- [Dokumentasi Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Layanan Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Keamanan Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Praktik Terbaik Manajemen Token Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Panduan Implementasi & Tutorial**
- [Azure API Management sebagai Gerbang Otentikasi MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Otentikasi Microsoft Entra ID dengan Server MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Penyimpanan dan Enkripsi Token yang Aman (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **Keamanan DevOps & Rantai Pasokan**
- [Keamanan Azure DevOps](https://azure.microsoft.com/products/devops)
- [Keamanan Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Perjalanan Keamanan Rantai Pasokan Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Dokumentasi Keamanan Tambahan**

Untuk panduan keamanan yang komprehensif, lihat dokumen khusus berikut di bagian ini:

- **[Contoh Otorisasi CIMD dan DCR](./samples/cimd-dcr-auth/README.md)** - Server sumber daya MCP TypeScript `2026-07-28` yang dapat dijalankan dengan membandingkan Dokumen Metadata Client ID yang disukai dengan fallback Pendaftaran Klien Dinamis yang usang
- **[Praktik Terbaik Keamanan MCP](./mcp-security-best-practices.md)** - Praktik terbaik keamanan lengkap untuk implementasi MCP
- **[Implementasi Azure Content Safety](./azure-content-safety-implementation.md)** - Contoh implementasi praktis untuk integrasi Azure Content Safety  
- **[Kontrol Keamanan MCP](./mcp-security-controls.md)** - Kontrol dan teknik keamanan terbaru untuk penerapan MCP
- **[Referensi Cepat Praktik Terbaik MCP](./mcp-best-practices.md)** - Panduan referensi cepat untuk praktik keamanan MCP penting
- **[BlueHat 2026: Mengamankan masa depan AI: Mengamankan MCP dengan pola pertahanan berlapis](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Pola pertahanan berlapis dari Microsoft Security Response Center (MSRC)

### **Pelatihan Keamanan Praktis**

- **[Lokakarya MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - Lokakarya praktis komprehensif untuk mengamankan server MCP di Azure dengan kemah progresif dari Base Camp ke Summit
- **[Panduan Keamanan OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)** - Arsitektur referensi dan panduan implementasi untuk semua risiko OWASP MCP Top 10

---

## Selanjutnya

Selanjutnya: [Bab 3: Memulai](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->