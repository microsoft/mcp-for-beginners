# Keselamatan MCP: Perlindungan Menyeluruh untuk Sistem AI

[![Amalan Terbaik Keselamatan MCP](../../../translated_images/ms/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Klik imej di atas untuk melihat video pelajaran ini)_

Keselamatan adalah asas kepada reka bentuk sistem AI, sebab itulah kami mengutamakannya sebagai bahagian kedua kami. Ini selaras dengan prinsip Microsoft **Secure by Design** daripada [Inisiatif Masa Depan Selamat](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Protokol Konteks Model (MCP) membawa keupayaan baharu yang hebat kepada aplikasi yang dikuasakan AI sambil memperkenalkan cabaran keselamatan unik yang melangkaui risiko perisian tradisional. Sistem MCP menghadapi kedua-dua kebimbangan keselamatan yang sedia ada (pengekodan selamat, keistimewaan minimum, keselamatan rantai bekalan) dan ancaman khusus AI baru termasuk suntikan arahan, pencemaran alat, pembajakan sesi, serangan pembantu keliru, kerentanan laluan token, dan pengubahsuaian keupayaan dinamik.

Pelajaran ini meneroka risiko keselamatan paling kritikal dalam pelaksanaan MCP—meliputi pengesahan, kebenaran, kebenaran berlebihan, suntikan arahan tidak langsung, keselamatan sesi, masalah pembantu keliru, pengurusan token, dan kerentanan rantai bekalan. Anda akan mempelajari kawalan yang boleh diambil tindakan dan amalan terbaik untuk mengurangkan risiko ini sambil menggunakan penyelesaian Microsoft seperti Pelindung Prompt, Keselamatan Kandungan Azure, dan Keselamatan Lanjutan GitHub untuk mengukuhkan penyebaran MCP anda.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- **Kenal pasti Ancaman Spesifik MCP**: Kenal risiko keselamatan unik dalam sistem MCP termasuk suntikan arahan, pencemaran alat, kebenaran berlebihan, pembajakan sesi, masalah pembantu keliru, kerentanan laluan token, dan risiko rantai bekalan
- **Terapkan Kawalan Keselamatan**: Laksanakan mitigasi berkesan termasuk pengesahan kukuh, akses keistimewaan minimum, pengurusan token selamat, kawalan keselamatan sesi, dan pengesahan rantai bekalan
- **Manfaatkan Penyelesaian Keselamatan Microsoft**: Fahami dan gunakan Microsoft Prompt Shields, Keselamatan Kandungan Azure, dan Keselamatan Lanjutan GitHub untuk perlindungan beban kerja MCP
- **Sahkan Keselamatan Alat**: Kenal kepentingan pengesahan metadata alat, pemantauan perubahan dinamik, dan pertahanan terhadap serangan suntikan arahan tidak langsung
- **Gabungkan Amalan Terbaik**: Gabungkan asas keselamatan yang telah terbukti (pengekodan selamat, pengukuhan pelayan, kepercayaan sifar) dengan kawalan khusus MCP untuk perlindungan menyeluruh

# Seni Bina & Kawalan Keselamatan MCP

Pelaksanaan MCP moden memerlukan pendekatan keselamatan berlapis yang menangani keselamatan perisian tradisional dan ancaman khusus AI. Spesifikasi MCP yang berkembang pesat terus mematangkan kawalan keselamatannya, membolehkan integrasi lebih baik dengan seni bina keselamatan perusahaan dan amalan terbaik yang telah terbukti.

Penyelidikan dari [Laporan Pertahanan Digital Microsoft](https://aka.ms/mddr) menunjukkan bahawa **98% pelanggaran yang dilaporkan boleh dicegah dengan amalan kebersihan keselamatan yang kukuh**. Strategi perlindungan paling berkesan menggabungkan amalan keselamatan asas dengan kawalan khusus MCP—ukuran keselamatan asas yang terbukti kekal paling berimpak dalam mengurangkan risiko keselamatan keseluruhan.

## Landskap Keselamatan Semasa

> **Nota:** Bab ini menggabungkan kawalan keselamatan MCP yang telah terbukti dengan
> panduan kebenaran **Spesifikasi MCP 2026-07-28** semasa. Sentiasa rujuk
> kepada [Spesifikasi MCP](https://modelcontextprotocol.io/specification/2026-07-28/),
> [repositori GitHub MCP](https://github.com/modelcontextprotocol), dan
> [dokumentasi amalan terbaik keselamatan](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> apabila melaksanakan kod sensitif keselamatan.

> **Kemas kini Kebenaran:** MCP `2026-07-28` menghendaki klien mengesahkan
> parameter `iss` pada respons kebenaran (RFC 9207) dan mengikat
> kelayakan berdaftar kepada pelayan kebenaran yang mengeluarkan. Pendaftaran Klien Dinamik
> sudah tidak digunakan; pelaksanaan baru harus menggunakan Dokumen Metadata ID Klien.
> Lihat [Perubahan dalam MCP: Spesifikasi 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> untuk senarai penuh perubahan kebenaran.

## 🏔️ Bengkel Sidang Kemuncak Keselamatan MCP (Sherpa)

Untuk **latihan keselamatan praktikal**, kami sangat mengesyorkan **Bengkel Sidang Kemuncak Keselamatan MCP** (Sherpa) - sebuah ekspedisi berpandu menyeluruh untuk mengamankan pelayan MCP di Microsoft Azure.

### Gambaran Keseluruhan Bengkel

[Bengkel Sidang Kemuncak Keselamatan MCP](https://azure-samples.github.io/sherpa/) menyediakan latihan keselamatan praktikal dan boleh diambil tindakan melalui metodologi "mudah terdedah → eksploit → baiki → sahkan" yang terbukti. Anda akan:

- **Belajar melalui Memecahkan Sesuatu**: Mengalami kerentanan secara langsung dengan mengeksploitasi pelayan yang sengaja tidak selamat
- **Gunakan Keselamatan Asli Azure**: Manfaatkan Azure Entra ID, Key Vault, Pengurusan API, dan Keselamatan Kandungan AI
- **Ikut Pertahanan Berlapis**: Melalui kem yang membina lapisan keselamatan menyeluruh
- **Terapkan Standard OWASP**: Setiap teknik dipetakan ke [Panduan Keselamatan MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/)
- **Dapatkan Kod Produksi**: Mendapatkan pelaksanaan yang berfungsi dan diuji

### Laluan Ekspedisi

| Kem | Fokus | Risiko OWASP Dilindungi |
|------|-------|---------------------|
| **Kem Asas** | Asas MCP & kerentanan pengesahan | MCP01, MCP07 |
| **Kem 1: Identiti** | OAuth 2.1, Identiti Terurus Azure, Key Vault | MCP01, MCP02, MCP07 |
| **Kem 2: Gerbang** | Pengurusan API, Titik Akhir Peribadi, tadbir urus | MCP02, MCP06, MCP07, MCP09 |
| **Kem 3: Keselamatan I/O** | Suntikan arahan, perlindungan PII, keselamatan kandungan | MCP03, MCP05, MCP06, MCP10 |
| **Kem 4: Pemantauan** | Analitik Log, papan pemuka, pengesanan ancaman | MCP04, MCP08 |
| **Sidang Kemuncak** | Ujian integrasi Pasukan Merah / Pasukan Biru | Semua |

**Mula**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## 10 Risiko Keselamatan Teratas MCP OWASP

[Panduan Keselamatan MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/) memperincikan sepuluh risiko keselamatan paling kritikal untuk pelaksanaan MCP:

| Risiko | Penerangan | Mitigasi Azure |
|------|-------------|------------------|
| **MCP01** | Pengurusan Token & Pendedahan Rahsia yang Tidak Betul | Azure Key Vault, Identiti Terurus |
| **MCP02** | Peningkatan Keistimewaan melalui Rentetan Skop | RBAC, Akses Bersyarat |
| **MCP03** | Pencemaran Alat | Pengesahan alat, pengesahan integriti |
| **MCP04** | Serangan Rantai Bekalan Perisian & Pemalsuan Pergantungan | Keselamatan Lanjutan GitHub, imbasan pergantungan |
| **MCP05** | Suntikan Perintah & Pelaksanaan | Pengesahan input, kotak pasir |
| **MCP06** | Subversi Aliran Niat | Keselamatan Kandungan AI Azure, Pelindung Prompt |
| **MCP07** | Pengesahan & Kebenaran Tidak Mencukupi | Azure Entra ID, OAuth 2.1 dengan PKCE |
| **MCP08** | Kekurangan Audit dan Telemetri | Azure Monitor, Application Insights |
| **MCP09** | Pelayan MCP Bayangan | Tadbir urus Pusat API, pengasingan rangkaian |
| **MCP10** | Suntikan Konteks & Pendedahan Berlebihan | Klasifikasi data, pendedahan minimum |

### Evolusi Pengesahan MCP

Spesifikasi MCP telah berkembang dengan ketara dalam pendekatannya terhadap pengesahan dan kebenaran:

- **Pendekatan Asal**: Spesifikasi awal menghendaki pemaju melaksanakan pelayan pengesahan tersuai, dengan pelayan MCP bertindak sebagai Pelayan Kebenaran OAuth 2.0 yang mengurus pengesahan pengguna secara langsung
- **Standard Semasa (`2026-07-28`)**: Pelayan MCP boleh mendelegasikan pengesahan
  kepada penyedia identiti luaran seperti Microsoft Entra ID. Klien juga mesti
  mematuhi keperluan pengesahan pengeluar dan pengikatan kelayakan semasa.
- **Keselamatan Lapisan Pengangkutan**: Sokongan dipertingkatkan untuk mekanisme penghantaran selamat dengan corak pengesahan yang betul untuk sambungan tempatan (STDIO) dan jarak jauh (HTTP Boleh Strim)

## Keselamatan Pengesahan & Kebenaran

### Cabaran Keselamatan Semasa

Pelaksanaan MCP moden menghadapi beberapa cabaran pengesahan dan kebenaran:

### Risiko & Vektor Ancaman

- **Logik Kebenaran Salah Konfigurasi**: Pelaksanaan kebenaran yang cacat dalam pelayan MCP boleh mendedahkan data sensitif dan menggunakan kawalan akses secara tidak betul
- **Kompromi Token OAuth**: Kecurian token pelayan MCP tempatan membolehkan penyerang menyamar sebagai pelayan dan mengakses perkhidmatan hiliran
- **Kerentanan Laluan Token**: Pengendalian token yang tidak betul mewujudkan laluan pintas kawalan keselamatan dan jurang akauntabiliti
- **Kebenaran Berlebihan**: Pelayan MCP yang berlebihan keistimewaan melanggar prinsip keistimewaan minimum dan memperluas permukaan serangan

#### Laluan Token: Corak Anti Kritikal

**Laluan token adalah dilarang secara eksplisit** dalam spesifikasi kebenaran MCP semasa kerana implikasi keselamatan yang serius:

##### Pengelakan Kawalan Keselamatan
- Pelayan MCP dan API hiliran melaksanakan kawalan keselamatan kritikal (had kadar, pengesahan permintaan, pemantauan trafik) yang bergantung pada pengesahan token yang betul
- Penggunaan token terus oleh klien ke API melangkaui perlindungan penting ini, merosakkan seni bina keselamatan

##### Cabaran Akauntabiliti & Audit  
- Pelayan MCP tidak dapat membezakannya antara klien yang menggunakan token yang dikeluarkan dari hulu, memecahkan jejak audit
- Log pelayan sumber hiliran menunjukkan asal permintaan yang mengelirukan dan bukannya perantara pelayan MCP sebenar
- Siasatan insiden dan audit pematuhan menjadi jauh lebih sukar

##### Risiko Eksfiltrasi Data
- Tuntutan token yang tidak disahkan membolehkan pelaku jahat dengan token yang dicuri menggunakan pelayan MCP sebagai proksi untuk eksfiltrasi data
- Pelanggaran sempadan kepercayaan membenarkan corak akses tanpa kebenaran yang melangkaui kawalan keselamatan yang dimaksudkan

##### Vektor Serangan Multi-Perkhidmatan
- Token yang dikompromi diterima oleh pelbagai perkhidmatan membolehkan pergerakan sisi melintasi sistem yang bersambung
- Andaian kepercayaan antara perkhidmatan boleh dilanggar apabila asal token tidak dapat disahkan

### Kawalan Keselamatan & Mitigasi

**Keperluan Keselamatan Kritikal:**

> **WAJIB**: Pelayan MCP **TIDAK BOLEH** menerima token yang tidak dikeluarkan secara eksplisit untuk pelayan MCP itu

#### Kawalan Pengesahan & Kebenaran

- **Semakan Kebenaran Teliti**: Lakukan audit menyeluruh terhadap logik kebenaran pelayan MCP untuk memastikan hanya pengguna dan klien yang dimaksudkan dapat mengakses sumber sensitif
  - **Panduan Pelaksanaan**: [Pengurusan API Azure sebagai Gerbang Pengesahan untuk Pelayan MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integrasi Identiti**: [Menggunakan Microsoft Entra ID untuk Pengesahan Pelayan MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Pengurusan Token Selamat**: Laksanakan [amalan terbaik pengesahan token dan kitar hayat Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Sahkan tuntutan audiens token sepadan dengan identiti pelayan MCP
  - Laksanakan dasar putaran dan tamat tempoh token yang betul
  - Cegah serangan ulang main token dan penggunaan tanpa kebenaran

- **Penyimpanan Token Terlindung**: Simpanan token yang selamat dengan penyulitan semasa rehat dan penghantaran
  - **Amalan Terbaik**: [Garis Panduan Penyimpanan & Penyulitan Token Selamat](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Pelaksanaan Kawalan Akses

- **Prinsip Keistimewaan Minimum**: Beri pelayan MCP hanya kebenaran minimum yang diperlukan untuk fungsi yang dimaksudkan
  - Kajian dan kemas kini kebenaran secara berkala untuk mengelakkan peningkatan keistimewaan
  - **Dokumentasi Microsoft**: [Akses Keistimewaan Minimum Selamat](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Kawalan Akses Berasaskan Peranan (RBAC)**: Laksanakan peranan granular
  - Hadkan peranan dengan ketat kepada sumber dan tindakan tertentu
  - Elakkan kebenaran luas atau tidak perlu yang memperluas permukaan serangan

- **Pemantauan Kebenaran Berterusan**: Laksanakan audit dan pemantauan akses berterusan
  - Pantau corak penggunaan kebenaran untuk anomali
  - Segera perbaiki keistimewaan berlebihan atau tidak digunakan

## Ancaman Keselamatan Spesifik AI

### Serangan Suntikan Arahan & Manipulasi Alat

Pelaksanaan MCP moden menghadapi vektor serangan khusus AI yang canggih yang tidak dapat diatasi sepenuhnya oleh langkah keselamatan tradisional:

#### **Suntikan Arahan Tidak Langsung (Suntikan Arahan Rentas Domain)**

**Suntikan Arahan Tidak Langsung** merupakan salah satu kerentanan paling kritikal dalam sistem AI yang diaktifkan MCP. Penyerang menyelitkan arahan berniat jahat dalam kandungan luaran—dokumen, halaman web, e-mel, atau sumber data—yang kemudian diproses oleh sistem AI sebagai arahan sah.

**Senario Serangan:**
- **Suntikan Berasaskan Dokumen**: Arahan berniat jahat tersembunyi dalam dokumen yang diproses yang mencetuskan tindakan AI yang tidak diingini
- **Eksploitasi Kandungan Web**: Halaman web yang dikompromi mengandungi arahan terbenam yang memanipulasi tingkah laku AI apabila dikikis
- **Serangan Berasaskan E-mel**: Arahan berniat jahat dalam e-mel yang menyebabkan pembantu AI membocorkan maklumat atau melakukan tindakan tanpa kebenaran
- **Pencemaran Sumber Data**: Pangkalan data atau API yang dikompromi menyajikan kandungan tercemar kepada sistem AI

**Impak Dunia Nyata**: Serangan ini boleh mengakibatkan eksfiltrasi data, pelanggaran privasi, penghasilan kandungan berbahaya, dan manipulasi interaksi pengguna. Untuk analisis terperinci, lihat [Suntikan Arahan dalam MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Rajah Serangan Suntikan Arahan](../../../translated_images/ms/prompt-injection.ed9fbfde297ca877.webp)

#### **Serangan Pencemaran Alat**

**Pencemaran Alat** mensasarkan metadata yang mentakrifkan alat MCP, mengeksploitasi bagaimana LLM mentafsir deskripsi dan parameter alat untuk membuat keputusan pelaksanaan.

**Mekanisme Serangan:**
- **Manipulasi Metadata**: Penyerang menyuntik arahan berniat jahat ke dalam deskripsi alat, definisi parameter, atau contoh penggunaan
- **Arahan Tidak Kelihatan**: Arahan tersembunyi dalam metadata alat yang diproses oleh model AI tetapi tidak kelihatan kepada pengguna manusia
- **Pengubahsuaian Alat Dinamik ("Rug Pulls")**: Alat yang diluluskan oleh pengguna kemudiannya diubahsuai untuk melakukan tindakan berniat jahat tanpa pengetahuan pengguna
- **Suntikan Parameter**: Kandungan berniat jahat tertanam dalam skema parameter alat yang mempengaruhi tingkah laku model


**Risiko Pelayan Hosted**: Pelayan MCP jauh mempunyai risiko yang lebih tinggi kerana definisi alat boleh dikemas kini selepas kelulusan awal pengguna, mewujudkan senario di mana alat yang sebelum ini selamat menjadi berbahaya. Untuk analisis menyeluruh, lihat [Serangan Penyingkiran Alat (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Rajah Serangan Suntikan Alat](../../../translated_images/ms/tool-injection.3b0b4a6b24de6bef.webp)

#### **Vektor Serangan AI Tambahan**

- **Suntikan Prompt Merentas Domain (XPIA)**: Serangan canggih yang menggunakan kandungan daripada pelbagai domain untuk melepasi kawalan keselamatan  
- **Pengubahsuaian Keupayaan Dinamik**: Perubahan masa nyata pada keupayaan alat yang mengelak penilaian keselamatan awal  
- **Keracunan Tetingkap Konteks**: Serangan yang memanipulasi tetingkap konteks yang besar untuk menyembunyikan arahan berbahaya  
- **Serangan Kekeliruan Model**: Mengeksploitasi batasan model untuk mencipta tingkah laku yang tidak dapat dijangka atau tidak selamat  


### Kesan Risiko Keselamatan AI

**Kesan Berimpak Tinggi:**
- **Exfiltrasi Data**: Akses tanpa kebenaran dan kecurian data peribadi atau sensitif syarikat  
- **Pelanggaran Privasi**: Pendedahan maklumat peribadi yang boleh dikenal pasti (PII) dan data perniagaan sulit  
- **Manipulasi Sistem**: Pengubahsuaian tidak disengajakan terhadap sistem dan aliran kerja kritikal  
- **Kecurian Kredensial**: Pengkompromian token pengesahan dan kredensial perkhidmatan  
- **Pergerakan Lateral**: Penggunaan sistem AI yang dikompromi sebagai titik tumpu untuk serangan rangkaian yang lebih luas  

### Penyelesaian Keselamatan AI Microsoft

#### **Perisai Prompt AI: Perlindungan Lanjutan Terhadap Serangan Suntikan**

Microsoft **Perisai Prompt AI** menyediakan pertahanan menyeluruh terhadap serangan suntikan langsung dan tidak langsung melalui pelbagai lapisan keselamatan:  

##### **Mekanisme Perlindungan Teras:**

1. **Pengesanan & Penapisan Lanjutan**  
   - Algoritma pembelajaran mesin dan teknik NLP mengesan arahan berbahaya dalam kandungan luar  
   - Analisis masa nyata dokumen, halaman web, e-mel dan sumber data untuk ancaman terbina  
   - Pemahaman kontekstual corak prompt yang sah berbanding berbahaya  

2. **Teknik Penyerlah**  
   - Membezakan antara arahan sistem yang dipercayai dan input luar yang mungkin dikompromi  
   - Kaedah transformasi teks yang meningkatkan relevansi model sambil mengasingkan kandungan berbahaya  
   - Membantu sistem AI mengekalkan hierarki arahan dengan betul dan mengabaikan arahan suntikan  

3. **Sistem Pembatas & Penandaan Data**  
   - Definisi sempadan jelas antara mesej sistem yang dipercayai dan teks input luar  
   - Penanda khas menyorot sempadan antara sumber data yang dipercayai dan yang tidak dipercaya  
   - Pemisahan jelas mengelakkan kekeliruan arahan dan pelaksanaan arahan tanpa kebenaran  

4. **Perisikan Ancaman Berterusan**  
   - Microsoft memantau pola serangan yang muncul dan mengemas kini pertahanan secara berterusan  
   - Pencarian ancaman proaktif untuk teknik suntikan dan vektor serangan baru  
   - Kemas kini model keselamatan berkala untuk mengekalkan keberkesanan terhadap ancaman yang berkembang  

5. **Integrasi Azure Content Safety**  
   - Sebahagian dari suite keselamatan kandungan Azure AI yang komprehensif  
   - Pengesanan tambahan untuk percubaan jailbreak, kandungan berbahaya, dan pelanggaran dasar keselamatan  
   - Kawalan keselamatan bersatu merentasi komponen aplikasi AI  

**Sumber Pelaksanaan**: [Dokumentasi Perisai Prompt Microsoft](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  

![Perlindungan Perisai Prompt Microsoft](../../../translated_images/ms/prompt-shield.ff5b95be76e9c78c.webp)


## Ancaman Keselamatan MCP Lanjutan

### Kelemahan Pengambilalihan Sesi

**Pengambilalihan sesi** adalah vektor serangan kritikal dalam pelaksanaan MCP berstatus di mana pihak tidak dibenarkan memperoleh dan menyalahgunakan pengecam sesi yang sah untuk menyamar sebagai klien dan melakukan tindakan tanpa kebenaran.  

#### **Senario Serangan & Risiko**

- **Suntikan Prompt Pengambilalihan Sesi**: Penyerang dengan ID sesi curi menyuntik acara berbahaya ke pelayan yang berkongsi status sesi, berpotensi mencetuskan tindakan berbahaya atau mengakses data sensitif  
- **Peniruan Langsung**: ID sesi curi membolehkan panggilan langsung ke pelayan MCP yang melepasi pengesahan, menganggap penyerang sebagai pengguna sah  
- **Aliran Boleh Disambung Terganggu**: Penyerang boleh menamatkan permintaan lebih awal, menyebabkan klien sah menyambung semula dengan kandungan yang mungkin berbahaya  

#### **Kawalan Keselamatan Pengurusan Sesi**

**Keperluan Kritikal:**
- **Pengesahan Kebenaran**: Pelayan MCP yang melaksanakan kebenaran **MESTI** mengesahkan SEMUA permintaan masuk dan **TIDAK BOLEH** bergantung pada sesi untuk pengesahan  
- **Penjanaan Sesi Selamat**: Gunakan ID sesi yang selamat secara kriptografi dan bukan deterministik yang dijana dengan penjana nombor rawak selamat  
- **Pengikatan Khusus Pengguna**: Ikat ID sesi kepada maklumat khusus pengguna menggunakan format seperti `<user_id>:<session_id>` untuk mengelakkan penyalahgunaan sesi silang pengguna  
- **Pengurusan Kitaran Hayat Sesi**: Laksanakan tamat tempoh, putaran, dan pembatalan yang betul untuk mengehadkan tempoh kelemahan  
- **Keselamatan Penghantaran**: HTTPS diwajibkan untuk semua komunikasi bagi mengelakkan penyadapan ID sesi  

### Masalah Pegawai Keliru

**Masalah pegawai keliru** berlaku apabila pelayan MCP bertindak sebagai proksi pengesahan antara klien dan perkhidmatan pihak ketiga, mewujudkan peluang untuk bypass kebenaran melalui eksploitasi ID klien statik.  

#### **Mekanisme Serangan & Risiko**

- **Bypass Persetujuan Berasaskan Kuki**: Pengesahan pengguna sebelum ini mencipta kuki persetujuan yang dieksploitasi penyerang melalui permintaan kebenaran berbahaya dengan URI redirect direka  
- **Kecurian Kod Kebenaran**: Kuki persetujuan yang sedia ada mungkin menyebabkan pelayan kebenaran melangkau skrin persetujuan, mengarahkan kod ke titik akhir yang dikawal penyerang  
- **Akses API Tanpa Kebenaran**: Kod kebenaran curi membolehkan pertukaran token dan penyamaran pengguna tanpa kelulusan eksplisit  

#### **Strategi Mitigasi**

**Kawalan Wajib:**
- **Keperluan Persetujuan Eksplisit**: Pelayan proksi MCP yang menggunakan ID klien statik **MESTI** mendapatkan persetujuan pengguna untuk setiap klien yang didaftarkan secara dinamik  
- **Pelaksanaan Keselamatan OAuth 2.1**: Ikuti amalan keselamatan OAuth terkini termasuk PKCE (Proof Key for Code Exchange) untuk semua permintaan kebenaran  
- **Pengesahan Klien Yang Ketat**: Laksanakan pengesahan tegas terhadap URI redirect dan pengecam klien untuk mengelakkan eksploitasi  

### Kelemahan Passthrough Token  

**Passthrough token** adalah anti-polisi eksplisit di mana pelayan MCP menerima token klien tanpa pengesahan yang betul dan meneruskannya ke API hiliran, melanggar spesifikasi kebenaran MCP.  

#### **Implikasi Keselamatan**

- **Pengelakan Kawalan**: Penggunaan token terus dari klien ke API melepasi kawalan penting seperti penghadkan kadar, pengesahan, dan pemantauan  
- **Kerosakan Jejak Audit**: Token yang dikeluarkan hiliran menjadikan pengenalan klien mustahil, merosakkan kemampuan penyiasatan insiden  
- **Exfiltrasi Data Berasaskan Proksi**: Token tidak disahkan membolehkan pelaku berniat jahat menggunakan pelayan sebagai proksi untuk akses data tanpa izin  
- **Pelanggaran Sempadan Kepercayaan**: Andaian kepercayaan perkhidmatan hiliran mungkin dilanggar apabila asal token tidak dapat disahkan  
- **Pengembangan Serangan Pelbagai Perkhidmatan**: Token yang dikompromi diterima di pelbagai perkhidmatan membolehkan pergerakan lateral  

#### **Kawalan Keselamatan Diperlukan**

**Keperluan Tidak Boleh Runding:**
- **Pengesahan Token**: Pelayan MCP **TIDAK BOLEH** menerima token yang tidak dikeluarkan secara eksplisit untuk pelayan MCP  
- **Pengesahan Audien**: Sentiasa sahkan tuntutan audien token sepadan dengan identiti pelayan MCP  
- **Kitaran Hayat Token Yang Betul**: Laksanakan token capaian jangka pendek dengan praktik putaran selamat  


## Keselamatan Rantaian Bekalan untuk Sistem AI

Keselamatan rantaian bekalan telah berkembang melebihi pergantungan perisian tradisional untuk merangkumi seluruh ekosistem AI. Pelaksanaan MCP moden mesti mengesahkan dan memantau dengan tegas semua komponen berkaitan AI, kerana setiap satu memperkenalkan potensi kelemahan yang boleh mengkompromi integriti sistem.  

### Komponen Rantaian Bekalan AI yang Diperluaskan

**Pergantungan Perisian Tradisional:**
- Perpustakaan dan rangka kerja sumber terbuka  
- Imej bekas dan sistem asas  
- Alat pembangunan dan saluran binaan  
- Komponen dan perkhidmatan infrastruktur  

**Elemen Rantaian Bekalan Khusus AI:**
- **Model Asas**: Model pra-latih dari pelbagai pembekal yang memerlukan pengesahan asal usul  
- **Perkhidmatan Embedding**: Perkhidmatan vektorisasi luar dan pencarian semantik  
- **Penyedia Konteks**: Sumber data, pangkalan pengetahuan, dan repositori dokumen  
- **API Pihak Ketiga**: Perkhidmatan AI luar, saluran ML, dan titik pemprosesan data  
- **Artifak Model**: Berat, konfigurasi, dan varian model yang dilatih halus  
- **Sumber Data Latihan**: Set data yang digunakan untuk latihan model dan pelarasan halus  

### Strategi Keselamatan Rantaian Bekalan Menyeluruh

#### **Pengesahan & Kepercayaan Komponen**
- **Pengesahan Asal Usul**: Sahkan asal, pelesenan, dan integriti semua komponen AI sebelum integrasi  
- **Penilaian Keselamatan**: Lakukan imbasan kerentanan dan ulasan keselamatan untuk model, sumber data, dan perkhidmatan AI  
- **Analisis Reputasi**: Nilai rekod keselamatan dan amalan pembekal perkhidmatan AI  
- **Pengesahan Pematuhan**: Pastikan semua komponen memenuhi keperluan keselamatan dan peraturan organisasi  

#### **Saluran Pengeluaran Selamat**  
- **CI/CD Automatik dan Selamat**: Integrasikan imbasan keselamatan dalam saluran pengeluaran automatik  
- **Integriti Artifak**: Laksanakan pengesahan kriptografi untuk semua artifak yang diterapkan (kod, model, konfigurasi)  
- **Pengeluaran Bertahap**: Gunakan strategi pengeluaran progresif dengan pengesahan keselamatan pada setiap tahap  
- **Repositori Artifak Terpercaya**: Terapkan hanya dari registri dan repositori artifak yang telah disahkan dan selamat  

#### **Pemantauan & Respons Berterusan**
- **Imbasan Pergantungan**: Pemantauan kerentanan berterusan untuk semua pergantungan perisian dan komponen AI  
- **Pemantauan Model**: Penilaian berterusan terhadap tingkah laku model, aliran prestasi, dan anomali keselamatan  
- **Penjejakan Kesihatan Perkhidmatan**: Pantau perkhidmatan AI luar untuk ketersediaan, insiden keselamatan, dan perubahan dasar  
- **Integrasi Perisikan Ancaman**: Masukkan data ancaman khusus untuk risiko keselamatan AI dan ML  

#### **Kawalan Akses & Privilege Paling Minimum**
- **Kebenaran Tahap Komponen**: Hadkan akses ke model, data, dan perkhidmatan berdasarkan keperluan perniagaan  
- **Pengurusan Akaun Perkhidmatan**: Laksanakan akaun perkhidmatan khusus dengan kebenaran minimum yang diperlukan  
- **Segmen Rangkaian**: Asingkan komponen AI dan hadkan akses rangkaian antara perkhidmatan  
- **Kawalan Gateway API**: Gunakan gateway API berpusat untuk mengawal dan memantau akses ke perkhidmatan AI luar  

#### **Respons Insiden & Pemulihan**
- **Prosedur Respons Pantas**: Proses yang ditetapkan untuk penampalan atau penggantian komponen AI yang dikompromi  
- **Putaran Kredensial**: Sistem automatik untuk memutarkan rahsia, kekunci API, dan kredensial perkhidmatan  
- **Keupayaan Rollback**: Keupayaan untuk segera kembali ke versi komponen AI yang diketahui selamat sebelum ini  
- **Pemulihan Pelanggaran Rantaian Bekalan**: Prosedur khusus untuk bertindak balas terhadap kompromi perkhidmatan AI hiliran  

### Alat Keselamatan & Integrasi Microsoft

**GitHub Advanced Security** menyediakan perlindungan rantaian bekalan yang menyeluruh termasuk:  
- **Imbasan Rahsia**: Pengesanan automatik kredensial, kekunci API, dan token dalam repositori  
- **Imbasan Pergantungan**: Penilaian kerentanan untuk pergantungan dan perpustakaan sumber terbuka  
- **Analisis CodeQL**: Analisis kod statik untuk kelemahan keselamatan dan isu pengekodan  
- **Wawasan Rantaian Bekalan**: Ketelusan dalam kesihatan pergantungan dan status keselamatan  

**Integrasi Azure DevOps & Azure Repos:**  
- Integrasi imbasan keselamatan tanpa gangguan merentasi platform pembangunan Microsoft  
- Pemeriksaan keselamatan automatik dalam Azure Pipelines untuk beban kerja AI  
- Penerapan dasar untuk pengeluaran komponen AI yang selamat  

**Amalan Dalaman Microsoft:**  
Microsoft melaksanakan amalan keselamatan rantaian bekalan yang meluas merentasi semua produk. Ketahui pendekatan terbukti di [Perjalanan Memastikan Keselamatan Rantaian Bekalan Perisian di Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).  


## Amalan Terbaik Keselamatan Asas

Pelaksanaan MCP mewarisi dan membina ke atas postur keselamatan sedia ada organisasi anda. Menguatkan amalan keselamatan asas dengan ketara meningkatkan keselamatan keseluruhan sistem AI dan pelaksanaan MCP.  

### Asas-asas Keselamatan Teras

#### **Amalan Pembangunan Selamat**
- **Pematuhan OWASP**: Lindungi daripada kerentanan aplikasi web [OWASP Top 10](https://owasp.org/www-project-top-ten/)  
- **Perlindungan Khusus AI**: Laksanakan kawalan untuk [OWASP Top 10 untuk LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- **Pengurusan Rahsia Selamat**: Gunakan peti besi khusus untuk token, kekunci API, dan data konfigurasi sensitif  
- **Penyulitan Sepenuh**: Laksanakan komunikasi selamat merentasi semua komponen aplikasi dan aliran data  
- **Pengesahan Input**: Pengesahan ketat bagi semua input pengguna, parameter API, dan sumber data  

#### **Pengukuhan Infrastruktur**
- **Pengesahan Berbilang Faktor**: MFA diwajibkan untuk semua akaun pentadbir dan perkhidmatan  
- **Pengurusan Tampalan**: Penampalan automatik dan tepat pada masanya untuk sistem operasi, rangka kerja, dan pergantungan  
- **Integrasi Penyedia Identiti**: Pengurusan identiti berpusat melalui penyedia identiti perusahaan (Microsoft Entra ID, Active Directory)  
- **Segmen Rangkaian**: Pengasingan logik komponen MCP untuk mengehadkan potensi pergerakan lateral  
- **Prinsip Privilege Paling Minimum**: Kebenaran minimum diperlukan untuk semua komponen sistem dan akaun  

#### **Pemantauan & Pengesanan Keselamatan**
- **Pencatatan Komprehensif**: Pencatatan terperinci aktiviti aplikasi AI, termasuk interaksi klien-pelayan MCP  
- **Integrasi SIEM**: Pengurusan maklumat dan peristiwa keselamatan berpusat untuk pengesanan anomali  
- **Analitik Tingkah Laku**: Pemantauan dikuasakan AI untuk mengesan corak luar biasa dalam tingkah laku sistem dan pengguna  
- **Perisikan Ancaman**: Integrasi suapan ancaman luar dan petunjuk kompromi (IOC)  
- **Respons Insiden**: Prosedur ditakrif dengan baik untuk pengesanan, respons, dan pemulihan insiden keselamatan  

#### **Seni Bina Zero Trust**
- **Jangan Percaya, Sentiasa Sahkan**: Pengesahan berterusan terhadap pengguna, peranti, dan sambungan rangkaian  
- **Mikro-Segmen**: Kawalan rangkaian granular yang mengasingkan beban kerja dan perkhidmatan individu  
- **Keselamatan Berfokus Identiti**: Polisi keselamatan berdasarkan identiti yang disahkan dan bukan lokasi rangkaian  
- **Penilaian Risiko Berterusan**: Penilaian postur keselamatan dinamik berdasarkan konteks dan tingkah laku semasa  
- **Akses Bersyarat**: Kawalan akses yang menyesuaikan berdasarkan faktor risiko, lokasi, dan kepercayaan peranti  

### Corak Integrasi Perusahaan

#### **Integrasi Ekosistem Keselamatan Microsoft**
- **Microsoft Defender for Cloud**: Pengurusan postur keselamatan cloud yang komprehensif  
- **Azure Sentinel**: Kemampuan SIEM dan SOAR asli cloud untuk perlindungan beban kerja AI  
- **Microsoft Entra ID**: Pengurusan identiti dan akses perusahaan dengan polisi akses bersyarat  
- **Azure Key Vault**: Pengurusan rahsia berpusat dengan sokongan modul keselamatan perkakasan (HSM)  
- **Microsoft Purview**: Tadbir urus data dan pematuhan untuk sumber data dan aliran kerja AI  

#### **Pematuhan & Tadbir Urus**
- **Penyesuaian Peraturan**: Pastikan pelaksanaan MCP memenuhi keperluan pematuhan khusus industri (GDPR, HIPAA, SOC 2)  

- **Pengelasan Data**: Pengkategorian dan pengendalian yang betul terhadap data sensitif yang diproses oleh sistem AI  
- **Jejak Audit**: Perekodan komprehensif untuk pematuhan peraturan dan investigasi forensik  
- **Kawalan Privasi**: Pelaksanaan prinsip privasi-secara-reka dalam seni bina sistem AI  
- **Pengurusan Perubahan**: Proses formal untuk tinjauan keselamatan terhadap pengubahsuaian sistem AI  

Amalan asas ini mewujudkan garis asas keselamatan yang kukuh yang meningkatkan keberkesanan kawalan keselamatan khusus MCP dan menyediakan perlindungan menyeluruh untuk aplikasi berasaskan AI.  

## Perkara Penting Keselamatan  

- **Pendekatan Keselamatan Berlapis**: Gabungkan amalan keselamatan asas (pengekodan selamat, keistimewaan minimum, pengesahan rantai bekalan, pemantauan berterusan) dengan kawalan khusus AI untuk perlindungan menyeluruh  

- **Lanskap Ancaman Khusus AI**: Sistem MCP menghadapi risiko unik termasuk suntikan arahan, pencemaran alat, pembajakan sesi, masalah wakil keliru, kerentanan laluan token, dan kebenaran berlebihan yang memerlukan mitigasi khusus  

- **Keunggulan Pengesahan & Kebenaran**: Laksanakan pengesahan kukuh menggunakan penyedia identiti luaran (Microsoft Entra ID), tegakkan pengesahan token yang betul, dan jangan sekali-kali terima token yang tidak secara eksplisit dikeluarkan untuk pelayan MCP anda  

- **Pencegahan Serangan AI**: Guna Microsoft Prompt Shields dan Azure Content Safety untuk mempertahankan terhadap serangan suntikan arahan tidak langsung dan pencemaran alat, sambil mengesahkan metadata alat dan memantau perubahan dinamik  

- **Keselamatan Sesi & Pengangkutan**: Gunakan ID sesi yang selamat secara kriptografi dan tidak deterministik yang dikaitkan dengan identiti pengguna, laksanakan pengurusan kitaran hayat sesi yang betul, dan jangan sekali-kali menggunakan sesi untuk pengesahan  

- **Amalan Terbaik Keselamatan OAuth**: Cegah serangan wakil keliru melalui persetujuan pengguna yang jelas untuk klien berdaftar secara dinamik, pelaksanaan OAuth 2.1 yang betul dengan PKCE, dan pengesahan URI pengalihan yang ketat  

- **Prinsip Keselamatan Token**: Elakkan corak anti laluan token, sahkan tuntutan audiens token, laksanakan token jangka pendek dengan putaran selamat, dan kekalkan sempadan kepercayaan yang jelas  

- **Keselamatan Rantaian Bekalan Menyeluruh**: Perlakukan semua komponen ekosistem AI (model, penanaman, penyedia konteks, API luaran) dengan ketegasan keselamatan yang sama seperti pergantungan perisian tradisional  

- **Evolusi Berterusan**: Kekal terkini dengan spesifikasi MCP yang berkembang pesat, menyumbang kepada piawaian komuniti keselamatan, dan mengekalkan sikap keselamatan adaptif seiring protokol matang  

- **Integrasi Keselamatan Microsoft**: Manfaatkan ekosistem keselamatan komprehensif Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) untuk perlindungan penskalaan MCP yang dipertingkatkan  

## Sumber Komprehensif  

### **Dokumentasi Rasmi Keselamatan MCP**  
- [Spesifikasi MCP (Semasa: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)  
- [Amalan Terbaik Keselamatan MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)  
- [Spesifikasi Kebenaran MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)  
- [Repositori GitHub MCP](https://github.com/modelcontextprotocol)  

### **Sumber Keselamatan OWASP MCP**  
- [Panduan Keselamatan OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - Top 10 OWASP MCP komprehensif dengan panduan pelaksanaan Azure  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Risiko keselamatan rasmi OWASP MCP  
- [Bengkel Sidang Kemuncak Keselamatan MCP (Sherpa)](https://azure-samples.github.io/sherpa/) - Latihan keselamatan praktik untuk MCP di Azure  

### **Piawaian & Amalan Terbaik Keselamatan**  
- [Amalan Terbaik Keselamatan OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [Top 10 Keselamatan Aplikasi Web OWASP](https://owasp.org/www-project-top-ten/)  
- [Top 10 OWASP untuk Model Bahasa Besar](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- [Laporan Pertahanan Digital Microsoft](https://aka.ms/mddr)  

### **Penyelidikan & Analisis Keselamatan AI**  
- [Suntikan Arahan dalam MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [Serangan Pencemaran Alat (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)  
- [Taklimat Penyelidikan Keselamatan MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)  

### **Penyelesaian Keselamatan Microsoft**  
- [Dokumentasi Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  
- [Perkhidmatan Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)  
- [Keselamatan Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)  
- [Amalan Terbaik Pengurusan Token Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)  
- [GitHub Advanced Security](https://github.com/security/advanced-security)  

### **Panduan Pelaksanaan & Tutorial**  
- [Pengurusan API Azure sebagai Pintu Autentikasi MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)  
- [Pengesahan Microsoft Entra ID dengan Pelayan MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)  
- [Penyimpanan & Penyulitan Token Selamat (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)  

### **DevOps & Keselamatan Rantaian Bekalan**  
- [Keselamatan Azure DevOps](https://azure.microsoft.com/products/devops)  
- [Keselamatan Repos Azure](https://azure.microsoft.com/products/devops/repos/)  
- [Perjalanan Keselamatan Rantaian Bekalan Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)  

## **Dokumentasi Keselamatan Tambahan**  

Untuk panduan keselamatan komprehensif, rujuk dokumen khusus dalam bahagian ini:  

- **[Contoh Kebenaran CIMD dan DCR](./samples/cimd-dcr-auth/README.md)** - Pelayan sumber MCP `2026-07-28` TypeScript yang boleh dijalankan membandingkan Dokumen Metadata ID Klien yang diutamakan dengan pendaftaran klien dinamik lama  
- **[Amalan Terbaik Keselamatan MCP](./mcp-security-best-practices.md)** - Amalan keselamatan lengkap untuk pelaksanaan MCP  
- **[Pelaksanaan Azure Content Safety](./azure-content-safety-implementation.md)** - Contoh pelaksanaan praktikal untuk integrasi Azure Content Safety  
- **[Kawalan Keselamatan MCP](./mcp-security-controls.md)** - Kawalan dan teknik keselamatan terkini untuk penskalaan MCP  
- **[Rujukan Pantas Amalan Terbaik MCP](./mcp-best-practices.md)** - Panduan rujukan pantas untuk amalan keselamatan MCP penting  
- **[BlueHat 2026: Memastikan masa depan AI: Mengamankan MCP dengan corak pertahanan berlapis](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Corak pertahanan berlapis dari Pusat Respons Keselamatan Microsoft (MSRC)  

### **Latihan Keselamatan Praktikal**  

- **[Bengkel Sidang Kemuncak Keselamatan MCP (Sherpa)](https://azure-samples.github.io/sherpa/)** - Bengkel praktikal komprehensif untuk mengamankan pelayan MCP di Azure dengan peringkat kem dari Base Camp ke Summit  
- **[Panduan Keselamatan OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)** - Seni bina rujukan dan panduan pelaksanaan untuk semua risiko OWASP MCP Top 10  

---  

## Apa Seterusnya  

Seterusnya: [Bab 3: Memulakan](../03-GettingStarted/README.md)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->