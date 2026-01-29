# MCP Güvenlik En İyi Uygulamaları 2025

Bu kapsamlı rehber, Model Context Protocol (MCP) sistemlerinin uygulanması için en son **MCP Spesifikasyonu 2025-11-25** ve güncel sektör standartlarına dayalı temel güvenlik en iyi uygulamalarını özetlemektedir. Bu uygulamalar, hem geleneksel güvenlik endişelerini hem de MCP dağıtımlarına özgü yapay zeka (YZ) tehditlerini ele almaktadır.

## Kritik Güvenlik Gereksinimleri

### Zorunlu Güvenlik Kontrolleri (MUST Gereksinimleri)

1. **Token Doğrulama**: MCP sunucuları, açıkça yalnızca MCP sunucusu için verilmemiş herhangi bir tokenı KABUL ETMEMELİDİR  
2. **Yetkilendirme Doğrulaması**: Yetkilendirme uygulayan MCP sunucuları TÜM gelen istekleri doğrulamalı ve kimlik doğrulama için oturumları KULLANMAMALIDIR  
3. **Kullanıcı Onayı**: Statik istemci kimlikleri kullanan MCP proxy sunucuları, her dinamik kayıtlı istemci için açık kullanıcı onayı ALMALIDIR  
4. **Güvenli Oturum Kimlikleri**: MCP sunucuları, güvenli rastgele sayı üreteçleri ile oluşturulan kriptografik olarak güvenli, belirlenemez oturum kimlikleri KULLANMALIDIR

## Temel Güvenlik Uygulamaları

### 1. Girdi Doğrulama ve Temizleme
- **Kapsamlı Girdi Doğrulama**: Tüm girdileri doğrulayın ve temizleyin; enjeksiyon saldırılarını, karışıklık sorunlarını ve prompt enjeksiyonu açıklarını önleyin  
- **Parametre Şeması Uygulaması**: Tüm araç parametreleri ve API girdileri için katı JSON şeması doğrulaması uygulayın  
- **İçerik Filtreleme**: Microsoft Prompt Shields ve Azure Content Safety kullanarak promptlarda ve yanıtlar içinde kötü amaçlı içeriği filtreleyin  
- **Çıktı Temizleme**: Kullanıcılara veya alt sistemlere sunmadan önce tüm model çıktılarının doğrulanması ve temizlenmesi

### 2. Kimlik Doğrulama ve Yetkilendirme Mükemmelliği  
- **Dış Kimlik Sağlayıcıları**: Özel kimlik doğrulama uygulamak yerine Microsoft Entra ID, OAuth 2.1 sağlayıcıları gibi yerleşik kimlik sağlayıcılarına kimlik doğrulamasını devredin  
- **İnce Taneli İzinler**: En az ayrıcalık prensibine uygun, araç bazlı ayrıntılı izinler uygulayın  
- **Token Yaşam Döngüsü Yönetimi**: Kısa ömürlü erişim tokenları kullanın, güvenli döndürme ve uygun hedef doğrulaması yapın  
- **Çok Faktörlü Kimlik Doğrulama**: Tüm yönetim erişimleri ve hassas işlemler için MFA zorunlu kılın

### 3. Güvenli İletişim Protokolleri
- **Taşıma Katmanı Güvenliği**: Tüm MCP iletişimlerinde HTTPS/TLS 1.3 kullanın ve sertifika doğrulamasını doğru yapın  
- **Uçtan Uca Şifreleme**: Yolda ve depolamada yüksek hassasiyetli veriler için ek şifreleme katmanları uygulayın  
- **Sertifika Yönetimi**: Otomatik yenileme süreçleri ile uygun sertifika yaşam döngüsü yönetimi sağlayın  
- **Protokol Sürümü Uygulaması**: Güncel MCP protokol sürümü (2025-11-25) ile uygun sürüm müzakeresi yapın

### 4. Gelişmiş Oran Sınırlama ve Kaynak Koruma
- **Çok Katmanlı Oran Sınırlama**: Kullanıcı, oturum, araç ve kaynak seviyelerinde oran sınırlama uygulayarak kötüye kullanımı önleyin  
- **Uyarlanabilir Oran Sınırlama**: Kullanım desenlerine ve tehdit göstergelerine uyum sağlayan makine öğrenimi tabanlı oran sınırlama kullanın  
- **Kaynak Kota Yönetimi**: Hesaplama kaynakları, bellek kullanımı ve yürütme süresi için uygun sınırlar belirleyin  
- **DDoS Koruması**: Kapsamlı DDoS koruma ve trafik analiz sistemleri kurun

### 5. Kapsamlı Kayıt Tutma ve İzleme
- **Yapılandırılmış Denetim Kayıtları**: Tüm MCP işlemleri, araç yürütmeleri ve güvenlik olayları için ayrıntılı, aranabilir kayıtlar uygulayın  
- **Gerçek Zamanlı Güvenlik İzleme**: MCP iş yükleri için yapay zeka destekli anomali tespiti ile SIEM sistemleri kurun  
- **Gizlilik Uyumlu Kayıt Tutma**: Veri gizliliği gereksinimlerine ve düzenlemelere uygun şekilde güvenlik olaylarını kaydedin  
- **Olay Müdahale Entegrasyonu**: Kayıt sistemlerini otomatik olay müdahale iş akışlarına bağlayın

### 6. Gelişmiş Güvenli Depolama Uygulamaları
- **Donanım Güvenlik Modülleri**: Kritik kriptografik işlemler için HSM destekli anahtar depolama (Azure Key Vault, AWS CloudHSM) kullanın  
- **Şifreleme Anahtarı Yönetimi**: Anahtar döndürme, ayrıştırma ve erişim kontrollerini doğru uygulayın  
- **Gizli Bilgi Yönetimi**: Tüm API anahtarları, tokenlar ve kimlik bilgilerini özel gizli yönetim sistemlerinde saklayın  
- **Veri Sınıflandırması**: Verileri hassasiyet seviyelerine göre sınıflandırın ve uygun koruma önlemleri uygulayın

### 7. Gelişmiş Token Yönetimi
- **Token Geçişinin Önlenmesi**: Güvenlik kontrollerini atlayan token geçişi desenlerini açıkça yasaklayın  
- **Hedef Doğrulaması**: Token hedef iddialarının amaçlanan MCP sunucu kimliği ile eşleştiğini her zaman doğrulayın  
- **İddia Bazlı Yetkilendirme**: Token iddiaları ve kullanıcı özelliklerine dayalı ince taneli yetkilendirme uygulayın  
- **Token Bağlama**: Tokenları uygun durumlarda belirli oturumlara, kullanıcılara veya cihazlara bağlayın

### 8. Güvenli Oturum Yönetimi
- **Kriptografik Oturum Kimlikleri**: Oturum kimliklerini tahmin edilemeyen, kriptografik olarak güvenli rastgele sayı üreteçleri ile oluşturun  
- **Kullanıcıya Özel Bağlama**: Oturum kimliklerini `<user_id>:<session_id>` gibi güvenli formatlarla kullanıcıya özel bilgilerle bağlayın  
- **Oturum Yaşam Döngüsü Kontrolleri**: Uygun oturum süresi sonu, döndürme ve geçersiz kılma mekanizmaları uygulayın  
- **Oturum Güvenlik Başlıkları**: Oturum koruması için uygun HTTP güvenlik başlıkları kullanın

### 9. YZ’ye Özgü Güvenlik Kontrolleri
- **Prompt Enjeksiyonu Savunması**: Microsoft Prompt Shields ile spotlighting, ayırıcılar ve veri işaretleme teknikleri uygulayın  
- **Araç Zehirlenmesi Önleme**: Araç meta verilerini doğrulayın, dinamik değişiklikleri izleyin ve araç bütünlüğünü kontrol edin  
- **Model Çıktısı Doğrulaması**: Model çıktılarında olası veri sızıntısı, zararlı içerik veya güvenlik politikası ihlallerini tarayın  
- **Bağlam Penceresi Koruması**: Bağlam penceresi zehirlenmesi ve manipülasyon saldırılarını önlemek için kontroller uygulayın

### 10. Araç Yürütme Güvenliği
- **Yürütme Sandboxing’i**: Araç yürütmelerini konteynerize, izole ortamlarda ve kaynak sınırları ile çalıştırın  
- **Ayrıcalık Ayrımı**: Araçları minimum gerekli ayrıcalıklarla ve ayrı hizmet hesaplarıyla çalıştırın  
- **Ağ İzolasyonu**: Araç yürütme ortamları için ağ segmentasyonu uygulayın  
- **Yürütme İzleme**: Araç yürütmelerini anormal davranış, kaynak kullanımı ve güvenlik ihlalleri açısından izleyin

### 11. Sürekli Güvenlik Doğrulaması
- **Otomatik Güvenlik Testleri**: GitHub Advanced Security gibi araçlarla CI/CD boru hatlarına güvenlik testlerini entegre edin  
- **Zafiyet Yönetimi**: AI modelleri ve dış hizmetler dahil tüm bağımlılıkları düzenli olarak tarayın  
- **Sızma Testleri**: Özellikle MCP uygulamalarını hedef alan düzenli güvenlik değerlendirmeleri yapın  
- **Güvenlik Kod İncelemeleri**: Tüm MCP ile ilgili kod değişiklikleri için zorunlu güvenlik incelemeleri uygulayın

### 12. YZ için Tedarik Zinciri Güvenliği
- **Bileşen Doğrulaması**: Tüm YZ bileşenlerinin (modeller, gömme vektörleri, API’ler) kökenini, bütünlüğünü ve güvenliğini doğrulayın  
- **Bağımlılık Yönetimi**: Tüm yazılım ve YZ bağımlılıklarının güncel envanterini tutun ve zafiyet takibi yapın  
- **Güvenilir Depolar**: Tüm YZ modelleri, kütüphaneler ve araçlar için doğrulanmış, güvenilir kaynaklar kullanın  
- **Tedarik Zinciri İzleme**: YZ hizmet sağlayıcıları ve model depolarındaki ihlalleri sürekli izleyin

## Gelişmiş Güvenlik Desenleri

### MCP için Sıfır Güven Mimarisi
- **Asla Güvenme, Her Zaman Doğrula**: Tüm MCP katılımcıları için sürekli doğrulama uygulayın  
- **Mikro Segmentasyon**: MCP bileşenlerini ayrıntılı ağ ve kimlik kontrolleri ile izole edin  
- **Koşullu Erişim**: Bağlam ve davranışa uyum sağlayan risk tabanlı erişim kontrolleri uygulayın  
- **Sürekli Risk Değerlendirmesi**: Güncel tehdit göstergelerine göre güvenlik duruşunu dinamik olarak değerlendirin

### Gizliliği Koruyan YZ Uygulamaları
- **Veri Azaltma**: Her MCP işlemi için yalnızca gerekli minimum veriyi açığa çıkarın  
- **Diferansiyel Gizlilik**: Hassas veri işleme için gizliliği koruyan teknikler uygulayın  
- **Homomorfik Şifreleme**: Şifrelenmiş veriler üzerinde güvenli hesaplama için gelişmiş şifreleme teknikleri kullanın  
- **Federated Learning**: Veri yerelliğini ve gizliliğini koruyan dağıtık öğrenme yaklaşımları uygulayın

### YZ Sistemleri için Olay Müdahalesi
- **YZ’ye Özgü Olay Prosedürleri**: YZ ve MCP’ye özgü tehditlere yönelik olay müdahale prosedürleri geliştirin  
- **Otomatik Müdahale**: Yaygın YZ güvenlik olayları için otomatik sınırlama ve iyileştirme uygulayın  
- **Adli Bilişim Yetkinlikleri**: YZ sistem ihlalleri ve veri sızıntıları için adli bilişim hazırlığını sürdürün  
- **Kurtarma Prosedürleri**: YZ model zehirlenmesi, prompt enjeksiyonu saldırıları ve hizmet ihlallerinden kurtulma prosedürleri oluşturun

## Uygulama Kaynakları ve Standartlar

### Resmi MCP Dokümantasyonu
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Güncel MCP protokol spesifikasyonu  
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Resmi güvenlik rehberi  
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Kimlik doğrulama ve yetkilendirme desenleri  
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Taşıma katmanı güvenlik gereksinimleri

### Microsoft Güvenlik Çözümleri
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Gelişmiş prompt enjeksiyonu koruması  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Kapsamlı YZ içerik filtreleme  
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Kurumsal kimlik ve erişim yönetimi  
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Güvenli gizli ve kimlik bilgisi yönetimi  
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Tedarik zinciri ve kod güvenliği taraması

### Güvenlik Standartları ve Çerçeveleri
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Güncel OAuth güvenlik rehberi  
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Web uygulaması güvenlik riskleri  
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - YZ’ye özgü güvenlik riskleri  
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Kapsamlı YZ risk yönetimi  
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Bilgi güvenliği yönetim sistemleri

### Uygulama Kılavuzları ve Eğitimler
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Kurumsal kimlik doğrulama desenleri  
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Kimlik sağlayıcı entegrasyonu  
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Token yönetimi en iyi uygulamaları  
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Gelişmiş şifreleme desenleri

### Gelişmiş Güvenlik Kaynakları
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Güvenli geliştirme uygulamaları  
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - YZ’ye özgü güvenlik testleri  
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - YZ tehdit modelleme metodolojisi  
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Gizliliği koruyan YZ teknikleri

### Uyumluluk ve Yönetişim
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - YZ sistemlerinde gizlilik uyumu  
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Sorumlu YZ uygulaması  
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - YZ hizmet sağlayıcıları için güvenlik kontrolleri  
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Sağlık sektörü YZ uyumluluk gereksinimleri

### DevSecOps ve Otomasyon
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Güvenli YZ geliştirme boru hatları  
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Sürekli güvenlik doğrulaması  
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Güvenli altyapı dağıtımı  
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - YZ iş yükü konteyner güvenliği

### İzleme ve Olay Müdahalesi  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Kapsamlı izleme çözümleri  
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - YZ’ye özgü olay prosedürleri  
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Güvenlik bilgi ve olay yönetimi  
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - YZ tehdit istihbarat kaynakları

## 🔄 Sürekli İyileştirme

### Gelişen Standartları Takip Edin
- **MCP Spesifikasyon Güncellemeleri**: Resmi MCP spesifikasyon değişikliklerini ve güvenlik duyurularını izleyin  
- **Tehdit İstihbaratı**: YZ güvenlik tehdit beslemelerine ve zafiyet veritabanlarına abone olun  
- **Topluluk Katılımı**: MCP güvenlik topluluğu tartışmalarına ve çalışma gruplarına katılın  
- **Düzenli Değerlendirme**: Üç aylık güvenlik duruşu değerlendirmeleri yapın ve uygulamaları güncelleyin

### MCP Güvenliğine Katkıda Bulunun
- **Güvenlik Araştırmaları**: MCP güvenlik araştırmalarına ve zafiyet açıklama programlarına katkı sağlayın  
- **En İyi Uygulama Paylaşımı**: Güvenlik uygulamalarını ve edinilen dersleri toplulukla paylaşın
- **Standart Geliştirme**: MCP spesifikasyon geliştirme ve güvenlik standardı oluşturma süreçlerine katılmak  
- **Araç Geliştirme**: MCP ekosistemi için güvenlik araçları ve kütüphaneleri geliştirmek ve paylaşmak  

---

*Bu belge, MCP Spesifikasyonu 2025-11-25'e dayanarak 18 Aralık 2025 itibarıyla MCP güvenlik en iyi uygulamalarını yansıtmaktadır. Güvenlik uygulamaları, protokol ve tehdit ortamı geliştikçe düzenli olarak gözden geçirilmeli ve güncellenmelidir.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->