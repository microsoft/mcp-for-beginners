# Amalan Terbaik Keselamatan MCP - Kemas Kini September 2026

Panduan komprehensif ini menggariskan amalan terbaik keselamatan penting untuk
melaksanakan sistem Protokol Konteks Model (MCP) berdasarkan
**Spesifikasi MCP 2026-07-28** dan piawaian industri semasa. Amalan ini
menangani kedua-dua keprihatinan keselamatan tradisional dan ancaman khusus AI
yang unik kepada pelaksanaan MCP.

## Keperluan Keselamatan Kritikal

### Kawalan Keselamatan Wajib (Keperluan MESTI)

1. **Pengesahan Token**: Pelayan MCP **TIDAK MESTI** menerima mana-mana token yang tidak dikeluarkan secara eksplisit untuk pelayan MCP itu sendiri
2. **Pengesahan Kebenaran**: Pelayan MCP yang melaksanakan kebenaran **MESTI** mengesahkan SEMUA permintaan masuk dan **TIDAK MESTI** menggunakan sesi untuk pengesahan  
3. **Persetujuan Pengguna**: Pelayan proksi MCP yang menggunakan ID klien pihak ketiga statik **MESTI** mendapatkan persetujuan jelas untuk setiap klien MCP sebelum meneruskan aliran kebenaran
4. **Keselamatan Pemegang Negara**: Pelayan MCP **TIDAK MESTI** menganggap pegangan pemegang negara aplikasi sebagai pengesahan dan **MESTI** menganugerahkan kebenaran setiap
	permintaan yang menggunakannya


## Amalan Keselamatan Teras

### 1. Pengesahan & Penyucian Input
- **Pengesahan Input Komprehensif**: Sahkan dan nyahcemar semua input untuk mengelakkan serangan suntikan, masalah ‘confused deputy’, dan kerentanan suntikan prompt
- **Penguatkuasaan Skema Parameter**: Laksanakan pengesahan skema JSON yang ketat untuk semua parameter alat dan input API
- **Penapisan Kandungan**: Gunakan Microsoft Prompt Shields dan Azure Content Safety untuk menapis kandungan berniat jahat dalam prompt dan respons
- **Penyucian Output**: Sahkan dan nyahcemar semua output model sebelum disampaikan kepada pengguna atau sistem hiliran

### 2. Kecemerlangan Pengesahan & Kebenaran  
- **Penyedia Identiti Luaran**: Delegasikan pengesahan kepada penyedia identiti yang sudah wujud (Microsoft Entra ID, penyedia OAuth 2.1) daripada melaksanakan pengesahan khusus
- **Pendaftaran Klien**: Utamakan Dokumen Metadata ID Klien atau prapendaftaran; gunakan Pendaftaran Klien Dinamik yang sudah tidak digunakan hanya untuk keserasian
- **Kebenaran Halus**: Laksanakan kebenaran terperinci khusus alat mengikut prinsip hak sebaik mungkin
- **Pengurusan Kitaran Hayat Token**: Gunakan token akses jangka pendek dengan putaran selamat dan pengesahan audien yang betul
- **Pengesahan Pelbagai Faktor**: Perlukan MFA untuk semua akses pentadbiran dan operasi sensitif

### 3. Protokol Komunikasi Selamat
- **Keselamatan Lapisan Pengangkutan**: Gunakan HTTPS dengan pengesahan sijil yang betul
	untuk komunikasi HTTP jauh MCP; gunakan pengasingan proses dan perakuan persekitaran
	untuk pelayan stdio tempatan
- **Penyulitan Hujung-ke-Hujung**: Laksanakan lapisan penyulitan tambahan untuk data sangat sensitif dalam transit dan semasa disimpan
- **Pengurusan Sijil**: Kekalkan pengurusan kitaran hayat sijil yang betul dengan proses pembaharuan automatik
- **Penguatkuasaan Versi Protokol**: Gunakan MCP `2026-07-28`, sertakan metadata versi yang diperlukan pada setiap permintaan, dan tolak versi yang tidak disokong


### 4. Hadkan Kadar & Perlindungan Sumber Lanjutan
- **Hadkan Kadar Berbilang Lapisan**: Laksanakan had kadar mengikut pengguna, perakuan,
  operasi, alat, dan sumber untuk mengelakkan penyalahgunaan
- **Hadkan Kadar Adaptif**: Gunakan had kadar berasaskan pembelajaran mesin yang menyesuaikan dengan corak penggunaan dan petunjuk ancaman
- **Pengurusan Kuota Sumber**: Tetapkan had sesuai untuk sumber pengiraan, penggunaan memori, dan masa pelaksanaan
- **Perlindungan DDoS**: Laksanakan perlindungan DDoS menyeluruh dan sistem analisis trafik

### 5. Pencatatan & Pemantauan Komprehensif
- **Pencatatan Audit Berstruktur**: Laksanakan log terperinci yang boleh dicari untuk semua operasi MCP, pelaksanaan alat, dan acara keselamatan
- **Pemantauan Keselamatan Masa Nyata**: Pasang sistem SIEM dengan pengesanan anomali berkuasa AI untuk beban kerja MCP
- **Pencatatan Mematuhi Privasi**: Catatkan acara keselamatan sambil menghormati keperluan privasi data dan peraturan
- **Integrasi Respons Insiden**: Sambungkan sistem pencatatan kepada aliran kerja respons insiden automatik

### 6. Amalan Penyimpanan Selamat Dipertingkat
- **Modul Keselamatan Perkakasan**: Gunakan storan kunci disokong HSM (Azure Key Vault, AWS CloudHSM) untuk operasi kriptografi kritikal
- **Pengurusan Kunci Penyulitan**: Laksanakan putaran kunci, pengasingan, dan kawalan akses yang betul untuk kunci penyulitan
- **Pengurusan Rahsia**: Simpan semua kunci API, token, dan perakuan dalam sistem pengurusan rahsia khusus
- **Pengelasan Data**: Klasifikasikan data berdasarkan tahap sensitiviti dan gunakan langkah-langkah perlindungan sesuai

### 7. Pengurusan Token Lanjutan
- **Pencegahan Penyaluran Token**: Secara jelas mengharamkan corak penyaluran token yang memintas kawalan keselamatan
- **Pengesahan Audien**: Sentiasa sahkan tuntutan audien token sepadan dengan identiti pelayan MCP yang dimaksudkan
- **Kebenaran Berasaskan Tuntutan**: Laksanakan kebenaran terperinci berdasarkan tuntutan token dan atribut pengguna
- **Pengikatan Token**: Sahkan bahawa token menyasarkan sumber MCP yang dimaksudkan dan
	mengikat pemegang negara aplikasi di pihak pelayan kepada prinsipal yang disahkan

### 8. Negara Aplikasi Selamat

- **Pemegang Negara Kriptografi**: Hasilkan pemegang yang kabur, tidak deterministik
	untuk negara yang merangkumi permintaan
- **Pengikatan Khusus Pengguna**: Ikat setiap pemegang di pihak pelayan kepada
	prinsipal yang disahkan; jangan percayai ID pengguna yang dibekalkan oleh klien
- **Kawalan Kitaran Hayat**: Tamatkan tempoh dan batalkan pemegang, dan takrifkan bagaimana pemanggil
	memulihkan dari negara lapuk
- **Kebenaran Per Permintaan**: Semak semula kebenaran setiap kali pemegang
	disebut; pemegang ialah nama, bukan kelayakan

### 9. Kawalan Keselamatan Khusus AI
- **Pertahanan Suntikan Prompt**: Gunakan Microsoft Prompt Shields dengan spotlighting, delimiter, dan teknik penandaan data
- **Pencegahan Peracunan Alat**: Sahkan metadata alat, pantau perubahan dinamik, dan sahkan integriti alat
- **Pengesahan Output Model**: Imbas output model untuk potensi kebocoran data, kandungan berbahaya, atau pelanggaran polisi keselamatan
- **Perlindungan Tetingkap Konteks**: Laksanakan kawalan untuk mengelakkan peracunan tetingkap konteks dan serangan manipulasi

### 10. Keselamatan Pelaksanaan Alat
- **Pelaksanaan Sandboxing**: Jalankan pelaksanaan alat dalam persekitaran terasing berbekas dengan had sumber
- **Pemisahan Keistimewaan**: Laksanakan alat dengan keistimewaan minimum yang diperlukan dan akaun servis berasingan
- **Pengasingan Rangkaian**: Laksanakan segmentasi rangkaian untuk persekitaran pelaksanaan alat
- **Pemantauan Pelaksanaan**: Pantau pelaksanaan alat untuk tingkah laku anomali, penggunaan sumber, dan pelanggaran keselamatan

### 11. Pengesahan Keselamatan Berterusan
- **Ujian Keselamatan Automatik**: Integrasikan ujian keselamatan ke dalam saluran CI/CD dengan alat seperti GitHub Advanced Security
- **Pengurusan Kerentanan**: Imbas secara berkala semua pergantungan, termasuk model AI dan perkhidmatan luaran
- **Ujian Penembusan**: Lakukan penilaian keselamatan berkala yang secara khusus mensasarkan pelaksanaan MCP
- **Ulasan Kod Keselamatan**: Laksanakan ulasan keselamatan wajib untuk semua perubahan kod berkaitan MCP

### 12. Keselamatan Rantaian Bekalan untuk AI
- **Verifikasi Komponen**: Sahkan asal-usul, integriti, dan keselamatan semua komponen AI (model, embedding, API)
- **Pengurusan Pergantungan**: Kekalkan inventori terkini semua pergantungan perisian dan AI dengan pengesanan kerentanan
- **Repositori Dipercayai**: Gunakan sumber yang disahkan dan dipercayai untuk semua model AI, perpustakaan, dan alat
- **Pemantauan Rantaian Bekalan**: Pantau secara berterusan untuk kompromi dalam penyedia perkhidmatan AI dan repositori model


## Corak Keselamatan Lanjutan

### Seni Bina Zero Trust untuk MCP
- **Jangan Percaya, Sentiasa Sahkan**: Laksanakan pengesahan berterusan untuk semua peserta MCP
- **Mikro-segmentasi**: Mengasingkan komponen MCP dengan kawalan rangkaian dan identiti yang terperinci
- **Akses Bersyarat**: Laksanakan kawalan akses berasaskan risiko yang menyesuaikan dengan konteks dan tingkah laku
- **Penilaian Risiko Berterusan**: Menilai secara dinamik kedudukan keselamatan berdasarkan indikator ancaman semasa

### Pelaksanaan AI Memelihara Privasi
- **Pemimimuman Data**: Hanya dedahkan data minimum yang perlu untuk setiap operasi MCP
- **Privasi Diferensial**: Laksanakan teknik pemeliharaan privasi untuk pemprosesan data sensitif
- **Penyulitan Homomorfik**: Gunakan teknik penyulitan lanjutan untuk pengiraan selamat ke atas data yang disulitkan
- **Pembelajaran Persekutuan**: Laksanakan pendekatan pembelajaran diedarkan yang memelihara lokaliti dan privasi data

### Respons Insiden untuk Sistem AI
- **Prosedur Insiden Khusus AI**: Bangunkan prosedur respons insiden yang disesuaikan untuk ancaman AI dan MCP
- **Respons Automatik**: Laksanakan pengandungan dan pembaikan automatik untuk insiden keselamatan AI biasa  
- **Keupayaan Perundangan**: Menyediakan kesiapsiagaan perundangan bagi kompromi sistem AI dan kebocoran data
- **Prosedur Pemulihan**: Menetapkan prosedur untuk pemulihan daripada pencemaran model AI, serangan suntikan prompt, dan kompromi perkhidmatan

## Sumber & Piawaian Pelaksanaan

### 🏔️ Latihan Keselamatan Praktikal
- **[Bengkel Sidang Kemuncak Keselamatan MCP (Sherpa)](https://azure-samples.github.io/sherpa/)** - Bengkel praktikal menyeluruh untuk mengamankan pelayan MCP di Azure
- **[Panduan Keselamatan OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)** - Seni bina rujukan dan panduan pelaksanaan OWASP MCP Top 10

### Dokumentasi Rasmi MCP
- [Spesifikasi MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Spesifikasi protokol MCP semasa
- [Amalan Terbaik Keselamatan MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Panduan keselamatan rasmi
- [Spesifikasi Kebenaran MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - Corak kebenaran HTTP
- [Pengangkutan MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Keperluan pengangkutan

### Penyelesaian Keselamatan Microsoft
- [Perisai Prompt Microsoft](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Perlindungan suntikan prompt lanjutan
- [Keselamatan Kandungan Azure](https://learn.microsoft.com/azure/ai-services/content-safety/) - Penapisan kandungan AI menyeluruh
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Pengurusan identiti dan akses perusahaan
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Pengurusan rahsia dan kelayakan selamat
- [Keselamatan Lanjutan GitHub](https://github.com/security/advanced-security) - Pengimbasan keselamatan rantaian bekalan dan kod

### Piawaian & Kerangka Kerja Keselamatan
- [Amalan Terbaik Keselamatan OAuth 2.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Panduan keselamatan OAuth semasa
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Risiko keselamatan aplikasi web
- [OWASP Top 10 untuk LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Risiko keselamatan khusus AI
- [Kerangka Pengurusan Risiko AI NIST](https://www.nist.gov/itl/ai-risk-management-framework) - Pengurusan risiko AI menyeluruh
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Sistem pengurusan keselamatan maklumat

### Panduan & Tutorial Pelaksanaan
- [Pengurusan API Azure sebagai Pintu Masuk Kebenaran MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Corak pengesahan perusahaan
- [Microsoft Entra ID dengan Pelayan MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integrasi penyedia identiti
- [Pelaksanaan Penyimpanan Token Selamat](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Amalan terbaik pengurusan token
- [Penyulitan Dari Hujung ke Hujung untuk AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Corak penyulitan lanjutan

### Sumber Keselamatan Lanjutan
- [Kitaran Hayat Pembangunan Keselamatan Microsoft](https://www.microsoft.com/sdl) - Amalan pembangunan selamat
- [Panduan Pasukan Merah AI](https://learn.microsoft.com/security/ai-red-team/) - Ujian keselamatan khusus AI
- [Pemodelan Ancaman untuk Sistem AI](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodologi pemodelan ancaman AI
- [Kejuruteraan Privasi untuk AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Teknik AI pemeliharaan privasi

### Pematuhan & Tadbir Urus
- [Pematuhan GDPR untuk AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Pematuhan privasi dalam sistem AI
- [Kerangka Tadbir Urus AI](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Pelaksanaan AI bertanggungjawab
- [SOC 2 untuk Perkhidmatan AI](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Kawalan keselamatan untuk pembekal perkhidmatan AI
- [Pematuhan HIPAA untuk AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Keperluan pematuhan AI penjagaan kesihatan

### DevSecOps & Automasi
- [Paip DevSecOps untuk AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Paip pembangunan AI yang selamat
- [Ujian Keselamatan Automatik](https://learn.microsoft.com/security/engineering/devsecops) - Pengesahan keselamatan berterusan
- [Keselamatan Infrastruktur sebagai Kod](https://learn.microsoft.com/security/engineering/infrastructure-security) - Penghantaran infrastruktur yang selamat
- [Keselamatan Kontena untuk AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Keselamatan pengkontenan beban kerja AI

### Pemantauan & Respons Insiden  
- [Azure Monitor untuk Beban Kerja AI](https://learn.microsoft.com/azure/azure-monitor/overview) - Penyelesaian pemantauan menyeluruh
- [Respons Insiden Keselamatan AI](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Prosedur insiden khusus AI
- [SIEM untuk Sistem AI](https://learn.microsoft.com/azure/sentinel/overview) - Pengurusan maklumat dan acara keselamatan

- [Intelijen Ancaman untuk AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - sumber intelijen ancaman AI

## 🔄 Penambahbaikan Berterusan

### Kekal Terkini dengan Piawaian Berkembang
- **Kemaskini Spesifikasi MCP**: Pantau perubahan spesifikasi MCP rasmi dan nasihat keselamatan
- **Intelijen Ancaman**: Langgani suapan ancaman keselamatan AI dan pangkalan data kerentanan  
- **Penglibatan Komuniti**: Sertai perbincangan komuniti keselamatan MCP dan kumpulan kerja
- **Penilaian Berkala**: Jalankan penilaian kedudukan keselamatan suku tahunan dan kemaskini amalan sepadan

### Menyumbang kepada Keselamatan MCP
- **Penyelidikan Keselamatan**: Sumbang kepada penyelidikan keselamatan MCP dan program pendedahan kerentanan
- **Perkongsian Amalan Terbaik**: Kongsi pelaksanaan keselamatan dan pengajaran dengan komuniti
- **Pembangunan Piawaian**: Sertai pembangunan spesifikasi MCP dan penciptaan piawaian keselamatan
- **Pembangunan Alat**: Bangunkan dan kongsi alat dan perpustakaan keselamatan untuk ekosistem MCP

---

*Dokumen ini mencerminkan amalan terbaik keselamatan MCP setakat 9 September 2026,
berdasarkan Spesifikasi MCP `2026-07-28`. Amalan keselamatan harus disemak secara berkala
selaras dengan perkembangan protokol dan landskap ancaman.*

## Apa Seterusnya

- Baca: [Amalan Terbaik Keselamatan MCP](./mcp-security-best-practices.md)
- Kembali ke: [Gambaran Keseluruhan Modul Keselamatan](./README.md)
- Terus ke: [Modul 3: Mula Bermula](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->