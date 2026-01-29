# Keamanan MCP: Perlindungan Komprehensif untuk Sistem AI

[![Praktik Terbaik Keamanan MCP](../../../translated_images/id/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Klik gambar di atas untuk menonton video pelajaran ini)_

Keamanan adalah dasar dalam desain sistem AI, itulah sebabnya kami memprioritaskannya sebagai bagian kedua. Ini sejalan dengan prinsip **Secure by Design** Microsoft dari [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) menghadirkan kemampuan baru yang kuat untuk aplikasi yang digerakkan AI sekaligus memperkenalkan tantangan keamanan unik yang melampaui risiko perangkat lunak tradisional. Sistem MCP menghadapi kekhawatiran keamanan yang sudah mapan (pengkodean aman, hak akses minimum, keamanan rantai pasokan) dan ancaman khusus AI baru termasuk injeksi prompt, keracunan alat, pembajakan sesi, serangan confused deputy, kerentanan token passthrough, dan modifikasi kapabilitas dinamis.

Pelajaran ini mengeksplorasi risiko keamanan paling kritis dalam implementasi MCP—meliputi autentikasi, otorisasi, izin berlebihan, injeksi prompt tidak langsung, keamanan sesi, masalah confused deputy, manajemen token, dan kerentanan rantai pasokan. Anda akan mempelajari kontrol yang dapat diterapkan dan praktik terbaik untuk mengurangi risiko ini sambil memanfaatkan solusi Microsoft seperti Prompt Shields, Azure Content Safety, dan GitHub Advanced Security untuk memperkuat penerapan MCP Anda.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- **Mengidentifikasi Ancaman Spesifik MCP**: Mengenali risiko keamanan unik dalam sistem MCP termasuk injeksi prompt, keracunan alat, izin berlebihan, pembajakan sesi, masalah confused deputy, kerentanan token passthrough, dan risiko rantai pasokan
- **Menerapkan Kontrol Keamanan**: Melaksanakan mitigasi efektif termasuk autentikasi yang kuat, akses hak minimum, manajemen token yang aman, kontrol keamanan sesi, dan verifikasi rantai pasokan
- **Memanfaatkan Solusi Keamanan Microsoft**: Memahami dan menerapkan Microsoft Prompt Shields, Azure Content Safety, dan GitHub Advanced Security untuk perlindungan beban kerja MCP
- **Memvalidasi Keamanan Alat**: Mengenali pentingnya validasi metadata alat, pemantauan perubahan dinamis, dan pertahanan terhadap serangan injeksi prompt tidak langsung
- **Mengintegrasikan Praktik Terbaik**: Menggabungkan dasar keamanan yang sudah mapan (pengkodean aman, penguatan server, zero trust) dengan kontrol spesifik MCP untuk perlindungan menyeluruh

# Arsitektur & Kontrol Keamanan MCP

Implementasi MCP modern memerlukan pendekatan keamanan berlapis yang menangani baik keamanan perangkat lunak tradisional maupun ancaman khusus AI. Spesifikasi MCP yang berkembang pesat terus mematangkan kontrol keamanannya, memungkinkan integrasi yang lebih baik dengan arsitektur keamanan perusahaan dan praktik terbaik yang sudah mapan.

Penelitian dari [Microsoft Digital Defense Report](https://aka.ms/mddr) menunjukkan bahwa **98% pelanggaran yang dilaporkan dapat dicegah dengan kebersihan keamanan yang kuat**. Strategi perlindungan paling efektif menggabungkan praktik keamanan dasar dengan kontrol spesifik MCP—langkah keamanan dasar yang terbukti tetap paling berdampak dalam mengurangi risiko keamanan secara keseluruhan.

## Lanskap Keamanan Saat Ini

> **Catatan:** Informasi ini mencerminkan standar keamanan MCP per **18 Desember 2025**. Protokol MCP terus berkembang dengan cepat, dan implementasi mendatang mungkin memperkenalkan pola autentikasi baru dan kontrol yang ditingkatkan. Selalu rujuk [Spesifikasi MCP](https://spec.modelcontextprotocol.io/), [repositori GitHub MCP](https://github.com/modelcontextprotocol), dan [dokumentasi praktik terbaik keamanan](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) terkini untuk panduan terbaru.

### Evolusi Autentikasi MCP

Spesifikasi MCP telah berkembang signifikan dalam pendekatannya terhadap autentikasi dan otorisasi:

- **Pendekatan Awal**: Spesifikasi awal mengharuskan pengembang mengimplementasikan server autentikasi khusus, dengan server MCP bertindak sebagai OAuth 2.0 Authorization Server yang mengelola autentikasi pengguna secara langsung
- **Standar Saat Ini (2025-11-25)**: Spesifikasi terbaru memungkinkan server MCP mendelegasikan autentikasi ke penyedia identitas eksternal (seperti Microsoft Entra ID), meningkatkan postur keamanan dan mengurangi kompleksitas implementasi
- **Keamanan Lapisan Transportasi**: Dukungan yang ditingkatkan untuk mekanisme transportasi aman dengan pola autentikasi yang tepat untuk koneksi lokal (STDIO) dan jarak jauh (Streamable HTTP)

## Keamanan Autentikasi & Otorisasi

### Tantangan Keamanan Saat Ini

Implementasi MCP modern menghadapi beberapa tantangan autentikasi dan otorisasi:

### Risiko & Vektor Ancaman

- **Logika Otorisasi Salah Konfigurasi**: Implementasi otorisasi yang cacat di server MCP dapat mengekspos data sensitif dan menerapkan kontrol akses secara keliru
- **Kompromi Token OAuth**: Pencurian token server MCP lokal memungkinkan penyerang menyamar sebagai server dan mengakses layanan hilir
- **Kerentanan Token Passthrough**: Penanganan token yang tidak tepat menciptakan bypass kontrol keamanan dan celah akuntabilitas
- **Izin Berlebihan**: Server MCP dengan hak akses berlebihan melanggar prinsip hak minimum dan memperluas permukaan serangan

#### Token Passthrough: Anti-Polanya yang Kritis

**Token passthrough secara eksplisit dilarang** dalam spesifikasi otorisasi MCP saat ini karena implikasi keamanan yang serius:

##### Pengelakan Kontrol Keamanan
- Server MCP dan API hilir menerapkan kontrol keamanan penting (pembatasan laju, validasi permintaan, pemantauan lalu lintas) yang bergantung pada validasi token yang tepat
- Penggunaan token langsung dari klien ke API melewati perlindungan penting ini, merusak arsitektur keamanan

##### Tantangan Akuntabilitas & Audit  
- Server MCP tidak dapat membedakan antara klien yang menggunakan token yang diterbitkan hulu, memutus jejak audit
- Log server sumber daya hilir menunjukkan asal permintaan yang menyesatkan, bukan perantara server MCP yang sebenarnya
- Investigasi insiden dan audit kepatuhan menjadi jauh lebih sulit

##### Risiko Eksfiltrasi Data
- Klaim token yang tidak tervalidasi memungkinkan aktor jahat dengan token curian menggunakan server MCP sebagai proxy untuk eksfiltrasi data
- Pelanggaran batas kepercayaan memungkinkan pola akses tidak sah yang melewati kontrol keamanan yang dimaksudkan

##### Vektor Serangan Multi-Layanan
- Token yang dikompromikan diterima oleh banyak layanan memungkinkan pergerakan lateral di seluruh sistem yang terhubung
- Asumsi kepercayaan antar layanan dapat dilanggar ketika asal token tidak dapat diverifikasi

### Kontrol Keamanan & Mitigasi

**Persyaratan Keamanan Kritis:**

> **WAJIB**: Server MCP **TIDAK BOLEH** menerima token apa pun yang tidak secara eksplisit diterbitkan untuk server MCP tersebut

#### Kontrol Autentikasi & Otorisasi

- **Tinjauan Otorisasi yang Ketat**: Lakukan audit menyeluruh terhadap logika otorisasi server MCP untuk memastikan hanya pengguna dan klien yang dimaksudkan yang dapat mengakses sumber daya sensitif
  - **Panduan Implementasi**: [Azure API Management sebagai Gerbang Autentikasi untuk Server MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integrasi Identitas**: [Menggunakan Microsoft Entra ID untuk Autentikasi Server MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Manajemen Token yang Aman**: Terapkan [praktik terbaik validasi token dan siklus hidup Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validasi klaim audiens token sesuai identitas server MCP
  - Terapkan rotasi token dan kebijakan kadaluarsa yang tepat
  - Cegah serangan replay token dan penggunaan tidak sah

- **Penyimpanan Token yang Terlindungi**: Amankan penyimpanan token dengan enkripsi baik saat diam maupun dalam transit
  - **Praktik Terbaik**: [Panduan Penyimpanan dan Enkripsi Token yang Aman](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementasi Kontrol Akses

- **Prinsip Hak Minimum**: Berikan server MCP hanya izin minimum yang diperlukan untuk fungsi yang dimaksudkan
  - Tinjauan dan pembaruan izin secara berkala untuk mencegah peningkatan hak akses yang tidak diinginkan
  - **Dokumentasi Microsoft**: [Akses Hak Minimum yang Aman](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Kontrol Akses Berbasis Peran (RBAC)**: Terapkan penugasan peran yang terperinci
  - Batasi cakupan peran secara ketat pada sumber daya dan tindakan spesifik
  - Hindari izin luas atau tidak perlu yang memperluas permukaan serangan

- **Pemantauan Izin Berkelanjutan**: Terapkan audit dan pemantauan akses secara terus-menerus
  - Pantau pola penggunaan izin untuk anomali
  - Segera perbaiki hak akses berlebihan atau yang tidak digunakan

## Ancaman Keamanan Khusus AI

### Serangan Injeksi Prompt & Manipulasi Alat

Implementasi MCP modern menghadapi vektor serangan khusus AI yang canggih yang tidak dapat sepenuhnya diatasi oleh langkah keamanan tradisional:

#### **Injeksi Prompt Tidak Langsung (Injeksi Prompt Lintas Domain)**

**Injeksi Prompt Tidak Langsung** merupakan salah satu kerentanan paling kritis dalam sistem AI yang diaktifkan MCP. Penyerang menyisipkan instruksi berbahaya dalam konten eksternal—dokumen, halaman web, email, atau sumber data—yang kemudian diproses sistem AI sebagai perintah sah.

**Skenario Serangan:**
- **Injeksi Berbasis Dokumen**: Instruksi berbahaya tersembunyi dalam dokumen yang diproses memicu tindakan AI yang tidak diinginkan
- **Eksploitasi Konten Web**: Halaman web yang dikompromikan berisi prompt tertanam yang memanipulasi perilaku AI saat di-scrape
- **Serangan Berbasis Email**: Prompt berbahaya dalam email menyebabkan asisten AI membocorkan informasi atau melakukan tindakan tidak sah
- **Kontaminasi Sumber Data**: Basis data atau API yang dikompromikan menyajikan konten tercemar ke sistem AI

**Dampak Dunia Nyata**: Serangan ini dapat menyebabkan eksfiltrasi data, pelanggaran privasi, pembuatan konten berbahaya, dan manipulasi interaksi pengguna. Untuk analisis mendalam, lihat [Injeksi Prompt di MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Diagram Serangan Injeksi Prompt](../../../translated_images/id/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Serangan Keracunan Alat**

**Keracunan Alat** menargetkan metadata yang mendefinisikan alat MCP, mengeksploitasi cara LLM menafsirkan deskripsi alat dan parameter untuk membuat keputusan eksekusi.

**Mekanisme Serangan:**
- **Manipulasi Metadata**: Penyerang menyisipkan instruksi berbahaya ke dalam deskripsi alat, definisi parameter, atau contoh penggunaan
- **Instruksi Tak Terlihat**: Prompt tersembunyi dalam metadata alat yang diproses oleh model AI tetapi tidak terlihat oleh pengguna manusia
- **Modifikasi Alat Dinamis ("Rug Pulls")**: Alat yang disetujui pengguna kemudian dimodifikasi untuk melakukan tindakan berbahaya tanpa sepengetahuan pengguna
- **Injeksi Parameter**: Konten berbahaya tertanam dalam skema parameter alat yang memengaruhi perilaku model

**Risiko Server Tuan Rumah**: Server MCP jarak jauh menghadirkan risiko tinggi karena definisi alat dapat diperbarui setelah persetujuan awal pengguna, menciptakan skenario di mana alat yang sebelumnya aman menjadi berbahaya. Untuk analisis komprehensif, lihat [Serangan Keracunan Alat (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Diagram Serangan Injeksi Alat](../../../translated_images/id/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Vektor Serangan AI Tambahan**

- **Injeksi Prompt Lintas Domain (XPIA)**: Serangan canggih yang memanfaatkan konten dari beberapa domain untuk melewati kontrol keamanan
- **Modifikasi Kapabilitas Dinamis**: Perubahan waktu nyata pada kapabilitas alat yang lolos dari penilaian keamanan awal
- **Keracunan Jendela Konteks**: Serangan yang memanipulasi jendela konteks besar untuk menyembunyikan instruksi berbahaya
- **Serangan Kebingungan Model**: Mengeksploitasi keterbatasan model untuk menciptakan perilaku yang tidak terduga atau tidak aman

### Dampak Risiko Keamanan AI

**Konsekuensi Berdampak Tinggi:**
- **Eksfiltrasi Data**: Akses dan pencurian data sensitif perusahaan atau pribadi tanpa izin
- **Pelanggaran Privasi**: Paparan informasi identitas pribadi (PII) dan data bisnis rahasia  
- **Manipulasi Sistem**: Modifikasi tidak disengaja pada sistem dan alur kerja kritis
- **Pencurian Kredensial**: Kompromi token autentikasi dan kredensial layanan
- **Pergerakan Lateral**: Penggunaan sistem AI yang dikompromikan sebagai titik pivot untuk serangan jaringan yang lebih luas

### Solusi Keamanan AI Microsoft

#### **AI Prompt Shields: Perlindungan Lanjutan terhadap Serangan Injeksi**

Microsoft **AI Prompt Shields** menyediakan pertahanan komprehensif terhadap serangan injeksi prompt langsung dan tidak langsung melalui beberapa lapisan keamanan:

##### **Mekanisme Perlindungan Inti:**

1. **Deteksi & Penyaringan Lanjutan**
   - Algoritma pembelajaran mesin dan teknik NLP mendeteksi instruksi berbahaya dalam konten eksternal
   - Analisis waktu nyata dokumen, halaman web, email, dan sumber data untuk ancaman tertanam
   - Pemahaman kontekstual pola prompt sah vs berbahaya

2. **Teknik Spotlighting**  
   - Membedakan antara instruksi sistem tepercaya dan input eksternal yang berpotensi dikompromikan
   - Metode transformasi teks yang meningkatkan relevansi model sambil mengisolasi konten berbahaya
   - Membantu sistem AI mempertahankan hierarki instruksi yang tepat dan mengabaikan perintah yang disisipkan

3. **Sistem Delimiter & Datamarking**
   - Definisi batas eksplisit antara pesan sistem tepercaya dan teks input eksternal
   - Penanda khusus menyoroti batas antara sumber data tepercaya dan tidak tepercaya
   - Pemisahan jelas mencegah kebingungan instruksi dan eksekusi perintah tidak sah

4. **Intelijen Ancaman Berkelanjutan**
   - Microsoft terus memantau pola serangan yang muncul dan memperbarui pertahanan
   - Perburuan ancaman proaktif untuk teknik injeksi dan vektor serangan baru
   - Pembaruan model keamanan reguler untuk menjaga efektivitas terhadap ancaman yang berkembang

5. **Integrasi Azure Content Safety**
   - Bagian dari rangkaian Azure AI Content Safety yang komprehensif
   - Deteksi tambahan untuk upaya jailbreak, konten berbahaya, dan pelanggaran kebijakan keamanan
   - Kontrol keamanan terpadu di seluruh komponen aplikasi AI

**Sumber Implementasi**: [Dokumentasi Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Perlindungan Microsoft Prompt Shields](../../../translated_images/id/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Ancaman Keamanan MCP Lanjutan

### Kerentanan Pembajakan Sesi

**Pembajakan sesi** merupakan vektor serangan kritis dalam implementasi MCP stateful di mana pihak tidak berwenang memperoleh dan menyalahgunakan pengenal sesi sah untuk menyamar sebagai klien dan melakukan tindakan tidak sah.

#### **Skenario Serangan & Risiko**

- **Injeksi Prompt Pembajakan Sesi**: Penyerang dengan ID sesi curian menyisipkan event berbahaya ke server yang berbagi status sesi, berpotensi memicu tindakan berbahaya atau mengakses data sensitif
- **Penyamaran Langsung**: ID sesi curian memungkinkan panggilan server MCP langsung yang melewati autentikasi, memperlakukan penyerang sebagai pengguna sah
- **Stream Dapat Dilanjutkan yang Dikompromikan**: Penyerang dapat menghentikan permintaan secara prematur, menyebabkan klien sah melanjutkan dengan konten yang berpotensi berbahaya

#### **Kontrol Keamanan untuk Manajemen Sesi**

**Persyaratan Kritis:**
- **Verifikasi Otorisasi**: Server MCP yang mengimplementasikan otorisasi **HARUS** memverifikasi SEMUA permintaan masuk dan **TIDAK BOLEH** mengandalkan sesi untuk autentikasi  
- **Pembuatan Sesi yang Aman**: Gunakan ID sesi yang kriptografis aman dan non-deterministik yang dihasilkan dengan generator angka acak yang aman  
- **Pengikatan Spesifik Pengguna**: Ikat ID sesi ke informasi spesifik pengguna menggunakan format seperti `<user_id>:<session_id>` untuk mencegah penyalahgunaan sesi antar pengguna  
- **Manajemen Siklus Hidup Sesi**: Terapkan masa berlaku, rotasi, dan invalidasi yang tepat untuk membatasi jendela kerentanan  
- **Keamanan Transportasi**: HTTPS wajib untuk semua komunikasi guna mencegah penyadapan ID sesi  

### Masalah Confused Deputy

**Masalah confused deputy** terjadi ketika server MCP bertindak sebagai proxy autentikasi antara klien dan layanan pihak ketiga, menciptakan peluang untuk melewati otorisasi melalui eksploitasi ID klien statis.

#### **Mekanisme Serangan & Risiko**

- **Bypass Persetujuan Berbasis Cookie**: Autentikasi pengguna sebelumnya membuat cookie persetujuan yang dieksploitasi penyerang melalui permintaan otorisasi berbahaya dengan URI pengalihan yang dibuat khusus  
- **Pencurian Kode Otorisasi**: Cookie persetujuan yang ada dapat menyebabkan server otorisasi melewati layar persetujuan, mengalihkan kode ke titik akhir yang dikendalikan penyerang  
- **Akses API Tidak Sah**: Kode otorisasi yang dicuri memungkinkan pertukaran token dan penyamaran pengguna tanpa persetujuan eksplisit  

#### **Strategi Mitigasi**

**Kontrol Wajib:**
- **Persyaratan Persetujuan Eksplisit**: Server proxy MCP yang menggunakan ID klien statis **HARUS** mendapatkan persetujuan pengguna untuk setiap klien yang terdaftar secara dinamis  
- **Implementasi Keamanan OAuth 2.1**: Ikuti praktik keamanan OAuth terkini termasuk PKCE (Proof Key for Code Exchange) untuk semua permintaan otorisasi  
- **Validasi Klien yang Ketat**: Terapkan validasi ketat terhadap URI pengalihan dan pengenal klien untuk mencegah eksploitasi  

### Kerentanan Token Passthrough  

**Token passthrough** merupakan anti-pola eksplisit di mana server MCP menerima token klien tanpa validasi yang tepat dan meneruskannya ke API hilir, melanggar spesifikasi otorisasi MCP.

#### **Implikasi Keamanan**

- **Penghindaran Kontrol**: Penggunaan token langsung dari klien ke API melewati pembatasan laju, validasi, dan kontrol pemantauan yang penting  
- **Kerusakan Jejak Audit**: Token yang diterbitkan dari hulu membuat identifikasi klien tidak mungkin, merusak kemampuan investigasi insiden  
- **Eksfiltrasi Data Berbasis Proxy**: Token yang tidak tervalidasi memungkinkan aktor jahat menggunakan server sebagai proxy untuk akses data tidak sah  
- **Pelanggaran Batas Kepercayaan**: Asumsi kepercayaan layanan hilir dapat dilanggar ketika asal token tidak dapat diverifikasi  
- **Perluasan Serangan Multi-layanan**: Token yang dikompromikan diterima di banyak layanan memungkinkan pergerakan lateral  

#### **Kontrol Keamanan yang Diperlukan**

**Persyaratan Tidak Bisa Ditawar:**
- **Validasi Token**: Server MCP **TIDAK BOLEH** menerima token yang tidak secara eksplisit diterbitkan untuk server MCP  
- **Verifikasi Audiens**: Selalu validasi klaim audiens token sesuai dengan identitas server MCP  
- **Siklus Hidup Token yang Tepat**: Terapkan token akses berumur pendek dengan praktik rotasi yang aman  

## Keamanan Rantai Pasokan untuk Sistem AI

Keamanan rantai pasokan telah berkembang melampaui ketergantungan perangkat lunak tradisional untuk mencakup seluruh ekosistem AI. Implementasi MCP modern harus secara ketat memverifikasi dan memantau semua komponen terkait AI, karena masing-masing memperkenalkan potensi kerentanan yang dapat mengompromikan integritas sistem.

### Komponen Rantai Pasokan AI yang Diperluas

**Ketergantungan Perangkat Lunak Tradisional:**
- Perpustakaan dan kerangka kerja open-source  
- Gambar kontainer dan sistem dasar  
- Alat pengembangan dan pipeline build  
- Komponen dan layanan infrastruktur  

**Elemen Rantai Pasokan Khusus AI:**
- **Model Dasar**: Model pra-latih dari berbagai penyedia yang memerlukan verifikasi asal-usul  
- **Layanan Embedding**: Layanan vektorisasi eksternal dan pencarian semantik  
- **Penyedia Konteks**: Sumber data, basis pengetahuan, dan repositori dokumen  
- **API Pihak Ketiga**: Layanan AI eksternal, pipeline ML, dan titik akhir pemrosesan data  
- **Artefak Model**: Bobot, konfigurasi, dan varian model yang disesuaikan  
- **Sumber Data Pelatihan**: Dataset yang digunakan untuk pelatihan dan penyetelan model  

### Strategi Keamanan Rantai Pasokan yang Komprehensif

#### **Verifikasi & Kepercayaan Komponen**
- **Validasi Asal-usul**: Verifikasi asal, lisensi, dan integritas semua komponen AI sebelum integrasi  
- **Penilaian Keamanan**: Lakukan pemindaian kerentanan dan tinjauan keamanan untuk model, sumber data, dan layanan AI  
- **Analisis Reputasi**: Evaluasi rekam jejak keamanan dan praktik penyedia layanan AI  
- **Verifikasi Kepatuhan**: Pastikan semua komponen memenuhi persyaratan keamanan dan regulasi organisasi  

#### **Pipeline Penyebaran yang Aman**  
- **Keamanan CI/CD Otomatis**: Integrasikan pemindaian keamanan di seluruh pipeline penyebaran otomatis  
- **Integritas Artefak**: Terapkan verifikasi kriptografis untuk semua artefak yang disebarkan (kode, model, konfigurasi)  
- **Penyebaran Bertahap**: Gunakan strategi penyebaran progresif dengan validasi keamanan di setiap tahap  
- **Repositori Artefak Terpercaya**: Sebarkan hanya dari registri dan repositori artefak yang terverifikasi dan aman  

#### **Pemantauan & Respons Berkelanjutan**
- **Pemindaian Ketergantungan**: Pemantauan kerentanan berkelanjutan untuk semua ketergantungan perangkat lunak dan komponen AI  
- **Pemantauan Model**: Penilaian berkelanjutan terhadap perilaku model, pergeseran performa, dan anomali keamanan  
- **Pelacakan Kesehatan Layanan**: Pantau layanan AI eksternal untuk ketersediaan, insiden keamanan, dan perubahan kebijakan  
- **Integrasi Intelijen Ancaman**: Gabungkan feed ancaman khusus risiko keamanan AI dan ML  

#### **Kontrol Akses & Privilege Paling Rendah**
- **Izin Tingkat Komponen**: Batasi akses ke model, data, dan layanan berdasarkan kebutuhan bisnis  
- **Manajemen Akun Layanan**: Terapkan akun layanan khusus dengan izin minimal yang diperlukan  
- **Segmentasi Jaringan**: Isolasi komponen AI dan batasi akses jaringan antar layanan  
- **Kontrol Gateway API**: Gunakan gateway API terpusat untuk mengontrol dan memantau akses ke layanan AI eksternal  

#### **Respons Insiden & Pemulihan**
- **Prosedur Respons Cepat**: Proses yang ditetapkan untuk patch atau penggantian komponen AI yang dikompromikan  
- **Rotasi Kredensial**: Sistem otomatis untuk merotasi rahasia, kunci API, dan kredensial layanan  
- **Kemampuan Rollback**: Kemampuan untuk cepat mengembalikan versi komponen AI yang diketahui baik sebelumnya  
- **Pemulihan Pelanggaran Rantai Pasokan**: Prosedur khusus untuk merespons kompromi layanan AI hulu  

### Alat & Integrasi Keamanan Microsoft

**GitHub Advanced Security** menyediakan perlindungan rantai pasokan komprehensif termasuk:  
- **Pemindaian Rahasia**: Deteksi otomatis kredensial, kunci API, dan token dalam repositori  
- **Pemindaian Ketergantungan**: Penilaian kerentanan untuk ketergantungan dan perpustakaan open-source  
- **Analisis CodeQL**: Analisis kode statis untuk kerentanan keamanan dan masalah pengkodean  
- **Wawasan Rantai Pasokan**: Visibilitas kesehatan ketergantungan dan status keamanan  

**Integrasi Azure DevOps & Azure Repos:**  
- Integrasi pemindaian keamanan mulus di seluruh platform pengembangan Microsoft  
- Pemeriksaan keamanan otomatis di Azure Pipelines untuk beban kerja AI  
- Penegakan kebijakan untuk penyebaran komponen AI yang aman  

**Praktik Internal Microsoft:**  
Microsoft menerapkan praktik keamanan rantai pasokan yang luas di semua produknya. Pelajari pendekatan terbukti di [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).  

## Praktik Terbaik Keamanan Dasar

Implementasi MCP mewarisi dan membangun di atas postur keamanan organisasi Anda yang sudah ada. Memperkuat praktik keamanan dasar secara signifikan meningkatkan keamanan keseluruhan sistem AI dan penyebaran MCP.

### Dasar-dasar Keamanan Inti

#### **Praktik Pengembangan Aman**
- **Kepatuhan OWASP**: Lindungi dari kerentanan aplikasi web [OWASP Top 10](https://owasp.org/www-project-top-ten/)  
- **Perlindungan Khusus AI**: Terapkan kontrol untuk [OWASP Top 10 untuk LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- **Manajemen Rahasia yang Aman**: Gunakan vault khusus untuk token, kunci API, dan data konfigurasi sensitif  
- **Enkripsi End-to-End**: Terapkan komunikasi aman di seluruh komponen aplikasi dan aliran data  
- **Validasi Input**: Validasi ketat semua input pengguna, parameter API, dan sumber data  

#### **Penguatan Infrastruktur**
- **Autentikasi Multi-Faktor**: MFA wajib untuk semua akun administratif dan layanan  
- **Manajemen Patch**: Patch otomatis dan tepat waktu untuk sistem operasi, kerangka kerja, dan ketergantungan  
- **Integrasi Penyedia Identitas**: Manajemen identitas terpusat melalui penyedia identitas perusahaan (Microsoft Entra ID, Active Directory)  
- **Segmentasi Jaringan**: Isolasi logis komponen MCP untuk membatasi potensi pergerakan lateral  
- **Prinsip Privilege Paling Rendah**: Izin minimal yang diperlukan untuk semua komponen dan akun sistem  

#### **Pemantauan & Deteksi Keamanan**
- **Logging Komprehensif**: Logging terperinci aktivitas aplikasi AI, termasuk interaksi klien-server MCP  
- **Integrasi SIEM**: Manajemen informasi dan kejadian keamanan terpusat untuk deteksi anomali  
- **Analitik Perilaku**: Pemantauan berbasis AI untuk mendeteksi pola tidak biasa dalam perilaku sistem dan pengguna  
- **Intelijen Ancaman**: Integrasi feed ancaman eksternal dan indikator kompromi (IOC)  
- **Respons Insiden**: Prosedur terdefinisi dengan baik untuk deteksi, respons, dan pemulihan insiden keamanan  

#### **Arsitektur Zero Trust**
- **Jangan Pernah Percaya, Selalu Verifikasi**: Verifikasi berkelanjutan pengguna, perangkat, dan koneksi jaringan  
- **Mikro-Segmentasi**: Kontrol jaringan granular yang mengisolasi beban kerja dan layanan individual  
- **Keamanan Berbasis Identitas**: Kebijakan keamanan berdasarkan identitas yang terverifikasi, bukan lokasi jaringan  
- **Penilaian Risiko Berkelanjutan**: Evaluasi postur keamanan dinamis berdasarkan konteks dan perilaku saat ini  
- **Akses Kondisional**: Kontrol akses yang beradaptasi berdasarkan faktor risiko, lokasi, dan kepercayaan perangkat  

### Pola Integrasi Perusahaan

#### **Integrasi Ekosistem Keamanan Microsoft**
- **Microsoft Defender for Cloud**: Manajemen postur keamanan cloud yang komprehensif  
- **Azure Sentinel**: SIEM dan SOAR cloud-native untuk perlindungan beban kerja AI  
- **Microsoft Entra ID**: Manajemen identitas dan akses perusahaan dengan kebijakan akses kondisional  
- **Azure Key Vault**: Manajemen rahasia terpusat dengan dukungan modul keamanan perangkat keras (HSM)  
- **Microsoft Purview**: Tata kelola data dan kepatuhan untuk sumber data dan alur kerja AI  

#### **Kepatuhan & Tata Kelola**
- **Penyesuaian Regulasi**: Pastikan implementasi MCP memenuhi persyaratan kepatuhan spesifik industri (GDPR, HIPAA, SOC 2)  
- **Klasifikasi Data**: Kategorisasi dan penanganan data sensitif yang diproses oleh sistem AI  
- **Jejak Audit**: Logging komprehensif untuk kepatuhan regulasi dan investigasi forensik  
- **Kontrol Privasi**: Implementasi prinsip privasi-dengan-desain dalam arsitektur sistem AI  
- **Manajemen Perubahan**: Proses formal untuk tinjauan keamanan modifikasi sistem AI  

Praktik dasar ini menciptakan baseline keamanan yang kuat yang meningkatkan efektivitas kontrol keamanan khusus MCP dan memberikan perlindungan komprehensif untuk aplikasi berbasis AI.

## Intisari Keamanan Utama

- **Pendekatan Keamanan Berlapis**: Gabungkan praktik keamanan dasar (pengkodean aman, privilege paling rendah, verifikasi rantai pasokan, pemantauan berkelanjutan) dengan kontrol khusus AI untuk perlindungan menyeluruh  

- **Lanskap Ancaman Khusus AI**: Sistem MCP menghadapi risiko unik termasuk injeksi prompt, keracunan alat, pembajakan sesi, masalah confused deputy, kerentanan token passthrough, dan izin berlebihan yang memerlukan mitigasi khusus  

- **Keunggulan Autentikasi & Otorisasi**: Terapkan autentikasi kuat menggunakan penyedia identitas eksternal (Microsoft Entra ID), tegakkan validasi token yang tepat, dan jangan pernah menerima token yang tidak secara eksplisit diterbitkan untuk server MCP Anda  

- **Pencegahan Serangan AI**: Terapkan Microsoft Prompt Shields dan Azure Content Safety untuk melindungi dari injeksi prompt tidak langsung dan serangan keracunan alat, sambil memvalidasi metadata alat dan memantau perubahan dinamis  

- **Keamanan Sesi & Transportasi**: Gunakan ID sesi yang kriptografis aman, non-deterministik, terikat pada identitas pengguna, terapkan manajemen siklus hidup sesi yang tepat, dan jangan pernah menggunakan sesi untuk autentikasi  

- **Praktik Terbaik Keamanan OAuth**: Cegah serangan confused deputy melalui persetujuan pengguna eksplisit untuk klien yang terdaftar dinamis, implementasi OAuth 2.1 yang tepat dengan PKCE, dan validasi URI pengalihan yang ketat  

- **Prinsip Keamanan Token**: Hindari anti-pola token passthrough, validasi klaim audiens token, terapkan token berumur pendek dengan rotasi aman, dan pertahankan batas kepercayaan yang jelas  

- **Keamanan Rantai Pasokan Komprehensif**: Perlakukan semua komponen ekosistem AI (model, embedding, penyedia konteks, API eksternal) dengan ketelitian keamanan yang sama seperti ketergantungan perangkat lunak tradisional  

- **Evolusi Berkelanjutan**: Tetap terkini dengan spesifikasi MCP yang berkembang cepat, berkontribusi pada standar komunitas keamanan, dan pertahankan postur keamanan adaptif seiring protokol matang  

- **Integrasi Keamanan Microsoft**: Manfaatkan ekosistem keamanan Microsoft yang komprehensif (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) untuk perlindungan penyebaran MCP yang ditingkatkan  

## Sumber Daya Komprehensif

### **Dokumentasi Keamanan Resmi MCP**
- [Spesifikasi MCP (Terkini: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [Praktik Terbaik Keamanan MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [Spesifikasi Otorisasi MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  
- [Repositori GitHub MCP](https://github.com/modelcontextprotocol)  

### **Standar & Praktik Terbaik Keamanan**
- [Praktik Terbaik Keamanan OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 Keamanan Aplikasi Web](https://owasp.org/www-project-top-ten/)  
- [OWASP Top 10 untuk Large Language Models](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- [Laporan Pertahanan Digital Microsoft](https://aka.ms/mddr)  

### **Riset & Analisis Keamanan AI**
- [Injeksi Prompt di MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [Serangan Keracunan Alat (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)  
- [MCP Security Research Briefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Solusi Keamanan Microsoft**
- [Dokumentasi Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Layanan Keamanan Konten Azure](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Keamanan Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Praktik Terbaik Manajemen Token Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [Keamanan Lanjutan GitHub](https://github.com/security/advanced-security)

### **Panduan Implementasi & Tutorial**
- [Manajemen API Azure sebagai Gerbang Otentikasi MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Otentikasi Microsoft Entra ID dengan Server MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Penyimpanan Token Aman dan Enkripsi (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **Keamanan DevOps & Rantai Pasokan**
- [Keamanan Azure DevOps](https://azure.microsoft.com/products/devops)
- [Keamanan Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Perjalanan Keamanan Rantai Pasokan Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Dokumentasi Keamanan Tambahan**

Untuk panduan keamanan yang komprehensif, lihat dokumen khusus di bagian ini:

- **[Praktik Terbaik Keamanan MCP 2025](./mcp-security-best-practices-2025.md)** - Praktik terbaik keamanan lengkap untuk implementasi MCP
- **[Implementasi Keamanan Konten Azure](./azure-content-safety-implementation.md)** - Contoh implementasi praktis untuk integrasi Keamanan Konten Azure  
- **[Kontrol Keamanan MCP 2025](./mcp-security-controls-2025.md)** - Kontrol dan teknik keamanan terbaru untuk penerapan MCP
- **[Referensi Cepat Praktik Terbaik MCP](./mcp-best-practices.md)** - Panduan referensi cepat untuk praktik keamanan MCP yang penting

---

## Selanjutnya

Selanjutnya: [Bab 3: Memulai](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->