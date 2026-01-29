# MCP Güvenlik Kontrolleri - Aralık 2025 Güncellemesi

> **Mevcut Standart**: Bu belge, [MCP Spesifikasyonu 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) güvenlik gereksinimlerini ve resmi [MCP Güvenlik En İyi Uygulamaları](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) yansıtıyor.

Model Context Protocol (MCP), hem geleneksel yazılım güvenliği hem de AI'ya özgü tehditleri ele alan gelişmiş güvenlik kontrolleriyle önemli ölçüde olgunlaştı. Bu belge, Aralık 2025 itibarıyla güvenli MCP uygulamaları için kapsamlı güvenlik kontrolleri sağlar.

## **ZORUNLU Güvenlik Gereksinimleri**

### **MCP Spesifikasyonundan Kritik Yasaklar:**

> **YASAK**: MCP sunucuları, açıkça MCP sunucusu için verilmemiş herhangi bir tokenı KABUL ETMEMELİDİR  
>
> **YASAK**: MCP sunucuları kimlik doğrulama için oturumları KULLANMAMALIDIR  
>
> **GEREKLİ**: Yetkilendirme uygulayan MCP sunucuları TÜM gelen istekleri doğrulamalıdır  
>
> **ZORUNLU**: Statik istemci kimlikleri kullanan MCP proxy sunucuları, her dinamik kayıtlı istemci için kullanıcı onayı ALMALIDIR

---

## 1. **Kimlik Doğrulama ve Yetkilendirme Kontrolleri**

### **Harici Kimlik Sağlayıcı Entegrasyonu**

**Mevcut MCP Standardı (2025-06-18)**, MCP sunucularının kimlik doğrulamayı harici kimlik sağlayıcılarına devretmesine izin verir ve bu önemli bir güvenlik iyileştirmesidir:

### **Harici Kimlik Sağlayıcı Entegrasyonu**

**Mevcut MCP Standardı (2025-11-25)**, MCP sunucularının kimlik doğrulamayı harici kimlik sağlayıcılarına devretmesine izin verir ve bu önemli bir güvenlik iyileştirmesidir:

**Güvenlik Faydaları:**
1. **Özel Kimlik Doğrulama Risklerini Ortadan Kaldırır**: Özel kimlik doğrulama uygulamalarından kaynaklanan zafiyet yüzeyini azaltır  
2. **Kurumsal Düzeyde Güvenlik**: Microsoft Entra ID gibi gelişmiş güvenlik özelliklerine sahip köklü kimlik sağlayıcılarını kullanır  
3. **Merkezi Kimlik Yönetimi**: Kullanıcı yaşam döngüsü yönetimi, erişim kontrolü ve uyumluluk denetimini basitleştirir  
4. **Çok Faktörlü Kimlik Doğrulama**: Kurumsal kimlik sağlayıcılarından MFA yeteneklerini devralır  
5. **Koşullu Erişim Politikaları**: Risk tabanlı erişim kontrolleri ve uyarlanabilir kimlik doğrulamadan faydalanır

**Uygulama Gereksinimleri:**
- **Token Hedef Kitle Doğrulaması**: Tüm tokenların açıkça MCP sunucusu için verilmiş olduğunu doğrulayın  
- **Yayıncı Doğrulaması**: Token yayıncısının beklenen kimlik sağlayıcı ile eşleştiğini doğrulayın  
- **İmza Doğrulaması**: Token bütünlüğünün kriptografik doğrulaması  
- **Süre Sonu Uygulaması**: Token ömrü sınırlarının sıkı uygulanması  
- **Kapsam Doğrulaması**: Tokenların istenen işlemler için uygun izinleri içerdiğinden emin olun

### **Yetkilendirme Mantığı Güvenliği**

**Kritik Kontroller:**
- **Kapsamlı Yetkilendirme Denetimleri**: Tüm yetkilendirme karar noktalarının düzenli güvenlik incelemeleri  
- **Hata Durumunda Güvenli Varsayılanlar**: Yetkilendirme mantığı kesin karar veremediğinde erişimi reddet  
- **İzin Sınırları**: Farklı ayrıcalık seviyeleri ve kaynak erişimi arasında net ayrım  
- **Denetim Kaydı**: Tüm yetkilendirme kararlarının güvenlik izleme için tam kaydı  
- **Düzenli Erişim İncelemeleri**: Kullanıcı izinleri ve ayrıcalık atamalarının periyodik doğrulaması

## 2. **Token Güvenliği ve Anti-Passthrough Kontrolleri**

### **Token Passthrough Önleme**

**Token passthrough MCP Yetkilendirme Spesifikasyonunda açıkça yasaktır** çünkü kritik güvenlik riskleri taşır:

**Ele Alınan Güvenlik Riskleri:**
- **Kontrol Atlatma**: Oran sınırlama, istek doğrulama ve trafik izleme gibi temel güvenlik kontrollerini atlar  
- **Hesap Verebilirlik Bozulması**: İstemci tanımlamasını imkansız hale getirir, denetim izlerini ve olay soruşturmalarını bozar  
- **Proxy Tabanlı Veri Çıkarma**: Kötü niyetli aktörlerin sunucuları yetkisiz veri erişimi için proxy olarak kullanmasına olanak tanır  
- **Güven Sınırı İhlalleri**: Alt hizmetlerin token kökenleri hakkındaki güven varsayımlarını bozar  
- **Yanal Hareket**: Birden fazla hizmette ele geçirilmiş tokenlar daha geniş saldırı yayılımına izin verir

**Uygulama Kontrolleri:**
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

### **Güvenli Token Yönetimi Desenleri**

**En İyi Uygulamalar:**
- **Kısa Ömürlü Tokenlar**: Sık token rotasyonu ile maruz kalma süresini minimize edin  
- **Tam Zamanında Verme**: Tokenları yalnızca belirli işlemler için gerektiğinde verin  
- **Güvenli Depolama**: Donanım güvenlik modülleri (HSM) veya güvenli anahtar kasaları kullanın  
- **Token Bağlama**: Mümkünse tokenları belirli istemcilere, oturumlara veya işlemlere bağlayın  
- **İzleme ve Uyarı**: Token kötüye kullanımı veya yetkisiz erişim kalıplarının gerçek zamanlı tespiti

## 3. **Oturum Güvenliği Kontrolleri**

### **Oturum Kaçırma Önleme**

**Ele Alınan Saldırı Vektörleri:**
- **Oturum Kaçırma Prompt Enjeksiyonu**: Paylaşılan oturum durumuna kötü niyetli olayların enjekte edilmesi  
- **Oturum Taklidi**: Çalınan oturum kimliklerinin yetkisiz kullanımı ile kimlik doğrulamanın atlatılması  
- **Devam Ettirilebilir Akış Saldırıları**: Sunucu tarafından gönderilen olayların devam ettirilmesi yoluyla kötü amaçlı içerik enjeksiyonu

**Zorunlu Oturum Kontrolleri:**
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

**İletim Güvenliği:**
- **HTTPS Zorunluluğu**: Tüm oturum iletişimi TLS 1.3 üzerinden  
- **Güvenli Çerez Özellikleri**: HttpOnly, Secure, SameSite=Strict  
- **Sertifika Sabitleme**: MITM saldırılarını önlemek için kritik bağlantılarda

### **Durumlu ve Durumsuz Düşünceler**

**Durumlu Uygulamalar İçin:**
- Paylaşılan oturum durumu enjeksiyon saldırılarına karşı ek koruma gerektirir  
- Kuyruk tabanlı oturum yönetimi bütünlük doğrulaması gerektirir  
- Birden fazla sunucu örneği güvenli oturum durumu senkronizasyonu gerektirir

**Durumsuz Uygulamalar İçin:**
- JWT veya benzeri token tabanlı oturum yönetimi  
- Oturum durumu bütünlüğünün kriptografik doğrulaması  
- Azaltılmış saldırı yüzeyi ancak sağlam token doğrulaması gerektirir

## 4. **AI'ya Özgü Güvenlik Kontrolleri**

### **Prompt Enjeksiyon Savunması**

**Microsoft Prompt Shields Entegrasyonu:**
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

**Uygulama Kontrolleri:**
- **Girdi Temizleme**: Tüm kullanıcı girdilerinin kapsamlı doğrulaması ve filtrelenmesi  
- **İçerik Sınırı Tanımı**: Sistem talimatları ile kullanıcı içeriği arasında net ayrım  
- **Talimat Hiyerarşisi**: Çelişen talimatlar için uygun öncelik kuralları  
- **Çıktı İzleme**: Potansiyel zararlı veya manipüle edilmiş çıktılarının tespiti

### **Araç Zehirlenmesi Önleme**

**Araç Güvenlik Çerçevesi:**
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

**Dinamik Araç Yönetimi:**
- **Onay İş Akışları**: Araç değişiklikleri için açık kullanıcı onayı  
- **Geri Alma Yeteneği**: Önceki araç sürümlerine geri dönme imkanı  
- **Değişiklik Denetimi**: Araç tanımı değişikliklerinin tam geçmişi  
- **Risk Değerlendirmesi**: Araç güvenlik duruşunun otomatik değerlendirmesi

## 5. **Confused Deputy Saldırısı Önleme**

### **OAuth Proxy Güvenliği**

**Saldırı Önleme Kontrolleri:**
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

**Uygulama Gereksinimleri:**
- **Kullanıcı Onayı Doğrulaması**: Dinamik istemci kaydı için onay ekranlarını asla atlamayın  
- **Yönlendirme URI Doğrulaması**: Yönlendirme hedeflerinin sıkı beyaz liste tabanlı doğrulaması  
- **Yetkilendirme Kodu Koruması**: Kısa ömürlü ve tek kullanımlık kodlar  
- **İstemci Kimlik Doğrulaması**: İstemci kimlik bilgileri ve meta verilerinin sağlam doğrulaması

## 6. **Araç Çalıştırma Güvenliği**

### **Sandboxing ve İzolasyon**

**Konteyner Tabanlı İzolasyon:**
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

**Süreç İzolasyonu:**
- **Ayrı Süreç Bağlamları**: Her araç çalıştırma izole süreç alanında  
- **Süreçler Arası İletişim**: Doğrulamalı güvenli IPC mekanizmaları  
- **Süreç İzleme**: Çalışma zamanı davranış analizi ve anomali tespiti  
- **Kaynak Kısıtlamaları**: CPU, bellek ve G/Ç işlemlerinde sert sınırlar

### **En Az Ayrıcalık Uygulaması**

**İzin Yönetimi:**
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

## 7. **Tedarik Zinciri Güvenlik Kontrolleri**

### **Bağımlılık Doğrulaması**

**Kapsamlı Bileşen Güvenliği:**
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

### **Sürekli İzleme**

**Tedarik Zinciri Tehdit Tespiti:**
- **Bağımlılık Sağlık İzleme**: Tüm bağımlılıkların güvenlik sorunları için sürekli değerlendirilmesi  
- **Tehdit İstihbaratı Entegrasyonu**: Ortaya çıkan tedarik zinciri tehditlerine gerçek zamanlı güncellemeler  
- **Davranışsal Analiz**: Dış bileşenlerde olağandışı davranış tespiti  
- **Otomatik Müdahale**: Ele geçirilmiş bileşenlerin anında kontrol altına alınması

## 8. **İzleme ve Tespit Kontrolleri**

### **Güvenlik Bilgi ve Olay Yönetimi (SIEM)**

**Kapsamlı Kayıt Stratejisi:**
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

### **Gerçek Zamanlı Tehdit Tespiti**

**Davranışsal Analitik:**
- **Kullanıcı Davranış Analitiği (UBA)**: Olağandışı kullanıcı erişim kalıplarının tespiti  
- **Varlık Davranış Analitiği (EBA)**: MCP sunucusu ve araç davranışlarının izlenmesi  
- **Makine Öğrenimi Anomali Tespiti**: AI destekli güvenlik tehditlerinin tanımlanması  
- **Tehdit İstihbaratı Korelasyonu**: Gözlemlenen faaliyetlerin bilinen saldırı kalıplarıyla eşleştirilmesi

## 9. **Olay Müdahalesi ve Kurtarma**

### **Otomatik Müdahale Yetkinlikleri**

**Anında Müdahale Eylemleri:**
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

### **Adli Bilişim Yetkinlikleri**

**Soruşturma Desteği:**
- **Denetim İzinin Korunması**: Kriptografik bütünlük ile değiştirilemez kayıtlar  
- **Delil Toplama**: İlgili güvenlik kanıtlarının otomatik toplanması  
- **Zaman Çizelgesi Yeniden İnşası**: Güvenlik olaylarına yol açan olayların ayrıntılı sıralaması  
- **Etkilenme Değerlendirmesi**: İhlal kapsamı ve veri maruziyetinin değerlendirilmesi

## **Temel Güvenlik Mimari İlkeleri**

### **Derin Savunma**
- **Çok Katmanlı Güvenlik**: Güvenlik mimarisinde tek hata noktası yok  
- **Yedekli Kontroller**: Kritik işlevler için örtüşen güvenlik önlemleri  
- **Hata Durumunda Güvenli Mekanizmalar**: Sistemler hata veya saldırı durumunda güvenli varsayılanlar

### **Sıfır Güven Uygulaması**
- **Asla Güvenme, Sürekli Doğrula**: Tüm varlıkların ve isteklerin sürekli doğrulanması  
- **En Az Ayrıcalık İlkesi**: Tüm bileşenler için minimum erişim hakları  
- **Mikro Segmentasyon**: Ayrıntılı ağ ve erişim kontrolleri

### **Sürekli Güvenlik Evrimi**
- **Tehdit Ortamına Uyum**: Ortaya çıkan tehditlere düzenli güncellemeler  
- **Güvenlik Kontrol Etkinliği**: Kontrollerin sürekli değerlendirilmesi ve iyileştirilmesi  
- **Spesifikasyon Uyumu**: Gelişen MCP güvenlik standartlarıyla uyum

---

## **Uygulama Kaynakları**

### **Resmi MCP Dokümantasyonu**
- [MCP Spesifikasyonu (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Güvenlik En İyi Uygulamaları](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Yetkilendirme Spesifikasyonu](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft Güvenlik Çözümleri**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Güvenlik Standartları**
- [OAuth 2.0 Güvenlik En İyi Uygulamaları (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [Büyük Dil Modelleri için OWASP Top 10](https://genai.owasp.org/)
- [NIST Siber Güvenlik Çerçevesi](https://www.nist.gov/cyberframework)

---

> **Önemli**: Bu güvenlik kontrolleri mevcut MCP spesifikasyonunu (2025-06-18) yansıtmaktadır. Standartlar hızla gelişmeye devam ettiğinden her zaman en güncel [resmi dokümantasyon](https://spec.modelcontextprotocol.io/) ile doğrulayınız.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->