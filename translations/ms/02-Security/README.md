# MCP Security: Perlindungan Komprehensif untuk Sistem AI

[![MCP Security Best Practices](../../../translated_images/ms/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Klik imej di atas untuk menonton video pelajaran ini)_

Keselamatan adalah asas kepada reka bentuk sistem AI, sebab itulah kami mengutamakannya sebagai bahagian kedua kami. Ini selaras dengan prinsip **Secure by Design** Microsoft dari [Inisiatif Masa Depan Selamat](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Protokol Konteks Model (MCP) membawa keupayaan baru yang hebat kepada aplikasi yang dipacu AI sambil memperkenalkan cabaran keselamatan unik yang melangkaui risiko perisian tradisional. Sistem MCP menghadapi kedua-dua kebimbangan keselamatan yang telah lama wujud (pengekodan selamat, keistimewaan paling minimum, keselamatan rantaian bekalan) dan ancaman khusus AI baru termasuk suntikan arahan, keracunan alat, pembajakan sesi, serangan pegawai keliru, kelemahan laluan token, dan pengubahsuaian keupayaan dinamik.

Pelajaran ini meneroka risiko keselamatan paling kritikal dalam pelaksanaan MCP—meliputi pengesahan, kebenaran, kebenaran berlebihan, suntikan arahan tidak langsung, keselamatan sesi, masalah pegawai keliru, pengurusan token, dan kelemahan rantaian bekalan. Anda akan mempelajari kawalan yang boleh diambil tindakan dan amalan terbaik untuk mengurangkan risiko ini sambil memanfaatkan penyelesaian Microsoft seperti Prompt Shields, Azure Content Safety, dan GitHub Advanced Security untuk mengukuhkan pelaksanaan MCP anda.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- **Kenal Pasti Ancaman Khusus MCP**: Mengenal pasti risiko keselamatan unik dalam sistem MCP termasuk suntikan arahan, keracunan alat, kebenaran berlebihan, pembajakan sesi, masalah pegawai keliru, kelemahan laluan token, dan risiko rantaian bekalan
- **Gunakan Kawalan Keselamatan**: Melaksanakan mitigasi berkesan termasuk pengesahan kukuh, akses keistimewaan paling minimum, pengurusan token selamat, kawalan keselamatan sesi, dan pengesahan rantaian bekalan
- **Manfaatkan Penyelesaian Keselamatan Microsoft**: Memahami dan menggunakan Microsoft Prompt Shields, Azure Content Safety, dan GitHub Advanced Security untuk perlindungan beban kerja MCP
- **Sahkan Keselamatan Alat**: Mengenal pasti kepentingan pengesahan metadata alat, pemantauan perubahan dinamik, dan mempertahankan terhadap serangan suntikan arahan tidak langsung
- **Gabungkan Amalan Terbaik**: Menggabungkan asas keselamatan yang telah ditetapkan (pengekodan selamat, pengukuhan pelayan, zero trust) dengan kawalan khusus MCP untuk perlindungan menyeluruh

# Seni Bina & Kawalan Keselamatan MCP

Pelaksanaan MCP moden memerlukan pendekatan keselamatan berlapis yang menangani kedua-dua keselamatan perisian tradisional dan ancaman khusus AI. Spesifikasi MCP yang berkembang pesat terus mematangkan kawalan keselamatannya, membolehkan integrasi lebih baik dengan seni bina keselamatan perusahaan dan amalan terbaik yang telah ditetapkan.

Penyelidikan dari [Laporan Pertahanan Digital Microsoft](https://aka.ms/mddr) menunjukkan bahawa **98% pelanggaran yang dilaporkan dapat dicegah dengan amalan kebersihan keselamatan yang kukuh**. Strategi perlindungan paling berkesan menggabungkan amalan keselamatan asas dengan kawalan khusus MCP—langkah keselamatan asas yang terbukti kekal paling berimpak dalam mengurangkan risiko keselamatan keseluruhan.

## Lanskap Keselamatan Semasa

> **Nota:** Maklumat ini mencerminkan piawaian keselamatan MCP setakat **18 Disember 2025**. Protokol MCP terus berkembang dengan pesat, dan pelaksanaan masa depan mungkin memperkenalkan corak pengesahan baru dan kawalan yang dipertingkatkan. Sentiasa rujuk [Spesifikasi MCP](https://spec.modelcontextprotocol.io/), [repositori MCP GitHub](https://github.com/modelcontextprotocol), dan [dokumentasi amalan terbaik keselamatan](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) terkini untuk panduan terbaru.

### Evolusi Pengesahan MCP

Spesifikasi MCP telah berkembang dengan ketara dalam pendekatannya terhadap pengesahan dan kebenaran:

- **Pendekatan Asal**: Spesifikasi awal memerlukan pembangun melaksanakan pelayan pengesahan tersuai, dengan pelayan MCP bertindak sebagai Pelayan Kebenaran OAuth 2.0 yang mengurus pengesahan pengguna secara langsung
- **Standard Semasa (2025-11-25)**: Spesifikasi terkini membenarkan pelayan MCP mendelegasikan pengesahan kepada penyedia identiti luaran (seperti Microsoft Entra ID), meningkatkan postur keselamatan dan mengurangkan kerumitan pelaksanaan
- **Keselamatan Lapisan Pengangkutan**: Sokongan dipertingkatkan untuk mekanisme pengangkutan selamat dengan corak pengesahan yang betul untuk sambungan tempatan (STDIO) dan jauh (Streamable HTTP)

## Keselamatan Pengesahan & Kebenaran

### Cabaran Keselamatan Semasa

Pelaksanaan MCP moden menghadapi beberapa cabaran pengesahan dan kebenaran:

### Risiko & Vektor Ancaman

- **Logik Kebenaran Salah Konfigurasi**: Pelaksanaan kebenaran yang cacat dalam pelayan MCP boleh mendedahkan data sensitif dan menggunakan kawalan akses secara salah
- **Kompromi Token OAuth**: Kecurian token pelayan MCP tempatan membolehkan penyerang menyamar sebagai pelayan dan mengakses perkhidmatan hiliran
- **Kelemahan Laluan Token**: Pengendalian token yang tidak betul mencipta laluan pintas kawalan keselamatan dan jurang akauntabiliti
- **Kebenaran Berlebihan**: Pelayan MCP yang mempunyai keistimewaan berlebihan melanggar prinsip keistimewaan paling minimum dan memperluaskan permukaan serangan

#### Laluan Token: Anti-Polisi Kritikal

**Laluan token adalah dilarang secara tegas** dalam spesifikasi kebenaran MCP semasa kerana implikasi keselamatan yang serius:

##### Pengelakan Kawalan Keselamatan
- Pelayan MCP dan API hiliran melaksanakan kawalan keselamatan kritikal (had kadar, pengesahan permintaan, pemantauan trafik) yang bergantung pada pengesahan token yang betul
- Penggunaan token terus dari klien ke API memintas perlindungan penting ini, melemahkan seni bina keselamatan

##### Cabaran Akauntabiliti & Audit  
- Pelayan MCP tidak dapat membezakan antara klien yang menggunakan token yang dikeluarkan oleh huluan, memecahkan jejak audit
- Log pelayan sumber hiliran menunjukkan asal permintaan yang mengelirukan dan bukan perantara pelayan MCP sebenar
- Penyiasatan insiden dan audit pematuhan menjadi jauh lebih sukar

##### Risiko Eksfiltrasi Data
- Tuntutan token yang tidak disahkan membolehkan pelaku jahat dengan token curi menggunakan pelayan MCP sebagai proksi untuk eksfiltrasi data
- Pelanggaran sempadan kepercayaan membenarkan corak akses tanpa kebenaran yang memintas kawalan keselamatan yang dimaksudkan

##### Vektor Serangan Pelbagai Perkhidmatan
- Token yang dikompromi diterima oleh pelbagai perkhidmatan membolehkan pergerakan sisi merentasi sistem yang bersambung
- Andaian kepercayaan antara perkhidmatan mungkin dilanggar apabila asal token tidak dapat disahkan

### Kawalan Keselamatan & Mitigasi

**Keperluan Keselamatan Kritikal:**

> **WAJIB**: Pelayan MCP **TIDAK BOLEH** menerima sebarang token yang tidak dikeluarkan secara eksplisit untuk pelayan MCP

#### Kawalan Pengesahan & Kebenaran

- **Semakan Kebenaran Teliti**: Lakukan audit menyeluruh terhadap logik kebenaran pelayan MCP untuk memastikan hanya pengguna dan klien yang dimaksudkan dapat mengakses sumber sensitif
  - **Panduan Pelaksanaan**: [Azure API Management sebagai Pintu Gerbang Pengesahan untuk Pelayan MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integrasi Identiti**: [Menggunakan Microsoft Entra ID untuk Pengesahan Pelayan MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Pengurusan Token Selamat**: Laksanakan [amalan terbaik pengesahan token dan kitar hayat Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Sahkan tuntutan audiens token sepadan dengan identiti pelayan MCP
  - Laksanakan dasar putaran dan tamat tempoh token yang betul
  - Cegah serangan ulang token dan penggunaan tanpa kebenaran

- **Penyimpanan Token Dilindungi**: Simpan token dengan penyulitan semasa rehat dan transit
  - **Amalan Terbaik**: [Garis Panduan Penyimpanan Token Selamat dan Penyulitan](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Pelaksanaan Kawalan Akses

- **Prinsip Keistimewaan Paling Minimum**: Berikan pelayan MCP hanya kebenaran minimum yang diperlukan untuk fungsi yang dimaksudkan
  - Semakan dan kemas kini kebenaran secara berkala untuk mengelakkan kelebihan keistimewaan
  - **Dokumentasi Microsoft**: [Akses Keistimewaan Paling Minimum yang Selamat](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Kawalan Akses Berasaskan Peranan (RBAC)**: Laksanakan penugasan peranan yang terperinci
  - Hadkan peranan dengan ketat kepada sumber dan tindakan tertentu
  - Elakkan kebenaran luas atau tidak perlu yang memperluaskan permukaan serangan

- **Pemantauan Kebenaran Berterusan**: Laksanakan audit dan pemantauan akses berterusan
  - Pantau corak penggunaan kebenaran untuk anomali
  - Segera betulkan keistimewaan berlebihan atau tidak digunakan

## Ancaman Keselamatan Khusus AI

### Serangan Suntikan Arahan & Manipulasi Alat

Pelaksanaan MCP moden menghadapi vektor serangan khusus AI yang canggih yang tidak dapat ditangani sepenuhnya oleh langkah keselamatan tradisional:

#### **Suntikan Arahan Tidak Langsung (Suntikan Arahan Rentas Domain)**

**Suntikan Arahan Tidak Langsung** mewakili salah satu kelemahan paling kritikal dalam sistem AI yang diaktifkan MCP. Penyerang menyisipkan arahan berniat jahat dalam kandungan luaran—dokumen, halaman web, e-mel, atau sumber data—yang kemudian diproses oleh sistem AI sebagai arahan sah.

**Senario Serangan:**
- **Suntikan Berasaskan Dokumen**: Arahan berniat jahat tersembunyi dalam dokumen yang diproses yang mencetuskan tindakan AI yang tidak diingini
- **Eksploitasi Kandungan Web**: Halaman web yang dikompromi mengandungi arahan tertanam yang memanipulasi tingkah laku AI apabila diimbas
- **Serangan Berasaskan E-mel**: Arahan berniat jahat dalam e-mel yang menyebabkan pembantu AI membocorkan maklumat atau melakukan tindakan tanpa kebenaran
- **Pencemaran Sumber Data**: Pangkalan data atau API yang dikompromi menyajikan kandungan tercemar kepada sistem AI

**Impak Dunia Sebenar**: Serangan ini boleh mengakibatkan eksfiltrasi data, pelanggaran privasi, penjanaan kandungan berbahaya, dan manipulasi interaksi pengguna. Untuk analisis terperinci, lihat [Suntikan Arahan dalam MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/ms/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Serangan Keracunan Alat**

**Keracunan Alat** mensasarkan metadata yang mentakrifkan alat MCP, mengeksploitasi bagaimana LLM mentafsirkan penerangan alat dan parameter untuk membuat keputusan pelaksanaan.

**Mekanisme Serangan:**
- **Manipulasi Metadata**: Penyerang menyisipkan arahan berniat jahat ke dalam penerangan alat, definisi parameter, atau contoh penggunaan
- **Arahan Tidak Kelihatan**: Arahan tersembunyi dalam metadata alat yang diproses oleh model AI tetapi tidak kelihatan kepada pengguna manusia
- **Pengubahsuaian Alat Dinamik ("Rug Pulls")**: Alat yang diluluskan oleh pengguna kemudian diubah untuk melakukan tindakan berniat jahat tanpa pengetahuan pengguna
- **Suntikan Parameter**: Kandungan berniat jahat disisipkan dalam skema parameter alat yang mempengaruhi tingkah laku model

**Risiko Pelayan Dihoskan**: Pelayan MCP jauh menghadirkan risiko tinggi kerana definisi alat boleh dikemas kini selepas kelulusan awal pengguna, mewujudkan senario di mana alat yang sebelum ini selamat menjadi berniat jahat. Untuk analisis menyeluruh, lihat [Serangan Keracunan Alat (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/ms/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Vektor Serangan AI Tambahan**

- **Suntikan Arahan Rentas Domain (XPIA)**: Serangan canggih yang menggunakan kandungan dari pelbagai domain untuk memintas kawalan keselamatan
- **Pengubahsuaian Keupayaan Dinamik**: Perubahan masa nyata keupayaan alat yang melarikan diri dari penilaian keselamatan awal
- **Keracunan Tetingkap Konteks**: Serangan yang memanipulasi tetingkap konteks besar untuk menyembunyikan arahan berniat jahat
- **Serangan Kekeliruan Model**: Mengeksploitasi had model untuk mencipta tingkah laku yang tidak dapat diramalkan atau tidak selamat

### Impak Risiko Keselamatan AI

**Kesan Berimpak Tinggi:**
- **Eksfiltrasi Data**: Akses tanpa kebenaran dan kecurian data sensitif perusahaan atau peribadi
- **Pelanggaran Privasi**: Pendedahan maklumat peribadi yang boleh dikenal pasti (PII) dan data perniagaan sulit  
- **Manipulasi Sistem**: Pengubahsuaian tidak diingini pada sistem dan aliran kerja kritikal
- **Kecurian Kredensial**: Kompromi token pengesahan dan kredensial perkhidmatan
- **Pergerakan Lateral**: Penggunaan sistem AI yang dikompromi sebagai titik tolak untuk serangan rangkaian yang lebih luas

### Penyelesaian Keselamatan AI Microsoft

#### **AI Prompt Shields: Perlindungan Lanjutan Terhadap Serangan Suntikan**

Microsoft **AI Prompt Shields** menyediakan pertahanan menyeluruh terhadap serangan suntikan arahan langsung dan tidak langsung melalui pelbagai lapisan keselamatan:

##### **Mekanisme Perlindungan Teras:**

1. **Pengesanan & Penapisan Lanjutan**
   - Algoritma pembelajaran mesin dan teknik NLP mengesan arahan berniat jahat dalam kandungan luaran
   - Analisis masa nyata dokumen, halaman web, e-mel, dan sumber data untuk ancaman tertanam
   - Pemahaman kontekstual corak arahan sah berbanding berniat jahat

2. **Teknik Penyorotan**  
   - Membezakan antara arahan sistem yang dipercayai dan input luaran yang berpotensi dikompromi
   - Kaedah transformasi teks yang meningkatkan relevansi model sambil mengasingkan kandungan berniat jahat
   - Membantu sistem AI mengekalkan hierarki arahan yang betul dan mengabaikan arahan yang disuntik

3. **Sistem Pembatas & Penandaan Data**
   - Definisi sempadan eksplisit antara mesej sistem yang dipercayai dan teks input luaran
   - Penanda khas menyorot sempadan antara sumber data yang dipercayai dan tidak dipercayai
   - Pemisahan jelas mengelakkan kekeliruan arahan dan pelaksanaan arahan tanpa kebenaran

4. **Perisikan Ancaman Berterusan**
   - Microsoft memantau corak serangan yang muncul dan mengemas kini pertahanan secara berterusan
   - Pemburuan ancaman proaktif untuk teknik suntikan dan vektor serangan baru
   - Kemas kini model keselamatan berkala untuk mengekalkan keberkesanan terhadap ancaman yang berkembang

5. **Integrasi Azure Content Safety**
   - Sebahagian daripada suite keselamatan kandungan Azure AI yang komprehensif
   - Pengesanan tambahan untuk cubaan jailbreak, kandungan berbahaya, dan pelanggaran dasar keselamatan
   - Kawalan keselamatan bersatu merentasi komponen aplikasi AI

**Sumber Pelaksanaan**: [Dokumentasi Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/ms/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Ancaman Keselamatan MCP Lanjutan

### Kelemahan Pembajakan Sesi

**Pembajakan sesi** mewakili vektor serangan kritikal dalam pelaksanaan MCP berstatus di mana pihak tidak dibenarkan memperoleh dan menyalahgunakan pengecam sesi sah untuk menyamar sebagai klien dan melakukan tindakan tanpa kebenaran.

#### **Senario Serangan & Risiko**

- **Suntikan Arahan Pembajakan Sesi**: Penyerang dengan ID sesi curi menyuntik acara berniat jahat ke dalam pelayan yang berkongsi keadaan sesi, berpotensi mencetuskan tindakan berbahaya atau mengakses data sensitif
- **Penyamaran Langsung**: ID sesi curi membolehkan panggilan pelayan MCP langsung yang memintas pengesahan, menganggap penyerang sebagai pengguna sah
- **Aliran Boleh Sambung Semula yang Dikompromi**: Penyerang boleh menamatkan permintaan lebih awal, menyebabkan klien sah menyambung semula dengan kandungan yang berpotensi berniat jahat

#### **Kawalan Keselamatan untuk Pengurusan Sesi**

**Keperluan Kritikal:**
- **Pengesahan Kebenaran**: Pelayan MCP yang melaksanakan kebenaran **MESTI** mengesahkan SEMUA permintaan masuk dan **TIDAK MESTI** bergantung pada sesi untuk pengesahan
- **Penjanaan Sesi Selamat**: Gunakan ID sesi yang selamat secara kriptografi dan tidak deterministik yang dijana dengan penjana nombor rawak yang selamat
- **Pengikatan Khusus Pengguna**: Ikat ID sesi kepada maklumat khusus pengguna menggunakan format seperti `<user_id>:<session_id>` untuk mengelakkan penyalahgunaan sesi silang pengguna
- **Pengurusan Kitaran Hayat Sesi**: Laksanakan tamat tempoh, putaran, dan pembatalan yang betul untuk mengehadkan tetingkap kerentanan
- **Keselamatan Pengangkutan**: HTTPS wajib untuk semua komunikasi bagi mengelakkan penyadapan ID sesi

### Masalah Deputi Keliru

**Masalah deputi keliru** berlaku apabila pelayan MCP bertindak sebagai proksi pengesahan antara klien dan perkhidmatan pihak ketiga, mewujudkan peluang untuk memintas kebenaran melalui eksploitasi ID klien statik.

#### **Mekanisme Serangan & Risiko**

- **Pintas Persetujuan Berasaskan Kuki**: Pengesahan pengguna sebelumnya mencipta kuki persetujuan yang dieksploitasi oleh penyerang melalui permintaan kebenaran berniat jahat dengan URI pengalihan yang direka
- **Kecurian Kod Kebenaran**: Kuki persetujuan sedia ada mungkin menyebabkan pelayan kebenaran melangkau skrin persetujuan, mengalihkan kod ke titik akhir yang dikawal penyerang  
- **Akses API Tanpa Kebenaran**: Kod kebenaran yang dicuri membolehkan pertukaran token dan penyamaran pengguna tanpa kelulusan eksplisit

#### **Strategi Mitigasi**

**Kawalan Wajib:**
- **Keperluan Persetujuan Eksplisit**: Pelayan proksi MCP yang menggunakan ID klien statik **MESTI** mendapatkan persetujuan pengguna untuk setiap klien yang didaftarkan secara dinamik
- **Pelaksanaan Keselamatan OAuth 2.1**: Ikuti amalan keselamatan OAuth terkini termasuk PKCE (Proof Key for Code Exchange) untuk semua permintaan kebenaran
- **Pengesahan Klien Ketat**: Laksanakan pengesahan ketat terhadap URI pengalihan dan pengecam klien untuk mengelakkan eksploitasi

### Kerentanan Penyaluran Token  

**Penyaluran token** mewakili anti-pola eksplisit di mana pelayan MCP menerima token klien tanpa pengesahan yang betul dan meneruskannya ke API hiliran, melanggar spesifikasi kebenaran MCP.

#### **Implikasi Keselamatan**

- **Pintas Kawalan**: Penggunaan token klien terus ke API memintas kawalan had kadar, pengesahan, dan pemantauan yang kritikal
- **Kerosakan Jejak Audit**: Token yang dikeluarkan dari hulu menjadikan pengenalan klien mustahil, memecahkan keupayaan siasatan insiden
- **Eksfiltrasi Data Berasaskan Proksi**: Token yang tidak disahkan membolehkan pelaku berniat jahat menggunakan pelayan sebagai proksi untuk akses data tanpa kebenaran
- **Pelanggaran Sempadan Kepercayaan**: Andaian kepercayaan perkhidmatan hiliran mungkin dilanggar apabila asal token tidak dapat disahkan
- **Pengembangan Serangan Pelbagai Perkhidmatan**: Token yang dikompromi diterima merentasi pelbagai perkhidmatan membolehkan pergerakan lateral

#### **Kawalan Keselamatan Diperlukan**

**Keperluan Tidak Boleh Dirunding:**
- **Pengesahan Token**: Pelayan MCP **TIDAK MESTI** menerima token yang tidak dikeluarkan secara eksplisit untuk pelayan MCP
- **Pengesahan Audiens**: Sentiasa sahkan tuntutan audiens token sepadan dengan identiti pelayan MCP
- **Kitaran Hayat Token yang Betul**: Laksanakan token capaian jangka pendek dengan amalan putaran selamat


## Keselamatan Rantaian Bekalan untuk Sistem AI

Keselamatan rantaian bekalan telah berkembang melebihi kebergantungan perisian tradisional untuk merangkumi keseluruhan ekosistem AI. Pelaksanaan MCP moden mesti mengesahkan dan memantau dengan ketat semua komponen berkaitan AI, kerana setiap satu memperkenalkan potensi kerentanan yang boleh menjejaskan integriti sistem.

### Komponen Rantaian Bekalan AI yang Diperluaskan

**Kebergantungan Perisian Tradisional:**
- Perpustakaan dan rangka kerja sumber terbuka
- Imej kontena dan sistem asas  
- Alat pembangunan dan saluran binaan
- Komponen dan perkhidmatan infrastruktur

**Elemen Rantaian Bekalan Khusus AI:**
- **Model Asas**: Model pra-latih dari pelbagai penyedia yang memerlukan pengesahan asal usul
- **Perkhidmatan Embedding**: Perkhidmatan vektorisasi dan carian semantik luaran
- **Penyedia Konteks**: Sumber data, pangkalan pengetahuan, dan repositori dokumen  
- **API Pihak Ketiga**: Perkhidmatan AI luaran, saluran ML, dan titik akhir pemprosesan data
- **Artefak Model**: Berat, konfigurasi, dan varian model yang disesuaikan
- **Sumber Data Latihan**: Set data yang digunakan untuk latihan dan penalaan model

### Strategi Keselamatan Rantaian Bekalan Menyeluruh

#### **Pengesahan Komponen & Kepercayaan**
- **Pengesahan Asal Usul**: Sahkan asal, lesen, dan integriti semua komponen AI sebelum integrasi
- **Penilaian Keselamatan**: Jalankan imbasan kerentanan dan ulasan keselamatan untuk model, sumber data, dan perkhidmatan AI
- **Analisis Reputasi**: Nilai rekod keselamatan dan amalan penyedia perkhidmatan AI
- **Pengesahan Pematuhan**: Pastikan semua komponen memenuhi keperluan keselamatan dan peraturan organisasi

#### **Saluran Penghantaran Selamat**  
- **Keselamatan CI/CD Automatik**: Integrasi imbasan keselamatan sepanjang saluran penghantaran automatik
- **Integriti Artefak**: Laksanakan pengesahan kriptografi untuk semua artefak yang dihantar (kod, model, konfigurasi)
- **Penghantaran Berperingkat**: Gunakan strategi penghantaran progresif dengan pengesahan keselamatan di setiap peringkat
- **Repositori Artefak Dipercayai**: Hantar hanya dari registri dan repositori artefak yang disahkan dan selamat

#### **Pemantauan & Respons Berterusan**
- **Imbasan Kebergantungan**: Pemantauan kerentanan berterusan untuk semua kebergantungan perisian dan komponen AI
- **Pemantauan Model**: Penilaian berterusan tingkah laku model, pergeseran prestasi, dan anomali keselamatan
- **Penjejakan Kesihatan Perkhidmatan**: Pantau perkhidmatan AI luaran untuk ketersediaan, insiden keselamatan, dan perubahan polisi
- **Integrasi Intelijen Ancaman**: Gabungkan suapan ancaman khusus untuk risiko keselamatan AI dan ML

#### **Kawalan Akses & Hak Istimewa Minimum**
- **Kebenaran Tahap Komponen**: Hadkan akses kepada model, data, dan perkhidmatan berdasarkan keperluan perniagaan
- **Pengurusan Akaun Perkhidmatan**: Laksanakan akaun perkhidmatan khusus dengan kebenaran minimum yang diperlukan
- **Segmentasi Rangkaian**: Pisahkan komponen AI dan hadkan akses rangkaian antara perkhidmatan
- **Kawalan Gerbang API**: Gunakan gerbang API berpusat untuk mengawal dan memantau akses ke perkhidmatan AI luaran

#### **Respons Insiden & Pemulihan**
- **Prosedur Respons Pantas**: Proses yang ditetapkan untuk menampal atau menggantikan komponen AI yang dikompromi
- **Putaran Kredensial**: Sistem automatik untuk memutar rahsia, kunci API, dan kredensial perkhidmatan
- **Keupayaan Rollback**: Keupayaan untuk segera kembali ke versi komponen AI yang diketahui baik
- **Pemulihan Pelanggaran Rantaian Bekalan**: Prosedur khusus untuk bertindak balas terhadap kompromi perkhidmatan AI hulu

### Alat & Integrasi Keselamatan Microsoft

**GitHub Advanced Security** menyediakan perlindungan rantaian bekalan menyeluruh termasuk:
- **Imbasan Rahsia**: Pengesanan automatik kredensial, kunci API, dan token dalam repositori
- **Imbasan Kebergantungan**: Penilaian kerentanan untuk kebergantungan dan perpustakaan sumber terbuka
- **Analisis CodeQL**: Analisis kod statik untuk kerentanan keselamatan dan isu pengkodan
- **Wawasan Rantaian Bekalan**: Ketelusan dalam kesihatan kebergantungan dan status keselamatan

**Integrasi Azure DevOps & Azure Repos:**
- Integrasi imbasan keselamatan lancar merentasi platform pembangunan Microsoft
- Pemeriksaan keselamatan automatik dalam Azure Pipelines untuk beban kerja AI
- Penguatkuasaan polisi untuk penghantaran komponen AI yang selamat

**Amalan Dalaman Microsoft:**
Microsoft melaksanakan amalan keselamatan rantaian bekalan yang meluas merentasi semua produk. Ketahui pendekatan terbukti di [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Amalan Terbaik Keselamatan Asas

Pelaksanaan MCP mewarisi dan membina atas postur keselamatan sedia ada organisasi anda. Memperkukuh amalan keselamatan asas secara signifikan meningkatkan keselamatan keseluruhan sistem AI dan penghantaran MCP.

### Asas Keselamatan Teras

#### **Amalan Pembangunan Selamat**
- **Pematuhan OWASP**: Lindungi daripada kerentanan aplikasi web [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- **Perlindungan Khusus AI**: Laksanakan kawalan untuk [OWASP Top 10 untuk LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Pengurusan Rahsia Selamat**: Gunakan peti besi khusus untuk token, kunci API, dan data konfigurasi sensitif
- **Penyulitan Sepanjang Jalan**: Laksanakan komunikasi selamat merentasi semua komponen aplikasi dan aliran data
- **Pengesahan Input**: Pengesahan ketat semua input pengguna, parameter API, dan sumber data

#### **Pengukuhan Infrastruktur**
- **Pengesahan Faktor Pelbagai**: MFA wajib untuk semua akaun pentadbir dan perkhidmatan
- **Pengurusan Tampalan**: Tampalan automatik dan tepat pada masanya untuk sistem operasi, rangka kerja, dan kebergantungan  
- **Integrasi Penyedia Identiti**: Pengurusan identiti berpusat melalui penyedia identiti perusahaan (Microsoft Entra ID, Active Directory)
- **Segmentasi Rangkaian**: Pengasingan logik komponen MCP untuk mengehadkan potensi pergerakan lateral
- **Prinsip Hak Istimewa Minimum**: Kebenaran minimum yang diperlukan untuk semua komponen dan akaun sistem

#### **Pemantauan & Pengesanan Keselamatan**
- **Pencatatan Menyeluruh**: Pencatatan terperinci aktiviti aplikasi AI, termasuk interaksi klien-pelayan MCP
- **Integrasi SIEM**: Pengurusan maklumat dan peristiwa keselamatan berpusat untuk pengesanan anomali
- **Analitik Tingkah Laku**: Pemantauan berkuasa AI untuk mengesan corak luar biasa dalam tingkah laku sistem dan pengguna
- **Intelijen Ancaman**: Integrasi suapan ancaman luaran dan indikator kompromi (IOC)
- **Respons Insiden**: Prosedur terperinci untuk pengesanan, respons, dan pemulihan insiden keselamatan

#### **Seni Bina Zero Trust**
- **Jangan Percaya, Sentiasa Sahkan**: Pengesahan berterusan pengguna, peranti, dan sambungan rangkaian
- **Mikro-Segmentasi**: Kawalan rangkaian granular yang mengasingkan beban kerja dan perkhidmatan individu
- **Keselamatan Berpusat Identiti**: Polisi keselamatan berdasarkan identiti yang disahkan dan bukan lokasi rangkaian
- **Penilaian Risiko Berterusan**: Penilaian postur keselamatan dinamik berdasarkan konteks dan tingkah laku semasa
- **Akses Bersyarat**: Kawalan akses yang menyesuaikan berdasarkan faktor risiko, lokasi, dan kepercayaan peranti

### Corak Integrasi Perusahaan

#### **Integrasi Ekosistem Keselamatan Microsoft**
- **Microsoft Defender for Cloud**: Pengurusan postur keselamatan awan menyeluruh
- **Azure Sentinel**: SIEM dan SOAR asli awan untuk perlindungan beban kerja AI
- **Microsoft Entra ID**: Pengurusan identiti dan akses perusahaan dengan polisi akses bersyarat
- **Azure Key Vault**: Pengurusan rahsia berpusat dengan sokongan modul keselamatan perkakasan (HSM)
- **Microsoft Purview**: Tadbir urus data dan pematuhan untuk sumber data dan aliran kerja AI

#### **Pematuhan & Tadbir Urus**
- **Penyesuaian Peraturan**: Pastikan pelaksanaan MCP memenuhi keperluan pematuhan khusus industri (GDPR, HIPAA, SOC 2)
- **Klasifikasi Data**: Pengkategorian dan pengendalian data sensitif yang diproses oleh sistem AI
- **Jejak Audit**: Pencatatan menyeluruh untuk pematuhan peraturan dan siasatan forensik
- **Kawalan Privasi**: Pelaksanaan prinsip privasi-semasa-reka bentuk dalam seni bina sistem AI
- **Pengurusan Perubahan**: Proses formal untuk ulasan keselamatan terhadap pengubahsuaian sistem AI

Amalan asas ini mewujudkan asas keselamatan yang kukuh yang meningkatkan keberkesanan kawalan keselamatan khusus MCP dan menyediakan perlindungan menyeluruh untuk aplikasi berasaskan AI.

## Intipati Utama Keselamatan

- **Pendekatan Keselamatan Berlapis**: Gabungkan amalan keselamatan asas (pengkodan selamat, hak istimewa minimum, pengesahan rantaian bekalan, pemantauan berterusan) dengan kawalan khusus AI untuk perlindungan menyeluruh

- **Lanskap Ancaman Khusus AI**: Sistem MCP menghadapi risiko unik termasuk suntikan prompt, keracunan alat, rampasan sesi, masalah deputi keliru, kerentanan penyaluran token, dan kebenaran berlebihan yang memerlukan mitigasi khusus

- **Kecemerlangan Pengesahan & Kebenaran**: Laksanakan pengesahan kukuh menggunakan penyedia identiti luaran (Microsoft Entra ID), kuatkuasakan pengesahan token yang betul, dan jangan sekali-kali menerima token yang tidak dikeluarkan secara eksplisit untuk pelayan MCP anda

- **Pencegahan Serangan AI**: Gunakan Microsoft Prompt Shields dan Azure Content Safety untuk mempertahankan daripada serangan suntikan prompt tidak langsung dan keracunan alat, sambil mengesahkan metadata alat dan memantau perubahan dinamik

- **Keselamatan Sesi & Pengangkutan**: Gunakan ID sesi yang selamat secara kriptografi, tidak deterministik dan diikat kepada identiti pengguna, laksanakan pengurusan kitaran hayat sesi yang betul, dan jangan gunakan sesi untuk pengesahan

- **Amalan Terbaik Keselamatan OAuth**: Cegah serangan deputi keliru melalui persetujuan pengguna eksplisit untuk klien yang didaftarkan secara dinamik, pelaksanaan OAuth 2.1 yang betul dengan PKCE, dan pengesahan URI pengalihan yang ketat  

- **Prinsip Keselamatan Token**: Elakkan anti-pola penyaluran token, sahkan tuntutan audiens token, laksanakan token jangka pendek dengan putaran selamat, dan kekalkan sempadan kepercayaan yang jelas

- **Keselamatan Rantaian Bekalan Menyeluruh**: Perlakukan semua komponen ekosistem AI (model, embedding, penyedia konteks, API luaran) dengan ketelitian keselamatan yang sama seperti kebergantungan perisian tradisional

- **Evolusi Berterusan**: Kekal terkini dengan spesifikasi MCP yang berkembang pesat, sumbang kepada piawaian komuniti keselamatan, dan kekalkan postur keselamatan adaptif semasa protokol matang

- **Integrasi Keselamatan Microsoft**: Manfaatkan ekosistem keselamatan Microsoft yang menyeluruh (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) untuk perlindungan penghantaran MCP yang dipertingkatkan

## Sumber Menyeluruh

### **Dokumentasi Rasmi Keselamatan MCP**
- [Spesifikasi MCP (Semasa: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Amalan Terbaik Keselamatan MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Spesifikasi Kebenaran MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [Repositori GitHub MCP](https://github.com/modelcontextprotocol)

### **Piawaian & Amalan Terbaik Keselamatan**
- [Amalan Terbaik Keselamatan OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Keselamatan Aplikasi Web](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 untuk Model Bahasa Besar](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Laporan Pertahanan Digital Microsoft](https://aka.ms/mddr)

### **Penyelidikan & Analisis Keselamatan AI**
- [Suntikan Prompt dalam MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Serangan Keracunan Alat (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Taklimat Penyelidikan Keselamatan MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Penyelesaian Keselamatan Microsoft**
- [Dokumentasi Pelindung Prompt Microsoft](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Perkhidmatan Keselamatan Kandungan Azure](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Keselamatan Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Amalan Terbaik Pengurusan Token Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [Keselamatan Lanjutan GitHub](https://github.com/security/advanced-security)

### **Panduan Pelaksanaan & Tutorial**
- [Pengurusan API Azure sebagai Pintu Masuk Pengesahan MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Pengesahan Microsoft Entra ID dengan Pelayan MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Penyimpanan Token Selamat dan Penyulitan (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **Keselamatan DevOps & Rantaian Bekalan**
- [Keselamatan Azure DevOps](https://azure.microsoft.com/products/devops)
- [Keselamatan Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Perjalanan Keselamatan Rantaian Bekalan Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Dokumentasi Keselamatan Tambahan**

Untuk panduan keselamatan yang komprehensif, rujuk dokumen khusus dalam bahagian ini:

- **[Amalan Terbaik Keselamatan MCP 2025](./mcp-security-best-practices-2025.md)** - Amalan terbaik keselamatan lengkap untuk pelaksanaan MCP
- **[Pelaksanaan Keselamatan Kandungan Azure](./azure-content-safety-implementation.md)** - Contoh pelaksanaan praktikal untuk integrasi Keselamatan Kandungan Azure  
- **[Kawalan Keselamatan MCP 2025](./mcp-security-controls-2025.md)** - Kawalan dan teknik keselamatan terkini untuk pelaksanaan MCP
- **[Rujukan Pantas Amalan Terbaik MCP](./mcp-best-practices.md)** - Panduan rujukan pantas untuk amalan keselamatan MCP penting

---

## Apa Seterusnya

Seterusnya: [Bab 3: Memulakan](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->