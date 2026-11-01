# Amalan Terbaik Keselamatan MCP - Kemas Kini September 2026

> **Penting:** Dokumen ini mencerminkan
> [Spesifikasi MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> dan rasmi
> [Amalan Terbaik Keselamatan MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

## 🏔️ Latihan Keselamatan Praktikal

Untuk pengalaman pelaksanaan praktikal, kami mengesyorkan **[Bengkel Sidang Kemuncak Keselamatan MCP (Sherpa)](https://azure-samples.github.io/sherpa/)** - ekspedisi terpandu menyeluruh untuk mengamankan pelayan MCP di Azure. Bengkel ini merangkumi semua risiko OWASP MCP Top 10 melalui metodologi "terdedah → eksploit → baiki → sahkan".

Semua amalan dalam dokumen ini selaras dengan **[Panduan Keselamatan OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)** untuk panduan pelaksanaan khusus Azure.

## Amalan Keselamatan Penting untuk Pelaksanaan MCP

Protokol Konteks Model memperkenalkan cabaran keselamatan unik yang melangkaui
keselamatan perisian tradisional. Amalan ini menangani keperluan asas
serta ancaman khusus MCP termasuk suntikan prompt, racun alat,
rampasan pemegang status, masalah ejen keliru, dan kelemahan penyaluran token.


### **Keperluan Keselamatan WAJIB** 

**Keperluan Kritikal dari Spesifikasi MCP:**

> **TIDAK BOLEH:** pelayan MCP **TIDAK BOLEH** menerima sebarang token yang tidak secara eksplisit dikeluarkan untuk pelayan MCP
> 
> **MESTI:** pelayan MCP yang melaksanakan kebenaran **MESTI** mengesahkan SEMUA permintaan masuk
>  
> **TIDAK BOLEH:** pelayan MCP **TIDAK BOLEH** menggunakan sesi untuk pengesahan
>
> **MESTI:** pelayan proksi MCP yang menggunakan ID klien pihak ketiga statik **MESTI**
> mendapatkan persetujuan untuk setiap klien MCP sebelum meneruskan kebenaran

---

## 1. **Keselamatan Token & Pengesahan**

**Kawalan Pengesahan & Kebenaran:**
   - **Semakan Kebenaran Teliti**: Lakukan audit menyeluruh ke atas logik kebenaran pelayan MCP untuk memastikan hanya pengguna dan klien yang dimaksudkan dapat mengakses sumber
   - **Integrasi Penyedia Identiti Luaran**: Gunakan penyedia identiti yang diterima seperti Microsoft Entra ID daripada melaksanakan pengesahan tersuai
   - **Pengesahan Penonton Token**: Sentiasa sahkan token yang dikeluarkan secara eksplisit untuk pelayan MCP anda - jangan terima token huluan
   - **Kitaran Hayat Token Yang Betul**: Laksanakan putaran token selamat, polisi luput, dan cegah serangan ulang token

**Penyimpanan Token Dilindungi:**
   - Gunakan Azure Key Vault atau storan kelayakan selamat yang serupa untuk semua rahsia
   - Laksanakan penyulitan untuk token sama ada dalam keadaan rehat atau transit
   - Putaran kelayakan berkala dan pemantauan untuk akses tanpa kebenaran

## 2. **Pemegang Status & Keselamatan Pengangkutan**

**Amalan Status Aplikasi Selamat:**

- **Pemegang Status Tidak Telus**: Gunakan pemegang yang selamat dan tidak deterministik untuk
   status aplikasi yang merentas permintaan
- **Pengikatan Spesifik Pengguna**: Ikat pemegang di pelayan kepada prinsipal yang sah
   dan tolak penggunaan semula silang pengguna
- **Pengurusan Kitaran Hayat**: Luput dan batalkan pemegang untuk mengehadkan
   tempoh kelemahan
- **Kebenaran Setiap Permintaan**: Jangan sekali-kali menganggap pemegang status sebagai pengesahan;
   benarkan setiap permintaan yang mengemukakannya

**Keselamatan Lapisan Pengangkutan:**

- Perlukan HTTPS untuk pengangkutan HTTP jauh dalam pengeluaran
- Gunakan pengasingan proses dan kelayakan persekitaran untuk pelayan stdio tempatan
- Konfigurasikan TLS moden dengan putaran sijil yang betul dan pengesahan yang sah

## 3. **Perlindungan Ancaman AI Spesifik** 🤖

**Pertahanan Suntikan Prompt:**
   - **Perisai Prompt Microsoft**: Gunakan AI Prompt Shields untuk pengesanan lanjutan dan penapisan arahan berniat jahat
   - **Sanitasi Input**: Sah dan sanitasi semua input untuk mencegah serangan suntikan dan masalah ejen keliru
   - **Sempadan Kandungan**: Gunakan sistem pemisah dan penandaan data untuk membezakan antara arahan yang dipercayai dan kandungan luar

**Pencegahan Racun Alat:**
   - **Pengesahan Metadata Alat**: Laksanakan pemeriksaan integriti untuk definisi alat dan pantau perubahan tidak dijangka
   - **Pemantauan Alat Dinamik**: Pantau tingkah laku masa nyata dan sediakan amaran untuk corak pelaksanaan tidak dijangka
   - **Alur Kelulusan**: Memerlukan kelulusan jelas pengguna untuk pengubahsuaian alat dan perubahan kebolehan

## 4. **Kawalan Akses & Kebenaran**

**Prinsip Keistimewaan Paling Rendah:**
   - Berikan pelayan MCP hanya kebenaran minimum yang diperlukan untuk fungsi yang dimaksudkan
   - Laksanakan kawalan akses berasaskan peranan (RBAC) dengan kebenaran terperinci
   - Kajian kebenaran berkala dan pemantauan berterusan untuk peningkatan keistimewaan

**Kawalan Kebenaran Semasa Berlaku:**
   - Terapkan had sumber untuk mengelak serangan kehabisan sumber
   - Gunakan pengasingan bekas untuk persekitaran pelaksanaan alat  
   - Laksanakan akses tepat pada masa untuk fungsi pentadbiran

## 5. **Keselamatan Kandungan & Pemantauan**

**Pelaksanaan Keselamatan Kandungan:**
   - **Integrasi Azure Content Safety**: Gunakan Azure Content Safety untuk mengesan kandungan berbahaya, cubaan jailbreak, dan pelanggaran polisi
   - **Analisis Tingkah Laku**: Laksanakan pemantauan tingkah laku masa nyata untuk mengesan anomali dalam pelayan MCP dan pelaksanaan alat
   - **Pencatatan Menyeluruh**: Catat semua percubaan pengesahan, panggilan alat, dan acara keselamatan dengan storan selamat dan tahan gangguan

**Pemantauan Berterusan:**
   - Pemberitahuan masa nyata untuk corak mencurigakan dan cubaan akses tanpa kebenaran  
   - Integrasi dengan sistem SIEM untuk pengurusan acara keselamatan berpusat
   - Audit keselamatan dan ujian penembusan berkala untuk pelaksanaan MCP

## 6. **Keselamatan Rantaian Bekalan**

**Pengesahan Komponen:**
   - **Imbasan Kebergantungan**: Gunakan pengimbasan kerentanan automatik untuk semua kebergantungan perisian dan komponen AI
   - **Pengesahan Sumber**: Sahkan asal, pelesenan, dan integriti model, sumber data, dan perkhidmatan luaran
   - **Pakej Bertandatangan**: Gunakan pakej bertandatangan kriptografi dan sahkan tandatangan sebelum pelaksanaan

**Saluran Pembangunan Selamat:**
   - **Keselamatan Lanjutan GitHub**: Laksanakan imbasan rahsia, analisis kebergantungan, dan analisis statik CodeQL
   - **Keselamatan CI/CD**: Integrasi pengesahan keselamatan sepanjang saluran pelaksanaan automatik
   - **Integriti Artifak**: Laksanakan pengesahan kriptografi untuk artifak dan konfigurasi yang dilaksanakan

## 7. **Keselamatan OAuth & Pencegahan Ejen Keliru**

**Pelaksanaan OAuth 2.1:**
   - **Pelaksanaan PKCE**: Gunakan Proof Key for Code Exchange (PKCE) untuk semua permintaan kebenaran
    - **Pendaftaran Klien**: Utamakan Dokumen Metadata ID Klien atau
       pra-pendaftaran; gunakan Pendaftaran Klien Dinamik yang usang hanya sebagai
       pilihan keserasian
    - **Persetujuan Eksplisit**: Proksi MCP yang menggunakan ID klien pihak ketiga statik mesti
       mendapatkan persetujuan untuk setiap klien MCP sebelum meneruskan kebenaran
   - **Pengesahan URI Redirect**: Laksanakan pengesahan ketat terhadap URI redirect dan penentu klien

**Keselamatan Proksi:**
   - Cegah pengelakan kebenaran melalui eksploitasi ID klien statik
   - Laksanakan aliran kerja persetujuan yang betul untuk akses API pihak ketiga
   - Pantau kecurian kod kebenaran dan akses API tanpa kebenaran

## 8. **Respons Insiden & Pemulihan**

**Keupayaan Respons Pantas:**
   - **Respons Automatik**: Laksanakan sistem automatik untuk putaran kelayakan dan penahanan ancaman
   - **Prosedur Pemulihan**: Keupayaan untuk cepat kembali ke konfigurasi dan komponen yang diketahui selamat
   - **Keupayaan Forensik**: Jejak audit terperinci dan pencatatan untuk penyiasatan insiden

**Komunikasi & Penyelarasan:**
   - Prosedur eskalasi jelas untuk insiden keselamatan
   - Integrasi dengan pasukan respons insiden organisasi
   - Simulasi insiden keselamatan dan latihan meja berkala

## 9. **Pematuhan & Tadbir Urus**

**Pematuhan Peraturan:**
   - Pastikan pelaksanaan MCP memenuhi keperluan industri spesifik (GDPR, HIPAA, SOC 2)
   - Laksanakan pengelasan data dan kawalan privasi untuk pemprosesan data AI
   - Kekalkan dokumentasi menyeluruh untuk audit pematuhan

**Pengurusan Perubahan:**
   - Proses semakan keselamatan formal untuk semua perubahan sistem MCP
   - Kawalan versi dan alur kelulusan untuk perubahan konfigurasi
   - Penilaian pematuhan berkala dan analisis jurang

## 10. **Kawalan Keselamatan Lanjutan**

**Seni Bina Zero Trust:**
   - **Jangan Percaya, Sentiasa Sahkan**: Pengesahan berterusan pengguna, peranti, dan sambungan
   - **Mikropengasingan**: Kawalan rangkaian terperinci yang mengasingkan komponen MCP individu
   - **Akses Bersyarat**: Kawalan akses berasaskan risiko yang menyesuaikan mengikut konteks dan tingkah laku semasa

**Perlindungan Aplikasi Semasa Berjalan:**
   - **Perlindungan Kendiri Aplikasi Semasa Berjalan (RASP)**: Gunakan teknik RASP untuk pengesanan ancaman masa sebenar
   - **Pemantauan Prestasi Aplikasi**: Pantau anomali prestasi yang mungkin menunjukkan serangan
   - **Polisi Keselamatan Dinamik**: Laksanakan polisi keselamatan yang menyesuaikan berdasarkan landskap ancaman semasa

## 11. **Integrasi Ekosistem Keselamatan Microsoft**

**Keselamatan Microsoft Menyeluruh:**
   - **Microsoft Defender for Cloud**: Pengurusan posisi keselamatan awan untuk beban kerja MCP
   - **Azure Sentinel**: Keupayaan SIEM dan SOAR asli awan untuk pengesanan ancaman lanjutan
   - **Microsoft Purview**: Tadbir urus data dan pematuhan untuk aliran kerja AI dan sumber data

**Pengurusan Identiti & Akses:**
   - **Microsoft Entra ID**: Pengurusan identiti perusahaan dengan polisi akses bersyarat
   - **Pengurusan Identiti Istimewa (PIM)**: Akses tepat pada masa dan alur kelulusan untuk fungsi pentadbiran
   - **Perlindungan Identiti**: Akses bersyarat berasaskan risiko dan respons automatik terhadap ancaman

## 12. **Evolusi Keselamatan Berterusan**

**Mengikuti Perkembangan Terkini:**
   - **Pemantauan Spesifikasi**: Kajian berkala kemas kini spesifikasi MCP dan perubahan panduan keselamatan
   - **Intelijen Ancaman**: Integrasi suapan ancaman spesifik AI dan petunjuk kompromi
   - **Penglibatan Komuniti Keselamatan**: Penyertaan aktif dalam komuniti keselamatan MCP dan program pendedahan kerentanan

**Keselamatan Adaptif:**
   - **Keselamatan Pembelajaran Mesin**: Gunakan pengesanan anomali berasaskan ML untuk mengenal pasti corak serangan baru
   - **Analitik Keselamatan Ramalan**: Laksanakan model ramalan untuk pengecaman ancaman proaktif
   - **Automasi Keselamatan**: Kemas kini polisi keselamatan secara automatik berdasarkan intelijen ancaman dan perubahan spesifikasi

---

## **Sumber Keselamatan Kritikal**

### **Dokumentasi Rasmi MCP**
- [Spesifikasi MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Amalan Terbaik Keselamatan MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Spesifikasi Kebenaran MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Sumber Keselamatan OWASP MCP**
- [Panduan Keselamatan OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - Senarai 10 Teratas OWASP MCP yang komprehensif dengan pelaksanaan Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Risiko keselamatan MCP rasmi OWASP
- [Bengkel Sidang Kemuncak Keselamatan MCP (Sherpa)](https://azure-samples.github.io/sherpa/) - Latihan keselamatan secara praktikal untuk MCP pada Azure

### **Penyelesaian Keselamatan Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Keselamatan Kandungan Azure](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Keselamatan Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Keselamatan Lanjutan GitHub](https://github.com/security/advanced-security)

### **Standard Keselamatan**
- [Amalan Terbaik Keselamatan OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 untuk Model Bahasa Besar](https://genai.owasp.org/)
- [Rangka Kerja Pengurusan Risiko AI NIST](https://www.nist.gov/itl/ai-risk-management-framework)

### **Panduan Pelaksanaan**
- [Gerbang Pengesahan MCP Pengurusan API Azure](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID dengan Pelayan MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Notis keselamatan:** Amalan keselamatan MCP berkembang dengan pesat. Sentiasa sahkan
> dengan [spesifikasi MCP semasa](https://modelcontextprotocol.io/specification/2026-07-28/)
> dan [dokumentasi keselamatan rasmi](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> sebelum pelaksanaan.

## Apa Seterusnya

- Baca: [Kawalan Keselamatan MCP](./mcp-security-controls.md)
- Kembali ke: [Gambaran Keseluruhan Modul Keselamatan](./README.md)
- Teruskan ke: [Modul 3: Bermula](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->