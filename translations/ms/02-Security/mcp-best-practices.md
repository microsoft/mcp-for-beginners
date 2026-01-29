# Amalan Terbaik Keselamatan MCP 2025

Panduan komprehensif ini menggariskan amalan terbaik keselamatan penting untuk melaksanakan sistem Protokol Konteks Model (MCP) berdasarkan **Spesifikasi MCP 2025-11-25** terkini dan piawaian industri semasa. Amalan ini menangani kedua-dua kebimbangan keselamatan tradisional dan ancaman khusus AI yang unik kepada pelaksanaan MCP.

## Keperluan Keselamatan Kritikal

### Kawalan Keselamatan Wajib (Keperluan MESTI)

1. **Pengesahan Token**: Pelayan MCP **MESTI TIDAK** menerima sebarang token yang tidak dikeluarkan secara eksplisit untuk pelayan MCP itu sendiri  
2. **Pengesahan Kebenaran**: Pelayan MCP yang melaksanakan kebenaran **MESTI** mengesahkan SEMUA permintaan masuk dan **MESTI TIDAK** menggunakan sesi untuk pengesahan  
3. **Persetujuan Pengguna**: Pelayan proksi MCP yang menggunakan ID klien statik **MESTI** mendapatkan persetujuan pengguna secara eksplisit untuk setiap klien yang didaftarkan secara dinamik  
4. **ID Sesi Selamat**: Pelayan MCP **MESTI** menggunakan ID sesi yang selamat secara kriptografi, tidak deterministik yang dijana dengan penjana nombor rawak yang selamat

## Amalan Keselamatan Teras

### 1. Pengesahan & Penapisan Input
- **Pengesahan Input Menyeluruh**: Sahkan dan tapis semua input untuk mengelakkan serangan suntikan, masalah wakil keliru, dan kerentanan suntikan arahan  
- **Penguatkuasaan Skema Parameter**: Laksanakan pengesahan skema JSON yang ketat untuk semua parameter alat dan input API  
- **Penapisan Kandungan**: Gunakan Microsoft Prompt Shields dan Azure Content Safety untuk menapis kandungan berniat jahat dalam arahan dan respons  
- **Penapisan Output**: Sahkan dan tapis semua output model sebelum dipersembahkan kepada pengguna atau sistem hiliran

### 2. Kecemerlangan Pengesahan & Kebenaran  
- **Penyedia Identiti Luaran**: Serahkan pengesahan kepada penyedia identiti yang telah ditubuhkan (Microsoft Entra ID, penyedia OAuth 2.1) dan bukannya melaksanakan pengesahan tersuai  
- **Kebenaran Berbutir Halus**: Laksanakan kebenaran berbutir halus khusus alat mengikut prinsip keistimewaan paling minimum  
- **Pengurusan Kitaran Hayat Token**: Gunakan token capaian jangka pendek dengan putaran selamat dan pengesahan audien yang betul  
- **Pengesahan Faktor Berganda**: Memerlukan MFA untuk semua akses pentadbiran dan operasi sensitif

### 3. Protokol Komunikasi Selamat
- **Keselamatan Lapisan Pengangkutan**: Gunakan HTTPS/TLS 1.3 untuk semua komunikasi MCP dengan pengesahan sijil yang betul  
- **Penyulitan Hujung-ke-Hujung**: Laksanakan lapisan penyulitan tambahan untuk data yang sangat sensitif semasa transit dan dalam simpanan  
- **Pengurusan Sijil**: Kekalkan pengurusan kitaran hayat sijil yang betul dengan proses pembaharuan automatik  
- **Penguatkuasaan Versi Protokol**: Gunakan versi protokol MCP terkini (2025-11-25) dengan rundingan versi yang betul.

### 4. Had Kadar & Perlindungan Sumber Lanjutan
- **Had Kadar Berlapis**: Laksanakan had kadar pada tahap pengguna, sesi, alat, dan sumber untuk mengelakkan penyalahgunaan  
- **Had Kadar Adaptif**: Gunakan had kadar berasaskan pembelajaran mesin yang menyesuaikan dengan corak penggunaan dan penunjuk ancaman  
- **Pengurusan Kuota Sumber**: Tetapkan had yang sesuai untuk sumber pengkomputeran, penggunaan memori, dan masa pelaksanaan  
- **Perlindungan DDoS**: Gunakan perlindungan DDoS yang komprehensif dan sistem analisis trafik

### 5. Log & Pemantauan Komprehensif
- **Log Audit Berstruktur**: Laksanakan log terperinci dan boleh dicari untuk semua operasi MCP, pelaksanaan alat, dan acara keselamatan  
- **Pemantauan Keselamatan Masa Nyata**: Gunakan sistem SIEM dengan pengesanan anomali berkuasa AI untuk beban kerja MCP  
- **Log Mematuhi Privasi**: Log acara keselamatan sambil menghormati keperluan dan peraturan privasi data  
- **Integrasi Respons Insiden**: Sambungkan sistem log kepada aliran kerja respons insiden automatik

### 6. Amalan Penyimpanan Selamat Dipertingkat
- **Modul Keselamatan Perkakasan**: Gunakan penyimpanan kunci yang disokong HSM (Azure Key Vault, AWS CloudHSM) untuk operasi kriptografi kritikal  
- **Pengurusan Kunci Penyulitan**: Laksanakan putaran kunci, pengasingan, dan kawalan akses yang betul untuk kunci penyulitan  
- **Pengurusan Rahsia**: Simpan semua kunci API, token, dan kelayakan dalam sistem pengurusan rahsia khusus  
- **Pengelasan Data**: Klasifikasikan data berdasarkan tahap kepekaan dan gunakan langkah perlindungan yang sesuai

### 7. Pengurusan Token Lanjutan
- **Pencegahan Penyaluran Token**: Larang secara eksplisit corak penyaluran token yang memintas kawalan keselamatan  
- **Pengesahan Audien**: Sentiasa sahkan tuntutan audien token sepadan dengan identiti pelayan MCP yang dimaksudkan  
- **Kebenaran Berasaskan Tuntutan**: Laksanakan kebenaran berbutir halus berdasarkan tuntutan token dan atribut pengguna  
- **Pengikatan Token**: Ikat token kepada sesi, pengguna, atau peranti tertentu jika sesuai

### 8. Pengurusan Sesi Selamat
- **ID Sesi Kriptografi**: Jana ID sesi menggunakan penjana nombor rawak yang selamat secara kriptografi (bukan urutan boleh diramal)  
- **Pengikatan Khusus Pengguna**: Ikat ID sesi kepada maklumat khusus pengguna menggunakan format selamat seperti `<user_id>:<session_id>`  
- **Kawalan Kitaran Hayat Sesi**: Laksanakan mekanisme tamat tempoh, putaran, dan pembatalan sesi yang betul  
- **Header Keselamatan Sesi**: Gunakan header keselamatan HTTP yang sesuai untuk perlindungan sesi

### 9. Kawalan Keselamatan Khusus AI
- **Pertahanan Suntikan Arahan**: Gunakan Microsoft Prompt Shields dengan spotlighting, delimiter, dan teknik penandaan data  
- **Pencegahan Keracunan Alat**: Sahkan metadata alat, pantau perubahan dinamik, dan sahkan integriti alat  
- **Pengesahan Output Model**: Imbas output model untuk kebocoran data berpotensi, kandungan berbahaya, atau pelanggaran dasar keselamatan  
- **Perlindungan Tetingkap Konteks**: Laksanakan kawalan untuk mengelakkan keracunan dan serangan manipulasi tetingkap konteks

### 10. Keselamatan Pelaksanaan Alat
- **Pengasingan Pelaksanaan**: Jalankan pelaksanaan alat dalam persekitaran berkontena, terasing dengan had sumber  
- **Pemisahan Keistimewaan**: Laksanakan alat dengan keistimewaan minimum yang diperlukan dan akaun perkhidmatan berasingan  
- **Pengasingan Rangkaian**: Laksanakan segmentasi rangkaian untuk persekitaran pelaksanaan alat  
- **Pemantauan Pelaksanaan**: Pantau pelaksanaan alat untuk tingkah laku anomali, penggunaan sumber, dan pelanggaran keselamatan

### 11. Pengesahan Keselamatan Berterusan
- **Ujian Keselamatan Automatik**: Integrasikan ujian keselamatan ke dalam saluran CI/CD dengan alat seperti GitHub Advanced Security  
- **Pengurusan Kerentanan**: Imbas secara berkala semua pergantungan, termasuk model AI dan perkhidmatan luaran  
- **Ujian Penembusan**: Jalankan penilaian keselamatan secara berkala yang khusus mensasarkan pelaksanaan MCP  
- **Ulasan Kod Keselamatan**: Laksanakan ulasan keselamatan wajib untuk semua perubahan kod berkaitan MCP

### 12. Keselamatan Rantaian Bekalan untuk AI
- **Pengesahan Komponen**: Sahkan asal usul, integriti, dan keselamatan semua komponen AI (model, embedding, API)  
- **Pengurusan Pergantungan**: Kekalkan inventori terkini semua perisian dan pergantungan AI dengan penjejakan kerentanan  
- **Repositori Dipercayai**: Gunakan sumber yang disahkan dan dipercayai untuk semua model AI, perpustakaan, dan alat  
- **Pemantauan Rantaian Bekalan**: Pantau secara berterusan untuk kompromi dalam penyedia perkhidmatan AI dan repositori model

## Corak Keselamatan Lanjutan

### Seni Bina Zero Trust untuk MCP
- **Jangan Percaya, Sentiasa Sahkan**: Laksanakan pengesahan berterusan untuk semua peserta MCP  
- **Mikro-segmentasi**: Asingkan komponen MCP dengan kawalan rangkaian dan identiti berbutir halus  
- **Akses Bersyarat**: Laksanakan kawalan akses berasaskan risiko yang menyesuaikan dengan konteks dan tingkah laku  
- **Penilaian Risiko Berterusan**: Nilai secara dinamik postur keselamatan berdasarkan penunjuk ancaman semasa

### Pelaksanaan AI Memelihara Privasi
- **Minimisasi Data**: Dedahkan hanya data minimum yang diperlukan untuk setiap operasi MCP  
- **Privasi Diferensial**: Laksanakan teknik memelihara privasi untuk pemprosesan data sensitif  
- **Penyulitan Homomorfik**: Gunakan teknik penyulitan lanjutan untuk pengiraan selamat ke atas data yang disulitkan  
- **Pembelajaran Persekutuan**: Laksanakan pendekatan pembelajaran teragih yang memelihara lokaliti dan privasi data

### Respons Insiden untuk Sistem AI
- **Prosedur Insiden Khusus AI**: Bangunkan prosedur respons insiden yang disesuaikan untuk ancaman khusus AI dan MCP  
- **Respons Automatik**: Laksanakan penahanan dan pemulihan automatik untuk insiden keselamatan AI biasa  
- **Keupayaan Forensik**: Kekalkan kesiapsiagaan forensik untuk kompromi sistem AI dan kebocoran data  
- **Prosedur Pemulihan**: Tetapkan prosedur untuk pemulihan daripada keracunan model AI, serangan suntikan arahan, dan kompromi perkhidmatan

## Sumber & Piawaian Pelaksanaan

### Dokumentasi Rasmi MCP
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Spesifikasi protokol MCP terkini  
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Panduan keselamatan rasmi  
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Corak pengesahan dan kebenaran  
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Keperluan keselamatan lapisan pengangkutan

### Penyelesaian Keselamatan Microsoft
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Perlindungan suntikan arahan lanjutan  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Penapisan kandungan AI komprehensif  
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Pengurusan identiti dan akses perusahaan  
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Pengurusan rahsia dan kelayakan selamat  
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Pengimbasan keselamatan rantaian bekalan dan kod

### Piawaian & Rangka Kerja Keselamatan
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Panduan keselamatan OAuth terkini  
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Risiko keselamatan aplikasi web  
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Risiko keselamatan khusus AI  
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Pengurusan risiko AI komprehensif  
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Sistem pengurusan keselamatan maklumat

### Panduan & Tutorial Pelaksanaan
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Corak pengesahan perusahaan  
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integrasi penyedia identiti  
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Amalan terbaik pengurusan token  
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Corak penyulitan lanjutan

### Sumber Keselamatan Lanjutan
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Amalan pembangunan selamat  
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - Ujian keselamatan khusus AI  
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodologi pemodelan ancaman AI  
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Teknik AI memelihara privasi

### Pematuhan & Tadbir Urus
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Pematuhan privasi dalam sistem AI  
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Pelaksanaan AI bertanggungjawab  
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Kawalan keselamatan untuk penyedia perkhidmatan AI  
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Keperluan pematuhan AI penjagaan kesihatan

### DevSecOps & Automasi
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Saluran pembangunan AI selamat  
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Pengesahan keselamatan berterusan  
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Penyebaran infrastruktur selamat  
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Keselamatan kontena beban kerja AI

### Pemantauan & Respons Insiden  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Penyelesaian pemantauan komprehensif  
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Prosedur insiden khusus AI  
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Pengurusan maklumat dan acara keselamatan  
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Sumber risikan ancaman AI

## 🔄 Penambahbaikan Berterusan

### Kekal Terkini dengan Piawaian Berkembang
- **Kemas Kini Spesifikasi MCP**: Pantau perubahan spesifikasi MCP rasmi dan nasihat keselamatan  
- **Risikan Ancaman**: Langgan suapan ancaman keselamatan AI dan pangkalan data kerentanan  
- **Penglibatan Komuniti**: Sertai perbincangan komuniti keselamatan MCP dan kumpulan kerja  
- **Penilaian Berkala**: Jalankan penilaian postur keselamatan suku tahunan dan kemas kini amalan mengikut keperluan

### Menyumbang kepada Keselamatan MCP
- **Penyelidikan Keselamatan**: Sumbang kepada penyelidikan keselamatan MCP dan program pendedahan kerentanan  
- **Perkongsian Amalan Terbaik**: Kongsi pelaksanaan keselamatan dan pengajaran yang diperoleh dengan komuniti
- **Pembangunan Standard**: Menyertai pembangunan spesifikasi MCP dan penciptaan standard keselamatan  
- **Pembangunan Alat**: Membangun dan berkongsi alat keselamatan serta perpustakaan untuk ekosistem MCP  

---

*Dokumen ini mencerminkan amalan terbaik keselamatan MCP setakat 18 Disember 2025, berdasarkan Spesifikasi MCP 2025-11-25. Amalan keselamatan harus dikaji semula dan dikemas kini secara berkala selaras dengan evolusi protokol dan landskap ancaman.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->