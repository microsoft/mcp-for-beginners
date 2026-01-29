# MCP Güvenlik En İyi Uygulamaları - Aralık 2025 Güncellemesi

> **Önemli**: Bu belge, en son [MCP Spesifikasyonu 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) güvenlik gereksinimlerini ve resmi [MCP Güvenlik En İyi Uygulamaları](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) yansıtıyor. En güncel rehberlik için her zaman mevcut spesifikasyona başvurun.

## MCP Uygulamaları için Temel Güvenlik Uygulamaları

Model Context Protocol, geleneksel yazılım güvenliğinin ötesine geçen benzersiz güvenlik zorlukları sunar. Bu uygulamalar, temel güvenlik gereksinimlerinin yanı sıra prompt enjeksiyonu, araç zehirlenmesi, oturum kaçırma, karışık vekil problemleri ve token geçişi açıkları gibi MCP'ye özgü tehditleri ele alır.

### **ZORUNLU Güvenlik Gereksinimleri**

**MCP Spesifikasyonundan Kritik Gereksinimler:**

### **ZORUNLU Güvenlik Gereksinimleri**

**MCP Spesifikasyonundan Kritik Gereksinimler:**

> **KABUL EDİLEMEZ**: MCP sunucuları, açıkça MCP sunucusu için verilmemiş herhangi bir tokenı **KABUL ETMEMELİDİR**
> 
> **GEREKLİDİR**: Yetkilendirme uygulayan MCP sunucuları, TÜM gelen istekleri doğrulamalıdır
>  
> **KABUL EDİLEMEZ**: MCP sunucuları kimlik doğrulama için oturumları kullanmamalıdır
>
> **GEREKLİDİR**: Statik istemci kimlikleri kullanan MCP proxy sunucuları, her dinamik kayıtlı istemci için kullanıcı onayı almalıdır

---

## 1. **Token Güvenliği ve Kimlik Doğrulama**

**Kimlik Doğrulama ve Yetkilendirme Kontrolleri:**
   - **Titiz Yetkilendirme İncelemesi**: MCP sunucu yetkilendirme mantığını kapsamlı denetimlerle sadece amaçlanan kullanıcılar ve istemcilerin kaynaklara erişmesini sağlayın
   - **Dış Kimlik Sağlayıcı Entegrasyonu**: Özel kimlik doğrulama uygulamak yerine Microsoft Entra ID gibi yerleşik kimlik sağlayıcıları kullanın
   - **Token Hedef Kitle Doğrulaması**: Tokenların açıkça MCP sunucunuz için verildiğini her zaman doğrulayın - asla yukarı akış tokenlarını kabul etmeyin
   - **Uygun Token Yaşam Döngüsü**: Güvenli token rotasyonu, sona erme politikaları uygulayın ve token tekrar saldırılarını önleyin

**Korunan Token Depolama:**
   - Tüm gizli bilgileri Azure Key Vault veya benzeri güvenli kimlik bilgisi depolarında saklayın
   - Tokenları hem dinlenme hem de iletim sırasında şifreleyin
   - Yetkisiz erişim için düzenli kimlik bilgisi rotasyonu ve izleme yapın

## 2. **Oturum Yönetimi ve Taşıma Güvenliği**

**Güvenli Oturum Uygulamaları:**
   - **Kriptografik Olarak Güvenli Oturum Kimlikleri**: Güvenli, belirlenemez oturum kimlikleri oluşturmak için güvenli rastgele sayı üreteçleri kullanın
   - **Kullanıcıya Özel Bağlama**: Oturum kimliklerini `<user_id>:<session_id>` gibi formatlarla kullanıcı kimliklerine bağlayarak kullanıcılar arası oturum kötüye kullanımını önleyin
   - **Oturum Yaşam Döngüsü Yönetimi**: Zafiyet pencerelerini sınırlamak için uygun sona erme, rotasyon ve geçersiz kılma uygulayın
   - **HTTPS/TLS Zorunluluğu**: Oturum kimliği yakalanmasını önlemek için tüm iletişimde HTTPS zorunlu kılın

**Taşıma Katmanı Güvenliği:**
   - Mümkün olduğunda TLS 1.3 yapılandırması ve uygun sertifika yönetimi uygulayın
   - Kritik bağlantılar için sertifika pinleme uygulayın
   - Düzenli sertifika rotasyonu ve geçerlilik doğrulaması yapın

## 3. **Yapay Zeka Özel Tehdit Koruması** 🤖

**Prompt Enjeksiyonu Savunması:**
   - **Microsoft Prompt Shields**: Kötü niyetli talimatların gelişmiş tespiti ve filtrelenmesi için AI Prompt Shields kullanın
   - **Girdi Temizleme**: Tüm girdileri doğrulayın ve temizleyin, enjeksiyon saldırılarını ve karışık vekil problemlerini önleyin
   - **İçerik Sınırları**: Güvenilir talimatlar ile dış içerik arasındaki ayrımı sağlamak için ayırıcı ve veri işaretleme sistemleri kullanın

**Araç Zehirlenmesi Önleme:**
   - **Araç Meta Verisi Doğrulaması**: Araç tanımları için bütünlük kontrolleri uygulayın ve beklenmeyen değişiklikleri izleyin
   - **Dinamik Araç İzleme**: Çalışma zamanı davranışını izleyin ve beklenmeyen yürütme kalıpları için uyarı kurun
   - **Onay İş Akışları**: Araç değişiklikleri ve yetenek değişiklikleri için açık kullanıcı onayı gerektirin

## 4. **Erişim Kontrolü ve İzinler**

**En Az Ayrıcalık İlkesi:**
   - MCP sunucularına yalnızca amaçlanan işlevsellik için gereken minimum izinleri verin
   - İnce taneli izinlerle rol tabanlı erişim kontrolü (RBAC) uygulayın
   - Düzenli izin incelemeleri ve ayrıcalık yükseltme için sürekli izleme yapın

**Çalışma Zamanı İzin Kontrolleri:**
   - Kaynak tükenme saldırılarını önlemek için kaynak sınırları uygulayın
   - Araç yürütme ortamları için konteyner izolasyonu kullanın  
   - Yönetim işlevleri için tam zamanında erişim uygulayın

## 5. **İçerik Güvenliği ve İzleme**

**İçerik Güvenliği Uygulaması:**
   - **Azure Content Safety Entegrasyonu**: Zararlı içerik, jailbreak girişimleri ve politika ihlallerini tespit etmek için Azure Content Safety kullanın
   - **Davranışsal Analiz**: MCP sunucu ve araç yürütme sırasında anormallikleri tespit etmek için çalışma zamanı davranış izleme uygulayın
   - **Kapsamlı Kayıt Tutma**: Tüm kimlik doğrulama denemeleri, araç çağrıları ve güvenlik olaylarını güvenli, değiştirilemez depolama ile kaydedin

**Sürekli İzleme:**
   - Şüpheli kalıplar ve yetkisiz erişim girişimleri için gerçek zamanlı uyarılar  
   - Merkezi güvenlik olay yönetimi için SIEM sistemleri ile entegrasyon
   - MCP uygulamalarının düzenli güvenlik denetimleri ve penetrasyon testleri

## 6. **Tedarik Zinciri Güvenliği**

**Bileşen Doğrulaması:**
   - Tüm yazılım bağımlılıkları ve AI bileşenleri için otomatik zafiyet taraması kullanın
   - Modellerin, veri kaynaklarının ve dış hizmetlerin kökenini, lisansını ve bütünlüğünü doğrulayın
   - Kriptografik olarak imzalanmış paketler kullanın ve dağıtımdan önce imzaları doğrulayın

**Güvenli Geliştirme Hattı:**
   - **GitHub Advanced Security**: Gizli tarama, bağımlılık analizi ve CodeQL statik analiz uygulayın
   - **CI/CD Güvenliği**: Otomatik dağıtım hatlarında güvenlik doğrulamasını entegre edin
   - **Artefakt Bütünlüğü**: Dağıtılan artefaktlar ve yapılandırmalar için kriptografik doğrulama uygulayın

## 7. **OAuth Güvenliği ve Karışık Vekil Önleme**

**OAuth 2.1 Uygulaması:**
   - Tüm yetkilendirme istekleri için Proof Key for Code Exchange (PKCE) kullanın
   - Karışık vekil saldırılarını önlemek için her dinamik kayıtlı istemci için açık kullanıcı onayı alın
   - Yönlendirme URI'ları ve istemci kimlikleri için sıkı doğrulama uygulayın

**Proxy Güvenliği:**
   - Statik istemci kimliği kötüye kullanımı yoluyla yetkilendirme atlamasını önleyin
   - Üçüncü taraf API erişimi için uygun onay iş akışları uygulayın
   - Yetkilendirme kodu hırsızlığı ve yetkisiz API erişimini izleyin

## 8. **Olay Müdahalesi ve Kurtarma**

**Hızlı Müdahale Yetkinlikleri:**
   - Kimlik bilgisi rotasyonu ve tehdit sınırlaması için otomatik sistemler uygulayın
   - Bilinen iyi yapılandırmalara ve bileşenlere hızlı geri dönüş yeteneği
   - Olay soruşturması için ayrıntılı denetim izleri ve kayıtlar

**İletişim ve Koordinasyon:**
   - Güvenlik olayları için net yükseltme prosedürleri
   - Kurumsal olay müdahale ekipleri ile entegrasyon
   - Düzenli güvenlik olayı simülasyonları ve masaüstü tatbikatları

## 9. **Uyumluluk ve Yönetişim**

**Düzenleyici Uyumluluk:**
   - MCP uygulamalarının sektör spesifik gereksinimleri (GDPR, HIPAA, SOC 2) karşıladığından emin olun
   - AI veri işleme için veri sınıflandırması ve gizlilik kontrolleri uygulayın
   - Uyumluluk denetimleri için kapsamlı dokümantasyon tutun

**Değişiklik Yönetimi:**
   - Tüm MCP sistem değişiklikleri için resmi güvenlik inceleme süreçleri
   - Yapılandırma değişiklikleri için sürüm kontrolü ve onay iş akışları
   - Düzenli uyumluluk değerlendirmeleri ve boşluk analizi

## 10. **Gelişmiş Güvenlik Kontrolleri**

**Sıfır Güven Mimarisi:**
   - **Asla Güvenme, Her Zaman Doğrula**: Kullanıcılar, cihazlar ve bağlantıların sürekli doğrulanması
   - **Mikro-segmentasyon**: Bireysel MCP bileşenlerini izole eden ayrıntılı ağ kontrolleri
   - **Koşullu Erişim**: Mevcut bağlam ve davranışa uyum sağlayan risk tabanlı erişim kontrolleri

**Çalışma Zamanı Uygulama Koruması:**
   - **Çalışma Zamanı Uygulama Kendi Kendini Koruma (RASP)**: Gerçek zamanlı tehdit tespiti için RASP teknikleri uygulayın
   - **Uygulama Performans İzleme**: Saldırıları gösterebilecek performans anormalliklerini izleyin
   - **Dinamik Güvenlik Politikaları**: Mevcut tehdit ortamına göre uyum sağlayan güvenlik politikaları uygulayın

## 11. **Microsoft Güvenlik Ekosistemi Entegrasyonu**

**Kapsamlı Microsoft Güvenliği:**
   - **Microsoft Defender for Cloud**: MCP iş yükleri için bulut güvenlik durumu yönetimi
   - **Azure Sentinel**: Gelişmiş tehdit tespiti için bulut yerel SIEM ve SOAR yetenekleri
   - **Microsoft Purview**: AI iş akışları ve veri kaynakları için veri yönetişimi ve uyumluluk

**Kimlik ve Erişim Yönetimi:**
   - **Microsoft Entra ID**: Koşullu erişim politikaları ile kurumsal kimlik yönetimi
   - **Ayrıcalıklı Kimlik Yönetimi (PIM)**: Yönetim işlevleri için tam zamanında erişim ve onay iş akışları
   - **Kimlik Koruma**: Risk tabanlı koşullu erişim ve otomatik tehdit yanıtı

## 12. **Sürekli Güvenlik Evrimi**

**Güncel Kalma:**
   - **Spesifikasyon İzleme**: MCP spesifikasyon güncellemeleri ve güvenlik rehberi değişikliklerini düzenli inceleme
   - **Tehdit İstihbaratı**: AI'ya özgü tehdit beslemeleri ve ihlal göstergelerinin entegrasyonu
   - **Güvenlik Topluluğu Katılımı**: MCP güvenlik topluluğu ve zafiyet açıklama programlarına aktif katılım

**Uyarlanabilir Güvenlik:**
   - **Makine Öğrenimi Güvenliği**: Yeni saldırı kalıplarını tanımlamak için ML tabanlı anomali tespiti kullanımı
   - **Öngörücü Güvenlik Analitiği**: Proaktif tehdit tanımlaması için öngörücü modeller uygulama
   - **Güvenlik Otomasyonu**: Tehdit istihbaratı ve spesifikasyon değişikliklerine dayalı otomatik güvenlik politikası güncellemeleri

---

## **Kritik Güvenlik Kaynakları**

### **Resmi MCP Dokümantasyonu**
- [MCP Spesifikasyonu (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Güvenlik En İyi Uygulamaları](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Yetkilendirme Spesifikasyonu](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft Güvenlik Çözümleri**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Güvenliği](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Güvenlik Standartları**
- [OAuth 2.0 Güvenlik En İyi Uygulamaları (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [Büyük Dil Modelleri için OWASP Top 10](https://genai.owasp.org/)
- [NIST AI Risk Yönetim Çerçevesi](https://www.nist.gov/itl/ai-risk-management-framework)

### **Uygulama Kılavuzları**
- [Azure API Management MCP Kimlik Doğrulama Geçidi](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID ile MCP Sunucuları](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Güvenlik Uyarısı**: MCP güvenlik uygulamaları hızla evrilmektedir. Uygulamadan önce her zaman mevcut [MCP spesifikasyonu](https://spec.modelcontextprotocol.io/) ve [resmi güvenlik dokümantasyonu](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) ile doğrulayın.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->