# Kontrol Keamanan MCP - Pembaruan Desember 2025

> **Standar Saat Ini**: Dokumen ini mencerminkan [Spesifikasi MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) persyaratan keamanan dan [Praktik Terbaik Keamanan MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) resmi.

Model Context Protocol (MCP) telah berkembang pesat dengan kontrol keamanan yang ditingkatkan yang menangani baik keamanan perangkat lunak tradisional maupun ancaman khusus AI. Dokumen ini menyediakan kontrol keamanan komprehensif untuk implementasi MCP yang aman per Desember 2025.

## **Persyaratan Keamanan MANDATORI**

### **Larangan Kritis dari Spesifikasi MCP:**

> **TERLARANG**: Server MCP **TIDAK BOLEH** menerima token apa pun yang tidak secara eksplisit diterbitkan untuk server MCP  
>
> **DILARANG**: Server MCP **TIDAK BOLEH** menggunakan sesi untuk otentikasi  
>
> **DIBUTUHKAN**: Server MCP yang mengimplementasikan otorisasi **HARUS** memverifikasi SEMUA permintaan masuk  
>
> **MANDATORI**: Server proxy MCP yang menggunakan ID klien statis **HARUS** memperoleh persetujuan pengguna untuk setiap klien yang terdaftar secara dinamis

---

## 1. **Kontrol Otentikasi & Otorisasi**

### **Integrasi Penyedia Identitas Eksternal**

**Standar MCP Saat Ini (2025-06-18)** memungkinkan server MCP mendelegasikan otentikasi ke penyedia identitas eksternal, yang merupakan peningkatan keamanan signifikan:

### **Integrasi Penyedia Identitas Eksternal**

**Standar MCP Saat Ini (2025-11-25)** memungkinkan server MCP mendelegasikan otentikasi ke penyedia identitas eksternal, yang merupakan peningkatan keamanan signifikan:

**Manfaat Keamanan:**
1. **Menghilangkan Risiko Otentikasi Kustom**: Mengurangi permukaan kerentanan dengan menghindari implementasi otentikasi kustom  
2. **Keamanan Tingkat Perusahaan**: Memanfaatkan penyedia identitas mapan seperti Microsoft Entra ID dengan fitur keamanan canggih  
3. **Manajemen Identitas Terpusat**: Mempermudah manajemen siklus hidup pengguna, kontrol akses, dan audit kepatuhan  
4. **Otentikasi Multi-Faktor**: Mewarisi kemampuan MFA dari penyedia identitas perusahaan  
5. **Kebijakan Akses Kondisional**: Mendapat manfaat dari kontrol akses berbasis risiko dan otentikasi adaptif  

**Persyaratan Implementasi:**
- **Validasi Audiens Token**: Verifikasi semua token secara eksplisit diterbitkan untuk server MCP  
- **Verifikasi Penerbit**: Validasi penerbit token sesuai dengan penyedia identitas yang diharapkan  
- **Verifikasi Tanda Tangan**: Validasi kriptografi integritas token  
- **Penegakan Kedaluwarsa**: Penegakan ketat batas waktu hidup token  
- **Validasi Ruang Lingkup**: Pastikan token berisi izin yang sesuai untuk operasi yang diminta  

### **Keamanan Logika Otorisasi**

**Kontrol Kritis:**
- **Audit Otorisasi Komprehensif**: Tinjauan keamanan rutin pada semua titik keputusan otorisasi  
- **Default Fail-Safe**: Tolak akses saat logika otorisasi tidak dapat membuat keputusan pasti  
- **Batasan Izin**: Pemisahan jelas antara tingkat hak istimewa dan akses sumber daya yang berbeda  
- **Pencatatan Audit**: Pencatatan lengkap semua keputusan otorisasi untuk pemantauan keamanan  
- **Tinjauan Akses Berkala**: Validasi berkala atas izin pengguna dan penugasan hak istimewa  

## 2. **Keamanan Token & Kontrol Anti-Passthrough**

### **Pencegahan Token Passthrough**

**Token passthrough secara eksplisit dilarang** dalam Spesifikasi Otorisasi MCP karena risiko keamanan kritis:

**Risiko Keamanan yang Ditangani:**
- **Penghindaran Kontrol**: Melewati kontrol keamanan penting seperti pembatasan laju, validasi permintaan, dan pemantauan lalu lintas  
- **Kerusakan Akuntabilitas**: Membuat identifikasi klien tidak mungkin, merusak jejak audit dan investigasi insiden  
- **Eksfiltrasi Berbasis Proxy**: Memungkinkan aktor jahat menggunakan server sebagai proxy untuk akses data tidak sah  
- **Pelanggaran Batas Kepercayaan**: Melanggar asumsi kepercayaan layanan hilir tentang asal token  
- **Pergerakan Lateral**: Token yang dikompromikan di berbagai layanan memungkinkan perluasan serangan yang lebih luas  

**Kontrol Implementasi:**
```yaml
Token Validation Requirements:
  audience_validation: MANDATORY
  issuer_verification: MANDATORY  
  signature_check: MANDATORY
  expiration_enforcement: MANDATORY
  scope_validation: MANDATORY
  
Token Lifecycle Management:
  rotation_frequency: "Short-lived tokens preferred"
  secure_storage: "Azure Key Vault or equivalent"
  transmission_security: "TLS 1.3 minimum"
  replay_protection: "Implemented via nonce/timestamp"
```

### **Pola Manajemen Token yang Aman**

**Praktik Terbaik:**
- **Token Berumur Pendek**: Meminimalkan jendela paparan dengan rotasi token yang sering  
- **Penerbitan Just-in-Time**: Terbitkan token hanya saat diperlukan untuk operasi spesifik  
- **Penyimpanan Aman**: Gunakan modul keamanan perangkat keras (HSM) atau brankas kunci yang aman  
- **Pengikatan Token**: Ikat token ke klien, sesi, atau operasi tertentu bila memungkinkan  
- **Pemantauan & Peringatan**: Deteksi waktu nyata penyalahgunaan token atau pola akses tidak sah  

## 3. **Kontrol Keamanan Sesi**

### **Pencegahan Pembajakan Sesi**

**Vektor Serangan yang Ditangani:**
- **Injeksi Prompt Pembajakan Sesi**: Peristiwa jahat disuntikkan ke dalam status sesi bersama  
- **Pemalsuan Sesi**: Penggunaan tidak sah ID sesi yang dicuri untuk melewati otentikasi  
- **Serangan Aliran Dapat Dilanjutkan**: Eksploitasi kelanjutan event server-sent untuk injeksi konten jahat  

**Kontrol Sesi Mandatori:**
```yaml
Session ID Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

Session Binding:
  user_binding: "REQUIRED - <user_id>:<session_id>"
  additional_identifiers: "Device fingerprint, IP validation"
  context_binding: "Request origin, user agent validation"
  
Session Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired session removal"
```

**Keamanan Transportasi:**
- **Penegakan HTTPS**: Semua komunikasi sesi melalui TLS 1.3  
- **Atribut Cookie Aman**: HttpOnly, Secure, SameSite=Strict  
- **Pemasangan Sertifikat**: Untuk koneksi kritis guna mencegah serangan MITM  

### **Pertimbangan Stateful vs Stateless**

**Untuk Implementasi Stateful:**
- Status sesi bersama memerlukan perlindungan tambahan terhadap serangan injeksi  
- Manajemen sesi berbasis antrean membutuhkan verifikasi integritas  
- Beberapa instance server memerlukan sinkronisasi status sesi yang aman  

**Untuk Implementasi Stateless:**
- Manajemen sesi berbasis token JWT atau serupa  
- Verifikasi kriptografi integritas status sesi  
- Permukaan serangan berkurang tetapi memerlukan validasi token yang kuat  

## 4. **Kontrol Keamanan Khusus AI**

### **Pertahanan Injeksi Prompt**

**Integrasi Microsoft Prompt Shields:**
```yaml
Detection Mechanisms:
  - "Advanced ML-based instruction detection"
  - "Contextual analysis of external content"
  - "Real-time threat pattern recognition"
  
Protection Techniques:
  - "Spotlighting trusted vs untrusted content"
  - "Delimiter systems for content boundaries"  
  - "Data marking for content source identification"
  
Integration Points:
  - "Azure Content Safety service"
  - "Real-time content filtering"
  - "Threat intelligence updates"
```

**Kontrol Implementasi:**
- **Sanitasi Input**: Validasi dan penyaringan komprehensif semua input pengguna  
- **Definisi Batas Konten**: Pemisahan jelas antara instruksi sistem dan konten pengguna  
- **Hierarki Instruksi**: Aturan prioritas yang tepat untuk instruksi yang bertentangan  
- **Pemantauan Output**: Deteksi output yang berpotensi berbahaya atau dimanipulasi  

### **Pencegahan Keracunan Alat**

**Kerangka Keamanan Alat:**
```yaml
Tool Definition Protection:
  validation:
    - "Schema validation against expected formats"
    - "Content analysis for malicious instructions" 
    - "Parameter injection detection"
    - "Hidden instruction identification"
  
  integrity_verification:
    - "Cryptographic hashing of tool definitions"
    - "Digital signatures for tool packages"
    - "Version control with change auditing"
    - "Tamper detection mechanisms"
  
  monitoring:
    - "Real-time change detection"
    - "Behavioral analysis of tool usage"
    - "Anomaly detection for execution patterns"
    - "Automated alerting for suspicious modifications"
```

**Manajemen Alat Dinamis:**
- **Alur Persetujuan**: Persetujuan pengguna eksplisit untuk modifikasi alat  
- **Kemampuan Rollback**: Kemampuan untuk mengembalikan versi alat sebelumnya  
- **Audit Perubahan**: Riwayat lengkap modifikasi definisi alat  
- **Penilaian Risiko**: Evaluasi otomatis postur keamanan alat  

## 5. **Pencegahan Serangan Confused Deputy**

### **Keamanan Proxy OAuth**

**Kontrol Pencegahan Serangan:**
```yaml
Client Registration:
  static_client_protection:
    - "Explicit user consent for dynamic registration"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```

**Persyaratan Implementasi:**
- **Verifikasi Persetujuan Pengguna**: Jangan pernah melewati layar persetujuan untuk pendaftaran klien dinamis  
- **Validasi URI Redirect**: Validasi ketat berbasis daftar putih tujuan pengalihan  
- **Perlindungan Kode Otorisasi**: Kode berumur pendek dengan penegakan penggunaan tunggal  
- **Verifikasi Identitas Klien**: Validasi kuat kredensial dan metadata klien  

## 6. **Keamanan Eksekusi Alat**

### **Sandboxing & Isolasi**

**Isolasi Berbasis Kontainer:**
```yaml
Execution Environment:
  containerization: "Docker/Podman with security profiles"
  resource_limits:
    cpu: "Configurable CPU quotas"
    memory: "Memory usage restrictions"
    disk: "Storage access limitations"
    network: "Network policy enforcement"
  
  privilege_restrictions:
    user_context: "Non-root execution mandatory"
    capability_dropping: "Remove unnecessary Linux capabilities"
    syscall_filtering: "Seccomp profiles for syscall restriction"
    filesystem: "Read-only root with minimal writable areas"
```

**Isolasi Proses:**
- **Konteks Proses Terpisah**: Setiap eksekusi alat dalam ruang proses terisolasi  
- **Komunikasi Antar-Proses**: Mekanisme IPC aman dengan validasi  
- **Pemantauan Proses**: Analisis perilaku runtime dan deteksi anomali  
- **Penegakan Sumber Daya**: Batas keras pada CPU, memori, dan operasi I/O  

### **Implementasi Hak Istimewa Minimum**

**Manajemen Izin:**
```yaml
Access Control:
  file_system:
    - "Minimal required directory access"
    - "Read-only access where possible"
    - "Temporary file cleanup automation"
    
  network_access:
    - "Explicit allowlist for external connections"
    - "DNS resolution restrictions" 
    - "Port access limitations"
    - "SSL/TLS certificate validation"
  
  system_resources:
    - "No administrative privilege elevation"
    - "Limited system call access"
    - "No hardware device access"
    - "Restricted environment variable access"
```

## 7. **Kontrol Keamanan Rantai Pasokan**

### **Verifikasi Ketergantungan**

**Keamanan Komponen Komprehensif:**
```yaml
Software Dependencies:
  scanning: 
    - "Automated vulnerability scanning (GitHub Advanced Security)"
    - "License compliance verification"
    - "Known vulnerability database checks"
    - "Malware detection and analysis"
  
  verification:
    - "Package signature verification"
    - "Checksum validation"
    - "Provenance attestation"
    - "Software Bill of Materials (SBOM)"

AI Components:
  model_verification:
    - "Model provenance validation"
    - "Training data source verification" 
    - "Model behavior testing"
    - "Adversarial robustness assessment"
  
  service_validation:
    - "Third-party API security assessment"
    - "Service level agreement review"
    - "Data handling compliance verification"
    - "Incident response capability evaluation"
```

### **Pemantauan Berkelanjutan**

**Deteksi Ancaman Rantai Pasokan:**
- **Pemantauan Kesehatan Ketergantungan**: Penilaian berkelanjutan semua ketergantungan untuk masalah keamanan  
- **Integrasi Intelijen Ancaman**: Pembaruan waktu nyata tentang ancaman rantai pasokan yang muncul  
- **Analisis Perilaku**: Deteksi perilaku tidak biasa pada komponen eksternal  
- **Respons Otomatis**: Penahanan segera komponen yang dikompromikan  

## 8. **Kontrol Pemantauan & Deteksi**

### **Manajemen Informasi dan Kejadian Keamanan (SIEM)**

**Strategi Pencatatan Komprehensif:**
```yaml
Authentication Events:
  - "All authentication attempts (success/failure)"
  - "Token issuance and validation events"
  - "Session creation, modification, termination"
  - "Authorization decisions and policy evaluations"

Tool Execution:
  - "Tool invocation details and parameters"
  - "Execution duration and resource usage"
  - "Output generation and content analysis"
  - "Error conditions and exception handling"

Security Events:
  - "Potential prompt injection attempts"
  - "Tool poisoning detection events"
  - "Session hijacking indicators"
  - "Unusual access patterns and anomalies"
```

### **Deteksi Ancaman Waktu Nyata**

**Analitik Perilaku:**
- **Analitik Perilaku Pengguna (UBA)**: Deteksi pola akses pengguna yang tidak biasa  
- **Analitik Perilaku Entitas (EBA)**: Pemantauan perilaku server MCP dan alat  
- **Deteksi Anomali Berbasis Pembelajaran Mesin**: Identifikasi ancaman keamanan berbasis AI  
- **Korelasi Intelijen Ancaman**: Pencocokan aktivitas yang diamati dengan pola serangan yang dikenal  

## 9. **Respons & Pemulihan Insiden**

### **Kemampuan Respons Otomatis**

**Tindakan Respons Segera:**
```yaml
Threat Containment:
  session_management:
    - "Immediate session termination"
    - "Account lockout procedures"
    - "Access privilege revocation"
  
  system_isolation:
    - "Network segmentation activation"
    - "Service isolation protocols"
    - "Communication channel restriction"

Recovery Procedures:
  credential_rotation:
    - "Automated token refresh"
    - "API key regeneration"
    - "Certificate renewal"
  
  system_restoration:
    - "Clean state restoration"
    - "Configuration rollback"
    - "Service restart procedures"
```

### **Kemampuan Forensik**

**Dukungan Investigasi:**
- **Pelestarian Jejak Audit**: Pencatatan tidak dapat diubah dengan integritas kriptografi  
- **Pengumpulan Bukti**: Pengumpulan otomatis artefak keamanan yang relevan  
- **Rekonstruksi Garis Waktu**: Urutan rinci peristiwa yang mengarah ke insiden keamanan  
- **Penilaian Dampak**: Evaluasi cakupan kompromi dan eksposur data  

## **Prinsip Arsitektur Keamanan Utama**

### **Pertahanan Berlapis**
- **Beberapa Lapisan Keamanan**: Tidak ada titik kegagalan tunggal dalam arsitektur keamanan  
- **Kontrol Redundan**: Langkah keamanan tumpang tindih untuk fungsi kritis  
- **Mekanisme Fail-Safe**: Default aman saat sistem menghadapi kesalahan atau serangan  

### **Implementasi Zero Trust**
- **Jangan Pernah Percaya, Selalu Verifikasi**: Validasi berkelanjutan semua entitas dan permintaan  
- **Prinsip Hak Istimewa Minimum**: Hak akses minimal untuk semua komponen  
- **Mikro-Segmentasi**: Kontrol jaringan dan akses yang granular  

### **Evolusi Keamanan Berkelanjutan**
- **Adaptasi Lanskap Ancaman**: Pembaruan rutin untuk menangani ancaman yang muncul  
- **Efektivitas Kontrol Keamanan**: Evaluasi dan peningkatan berkelanjutan kontrol  
- **Kepatuhan Spesifikasi**: Penyesuaian dengan standar keamanan MCP yang berkembang  

---

## **Sumber Daya Implementasi**

### **Dokumentasi Resmi MCP**
- [Spesifikasi MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Praktik Terbaik Keamanan MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Spesifikasi Otorisasi MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Solusi Keamanan Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Standar Keamanan**
- [Praktik Terbaik Keamanan OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 untuk Model Bahasa Besar](https://genai.owasp.org/)
- [Kerangka Kerja Keamanan Siber NIST](https://www.nist.gov/cyberframework)

---

> **Penting**: Kontrol keamanan ini mencerminkan spesifikasi MCP saat ini (2025-06-18). Selalu verifikasi dengan [dokumentasi resmi](https://spec.modelcontextprotocol.io/) terbaru karena standar terus berkembang dengan cepat.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->