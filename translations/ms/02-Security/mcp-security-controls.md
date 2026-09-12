# Kawalan Keselamatan MCP - Kemas Kini September 2026

> **Standard semasa:** Dokumen ini mencerminkan
> [Spesifikasi MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> dan rasmi
> [Amalan Terbaik Keselamatan MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Protokol Konteks Model (MCP) telah berkembang dengan ketara dengan kawalan keselamatan yang dipertingkatkan yang menangani kedua-dua keselamatan perisian tradisional dan ancaman khusus AI. Dokumen ini menyediakan kawalan keselamatan menyeluruh untuk pelaksanaan MCP yang selamat sejajar dengan rangka kerja OWASP MCP Top 10.

## 🏔️ Latihan Keselamatan Praktikal

Untuk pengalaman pelaksanaan keselamatan secara praktikal, kami mengesyorkan **[Bengkel Sidang Kemuncak Keselamatan MCP (Sherpa)](https://azure-samples.github.io/sherpa/)** - satu ekspedisi terpandu menyeluruh untuk mengamankan pelayan MCP di Azure menggunakan metodologi "mudah terdedah → eksploit → baiki → sahkan".

Semua kawalan keselamatan dalam dokumen ini selaras dengan **[Panduan Keselamatan Azure MCP OWASP](https://microsoft.github.io/mcp-azure-security-guide/)**, yang menyediakan seni bina rujukan dan panduan pelaksanaan khusus Azure untuk risiko OWASP MCP Top 10.

## **KEPERLUAN Keselamatan WAJIB**

### **Larangan Kritikal dari Spesifikasi MCP:**

> **DILARANG**: Pelayan MCP **TIDAK BOLEH** menerima mana-mana token yang tidak secara eksplisit dikeluarkan untuk pelayan MCP
>
> **DILARANG**: Pelayan MCP **TIDAK BOLEH** menggunakan sesi untuk pengesahan  
>
> **DISELAKAR**: Pelayan MCP yang melaksanakan kebenaran **MESTI** mengesahkan SEMUA permintaan masuk
>
> **WAJIB**: Pelayan proksi MCP yang menggunakan ID klien pihak ketiga statik
> **MESTI** mendapatkan persetujuan untuk setiap klien MCP sebelum meneruskan kebenaran

---

## 1. **Kawalan Pengesahan & Kebenaran**

### **Integrasi Penyedia Identiti Luaran**

**Spesifikasi MCP `2026-07-28`** membenarkan pelayan MCP mendelegasikan
pengesahan kepada penyedia identiti luaran. Kebenaran untuk pengangkut HTTP
dinilai setiap permintaan; pelayan stdio setempat diperoleh kelayakan
dari persekitaran mereka sebaliknya.

**Risiko OWASP MCP yang Ditangani**: [MCP07 - Pengesahan & Kebenaran Tidak Mencukupi](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Manfaat Keselamatan:**
1. **Menghapuskan Risiko Pengesahan Tersuai**: Mengurangkan permukaan kerentanan dengan mengelak pelaksanaan pengesahan tersuai
2. **Keselamatan Kelas Perusahaan**: Memanfaatkan penyedia identiti yang telah wujud seperti Microsoft Entra ID dengan ciri keselamatan maju
3. **Pengurusan Identiti Berpusat**: Memudahkan pengurusan kitar hayat pengguna, kawalan akses, dan audit pematuhan
4. **Pengesahan Faktor Berganda**: Mewarisi keupayaan MFA daripada penyedia identiti perusahaan
5. **Polisi Akses Bersyarat**: Manfaat daripada kawalan akses berasaskan risiko dan pengesahan adaptif

**Keperluan Pelaksanaan:**
- **Pendaftaran Klien**: Utamakan Dokumen Metadata ID Klien atau
  pra-pendaftaran; gunakan Pendaftaran Klien Dinamik yang telah lapuk hanya untuk
  keserasian
- **Pengesahan Audiens Token**: Sahkan semua token dikeluarkan secara eksplisit untuk pelayan MCP
- **Pengesahan Penerbit**: Sahkan penerbit token sepadan dengan penyedia identiti yang dijangka
- **Pengesahan Tandatangan**: Pengesahan kriptografi integriti token
- **Penguatkuasaan Tempoh Sah**: Penguatkuasaan ketat had jangka hayat token
- **Pengesahan Skop**: Pastikan token mengandungi kebenaran yang sesuai untuk operasi yang diminta

### **Keselamatan Logik Kebenaran**

**Kawalan Kritikal:**
- **Audit Kebenaran Menyeluruh**: Semakan keselamatan berkala bagi semua titik keputusan kebenaran
- **Default Gagal-Selamat**: Tolak akses apabila logik kebenaran tidak dapat membuat keputusan muktamad
- **Sempadan Kebenaran**: Pemisahan jelas antara tahap keistimewaan yang berbeza dan akses sumber
- **Log Audit**: Pencatatan lengkap semua keputusan kebenaran untuk pemantauan keselamatan
- **Semakan Akses Berkala**: Pengesahan berkala bagi kebenaran pengguna dan penugasan keistimewaan

## 2. **Kawalan Keselamatan Token & Anti-Passthrough**

**Risiko OWASP MCP yang Ditangani**: [MCP01 - Pengurusan Token & Pendedahan Rahsia yang Tidak Betul](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Pencegahan Token Passthrough**

**Token passthrough secara eksplisit dilarang** dalam Spesifikasi Kebenaran MCP kerana risiko keselamatan kritikal:

**Risiko Keselamatan yang Ditangani:**
- **Pengelakan Kawalan**: Mengelakkan kawalan keselamatan penting seperti had kadar, pengesahan permintaan, dan pemantauan trafik
- **Kerosakan Akauntabiliti**: Menjadikan pengenalpastian klien tidak mungkin, merosakkan jejak audit dan penyiasatan insiden
- **Eksfiltrasi Berasaskan Proksi**: Membolehkan pelaku jahat menggunakan pelayan sebagai proksi untuk akses data tanpa kebenaran
- **Pelanggaran Sempadan Kepercayaan**: Memecahkan andaian kepercayaan perkhidmatan hiliran tentang asal token
- **Pergerakan Lateral**: Token yang dikompromi merentas pelbagai perkhidmatan membolehkan pengembangan serangan lebih luas

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
- **Token Jangka Pendek**: Mengehadkan tetingkap pendedahan dengan putaran token yang kerap
- **Penerbitan Just-in-Time**: Keluarkan token hanya apabila diperlukan untuk operasi tertentu
- **Penyimpanan Selamat**: Gunakan modul keselamatan perkakasan (HSM) atau peti kunci utama yang selamat
- **Pengikatan Token**: Sahkan audiens dan penerbit token untuk sumber MCP,
  klien, dan operasi yang dimaksudkan
- **Pemantauan & Amaran**: Pengesanan masa nyata terhadap penyalahgunaan token atau corak akses tanpa kebenaran

## 3. **Kawalan Keselamatan Keadaan Aplikasi**

### **Pencegahan Penculikan Pemegang Keadaan**

**Vektor Serangan yang Ditangani:**
- **Meneka Pemegang**: Pengecam yang boleh diramal mendedahkan keadaan pemanggil lain
- **Penggunaan Semula Antara Pengguna**: Pemegang yang dicuri digunakan dengan identiti yang berbeza
- **Kebenaran Implisit**: Pemilikan pemegang disalahanggap sebagai
  bukti akses

**Kawalan Pemegang Keadaan:**

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

**Keselamatan Pengangkutan:**
- **Penguatkuasaan HTTPS**: Memerlukan HTTPS untuk pengangkut HTTP jauh
- **Pengendalian Kelayakan**: Hantar dan sahkan kebenaran pada setiap permintaan HTTP
- **Pengasingan stdio**: Lindungi pelayan stdio tempatan melalui pengasingan proses dan
  kawalan kelayakan persekitaran

### **Pertimbangan Negeri vs Tanpa Negeri**

MCP `2026-07-28` adalah tanpa negeri di lapisan protokol. Aplikasi masih boleh
menyimpan keadaan dengan memulangkan pemegang jelas dari satu panggilan alat dan menerimanya
sebagai argumen biasa pada panggilan kemudiannya.

- Simpan keadaan secara bebas daripada mana-mana sambungan pengangkut tunggal.
- Ikat pemegang keadaan kepada pelayan prinsip yang disahkan di sisi pelayan.
- Anggap pemegang sebagai nama, bukan sebagai kelayakan pemegang.
- Tetapkan tempoh tamat dan tingkah laku pemulihan untuk pemegang yang lapuk.

## 4. **Kawalan Keselamatan Khusus AI**

**Risiko OWASP MCP yang Ditangani**:

- [MCP06 - Subversi Aliran Niat](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Racun Alat](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Suntikan & Pelaksanaan Perintah](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Pertahanan Suntikan Prompt**

**Integrasi Pelindung Prompt Microsoft:**
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
- **Pensihatan Input**: Pengesahan dan penapisan menyeluruh bagi semua input pengguna
- **Definisi Sempadan Kandungan**: Pemisahan jelas antara arahan sistem dan kandungan pengguna
- **Hierarki Arahan**: Peraturan keutamaan yang betul untuk arahan yang bertentangan
- **Pemantauan Output**: Pengesanan output yang berpotensi berbahaya atau dimanipulasi

### **Pencegahan Racun Alat**

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
- **Aliran Kerja Kelulusan**: Persetujuan pengguna yang jelas untuk pengubahsuaian alat
- **Keupayaan Punggutan Balik**: Keupayaan untuk kembali ke versi alat sebelumnya
- **Audit Perubahan**: Sejarah lengkap pengubahsuaian definisi alat
- **Penilaian Risiko**: Penilaian automatik terhadap kedudukan keselamatan alat

## 5. **Pencegahan Serangan Deputi Keliru**

### **Keselamatan Proksi OAuth**

**Kawalan Pencegahan Serangan:**
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

**Keperluan Pelaksanaan:**
- **Pendaftaran Pelanggan**: Utamakan pra-pendaftaran atau Metadata ID Pelanggan
  Dokumen; anggapkan Pendaftaran Pelanggan Dinamik sebagai sokongan kesesuaian
- **Pengesahan Persetujuan Pengguna**: Proksi MCP yang menggunakan ID klien pihak ketiga statik
  mesti mendapatkan persetujuan per-klien sebelum meneruskan kebenaran
- **Pengesahan URI Pengalihan**: Pengesahan berasaskan senarai putih yang ketat untuk destinasi pengalihan
- **Perlindungan Kod Kebenaran**: Kod jangka masa pendek dengan penguatkuasaan guna sekali
- **Pengesahan Identiti Pelanggan**: Pengesahan kukuh kredensial dan metadata pelanggan

## 6. **Keselamatan Pelaksanaan Alat**

### **Penjarakan & Pengasingan**

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
- **Konteks Proses Berasingan**: Setiap pelaksanaan alat dalam ruang proses terasing
- **Komunikasi Antara Proses**: Mekanisme IPC selamat dengan pengesahan
- **Pemantauan Proses**: Analisis tingkah laku runtime dan pengesanan anomali
- **Penguatkuasaan Sumber**: Had keras pada CPU, memori, dan operasi I/O

### **Pelaksanaan Hak Istimewa Terendah**

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

**Risiko OWASP MCP Ditangani**: [MCP04 - Serangan Rantaian Bekalan Perisian & Pemalsuan Kebergantungan](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

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
- **Integrasi Intelijen Ancaman**: Kemas kini masa nyata terhadap ancaman rantaian bekalan yang muncul
- **Analisis Tingkah Laku**: Pengesanan tingkah laku luar biasa dalam komponen luaran
- **Tindak Balas Automatik**: Pengawalan segera terhadap komponen yang dikompromi

## 8. **Kawalan Pemantauan & Pengesanan**

**Risiko OWASP MCP Ditangani**: [MCP08 - Kekurangan Audit dan Telemetri](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Pengurusan Maklumat Keselamatan dan Acara (SIEM)**

**Strategi Pembalakan Menyeluruh:**
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
- **Analitik Tingkah Laku Entiti (EBA)**: Pemantauan tingkah laku pelayan dan alat MCP
- **Pengesanan Anomali Pembelajaran Mesin**: Pengenalpastian ancaman keselamatan dikuasakan oleh AI
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

**Sokongan Penyiasatan:**
- **Pemeliharaan Jejak Audit**: Pembalakan tidak berubah dengan integriti kriptografi
- **Pengumpulan Bukti**: Pengumpulan automatik artifak keselamatan berkaitan
- **Pembinaan Semula Garis Masa**: Susunan terperinci acara yang membawa kepada insiden keselamatan
- **Penilaian Impak**: Penilaian skop kompromi dan pendedahan data

## **Prinsip Utama Seni Bina Keselamatan**

### **Pertahanan Berlapis**
- **Berbilang Lapisan Keselamatan**: Tiada titik kegagalan tunggal dalam seni bina keselamatan
- **Kawalan Redundan**: Langkah keselamatan bertindih untuk fungsi kritikal
- **Mekanisme Gagal Selamat**: Lalai selamat apabila sistem menghadapi ralat atau serangan

### **Pelaksanaan Kepercayaan Sifar**
- **Jangan Pernah Percaya, Sentiasa Sahkan**: Pengesahan berterusan semua entiti dan permintaan
- **Prinsip Hak Istimewa Terendah**: Hak akses minimum untuk semua komponen
- **Micro-segmentasi**: Kawalan rangkaian dan akses granular

### **Evolusi Keselamatan Berterusan**
- **Penyesuaian Lanskap Ancaman**: Kemas kini berkala untuk menangani ancaman yang muncul
- **Keberkesanan Kawalan Keselamatan**: Penilaian dan penambahbaikan berterusan kawalan
- **Pematuhan Spesifikasi**: Penyesuaian dengan piawaian keselamatan MCP yang berkembang

---

## **Sumber Pelaksanaan**

### **Dokumentasi Rasmi MCP**
- [Spesifikasi MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Amalan Terbaik Keselamatan MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Spesifikasi Kebenaran MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Sumber Keselamatan OWASP MCP**
- [Panduan Keselamatan OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/) - Top 10 OWASP MCP lengkap dengan pelaksanaan Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Risiko keselamatan rasmi OWASP MCP
- [Bengkel Sidang Kemuncak Keselamatan MCP (Sherpa)](https://azure-samples.github.io/sherpa/) - Latihan keselamatan praktikal untuk MCP di Azure

### **Penyelesaian Keselamatan Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Piawaian Keselamatan**
- [Amalan Terbaik Keselamatan OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Top 10 untuk Model Bahasa Besar](https://genai.owasp.org/)

- [Rangka Kerja Keselamatan Siber NIST](https://www.nist.gov/cyberframework)

---

> **Penting:** Kawalan keselamatan ini mencerminkan Spesifikasi MCP
> `2026-07-28`. Sentiasa sahkan dengan
> [dokumentasi rasmi terkini](https://modelcontextprotocol.io/specification/2026-07-28/)
> kerana piawaian terus berkembang.

## Apa Seterusnya

- Kembali ke: [Gambaran Keseluruhan Modul Keselamatan](./README.md)
- Teruskan ke: [Modul 3: Bermula](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->