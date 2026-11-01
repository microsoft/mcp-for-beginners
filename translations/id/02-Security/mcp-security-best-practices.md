# Praktik Terbaik Keamanan MCP - Pembaruan September 2026

> **Penting:** Dokumen ini mencerminkan
> [Spesifikasi MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> dan resmi
> [Praktik Terbaik Keamanan MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

## 🏔️ Pelatihan Keamanan Praktis

Untuk pengalaman implementasi praktis, kami merekomendasikan **[Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - ekspedisi terpandu komprehensif untuk mengamankan server MCP di Azure. Workshop ini mencakup semua risiko OWASP MCP Top 10 melalui metodologi "rentan → eksploitasi → perbaikan → validasi".

Semua praktik dalam dokumen ini selaras dengan **[Panduan Keamanan MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/)** untuk panduan implementasi spesifik Azure.

## Praktik Keamanan Esensial untuk Implementasi MCP

Model Context Protocol memperkenalkan tantangan keamanan unik yang melampaui
keamanan perangkat lunak tradisional. Praktik ini menangani kebutuhan dasar
dan ancaman khusus MCP termasuk injeksi prompt, keracunan alat,
pembajakan state-handle, masalah deputy bingung, dan kerentanan penerusan token.


### **Persyaratan Keamanan WAJIB** 

**Persyaratan Kritis dari Spesifikasi MCP:**

> **TIDAK BOLEH**: Server MCP **TIDAK BOLEH** menerima token apapun yang tidak secara eksplisit diterbitkan untuk server MCP tersebut
> 
> **HARUS**: Server MCP yang mengimplementasikan otorisasi **HARUS** memverifikasi SEMUA permintaan masuk
>  
> **TIDAK BOLEH**: Server MCP **TIDAK BOLEH** menggunakan sesi untuk autentikasi
>
> **HARUS**: Proxy server MCP yang menggunakan ID klien pihak ketiga statis **HARUS**
> memperoleh persetujuan untuk setiap klien MCP sebelum meneruskan otorisasi

---

## 1. **Keamanan Token & Autentikasi**

**Kontrol Autentikasi & Otorisasi:**
   - **Review Otorisasi yang Ketat**: Lakukan audit menyeluruh pada logika otorisasi server MCP untuk memastikan hanya pengguna dan klien yang dimaksud yang dapat mengakses sumber daya
   - **Integrasi Penyedia Identitas Eksternal**: Gunakan penyedia identitas yang sudah mapan seperti Microsoft Entra ID daripada mengimplementasikan autentikasi kustom
   - **Validasi Audiens Token**: Selalu validasi bahwa token secara eksplisit diterbitkan untuk server MCP Anda - jangan pernah menerima token upstream
   - **Siklus Hidup Token yang Tepat**: Implementasikan rotasi token yang aman, kebijakan kadaluwarsa, dan cegah serangan pemutaran token

**Penyimpanan Token yang Dilindungi:**
   - Gunakan Azure Key Vault atau penyimpanan kredensial aman serupa untuk semua rahasia
   - Implementasikan enkripsi untuk token baik saat diam maupun saat transit
   - Rotasi kredensial secara rutin dan pemantauan untuk akses tidak sah

## 2. **Keamanan State Handle & Transportasi**

**Praktik State Aplikasi yang Aman:**

- **Opaque State Handles**: Gunakan handles yang aman dan nondeterministik untuk
   state aplikasi yang melintasi permintaan
- **Bindings Khusus Pengguna**: Kaitkan handles di sisi server dengan prinsip yang terautentikasi dan tolak penggunaan silang pengguna
- **Manajemen Siklus Hidup**: Kedaluwarsa dan cabut handles untuk membatasi jendela kerentanan
- **Otorisasi per Permintaan**: Jangan pernah memperlakukan state handle sebagai autentikasi;
   otorisasi setiap permintaan yang menyajikannya

**Keamanan Lapisan Transportasi:**

- Wajibkan HTTPS untuk transportasi HTTP jarak jauh di produksi

- Konfigurasikan TLS modern dengan rotasi sertifikat dan validasi yang tepat

## 3. **Perlindungan Ancaman Khusus AI** 🤖

**Pertahanan Injeksi Prompt:**

   - **Sanitasi Input**: Validasi dan sanitasi semua input untuk mencegah serangan injeksi dan masalah deputy bingung
   - **Batas Konten**: Gunakan sistem delimiter dan penandaan data untuk membedakan antara instruksi terpercaya dan konten eksternal

**Pencegahan Keracunan Alat:**

   - **Pemantauan Dinamis Alat**: Pantau perilaku runtime dan siapkan peringatan untuk pola eksekusi yang tak terduga
   - **Workflow Persetujuan**: Memerlukan persetujuan eksplisit pengguna untuk modifikasi dan perubahan kapabilitas alat

## 4. **Kontrol Akses & Izin**

**Prinsip Hak Istimewa Minimum:**

   - Terapkan kontrol akses berbasis peran (RBAC) dengan izin terperinci
   - Tinjauan izin secara reguler dan pemantauan terus-menerus untuk eskalasi hak istimewa

**Kontrol Izin Saat Runtime:**

   - Gunakan isolasi kontainer untuk lingkungan eksekusi alat  
   - Terapkan akses tepat waktu (just-in-time) untuk fungsi administratif

## 5. **Keamanan Konten & Pemantauan**

**Implementasi Keamanan Konten:**

   - **Analisis Perilaku**: Terapkan pemantauan perilaku runtime untuk mendeteksi anomali dalam eksekusi server MCP dan alat
   - **Logging Komprehensif**: Catat semua upaya autentikasi, pemanggilan alat, dan peristiwa keamanan dengan penyimpanan yang aman dan tahan-tamper

**Pemantauan Berkelanjutan:**

   - Integrasi dengan sistem SIEM untuk manajemen peristiwa keamanan terpusat
   - Audit keamanan reguler dan pengujian penetrasi implementasi MCP

## 6. **Keamanan Rantai Pasokan**

**Verifikasi Komponen:**

   - **Validasi Asal Usul**: Verifikasi asal, lisensi, dan integritas model, sumber data, dan layanan eksternal
   - **Paket Tertanda**: Gunakan paket yang ditandatangani secara kriptografi dan verifikasi tanda tangan sebelum penerapan

**Pipeline Pengembangan yang Aman:**

   - **Keamanan CI/CD**: Integrasikan validasi keamanan di seluruh pipeline deployment otomatis
   - **Integritas Artifak**: Terapkan verifikasi kriptografi untuk artifak dan konfigurasi yang diterapkan

## 7. **Keamanan OAuth & Pencegahan Deputy Bingung**

**Implementasi OAuth 2.1:**

   - **Registrasi Klien**: Utamakan Dokumen Metadata Client ID atau
      pra-registrasi; gunakan registrasi dinamis klien yang usang hanya sebagai
      fallback kompatibilitas
   - **Persetujuan Eksplisit**: Proxy MCP yang menggunakan Client ID pihak ketiga statis harus
      memperoleh persetujuan untuk setiap klien MCP sebelum meneruskan otorisasi
   - **Validasi URI Redirect**: Terapkan validasi ketat pada URI redirect dan identifikasi klien

**Keamanan Proxy:**

   - Terapkan workflow persetujuan yang tepat untuk akses API pihak ketiga
   - Pantau pencurian kode otorisasi dan akses API tidak sah

## 8. **Respon Insiden & Pemulihan**

**Kemampuan Respon Cepat:**

   - **Prosedur Rollback**: Kemampuan cepat mengembalikan konfigurasi dan komponen ke kondisi baik yang diketahui
   - **Kemampuan Forensik**: Jejak audit rinci dan pencatatan untuk investigasi insiden

**Komunikasi & Koordinasi:**

   - Integrasi dengan tim respons insiden organisasi
   - Simulasi insiden keamanan dan latihan tabletop secara reguler

## 9. **Kepatuhan & Tata Kelola**

**Kepatuhan Regulasi:**

   - Implementasikan klasifikasi data dan kontrol privasi untuk pemrosesan data AI
   - Pertahankan dokumentasi komprehensif untuk audit kepatuhan

**Manajemen Perubahan:**

   - Kontrol versi dan workflow persetujuan untuk perubahan konfigurasi
   - Penilaian kepatuhan reguler dan analisis kesenjangan

## 10. **Kontrol Keamanan Lanjutan**

**Arsitektur Zero Trust:**

   - **Mikro-segmentasi**: Kontrol jaringan granular yang mengisolasi komponen MCP individual
   - **Akses Kondisional**: Kontrol akses berbasis risiko yang menyesuaikan dengan konteks dan perilaku saat ini

**Perlindungan Aplikasi Saat Runtime:**

   - **Pemantauan Kinerja Aplikasi**: Pantau anomali kinerja yang dapat menunjukkan serangan
   - **Kebijakan Keamanan Dinamis**: Terapkan kebijakan keamanan yang beradaptasi berdasarkan lanskap ancaman saat ini

## 11. **Integrasi Ekosistem Keamanan Microsoft**

**Keamanan Microsoft Komprehensif:**

   - **Azure Sentinel**: SIEM dan SOAR cloud-native untuk deteksi ancaman lanjutan
   - **Microsoft Purview**: Tata kelola data dan kepatuhan untuk alur kerja dan sumber data AI

**Manajemen Identitas & Akses:**

   - **Privileged Identity Management (PIM)**: Akses tepat waktu dan workflow persetujuan untuk fungsi administrasi
   - **Perlindungan Identitas**: Akses kondisional berbasis risiko dan respon ancaman otomatis

## 12. **Evolusi Keamanan Berkelanjutan**

**Tetap Terupdate:**

   - **Intelijen Ancaman**: Integrasi umpan ancaman khusus AI dan indikator kompromi
   - **Keterlibatan Komunitas Keamanan**: Partisipasi aktif dalam komunitas keamanan MCP dan program pengungkapan kerentanan

**Keamanan Adaptif:**

   - **Analitik Keamanan Prediktif**: Terapkan model prediktif untuk identifikasi ancaman proaktif
   - **Otomasi Keamanan**: Pembaruan kebijakan keamanan otomatis berdasarkan intelijen ancaman dan perubahan spesifikasi

---

## **Sumber Daya Keamanan Kritis**

### **Dokumentasi Resmi MCP**

### **Dokumentasi Resmi MCP**
- [Spesifikasi MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Praktik Terbaik Keamanan MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Spesifikasi Otorisasi MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Sumber Daya Keamanan OWASP MCP**
- [Panduan Keamanan OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - OWASP MCP Top 10 yang komprehensif dengan implementasi Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Risiko keamanan resmi OWASP MCP
- [Workshop Summit Keamanan MCP (Sherpa)](https://azure-samples.github.io/sherpa/) - Pelatihan keamanan langsung untuk MCP di Azure

### **Solusi Keamanan Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Keamanan Konten Azure](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Keamanan Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Standar Keamanan**
- [Praktik Terbaik Keamanan OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 untuk Large Language Models](https://genai.owasp.org/)
- [Kerangka Manajemen Risiko AI NIST](https://www.nist.gov/itl/ai-risk-management-framework)

### **Panduan Implementasi**
- [Gerbang Autentikasi Azure API Management MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID dengan Server MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Pemberitahuan keamanan:** Praktik keamanan MCP berkembang dengan cepat. Selalu verifikasi
> terhadap [spesifikasi MCP](https://modelcontextprotocol.io/specification/2026-07-28/) yang berlaku saat ini
> dan [dokumentasi keamanan resmi](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> sebelum penerapan.

## Apa Selanjutnya

- Baca: [Kontrol Keamanan MCP](./mcp-security-controls.md)
- Kembali ke: [Ikhtisar Modul Keamanan](./README.md)
- Lanjut ke: [Modul 3: Memulai](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->