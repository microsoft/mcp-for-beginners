# Kawalan Keselamatan MCP - Kemas Kini Disember 2025

> **Standard Semasa**: Dokumen ini mencerminkan keperluan keselamatan [Spesifikasi MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) dan [Amalan Terbaik Keselamatan MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) rasmi.

Model Context Protocol (MCP) telah matang dengan ketara dengan kawalan keselamatan yang dipertingkatkan yang menangani kedua-dua keselamatan perisian tradisional dan ancaman khusus AI. Dokumen ini menyediakan kawalan keselamatan menyeluruh untuk pelaksanaan MCP yang selamat setakat Disember 2025.

## **Keperluan Keselamatan WAJIB**

### **Larangan Kritikal dari Spesifikasi MCP:**

> **DILARANG**: Pelayan MCP **TIDAK BOLEH** menerima sebarang token yang tidak dikeluarkan secara eksplisit untuk pelayan MCP  
>
> **DILARANG**: Pelayan MCP **TIDAK BOLEH** menggunakan sesi untuk pengesahan  
>
> **DIKEHENDAKI**: Pelayan MCP yang melaksanakan kebenaran **MESTI** mengesahkan SEMUA permintaan masuk  
>
> **WAJIB**: Pelayan proksi MCP yang menggunakan ID klien statik **MESTI** mendapatkan persetujuan pengguna untuk setiap klien yang didaftarkan secara dinamik

---

## 1. **Kawalan Pengesahan & Kebenaran**

### **Integrasi Penyedia Identiti Luaran**

**Standard MCP Semasa (2025-06-18)** membenarkan pelayan MCP mendelegasikan pengesahan kepada penyedia identiti luaran, mewakili peningkatan keselamatan yang ketara:

### **Integrasi Penyedia Identiti Luaran**

**Standard MCP Semasa (2025-11-25)** membenarkan pelayan MCP mendelegasikan pengesahan kepada penyedia identiti luaran, mewakili peningkatan keselamatan yang ketara:

**Manfaat Keselamatan:**
1. **Menghapuskan Risiko Pengesahan Tersuai**: Mengurangkan permukaan kerentanan dengan mengelakkan pelaksanaan pengesahan tersuai  
2. **Keselamatan Gred Perusahaan**: Memanfaatkan penyedia identiti yang telah mantap seperti Microsoft Entra ID dengan ciri keselamatan lanjutan  
3. **Pengurusan Identiti Berpusat**: Memudahkan pengurusan kitar hayat pengguna, kawalan akses, dan audit pematuhan  
4. **Pengesahan Pelbagai Faktor**: Mewarisi keupayaan MFA dari penyedia identiti perusahaan  
5. **Polisi Akses Bersyarat**: Mendapat manfaat kawalan akses berasaskan risiko dan pengesahan adaptif

**Keperluan Pelaksanaan:**
- **Pengesahan Audiens Token**: Sahkan semua token dikeluarkan secara eksplisit untuk pelayan MCP  
- **Pengesahan Penerbit**: Sahkan penerbit token sepadan dengan penyedia identiti yang dijangka  
- **Pengesahan Tandatangan**: Pengesahan kriptografi integriti token  
- **Penguatkuasaan Tempoh Sah**: Penguatkuasaan ketat had hayat token  
- **Pengesahan Skop**: Pastikan token mengandungi kebenaran yang sesuai untuk operasi yang diminta

### **Keselamatan Logik Kebenaran**

**Kawalan Kritikal:**
- **Audit Kebenaran Menyeluruh**: Semakan keselamatan berkala bagi semua titik keputusan kebenaran  
- **Default Fail-Safe**: Tolak akses apabila logik kebenaran tidak dapat membuat keputusan muktamad  
- **Sempadan Kebenaran**: Pemisahan jelas antara tahap keistimewaan dan akses sumber yang berbeza  
- **Log Audit**: Perekodan lengkap semua keputusan kebenaran untuk pemantauan keselamatan  
- **Semakan Akses Berkala**: Pengesahan berkala ke atas kebenaran pengguna dan penugasan keistimewaan

## 2. **Keselamatan Token & Kawalan Anti-Passthrough**

### **Pencegahan Passthrough Token**

**Passthrough token secara eksplisit dilarang** dalam Spesifikasi Kebenaran MCP kerana risiko keselamatan kritikal:

**Risiko Keselamatan Ditangani:**
- **Pengelakan Kawalan**: Memintas kawalan keselamatan penting seperti had kadar, pengesahan permintaan, dan pemantauan trafik  
- **Kerosakan Akauntabiliti**: Menjadikan pengenalan klien mustahil, merosakkan jejak audit dan siasatan insiden  
- **Eksfiltrasi Berasaskan Proksi**: Membolehkan pelaku jahat menggunakan pelayan sebagai proksi untuk akses data tanpa kebenaran  
- **Pelanggaran Sempadan Kepercayaan**: Memecahkan andaian kepercayaan perkhidmatan hiliran tentang asal token  
- **Pergerakan Lateral**: Token yang dikompromi merentasi pelbagai perkhidmatan membolehkan pengembangan serangan yang lebih luas

**Kawalan Pelaksanaan:**
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

### **Corak Pengurusan Token Selamat**

**Amalan Terbaik:**
- **Token Jangka Pendek**: Meminimumkan tempoh pendedahan dengan putaran token yang kerap  
- **Penerbitan Just-in-Time**: Keluarkan token hanya apabila diperlukan untuk operasi tertentu  
- **Penyimpanan Selamat**: Gunakan modul keselamatan perkakasan (HSM) atau peti kunci selamat  
- **Pengikatan Token**: Ikat token kepada klien, sesi, atau operasi tertentu jika boleh  
- **Pemantauan & Amaran**: Pengesanan masa nyata penyalahgunaan token atau corak akses tanpa kebenaran

## 3. **Kawalan Keselamatan Sesi**

### **Pencegahan Pengambilalihan Sesi**

**Vektor Serangan Ditangani:**
- **Suntikan Prompt Pengambilalihan Sesi**: Peristiwa berniat jahat disuntik ke dalam keadaan sesi yang dikongsi  
- **Peniruan Sesi**: Penggunaan tanpa kebenaran ID sesi yang dicuri untuk memintas pengesahan  
- **Serangan Aliran Boleh Disambung Semula**: Eksploitasi penyambungan semula acara yang dihantar pelayan untuk suntikan kandungan berniat jahat

**Kawalan Sesi Wajib:**
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

**Keselamatan Pengangkutan:**
- **Penguatkuasaan HTTPS**: Semua komunikasi sesi melalui TLS 1.3  
- **Atribut Kukis Selamat**: HttpOnly, Secure, SameSite=Strict  
- **Pemasangan Sijil**: Untuk sambungan kritikal bagi mengelakkan serangan MITM

### **Pertimbangan Stateful vs Stateless**

**Untuk Pelaksanaan Stateful:**
- Keadaan sesi yang dikongsi memerlukan perlindungan tambahan terhadap serangan suntikan  
- Pengurusan sesi berasaskan antrian memerlukan pengesahan integriti  
- Beberapa contoh pelayan memerlukan penyelarasan keadaan sesi yang selamat

**Untuk Pelaksanaan Stateless:**
- Pengurusan sesi berasaskan token JWT atau serupa  
- Pengesahan kriptografi integriti keadaan sesi  
- Permukaan serangan dikurangkan tetapi memerlukan pengesahan token yang kukuh

## 4. **Kawalan Keselamatan Khusus AI**

### **Pertahanan Suntikan Prompt**

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

**Kawalan Pelaksanaan:**
- **Sanitasi Input**: Pengesahan dan penapisan menyeluruh semua input pengguna  
- **Definisi Sempadan Kandungan**: Pemisahan jelas antara arahan sistem dan kandungan pengguna  
- **Hierarki Arahan**: Peraturan keutamaan yang betul untuk arahan yang bertentangan  
- **Pemantauan Output**: Pengesanan output yang berpotensi berbahaya atau dimanipulasi

### **Pencegahan Keracunan Alat**

**Rangka Kerja Keselamatan Alat:**
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

**Pengurusan Alat Dinamik:**
- **Aliran Kerja Kelulusan**: Persetujuan pengguna secara eksplisit untuk pengubahsuaian alat  
- **Keupayaan Rollback**: Kebolehan untuk kembali ke versi alat sebelumnya  
- **Audit Perubahan**: Sejarah lengkap pengubahsuaian definisi alat  
- **Penilaian Risiko**: Penilaian automatik terhadap postur keselamatan alat

## 5. **Pencegahan Serangan Confused Deputy**

### **Keselamatan Proksi OAuth**

**Kawalan Pencegahan Serangan:**
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

**Keperluan Pelaksanaan:**
- **Pengesahan Persetujuan Pengguna**: Jangan sesekali langkau skrin persetujuan untuk pendaftaran klien dinamik  
- **Pengesahan URI Redirect**: Pengesahan berasaskan senarai putih yang ketat untuk destinasi redirect  
- **Perlindungan Kod Kebenaran**: Kod jangka pendek dengan penguatkuasaan guna sekali sahaja  
- **Pengesahan Identiti Klien**: Pengesahan kukuh ke atas kelayakan dan metadata klien

## 6. **Keselamatan Pelaksanaan Alat**

### **Pengasingan & Sandboxing**

**Pengasingan Berasaskan Kontena:**
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

**Pengasingan Proses:**
- **Konteks Proses Berasingan**: Setiap pelaksanaan alat dalam ruang proses yang terasing  
- **Komunikasi Antara Proses**: Mekanisme IPC selamat dengan pengesahan  
- **Pemantauan Proses**: Analisis tingkah laku masa nyata dan pengesanan anomali  
- **Penguatkuasaan Sumber**: Had keras ke atas CPU, memori, dan operasi I/O

### **Pelaksanaan Keistimewaan Minimum**

**Pengurusan Kebenaran:**
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

## 7. **Kawalan Keselamatan Rantaian Bekalan**

### **Pengesahan Kebergantungan**

**Keselamatan Komponen Menyeluruh:**
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

### **Pemantauan Berterusan**

**Pengesanan Ancaman Rantaian Bekalan:**
- **Pemantauan Kesihatan Kebergantungan**: Penilaian berterusan semua kebergantungan untuk isu keselamatan  
- **Integrasi Intelijen Ancaman**: Kemas kini masa nyata mengenai ancaman rantaian bekalan yang muncul  
- **Analisis Tingkah Laku**: Pengesanan tingkah laku luar biasa dalam komponen luaran  
- **Tindak Balas Automatik**: Pengawalan segera komponen yang dikompromi

## 8. **Kawalan Pemantauan & Pengesanan**

### **Pengurusan Maklumat dan Peristiwa Keselamatan (SIEM)**

**Strategi Perekodan Menyeluruh:**
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

### **Pengesanan Ancaman Masa Nyata**

**Analitik Tingkah Laku:**
- **Analitik Tingkah Laku Pengguna (UBA)**: Pengesanan corak akses pengguna yang luar biasa  
- **Analitik Tingkah Laku Entiti (EBA)**: Pemantauan tingkah laku pelayan MCP dan alat  
- **Pengesanan Anomali Pembelajaran Mesin**: Pengenalan ancaman keselamatan berkuasa AI  
- **Korelasi Intelijen Ancaman**: Memadankan aktiviti yang diperhatikan dengan corak serangan yang diketahui

## 9. **Tindak Balas & Pemulihan Insiden**

### **Keupayaan Tindak Balas Automatik**

**Tindakan Tindak Balas Segera:**
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

### **Keupayaan Forensik**

**Sokongan Siasatan:**
- **Pemeliharaan Jejak Audit**: Perekodan tidak boleh diubah dengan integriti kriptografi  
- **Pengumpulan Bukti**: Pengumpulan automatik artifak keselamatan yang berkaitan  
- **Pembinaan Semula Garis Masa**: Urutan terperinci peristiwa yang membawa kepada insiden keselamatan  
- **Penilaian Impak**: Penilaian skop kompromi dan pendedahan data

## **Prinsip Utama Seni Bina Keselamatan**

### **Pertahanan Berlapis**
- **Berbilang Lapisan Keselamatan**: Tiada titik kegagalan tunggal dalam seni bina keselamatan  
- **Kawalan Redundan**: Langkah keselamatan bertindih untuk fungsi kritikal  
- **Mekanisme Fail-Safe**: Tetapan selamat apabila sistem menghadapi ralat atau serangan

### **Pelaksanaan Zero Trust**
- **Jangan Pernah Percaya, Sentiasa Sahkan**: Pengesahan berterusan semua entiti dan permintaan  
- **Prinsip Keistimewaan Minimum**: Hak akses minimum untuk semua komponen  
- **Mikro-Segmentasi**: Kawalan rangkaian dan akses yang terperinci

### **Evolusi Keselamatan Berterusan**
- **Penyesuaian Lanskap Ancaman**: Kemas kini berkala untuk menangani ancaman yang muncul  
- **Keberkesanan Kawalan Keselamatan**: Penilaian dan penambahbaikan berterusan kawalan  
- **Pematuhan Spesifikasi**: Penyesuaian dengan standard keselamatan MCP yang berkembang

---

## **Sumber Pelaksanaan**

### **Dokumentasi Rasmi MCP**
- [Spesifikasi MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Amalan Terbaik Keselamatan MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Spesifikasi Kebenaran MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Penyelesaian Keselamatan Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Standard Keselamatan**
- [Amalan Terbaik Keselamatan OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 untuk Model Bahasa Besar](https://genai.owasp.org/)
- [Rangka Kerja Keselamatan Siber NIST](https://www.nist.gov/cyberframework)

---

> **Penting**: Kawalan keselamatan ini mencerminkan spesifikasi MCP semasa (2025-06-18). Sentiasa sahkan dengan [dokumentasi rasmi](https://spec.modelcontextprotocol.io/) terkini kerana standard terus berkembang dengan pesat.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->