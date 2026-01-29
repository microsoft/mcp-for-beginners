# Amalan Terbaik Keselamatan MCP - Kemas Kini Disember 2025

> **Penting**: Dokumen ini mencerminkan keperluan keselamatan terkini [Spesifikasi MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) dan [Amalan Terbaik Keselamatan MCP rasmi](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Sentiasa rujuk spesifikasi semasa untuk panduan yang paling terkini.

## Amalan Keselamatan Penting untuk Pelaksanaan MCP

Model Context Protocol memperkenalkan cabaran keselamatan unik yang melangkaui keselamatan perisian tradisional. Amalan ini menangani keperluan keselamatan asas dan ancaman khusus MCP termasuk suntikan arahan, pencemaran alat, pembajakan sesi, masalah wakil keliru, dan kelemahan laluan token.

### **Keperluan Keselamatan WAJIB**

**Keperluan Kritikal dari Spesifikasi MCP:**

### **Keperluan Keselamatan WAJIB**

**Keperluan Kritikal dari Spesifikasi MCP:**

> **TIDAK BOLEH**: Pelayan MCP **TIDAK BOLEH** menerima sebarang token yang tidak dikeluarkan secara eksplisit untuk pelayan MCP
> 
> **MESTI**: Pelayan MCP yang melaksanakan kebenaran **MESTI** mengesahkan SEMUA permintaan masuk
>  
> **TIDAK BOLEH**: Pelayan MCP **TIDAK BOLEH** menggunakan sesi untuk pengesahan
>
> **MESTI**: Pelayan proksi MCP yang menggunakan ID klien statik **MESTI** mendapatkan persetujuan pengguna untuk setiap klien yang didaftarkan secara dinamik

---

## 1. **Keselamatan Token & Pengesahan**

**Kawalan Pengesahan & Kebenaran:**
   - **Semakan Kebenaran Teliti**: Lakukan audit menyeluruh terhadap logik kebenaran pelayan MCP untuk memastikan hanya pengguna dan klien yang dimaksudkan boleh mengakses sumber
   - **Integrasi Penyedia Identiti Luaran**: Gunakan penyedia identiti yang telah ditetapkan seperti Microsoft Entra ID dan bukannya melaksanakan pengesahan tersuai
   - **Pengesahan Audiens Token**: Sentiasa sahkan bahawa token dikeluarkan secara eksplisit untuk pelayan MCP anda - jangan terima token dari hulu
   - **Kitaran Hayat Token yang Betul**: Laksanakan putaran token yang selamat, polisi tamat tempoh, dan cegah serangan ulang token

**Penyimpanan Token yang Dilindungi:**
   - Gunakan Azure Key Vault atau storan kelayakan selamat yang serupa untuk semua rahsia
   - Laksanakan penyulitan untuk token semasa disimpan dan dalam transit
   - Putaran kelayakan secara berkala dan pemantauan untuk akses tanpa kebenaran

## 2. **Pengurusan Sesi & Keselamatan Pengangkutan**

**Amalan Sesi Selamat:**
   - **ID Sesi Kriptografi Selamat**: Gunakan ID sesi yang selamat dan tidak deterministik yang dijana dengan penjana nombor rawak selamat
   - **Pengikatan Spesifik Pengguna**: Ikat ID sesi kepada identiti pengguna menggunakan format seperti `<user_id>:<session_id>` untuk mengelakkan penyalahgunaan sesi silang pengguna
   - **Pengurusan Kitaran Hayat Sesi**: Laksanakan tamat tempoh, putaran, dan pembatalan yang betul untuk mengehadkan tetingkap kelemahan
   - **Penguatkuasaan HTTPS/TLS**: HTTPS wajib untuk semua komunikasi bagi mengelakkan penyadapan ID sesi

**Keselamatan Lapisan Pengangkutan:**
   - Konfigurasikan TLS 1.3 jika boleh dengan pengurusan sijil yang betul
   - Laksanakan pin sijil untuk sambungan kritikal
   - Putaran sijil secara berkala dan pengesahan kesahihan

## 3. **Perlindungan Ancaman Khusus AI** 🤖

**Pertahanan Suntikan Arahan:**
   - **Perisai Arahan Microsoft**: Gunakan AI Prompt Shields untuk pengesanan dan penapisan arahan berniat jahat yang maju
   - **Penapisan Input**: Sahkan dan tapis semua input untuk mengelakkan serangan suntikan dan masalah wakil keliru
   - **Sempadan Kandungan**: Gunakan sistem pemisah dan penandaan data untuk membezakan antara arahan dipercayai dan kandungan luaran

**Pencegahan Pencemaran Alat:**
   - **Pengesahan Metadata Alat**: Laksanakan pemeriksaan integriti untuk definisi alat dan pantau perubahan yang tidak dijangka
   - **Pemantauan Alat Dinamik**: Pantau tingkah laku masa nyata dan sediakan amaran untuk corak pelaksanaan yang tidak dijangka
   - **Aliran Kerja Kelulusan**: Memerlukan kelulusan pengguna secara eksplisit untuk pengubahsuaian alat dan perubahan keupayaan

## 4. **Kawalan Akses & Kebenaran**

**Prinsip Hak Istimewa Minimum:**
   - Berikan pelayan MCP hanya kebenaran minimum yang diperlukan untuk fungsi yang dimaksudkan
   - Laksanakan kawalan akses berasaskan peranan (RBAC) dengan kebenaran terperinci
   - Semakan kebenaran berkala dan pemantauan berterusan untuk peningkatan hak istimewa

**Kawalan Kebenaran Masa Jalan:**
   - Gunakan had sumber untuk mengelakkan serangan kehabisan sumber
   - Gunakan pengasingan kontena untuk persekitaran pelaksanaan alat  
   - Laksanakan akses tepat pada masa untuk fungsi pentadbiran

## 5. **Keselamatan Kandungan & Pemantauan**

**Pelaksanaan Keselamatan Kandungan:**
   - **Integrasi Azure Content Safety**: Gunakan Azure Content Safety untuk mengesan kandungan berbahaya, cubaan jailbreak, dan pelanggaran polisi
   - **Analisis Tingkah Laku**: Laksanakan pemantauan tingkah laku masa nyata untuk mengesan anomali dalam pelayan MCP dan pelaksanaan alat
   - **Pencatatan Menyeluruh**: Catat semua percubaan pengesahan, panggilan alat, dan acara keselamatan dengan storan selamat dan tahan gangguan

**Pemantauan Berterusan:**
   - Amaran masa nyata untuk corak mencurigakan dan percubaan akses tanpa kebenaran  
   - Integrasi dengan sistem SIEM untuk pengurusan acara keselamatan berpusat
   - Audit keselamatan berkala dan ujian penembusan pelaksanaan MCP

## 6. **Keselamatan Rantaian Bekalan**

**Pengesahan Komponen:**
   - **Imbasan Kebergantungan**: Gunakan imbasan kerentanan automatik untuk semua kebergantungan perisian dan komponen AI
   - **Pengesahan Asal Usul**: Sahkan asal, pelesenan, dan integriti model, sumber data, dan perkhidmatan luaran
   - **Pakej Bertandatangan**: Gunakan pakej bertandatangan kriptografi dan sahkan tandatangan sebelum penyebaran

**Saluran Pembangunan Selamat:**
   - **Keselamatan Lanjutan GitHub**: Laksanakan imbasan rahsia, analisis kebergantungan, dan analisis statik CodeQL
   - **Keselamatan CI/CD**: Integrasi pengesahan keselamatan sepanjang saluran penyebaran automatik
   - **Integriti Artifak**: Laksanakan pengesahan kriptografi untuk artifak dan konfigurasi yang disebarkan

## 7. **Keselamatan OAuth & Pencegahan Wakil Keliru**

**Pelaksanaan OAuth 2.1:**
   - **Pelaksanaan PKCE**: Gunakan Proof Key for Code Exchange (PKCE) untuk semua permintaan kebenaran
   - **Persetujuan Eksplisit**: Dapatkan persetujuan pengguna untuk setiap klien yang didaftarkan secara dinamik bagi mengelakkan serangan wakil keliru
   - **Pengesahan URI Redirect**: Laksanakan pengesahan ketat terhadap URI redirect dan pengecam klien

**Keselamatan Proksi:**
   - Elakkan pengelakan kebenaran melalui eksploitasi ID klien statik
   - Laksanakan aliran kerja persetujuan yang betul untuk akses API pihak ketiga
   - Pantau kecurian kod kebenaran dan akses API tanpa kebenaran

## 8. **Tindak Balas Insiden & Pemulihan**

**Keupayaan Tindak Balas Pantas:**
   - **Tindak Balas Automatik**: Laksanakan sistem automatik untuk putaran kelayakan dan pengawalan ancaman
   - **Prosedur Rollback**: Keupayaan untuk segera kembali ke konfigurasi dan komponen yang diketahui baik
   - **Keupayaan Forensik**: Jejak audit terperinci dan pencatatan untuk penyiasatan insiden

**Komunikasi & Penyelarasan:**
   - Prosedur eskalasi jelas untuk insiden keselamatan
   - Integrasi dengan pasukan tindak balas insiden organisasi
   - Simulasi insiden keselamatan dan latihan meja berkala

## 9. **Pematuhan & Tadbir Urus**

**Pematuhan Peraturan:**
   - Pastikan pelaksanaan MCP memenuhi keperluan khusus industri (GDPR, HIPAA, SOC 2)
   - Laksanakan pengelasan data dan kawalan privasi untuk pemprosesan data AI
   - Kekalkan dokumentasi menyeluruh untuk audit pematuhan

**Pengurusan Perubahan:**
   - Proses semakan keselamatan formal untuk semua pengubahsuaian sistem MCP
   - Kawalan versi dan aliran kerja kelulusan untuk perubahan konfigurasi
   - Penilaian pematuhan berkala dan analisis jurang

## 10. **Kawalan Keselamatan Lanjutan**

**Seni Bina Zero Trust:**
   - **Jangan Percaya, Sentiasa Sahkan**: Pengesahan berterusan pengguna, peranti, dan sambungan
   - **Mikro-segmentasi**: Kawalan rangkaian terperinci yang mengasingkan komponen MCP individu
   - **Akses Bersyarat**: Kawalan akses berasaskan risiko yang menyesuaikan dengan konteks dan tingkah laku semasa

**Perlindungan Aplikasi Masa Jalan:**
   - **Perlindungan Kendiri Aplikasi Masa Jalan (RASP)**: Gunakan teknik RASP untuk pengesanan ancaman masa nyata
   - **Pemantauan Prestasi Aplikasi**: Pantau anomali prestasi yang mungkin menunjukkan serangan
   - **Polisi Keselamatan Dinamik**: Laksanakan polisi keselamatan yang menyesuaikan berdasarkan landskap ancaman semasa

## 11. **Integrasi Ekosistem Keselamatan Microsoft**

**Keselamatan Microsoft Menyeluruh:**
   - **Microsoft Defender for Cloud**: Pengurusan postur keselamatan awan untuk beban kerja MCP
   - **Azure Sentinel**: SIEM dan SOAR asli awan untuk pengesanan ancaman lanjutan
   - **Microsoft Purview**: Tadbir urus data dan pematuhan untuk aliran kerja AI dan sumber data

**Pengurusan Identiti & Akses:**
   - **Microsoft Entra ID**: Pengurusan identiti perusahaan dengan polisi akses bersyarat
   - **Pengurusan Identiti Beristimewa (PIM)**: Akses tepat pada masa dan aliran kerja kelulusan untuk fungsi pentadbiran
   - **Perlindungan Identiti**: Akses bersyarat berasaskan risiko dan tindak balas ancaman automatik

## 12. **Evolusi Keselamatan Berterusan**

**Sentiasa Terkini:**
   - **Pemantauan Spesifikasi**: Semakan berkala kemas kini spesifikasi MCP dan perubahan panduan keselamatan
   - **Perisikan Ancaman**: Integrasi suapan ancaman khusus AI dan penunjuk kompromi
   - **Penglibatan Komuniti Keselamatan**: Penyertaan aktif dalam komuniti keselamatan MCP dan program pendedahan kerentanan

**Keselamatan Adaptif:**
   - **Keselamatan Pembelajaran Mesin**: Gunakan pengesanan anomali berasaskan ML untuk mengenal pasti corak serangan baru
   - **Analitik Keselamatan Ramalan**: Laksanakan model ramalan untuk pengenalpastian ancaman proaktif
   - **Automasi Keselamatan**: Kemas kini polisi keselamatan automatik berdasarkan perisikan ancaman dan perubahan spesifikasi

---

## **Sumber Keselamatan Kritikal**

### **Dokumentasi Rasmi MCP**
- [Spesifikasi MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Amalan Terbaik Keselamatan MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Spesifikasi Kebenaran MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Penyelesaian Keselamatan Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
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

> **Notis Keselamatan**: Amalan keselamatan MCP berkembang dengan pantas. Sentiasa sahkan dengan [spesifikasi MCP semasa](https://spec.modelcontextprotocol.io/) dan [dokumentasi keselamatan rasmi](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) sebelum pelaksanaan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->