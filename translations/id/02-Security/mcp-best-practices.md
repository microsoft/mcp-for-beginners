# Praktik Terbaik Keamanan MCP - Pembaruan September 2026

Panduan komprehensif ini menguraikan praktik terbaik keamanan penting untuk
mengimplementasikan sistem Model Context Protocol (MCP) berdasarkan
**Spesifikasi MCP 2026-07-28** dan standar industri saat ini. Praktik-praktik ini
mengatasi baik kekhawatiran keamanan tradisional maupun ancaman
khusus AI yang unik untuk implementasi MCP.

## Persyaratan Keamanan Kritis

### Kontrol Keamanan Wajib (Persyaratan HARUS)

1. **Validasi Token**: Server MCP **TIDAK BOLEH** menerima token apa pun yang tidak secara eksplisit diterbitkan untuk server MCP itu sendiri
2. **Verifikasi Otorisasi**: Server MCP yang mengimplementasikan otorisasi **HARUS** memverifikasi SEMUA permintaan masuk dan **TIDAK BOLEH** menggunakan sesi untuk autentikasi  
3. **Persetujuan Pengguna**: Server proxy MCP yang menggunakan ID klien pihak ketiga statis **HARUS** mendapatkan persetujuan eksplisit untuk setiap klien MCP sebelum meneruskan alur otorisasi
4. **Keamanan Handle Status**: Server MCP **TIDAK BOLEH** menganggap kepemilikan
	handle status aplikasi sebagai autentikasi dan **HARUS** mengotorisasi setiap
	permintaan yang menggunakan handle tersebut

## Praktik Keamanan Inti

### 1. Validasi & Sanitasi Masukan
- **Validasi Masukan Menyeluruh**: Validasi dan sanitasi semua masukan untuk mencegah serangan injeksi, masalah deputi bingung, dan kerentanan injeksi prompt
- **Penegakan Skema Parameter**: Terapkan validasi skema JSON yang ketat untuk semua parameter alat dan masukan API
- **Penyaringan Konten**: Gunakan Microsoft Prompt Shields dan Azure Content Safety untuk menyaring konten berbahaya dalam prompt dan respons
- **Sanitasi Keluaran**: Validasi dan sanitasi semua keluaran model sebelum disajikan ke pengguna atau sistem hilir

### 2. Keunggulan Autentikasi & Otorisasi  
- **Penyedia Identitas Eksternal**: Delegasikan autentikasi ke penyedia identitas yang sudah mapan (Microsoft Entra ID, penyedia OAuth 2.1) daripada mengimplementasikan autentikasi kustom
- **Registrasi Klien**: Utamakan Dokumen Metadata ID Klien atau pra-registrasi; gunakan Registrasi Klien Dinamis yang sudah usang hanya untuk kompatibilitas
- **Izin Terperinci**: Terapkan izin granular spesifik alat mengikuti prinsip hak istimewa paling sedikit
- **Manajemen Siklus Hidup Token**: Gunakan token akses berumur pendek dengan rotasi yang aman dan validasi audiens yang tepat
- **Autentikasi Multi-Faktor**: Wajibkan MFA untuk semua akses administratif dan operasi sensitif

### 3. Protokol Komunikasi Aman
- **Transport Layer Security**: Gunakan HTTPS dengan validasi sertifikat yang tepat
	untuk komunikasi HTTP MCP jarak jauh; gunakan isolasi proses dan kredensial lingkungan
	untuk server stdio lokal
- **Enkripsi End-to-End**: Terapkan lapisan enkripsi tambahan untuk data yang sangat sensitif dalam transit dan saat disimpan
- **Manajemen Sertifikat**: Pertahankan manajemen siklus hidup sertifikat yang tepat dengan proses perpanjangan otomatis
- **Penegakan Versi Protokol**: Gunakan MCP `2026-07-28`, sertakan metadata versi yang diperlukan
	pada setiap permintaan, dan tolak versi yang tidak didukung

### 4. Pembatasan Laju & Perlindungan Sumber Daya Lanjutan
- **Pembatasan Laju Multi-lapis**: Terapkan pembatasan laju berdasarkan pengguna, kredensial,
  operasi, alat, dan sumber daya untuk mencegah penyalahgunaan
- **Pembatasan Laju Adaptif**: Gunakan pembatasan laju berbasis pembelajaran mesin yang beradaptasi dengan pola penggunaan dan indikator ancaman
- **Manajemen Kuota Sumber Daya**: Tetapkan batas yang sesuai untuk sumber daya komputasi, penggunaan memori, dan waktu eksekusi
- **Perlindungan DDoS**: Terapkan sistem perlindungan DDoS dan analisis lalu lintas yang komprehensif

### 5. Logging & Pemantauan Komprehensif
- **Logging Audit Terstruktur**: Terapkan log terperinci yang dapat dicari untuk semua operasi MCP, eksekusi alat, dan kejadian keamanan
- **Pemantauan Keamanan Waktu Nyata**: Terapkan sistem SIEM dengan deteksi anomali bertenaga AI untuk beban kerja MCP
- **Logging Sesuai Privasi**: Catat kejadian keamanan sambil menghormati persyaratan dan regulasi privasi data
- **Integrasi Respons Insiden**: Hubungkan sistem logging ke alur kerja respons insiden otomatis

### 6. Praktik Penyimpanan Aman yang Ditingkatkan
- **Hardware Security Modules**: Gunakan penyimpanan kunci berbasis HSM (Azure Key Vault, AWS CloudHSM) untuk operasi kriptografi penting
- **Manajemen Kunci Enkripsi**: Terapkan rotasi kunci, segregasi, dan kontrol akses yang tepat untuk kunci enkripsi
- **Manajemen Rahasia**: Simpan semua API key, token, dan kredensial dalam sistem manajemen rahasia khusus
- **Klasifikasi Data**: Klasifikasikan data berdasarkan tingkat sensitivitas dan terapkan langkah perlindungan yang sesuai

### 7. Manajemen Token Lanjutan
- **Pencegahan Token Passthrough**: Larang secara tegas pola token passthrough yang melewati kontrol keamanan
- **Validasi Audiens**: Selalu verifikasi klaim audiens token cocok dengan identitas server MCP yang dituju
- **Otorisasi Berbasis Klaim**: Terapkan otorisasi terperinci berdasarkan klaim token dan atribut pengguna
- **Token Binding**: Validasi bahwa token menargetkan sumber daya MCP yang dimaksud dan
	ikat handle status aplikasi di sisi server ke prinsipal yang terautentikasi

### 8. Status Aplikasi yang Aman

- **Handle Status Kriptografi**: Hasilkan handle buram, non-deterministik
	untuk status yang melintasi permintaan
- **Binding Spesifik Pengguna**: Ikat setiap handle di sisi server ke
	prinsipal yang terautentikasi; jangan percaya ID pengguna yang diberikan oleh klien
- **Kontrol Siklus Hidup**: Kedaluwarsakan dan cabut handle, serta definisikan bagaimana pemanggil
	memulihkan dari status usang
- **Otorisasi Per Permintaan**: Periksa ulang otorisasi kapan pun sebuah handle
	disajikan; handle adalah nama, bukan kredensial

### 9. Kontrol Keamanan Khusus AI
- **Pertahanan Injeksi Prompt**: Terapkan Microsoft Prompt Shields dengan teknik sorotan, pembatas, dan datamarking
- **Pencegahan Keracunan Alat**: Validasi metadata alat, pantau perubahan dinamis, dan verifikasi integritas alat
- **Validasi Keluaran Model**: Pindai keluaran model untuk potensi kebocoran data, konten berbahaya, atau pelanggaran kebijakan keamanan
- **Perlindungan Jendela Konteks**: Terapkan kontrol untuk mencegah keracunan jendela konteks dan serangan manipulasi

### 10. Keamanan Eksekusi Alat
- **Sandboxing Eksekusi**: Jalankan eksekusi alat dalam lingkungan terisolasi berbasis kontainer dengan batas sumber daya
- **Pemecahan Hak Istimewa**: Eksekusi alat dengan hak istimewa minimum yang diperlukan dan pisahkan akun layanan
- **Isolasi Jaringan**: Terapkan segmentasi jaringan untuk lingkungan eksekusi alat
- **Pemantauan Eksekusi**: Pantau eksekusi alat untuk perilaku anomali, penggunaan sumber daya, dan pelanggaran keamanan

### 11. Validasi Keamanan Berkelanjutan
- **Pengujian Keamanan Otomatis**: Integrasikan pengujian keamanan ke dalam pipeline CI/CD dengan alat seperti GitHub Advanced Security
- **Manajemen Kerentanan**: Pindai secara rutin semua dependensi, termasuk model AI dan layanan eksternal
- **Pengujian Penetrasi**: Lakukan penilaian keamanan rutin yang secara khusus menargetkan implementasi MCP
- **Review Kode Keamanan**: Terapkan review keamanan wajib untuk semua perubahan kode terkait MCP

### 12. Keamanan Rantai Pasokan untuk AI
- **Verifikasi Komponen**: Verifikasi asal-usul, integritas, dan keamanan semua komponen AI (model, embedding, API)
- **Manajemen Dependensi**: Pertahankan inventaris terkini dari semua dependensi perangkat lunak dan AI dengan pelacakan kerentanan
- **Repositori Terpercaya**: Gunakan sumber yang terverifikasi dan terpercaya untuk semua model AI, pustaka, dan alat
- **Pemantauan Rantai Pasokan**: Pantau secara terus menerus kompromi pada penyedia layanan AI dan repositori model


## Pola Keamanan Lanjutan

### Arsitektur Zero Trust untuk MCP
- **Jangan Pernah Percaya, Selalu Verifikasi**: Terapkan verifikasi berkelanjutan untuk semua peserta MCP
- **Mikro-segmentasi**: Isolasi komponen MCP dengan kendali jaringan dan identitas yang terperinci
- **Akses Bersyarat**: Terapkan kontrol akses berbasis risiko yang beradaptasi dengan konteks dan perilaku
- **Penilaian Risiko Berkelanjutan**: Evaluasi secara dinamis postur keamanan berdasarkan indikator ancaman saat ini

### Implementasi AI yang Melindungi Privasi
- **Minimisasi Data**: Hanya paparkan data yang paling diperlukan untuk setiap operasi MCP
- **Privasi Diferensial**: Terapkan teknik pelestarian privasi untuk pemrosesan data sensitif
- **Enkripsi Homomorfik**: Gunakan teknik enkripsi canggih untuk perhitungan aman pada data terenkripsi
- **Pembelajaran Federasi**: Terapkan pendekatan pembelajaran terdistribusi yang menjaga lokasi data dan privasi

### Tanggapan Insiden untuk Sistem AI
- **Prosedur Insiden Khusus AI**: Kembangkan prosedur tanggapan insiden yang disesuaikan untuk ancaman spesifik AI dan MCP
- **Tanggapan Otomatis**: Terapkan penahanan dan perbaikan otomatis untuk insiden keamanan AI yang umum  
- **Kemampuan Forensik**: Pertahankan kesiapan forensik untuk kompromi sistem AI dan kebocoran data
- **Prosedur Pemulihan**: Tetapkan prosedur untuk pemulihan dari keracunan model AI, serangan injeksi prompt, dan kompromi layanan

## Sumber Daya & Standar Implementasi

### 🏔️ Pelatihan Keamanan Praktis
- **[Lokakarya MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - Lokakarya praktis komprehensif untuk mengamankan server MCP di Azure
- **[Panduan Keamanan OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)** - Arsitektur referensi dan panduan implementasi OWASP MCP Top 10

### Dokumentasi Resmi MCP
- [Spesifikasi MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Spesifikasi protokol MCP saat ini
- [Praktik Terbaik Keamanan MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Panduan keamanan resmi
- [Spesifikasi Otorisasi MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - Pola otorisasi HTTP
- [Transport MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Persyaratan transportasi

### Solusi Keamanan Microsoft
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Perlindungan injeksi prompt tingkat lanjut
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Penyaringan konten AI secara komprehensif
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Manajemen identitas dan akses perusahaan
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Manajemen rahasia dan kredensial yang aman
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Pemindaian keamanan rantai pasokan dan kode

### Standar & Kerangka Keamanan
- [Praktik Terbaik Keamanan OAuth 2.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Panduan keamanan OAuth saat ini
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Risiko keamanan aplikasi web
- [OWASP Top 10 untuk LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Risiko keamanan spesifik AI
- [Kerangka Manajemen Risiko AI NIST](https://www.nist.gov/itl/ai-risk-management-framework) - Manajemen risiko AI secara komprehensif
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Sistem manajemen keamanan informasi

### Panduan & Tutorial Implementasi
- [Manajemen API Azure sebagai Gerbang Otorisasi MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Pola otentikasi perusahaan
- [Microsoft Entra ID dengan Server MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integrasi penyedia identitas
- [Implementasi Penyimpanan Token yang Aman](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Praktik terbaik manajemen token
- [Enkripsi End-to-End untuk AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Pola enkripsi lanjutan

### Sumber Daya Keamanan Lanjutan
- [Siklus Hidup Pengembangan Keamanan Microsoft](https://www.microsoft.com/sdl) - Praktik pengembangan yang aman
- [Panduan Tim Merah AI](https://learn.microsoft.com/security/ai-red-team/) - Pengujian keamanan spesifik AI
- [Pemodelan Ancaman untuk Sistem AI](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodologi pemodelan ancaman AI
- [Rekayasa Privasi untuk AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Teknik AI yang melindungi privasi

### Kepatuhan & Tata Kelola
- [Kepatuhan GDPR untuk AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Kepatuhan privasi dalam sistem AI
- [Kerangka Tata Kelola AI](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Implementasi AI yang bertanggung jawab
- [SOC 2 untuk Layanan AI](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Kontrol keamanan untuk penyedia layanan AI
- [Kepatuhan HIPAA untuk AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Persyaratan kepatuhan AI di layanan kesehatan

### DevSecOps & Otomatisasi
- [Pipeline DevSecOps untuk AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Pipeline pengembangan AI yang aman
- [Pengujian Keamanan Otomatis](https://learn.microsoft.com/security/engineering/devsecops) - Validasi keamanan berkelanjutan
- [Keamanan Infrastruktur sebagai Kode](https://learn.microsoft.com/security/engineering/infrastructure-security) - Penyebaran infrastruktur yang aman
- [Keamanan Kontainer untuk AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Keamanan kontainer beban kerja AI

### Pemantauan & Tanggapan Insiden  
- [Azure Monitor untuk Beban Kerja AI](https://learn.microsoft.com/azure/azure-monitor/overview) - Solusi pemantauan komprehensif
- [Tanggapan Insiden Keamanan AI](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Prosedur insiden spesifik AI
- [SIEM untuk Sistem AI](https://learn.microsoft.com/azure/sentinel/overview) - Manajemen informasi dan peristiwa keamanan

- [Intelijen Ancaman untuk AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Sumber intelijen ancaman AI

## 🔄 Peningkatan Berkelanjutan

### Tetap Terkini dengan Standar yang Berkembang
- **Pembaruan Spesifikasi MCP**: Pantau perubahan spesifikasi MCP resmi dan advis keamanan
- **Intelijen Ancaman**: Berlangganan feed ancaman keamanan AI dan basis data kerentanan  
- **Keterlibatan Komunitas**: Ikut serta dalam diskusi komunitas keamanan MCP dan kelompok kerja
- **Penilaian Rutin**: Lakukan penilaian postur keamanan triwulanan dan perbarui praktik sesuai kebutuhan

### Berkontribusi pada Keamanan MCP
- **Riset Keamanan**: Berkontribusi pada riset keamanan MCP dan program pengungkapan kerentanan
- **Berbagi Praktik Terbaik**: Bagikan penerapan keamanan dan pelajaran yang didapat dengan komunitas
- **Pengembangan Standar**: Ikut serta dalam pengembangan spesifikasi MCP dan pembuatan standar keamanan
- **Pengembangan Alat**: Kembangkan dan bagikan alat serta pustaka keamanan untuk ekosistem MCP

---

*Dokumen ini mencerminkan praktik terbaik keamanan MCP per 9 September 2026,
berdasarkan Spesifikasi MCP `2026-07-28`. Praktik keamanan harus secara rutin
ditinjau seiring evolusi protokol dan lanskap ancaman.*

## Selanjutnya

- Baca: [Praktik Terbaik Keamanan MCP](./mcp-security-best-practices.md)
- Kembali ke: [Ikhtisar Modul Keamanan](./README.md)
- Lanjut ke: [Modul 3: Memulai](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->