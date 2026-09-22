# Kontrol Keamanan MCP - Pembaruan September 2026

> **Standar saat ini:** Dokumen ini mencerminkan
> [Spesifikasi MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> dan
> [Praktik Keamanan Terbaik MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) resmi.

Protokol Konteks Model (MCP) telah berkembang pesat dengan kontrol keamanan yang ditingkatkan untuk menangani keamanan perangkat lunak tradisional dan ancaman khusus AI. Dokumen ini menyediakan kontrol keamanan komprehensif untuk implementasi MCP yang aman sesuai dengan kerangka kerja OWASP MCP Top 10.

## 🏔️ Pelatihan Keamanan Praktis

Untuk pengalaman praktis penerapan keamanan, kami merekomendasikan **[Lokakarya MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - ekspedisi terpandu lengkap untuk mengamankan server MCP di Azure dengan metodologi "rentan → eksploitasi → perbaiki → validasi".

Semua kontrol keamanan dalam dokumen ini selaras dengan **[Panduan Keamanan MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/)**, yang menyediakan arsitektur referensi dan panduan implementasi Azure khusus untuk risiko OWASP MCP Top 10.

## **Persyaratan Keamanan WAJIB**

### **Larangan Kritis dari Spesifikasi MCP:**

> **TERLARANG**: Server MCP **TIDAK BOLEH** menerima token apa pun yang tidak secara eksplisit diterbitkan untuk server MCP
>
> **DILARANG**: Server MCP **TIDAK BOLEH** menggunakan sesi untuk autentikasi  
>
> **DIPERLUKAN**: Server MCP yang menerapkan otorisasi **HARUS** memverifikasi SEMUA permintaan masuk
>
> **WAJIB**: Server proxy MCP yang menggunakan ID klien pihak ketiga statis
> **HARUS** memperoleh persetujuan untuk setiap klien MCP sebelum meneruskan otorisasi

---

## 1. **Kontrol Autentikasi & Otorisasi**

### **Integrasi Penyedia Identitas Eksternal**

**Spesifikasi MCP `2026-07-28`** mengizinkan server MCP mendelegasikan
autentikasi ke penyedia identitas eksternal. Otorisasi untuk transport HTTP
dievaluasi per permintaan; server stdio lokal mengambil kredensial
dari lingkungan mereka sebagai gantinya.

**Risiko OWASP MCP yang Ditangani**: [MCP07 - Autentikasi & Otorisasi Tidak Memadai](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Manfaat Keamanan:**
1. **Menghilangkan Risiko Autentikasi Kustom**: Mengurangi permukaan kerentanan dengan menghindari implementasi autentikasi kustom
2. **Keamanan Kelas Perusahaan**: Memanfaatkan penyedia identitas mapan seperti Microsoft Entra ID dengan fitur keamanan canggih
3. **Manajemen Identitas Terpusat**: Mempermudah manajemen siklus hidup pengguna, kontrol akses, dan audit kepatuhan
4. **Autentikasi Multi-Faktor**: Mewarisi kemampuan MFA dari penyedia identitas perusahaan
5. **Kebijakan Akses Kondisional**: Mendapat manfaat dari kontrol akses berbasis risiko dan autentikasi adaptif

**Persyaratan Implementasi:**
- **Pendaftaran Klien**: Utamakan Dokumen Metadata ID Klien atau
  pra-pendaftaran; gunakan Pendaftaran Klien Dinamis yang sudah usang hanya untuk
  kompatibilitas
- **Validasi Audiens Token**: Verifikasi semua token diterbitkan secara eksplisit untuk server MCP
- **Verifikasi Penerbit**: Validasi penerbit token sesuai dengan penyedia identitas yang diharapkan
- **Verifikasi Tanda Tangan**: Validasi kriptografi integritas token
- **Penegakan Kadaluarsa**: Penegakan ketat batas waktu hidup token
- **Validasi Ruang Lingkup**: Pastikan token berisi izin yang sesuai untuk operasi yang diminta

### **Keamanan Logika Otorisasi**

**Kontrol Kritis:**
- **Audit Otorisasi Komprehensif**: Tinjauan keamanan berkala untuk semua titik keputusan otorisasi
- **Default Aman**: Tolak akses ketika logika otorisasi tidak dapat membuat keputusan pasti
- **Batasan Izin**: Pemisahan jelas antara tingkat hak istimewa dan akses sumber daya
- **Logging Audit**: Pencatatan lengkap semua keputusan otorisasi untuk pemantauan keamanan
- **Tinjauan Akses Reguler**: Validasi berkala atas izin pengguna dan penugasan hak istimewa

## 2. **Keamanan Token & Kontrol Anti-Passthrough**

**Risiko OWASP MCP yang Ditangani**: [MCP01 - Kesalahan Pengelolaan Token & Paparan Rahasia](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Pencegahan Token Passthrough**

**Token passthrough secara eksplisit dilarang** dalam Spesifikasi Otorisasi MCP karena risiko keamanan kritis:

**Risiko Keamanan yang Ditangani:**
- **Pengelakan Kontrol**: Melewati kontrol keamanan penting seperti pembatasan laju, validasi permintaan, dan pemantauan lalu lintas
- **Patah Kendali Akuntabilitas**: Membuat identifikasi klien menjadi tidak mungkin, merusak jejak audit dan penyelidikan insiden
- **Eksfiltrasi Berbasis Proxy**: Memungkinkan aktor jahat menggunakan server sebagai proxy untuk akses data tanpa izin
- **Pelanggaran Batas Kepercayaan**: Mematahkan asumsi kepercayaan layanan hilir tentang asal token
- **Pergerakan Lateral**: Token yang dikompromikan di beberapa layanan memungkinkan perluasan serangan lebih luas

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
- **Token Berumur Pendek**: Minimalkan jendela paparan dengan rotasi token yang sering
- **Penerbitan Tepat Waktu**: Terbitkan token hanya saat dibutuhkan untuk operasi spesifik
- **Penyimpanan Aman**: Gunakan modul keamanan perangkat keras (HSM) atau brankas kunci aman
- **Pengikatan Token**: Validasi audiens dan penerbit token untuk sumber daya MCP,
  klien, dan operasi yang dimaksud
- **Pemantauan & Peringatan**: Deteksi waktu nyata penyalahgunaan token atau pola akses tidak sah

## 3. **Kontrol Keamanan Status Aplikasi**

### **Pencegahan Pembajakan Handle Status**

**Vektor Serangan yang Ditangani:**
- **Tebakan Handle**: Pengenal yang dapat diprediksi mengekspos status pemanggil lain
- **Penggunaan Ulang Lintas Pengguna**: Handle yang dicuri digunakan dengan identitas berbeda
- **Otorisasi Implisit**: Kepemilikan handle secara keliru dianggap sebagai
  bukti akses

**Kontrol Handle Status:**

```yaml
State Handle Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

State Binding:
  user_binding: "Bind server-side to the authenticated principal"
  authorization: "Recheck on every request"
  client_input: "Never trust a client-supplied user ID"
  
State Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired state removal"
```

**Keamanan Transportasi:**
- **Penegakan HTTPS**: Mewajibkan HTTPS pada transport HTTP jarak jauh
- **Penanganan Kredensial**: Kirim dan validasi otorisasi pada setiap permintaan HTTP
- **Isolasi stdio**: Lindungi server stdio lokal melalui isolasi proses dan
  kontrol kredensial lingkungan

### **Pertimbangan Stateful vs Stateless**

MCP `2026-07-28` bersifat stateless di lapisan protokol. Aplikasi masih dapat
mempertahankan status dengan mengembalikan handle eksplisit dari satu pemanggilan alat dan menerimanya sebagai argumen biasa pada pemanggilan selanjutnya.


- Simpan status secara independen dari koneksi transportasi mana pun.
- Kaitkan handle status dengan principal yang diautentikasi di sisi server.
- Perlakukan handle sebagai nama, bukan sebagai kredensial pembawa.
- Definisikan perilaku kadaluarsa dan pemulihan untuk handle yang usang.

## 4. **Kontrol Keamanan Khusus AI**

**Risiko OWASP MCP yang Ditangani**:

- [MCP06 - Subversi Aliran Niat](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Keracunan Alat](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Injeksi & Eksekusi Perintah](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

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
- **Sanitasi Input**: Validasi dan pemfilteran menyeluruh dari semua input pengguna
- **Definisi Batas Konten**: Pemisahan jelas antara instruksi sistem dan konten pengguna
- **Hierarki Instruksi**: Aturan preseden yang tepat untuk instruksi yang bertentangan
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
- **Alur Persetujuan**: Persetujuan eksplisit pengguna untuk modifikasi alat
- **Kemampuan Rollback**: Kemampuan untuk mengembalikan versi alat sebelumnya
- **Audit Perubahan**: Riwayat lengkap modifikasi definisi alat
- **Penilaian Risiko**: Evaluasi otomatis postur keamanan alat

## 5. **Pencegahan Serangan Deputi Bingung**

### **Keamanan Proxy OAuth**

**Kontrol Pencegahan Serangan:**
```yaml
Client Registration:
  preferred_methods:
    - "Pre-registration when client and server have an existing relationship"
    - "Client ID Metadata Documents for clients without prior registration"
  compatibility_fallback:
    - "Dynamic Client Registration only when CIMD is unavailable"
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
- **Registrasi Klien**: Lebih baik pra-registrasi atau Metadata ID Klien
  Dokumen; anggap Registrasi Klien Dinamis sebagai fallback kompatibilitas
- **Verifikasi Persetujuan Pengguna**: Proxy MCP yang menggunakan ID klien pihak ketiga statis
  harus mendapatkan persetujuan per klien sebelum meneruskan otorisasi
- **Validasi URI Redirect**: Validasi berbasis whitelist yang ketat untuk tujuan redirect
- **Perlindungan Kode Otorisasi**: Kode dengan masa berlaku pendek dan penegakan penggunaan sekali
- **Verifikasi Identitas Klien**: Validasi yang kuat atas kredensial dan metadata klien

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
- **Komunikasi Antar-Proses**: Mekanisme IPC yang aman dengan validasi
- **Pemantauan Proses**: Analisis perilaku runtime dan deteksi anomali
- **Penegakan Sumber Daya**: Batas keras pada CPU, memori, dan operasi I/O

### **Implementasi Prinsip Hak Istimewa Paling Rendah**

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

**Risiko OWASP MCP yang Ditangani**: [MCP04 - Serangan Rantai Pasokan Perangkat Lunak & Perusakan Dependensi](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Verifikasi Dependensi**

**Keamanan Komponen Menyeluruh:**
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
- **Pemantauan Kesehatan Dependensi**: Penilaian terus-menerus semua dependensi untuk masalah keamanan
- **Integrasi Intelijen Ancaman**: Pembaruan waktu nyata tentang ancaman rantai pasokan yang muncul
- **Analisis Perilaku**: Deteksi perilaku tidak biasa pada komponen eksternal
- **Respon Otomatis**: Penahanan segera komponen yang terekspos

## 8. **Kontrol Pemantauan & Deteksi**

**Risiko OWASP MCP yang Ditangani**: [MCP08 - Kurangnya Audit dan Telemetri](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Manajemen Informasi dan Peristiwa Keamanan (SIEM)**

**Strategi Logging Menyeluruh:**
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
- **Korelasi Intelijen Ancaman**: Mencocokkan aktivitas yang diamati dengan pola serangan yang dikenal

## 9. **Respons Insiden & Pemulihan**

### **Kemampuan Respon Otomatis**

**Tindakan Respon Segera:**
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
- **Pelestarian Jejak Audit**: Logging tak dapat diubah dengan integritas kriptografis
- **Pengumpulan Bukti**: Pengumpulan otomatis artefak keamanan yang relevan
- **Rekonstruksi Linimasa**: Urutan rinci peristiwa yang mengarah pada insiden keamanan
- **Penilaian Dampak**: Evaluasi cakupan kompromi dan eksposur data

## **Prinsip Arsitektur Keamanan Utama**

### **Pertahanan Bertingkat**
- **Beberapa Lapisan Keamanan**: Tidak ada titik kegagalan tunggal dalam arsitektur keamanan
- **Kontrol Redundan**: Langkah keamanan yang tumpang tindih untuk fungsi kritis
- **Mekanisme Fail-Safe**: Default aman saat sistem mengalami kesalahan atau serangan

### **Implementasi Zero Trust**
- **Jangan Pernah Percaya, Selalu Verifikasi**: Validasi berkelanjutan semua entitas dan permintaan
- **Prinsip Hak Istimewa Paling Rendah**: Hak akses minimal untuk semua komponen
- **Mikro-Segmentasi**: Kontrol jaringan dan akses yang terperinci

### **Evolusi Keamanan Berkelanjutan**
- **Adaptasi Lanskap Ancaman**: Pembaruan rutin untuk mengatasi ancaman yang muncul
- **Efektivitas Kontrol Keamanan**: Evaluasi dan peningkatan kontrol yang berkelanjutan
- **Kepatuhan Spesifikasi**: Penyesuaian dengan standar keamanan MCP yang berkembang

---

## **Sumber Daya Implementasi**

### **Dokumentasi Resmi MCP**
- [Spesifikasi MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Praktik Terbaik Keamanan MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Spesifikasi Otorisasi MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Sumber Daya Keamanan OWASP MCP**
- [Panduan Keamanan Azure OWASP MCP](https://microsoft.github.io/mcp-azure-security-guide/) - OWASP MCP Top 10 komprehensif dengan implementasi Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Risiko keamanan resmi OWASP MCP
- [Lokakarya MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Pelatihan keamanan praktis untuk MCP di Azure

### **Solusi Keamanan Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Keamanan Konten Azure](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Standar Keamanan**
- [Praktik Terbaik Keamanan OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Top 10 untuk Model Bahasa Besar](https://genai.owasp.org/)

- [Kerangka Kerja Keamanan Siber NIST](https://www.nist.gov/cyberframework)

---

> **Penting:** Kontrol keamanan ini mencerminkan Spesifikasi MCP
> `2026-07-28`. Selalu verifikasi terhadap
> [dokumentasi resmi saat ini](https://modelcontextprotocol.io/specification/2026-07-28/)
> karena standar terus berkembang.

## Apa Berikutnya

- Kembali ke: [Ikhtisar Modul Keamanan](./README.md)
- Lanjut ke: [Modul 3: Memulai](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->