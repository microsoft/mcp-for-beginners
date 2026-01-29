# Değişiklik Günlüğü: Yeni Başlayanlar için MCP Müfredatı

Bu belge, Model Context Protocol (MCP) için Yeni Başlayanlar müfredatında yapılan tüm önemli değişikliklerin kaydıdır. Değişiklikler ters kronolojik sırayla (en yeni değişiklikler önce) belgelenmiştir.

## 18 Aralık 2025

### Güvenlik Dokümantasyonu Güncellemesi - MCP Spesifikasyonu 2025-11-25

#### MCP Güvenlik En İyi Uygulamaları (02-Security/mcp-best-practices.md) - Spesifikasyon Sürümü Güncellemesi
- **Protokol Sürümü Güncellemesi**: En son MCP Spesifikasyonu 2025-11-25 (25 Kasım 2025'te yayınlandı) referans alındı
  - Tüm spesifikasyon sürüm referansları 2025-06-18’den 2025-11-25’e güncellendi
  - Belge tarih referansları 18 Ağustos 2025’ten 18 Aralık 2025’e güncellendi
  - Tüm spesifikasyon URL’lerinin güncel dokümantasyona işaret ettiği doğrulandı
- **İçerik Doğrulaması**: Güvenlik en iyi uygulamalarının en son standartlara göre kapsamlı doğrulaması yapıldı
  - **Microsoft Güvenlik Çözümleri**: Prompt Shields (önceden "Jailbreak risk tespiti"), Azure Content Safety, Microsoft Entra ID ve Azure Key Vault için güncel terimler ve bağlantılar doğrulandı
  - **OAuth 2.1 Güvenliği**: En son OAuth güvenlik en iyi uygulamaları ile uyum teyit edildi
  - **OWASP Standartları**: LLM’ler için OWASP Top 10 referanslarının güncel olduğu doğrulandı
  - **Azure Hizmetleri**: Tüm Microsoft Azure dokümantasyon bağlantıları ve en iyi uygulamalar doğrulandı
- **Standartlarla Uyum**: Referans verilen tüm güvenlik standartlarının güncel olduğu teyit edildi
  - NIST AI Risk Yönetimi Çerçevesi
  - ISO 27001:2022
  - OAuth 2.1 Güvenlik En İyi Uygulamaları
  - Azure güvenlik ve uyumluluk çerçeveleri
- **Uygulama Kaynakları**: Tüm uygulama kılavuzu bağlantıları ve kaynaklar doğrulandı
  - Azure API Yönetimi kimlik doğrulama desenleri
  - Microsoft Entra ID entegrasyon kılavuzları
  - Azure Key Vault gizli yönetimi
  - DevSecOps boru hatları ve izleme çözümleri

### Dokümantasyon Kalite Güvencesi
- **Spesifikasyon Uyumu**: Tüm zorunlu MCP güvenlik gereksinimlerinin (MUST/MUST NOT) en son spesifikasyonla uyumlu olduğu sağlandı
- **Kaynak Güncelliği**: Microsoft dokümantasyonu, güvenlik standartları ve uygulama kılavuzlarına tüm dış bağlantılar doğrulandı
- **En İyi Uygulamalar Kapsamı**: Kimlik doğrulama, yetkilendirme, yapay zekaya özgü tehditler, tedarik zinciri güvenliği ve kurumsal desenlerin kapsamlı şekilde ele alındığı teyit edildi

## 6 Ekim 2025

### Başlarken Bölümü Genişletmesi – Gelişmiş Sunucu Kullanımı & Basit Kimlik Doğrulama

#### Gelişmiş Sunucu Kullanımı (03-GettingStarted/10-advanced)
- **Yeni Bölüm Eklendi**: Hem düzenli hem de düşük seviyeli sunucu mimarilerini kapsayan kapsamlı bir gelişmiş MCP sunucu kullanımı rehberi tanıtıldı.
  - **Düzenli ve Düşük Seviyeli Sunucu**: Her iki yaklaşım için Python ve TypeScript kod örnekleriyle detaylı karşılaştırma.
  - **Handler Tabanlı Tasarım**: Ölçeklenebilir, esnek sunucu uygulamaları için handler tabanlı araç/kaynak/prompt yönetimi açıklaması.
  - **Pratik Desenler**: Gelişmiş özellikler ve mimari için düşük seviyeli sunucu desenlerinin faydalı olduğu gerçek dünya senaryoları.

#### Basit Kimlik Doğrulama (03-GettingStarted/11-simple-auth)
- **Yeni Bölüm Eklendi**: MCP sunucularında basit kimlik doğrulama uygulaması için adım adım rehber.
  - **Kimlik Doğrulama Kavramları**: Kimlik doğrulama ile yetkilendirme arasındaki fark ve kimlik bilgisi yönetimi net açıklaması.
  - **Temel Kimlik Doğrulama Uygulaması**: Python (Starlette) ve TypeScript (Express) için ara katman tabanlı kimlik doğrulama desenleri ve kod örnekleri.
  - **Gelişmiş Güvenliğe Geçiş**: Basit kimlik doğrulama ile başlayıp OAuth 2.1 ve RBAC’ye ilerleme rehberi, gelişmiş güvenlik modüllerine referanslar.

Bu eklemeler, temel kavramları gelişmiş üretim desenleriyle birleştirerek daha sağlam, güvenli ve esnek MCP sunucu uygulamaları oluşturmak için pratik, uygulamalı rehberlik sağlar.

## 29 Eylül 2025

### MCP Sunucu Veritabanı Entegrasyon Laboratuvarları - Kapsamlı Uygulamalı Öğrenme Yolu

#### 11-MCPServerHandsOnLabs - Yeni Tam Veritabanı Entegrasyon Müfredatı
- **Tam 13 Laboratuvarlık Öğrenme Yolu**: PostgreSQL veritabanı entegrasyonlu üretime hazır MCP sunucuları oluşturmak için kapsamlı uygulamalı müfredat eklendi
  - **Gerçek Dünya Uygulaması**: Kurumsal düzey desenleri gösteren Zava Retail analiz kullanım senaryosu
  - **Yapılandırılmış Öğrenme İlerlemesi**:
    - **Laboratuvarlar 00-03: Temeller** - Giriş, Temel Mimari, Güvenlik & Çoklu Kiracı, Ortam Kurulumu
    - **Laboratuvarlar 04-06: MCP Sunucu İnşası** - Veritabanı Tasarımı & Şema, MCP Sunucu Uygulaması, Araç Geliştirme  
    - **Laboratuvarlar 07-09: Gelişmiş Özellikler** - Anlamsal Arama Entegrasyonu, Test & Hata Ayıklama, VS Code Entegrasyonu
    - **Laboratuvarlar 10-12: Üretim & En İyi Uygulamalar** - Dağıtım Stratejileri, İzleme & Gözlemlenebilirlik, En İyi Uygulamalar & Optimizasyon
  - **Kurumsal Teknolojiler**: FastMCP çerçevesi, pgvector ile PostgreSQL, Azure OpenAI gömme, Azure Container Apps, Application Insights
  - **Gelişmiş Özellikler**: Satır Seviyesi Güvenlik (RLS), anlamsal arama, çoklu kiracı veri erişimi, vektör gömmeleri, gerçek zamanlı izleme

#### Terminoloji Standartlaştırması - Modülden Laboratuvara Dönüşüm
- **Kapsamlı Dokümantasyon Güncellemesi**: 11-MCPServerHandsOnLabs içindeki tüm README dosyaları "Modül" yerine "Laboratuvar" terimini kullanacak şekilde sistematik olarak güncellendi
  - **Bölüm Başlıkları**: Tüm 13 laboratuvarda "Bu Modül Neleri Kapsar" başlığı "Bu Laboratuvar Neleri Kapsar" olarak değiştirildi
  - **İçerik Açıklaması**: "Bu modül sağlar..." ifadeleri "Bu laboratuvar sağlar..." olarak değiştirildi
  - **Öğrenme Hedefleri**: "Bu modülün sonunda..." ifadeleri "Bu laboratuvarın sonunda..." olarak güncellendi
  - **Navigasyon Bağlantıları**: Tüm "Modül XX:" referansları çapraz referanslarda ve navigasyonda "Laboratuvar XX:" olarak dönüştürüldü
  - **Tamamlama Takibi**: "Bu modülü tamamladıktan sonra..." ifadeleri "Bu laboratuvarı tamamladıktan sonra..." olarak güncellendi
  - **Teknik Referanslar Korundu**: Yapılandırma dosyalarındaki Python modül referansları (örneğin `"module": "mcp_server.main"`) korundu

#### Çalışma Rehberi Geliştirmesi (study_guide.md)
- **Görsel Müfredat Haritası**: Kapsamlı laboratuvar yapısı görselleştirmesi ile yeni "11. Veritabanı Entegrasyon Laboratuvarları" bölümü eklendi
- **Depo Yapısı**: On bölümden on bir ana bölüme ve detaylı 11-MCPServerHandsOnLabs açıklamasına güncellendi
- **Öğrenme Yolu Rehberi**: 00-11 bölümlerini kapsayacak şekilde navigasyon talimatları geliştirildi
- **Teknoloji Kapsamı**: FastMCP, PostgreSQL, Azure hizmetleri entegrasyon detayları eklendi
- **Öğrenme Çıktıları**: Üretime hazır sunucu geliştirme, veritabanı entegrasyon desenleri ve kurumsal güvenlik vurgulandı

#### Ana README Yapılandırma Geliştirmesi
- **Laboratuvar Tabanlı Terminoloji**: 11-MCPServerHandsOnLabs içindeki ana README.md dosyası tutarlı şekilde "Laboratuvar" yapısını kullanacak şekilde güncellendi
- **Öğrenme Yolu Organizasyonu**: Temel kavramlardan gelişmiş uygulamaya ve üretim dağıtımına net ilerleme sağlandı
- **Gerçek Dünya Odaklılık**: Kurumsal düzey desenler ve teknolojilerle pratik, uygulamalı öğrenme vurgulandı

### Dokümantasyon Kalite ve Tutarlılık İyileştirmeleri
- **Uygulamalı Öğrenme Vurgusu**: Dokümantasyon boyunca pratik, laboratuvar tabanlı yaklaşım güçlendirildi
- **Kurumsal Desenlere Odaklanma**: Üretime hazır uygulamalar ve kurumsal güvenlik hususları ön plana çıkarıldı
- **Teknoloji Entegrasyonu**: Modern Azure hizmetleri ve yapay zeka entegrasyon desenlerinin kapsamlı ele alınması
- **Öğrenme İlerlemesi**: Temel kavramlardan üretim dağıtımına net, yapılandırılmış yol

## 26 Eylül 2025

### Vaka Çalışmaları Geliştirmesi - GitHub MCP Registry Entegrasyonu

#### Vaka Çalışmaları (09-CaseStudy/) - Ekosistem Geliştirme Odaklı
- **README.md**: Kapsamlı GitHub MCP Registry vaka çalışması ile büyük genişleme
  - **GitHub MCP Registry Vaka Çalışması**: Eylül 2025’te GitHub’ın MCP Registry lansmanını inceleyen yeni kapsamlı vaka çalışması
    - **Sorun Analizi**: Parçalanmış MCP sunucu keşfi ve dağıtım zorluklarının detaylı incelenmesi
    - **Çözüm Mimarisi**: GitHub’ın merkezi kayıt yaklaşımı ve tek tıklamayla VS Code kurulumu
    - **İş Etkisi**: Geliştirici işe alım ve verimlilikte ölçülebilir iyileşmeler
    - **Stratejik Değer**: Modüler ajan dağıtımı ve araçlar arası birlikte çalışabilirlik vurgusu
    - **Ekosistem Geliştirme**: Ajan tabanlı entegrasyon için temel platform olarak konumlandırma
  - **Geliştirilmiş Vaka Çalışması Yapısı**: Tüm yedi vaka çalışması tutarlı format ve kapsamlı açıklamalarla güncellendi
    - Azure AI Seyahat Ajanları: Çoklu ajan orkestrasyon vurgusu
    - Azure DevOps Entegrasyonu: İş akışı otomasyonu odaklı
    - Gerçek Zamanlı Dokümantasyon Getirme: Python konsol istemcisi uygulaması
    - Etkileşimli Çalışma Planı Üreticisi: Chainlit sohbet tabanlı web uygulaması
    - Editör İçi Dokümantasyon: VS Code ve GitHub Copilot entegrasyonu
    - Azure API Yönetimi: Kurumsal API entegrasyon desenleri
    - GitHub MCP Registry: Ekosistem geliştirme ve topluluk platformu
  - **Kapsamlı Sonuç Bölümü**: Çoklu MCP uygulama boyutlarını kapsayan yedi vaka çalışmasını vurgulayan yeniden yazılmış sonuç bölümü
    - Kurumsal Entegrasyon, Çoklu Ajan Orkestrasyonu, Geliştirici Verimliliği
    - Ekosistem Geliştirme, Eğitim Uygulamaları kategorilendirmesi
    - Mimari desenler, uygulama stratejileri ve en iyi uygulamalar hakkında geliştirilmiş içgörüler
    - MCP’nin olgun, üretime hazır protokol olarak önemi vurgusu

#### Çalışma Rehberi Güncellemeleri (study_guide.md)
- **Görsel Müfredat Haritası**: Vaka Çalışmaları bölümüne GitHub MCP Registry eklendi
- **Vaka Çalışmaları Açıklaması**: Genel açıklamalardan yedi kapsamlı vaka çalışmasının detaylı dökümüne yükseltildi
- **Depo Yapısı**: Bölüm 10, kapsamlı vaka çalışması içeriği ve spesifik uygulama detayları ile güncellendi
- **Değişiklik Günlüğü Entegrasyonu**: 26 Eylül 2025 girdisi, GitHub MCP Registry eklemesi ve vaka çalışması geliştirmelerini belgeledi
- **Tarih Güncellemeleri**: Alt bilgi zaman damgası en son revizyona (26 Eylül 2025) göre güncellendi

### Dokümantasyon Kalite İyileştirmeleri
- **Tutarlılık Artırma**: Tüm yedi örnekte vaka çalışması formatı ve yapısı standartlaştırıldı
- **Kapsamlı Kapsama**: Vaka çalışmaları artık kurumsal, geliştirici verimliliği ve ekosistem geliştirme senaryolarını kapsıyor
- **Stratejik Konumlandırma**: MCP’nin ajan tabanlı sistem dağıtımı için temel platform olarak önemi güçlendirildi
- **Kaynak Entegrasyonu**: Ek kaynaklar arasında GitHub MCP Registry bağlantısı eklendi

## 15 Eylül 2025

### Gelişmiş Konular Genişletmesi - Özel Taşıyıcılar & Bağlam Mühendisliği

#### MCP Özel Taşıyıcılar (05-AdvancedTopics/mcp-transport/) - Yeni Gelişmiş Uygulama Rehberi
- **README.md**: Özel MCP taşıyıcı mekanizmaları için tam uygulama rehberi
  - **Azure Event Grid Taşıyıcısı**: Kapsamlı sunucusuz olay tabanlı taşıyıcı uygulaması
    - C#, TypeScript ve Python örnekleri ile Azure Functions entegrasyonu
    - Ölçeklenebilir MCP çözümleri için olay tabanlı mimari desenler
    - Webhook alıcıları ve push tabanlı mesaj işleme
  - **Azure Event Hubs Taşıyıcısı**: Yüksek verimli akış taşıyıcı uygulaması
    - Düşük gecikmeli senaryolar için gerçek zamanlı akış yetenekleri
    - Bölümlendirme stratejileri ve kontrol noktası yönetimi
    - Mesaj toplama ve performans optimizasyonu
  - **Kurumsal Entegrasyon Desenleri**: Üretime hazır mimari örnekler
    - Birden çok Azure Functions arasında dağıtılmış MCP işleme
    - Birden çok taşıyıcı türünü birleştiren hibrit taşıyıcı mimarileri
    - Mesaj dayanıklılığı, güvenilirlik ve hata yönetimi stratejileri
  - **Güvenlik & İzleme**: Azure Key Vault entegrasyonu ve gözlemlenebilirlik desenleri
    - Yönetilen kimlik doğrulama ve en az ayrıcalık erişimi
    - Application Insights telemetri ve performans izleme
    - Devre kesiciler ve hata toleransı desenleri
  - **Test Çerçeveleri**: Özel taşıyıcılar için kapsamlı test stratejileri
    - Test çiftleri ve taklit çerçeveleri ile birim testi
    - Azure Test Containers ile entegrasyon testi
    - Performans ve yük testi değerlendirmeleri

#### Bağlam Mühendisliği (05-AdvancedTopics/mcp-contextengineering/) - Yükselen AI Disiplini
- **README.md**: Bağlam mühendisliği alanının kapsamlı keşfi
  - **Temel İlkeler**: Tam bağlam paylaşımı, eylem karar farkındalığı ve bağlam penceresi yönetimi
  - **MCP Protokol Uyum**: MCP tasarımının bağlam mühendisliği zorluklarını nasıl ele aldığı
    - Bağlam pencere sınırlamaları ve kademeli yükleme stratejileri
    - Alaka belirleme ve dinamik bağlam getirme
    - Çok modlu bağlam işleme ve güvenlik hususları
  - **Uygulama Yaklaşımları**: Tek iş parçacıklı ve çoklu ajan mimarileri
    - Bağlam parçalama ve önceliklendirme teknikleri
    - Kademeli bağlam yükleme ve sıkıştırma stratejileri
    - Katmanlı bağlam yaklaşımları ve getirme optimizasyonu
  - **Ölçüm Çerçevesi**: Bağlam etkinliği değerlendirmesi için gelişen metrikler
    - Girdi verimliliği, performans, kalite ve kullanıcı deneyimi değerlendirmeleri
    - Bağlam optimizasyonu için deneysel yaklaşımlar
    - Hata analizi ve iyileştirme metodolojileri

#### Müfredat Navigasyon Güncellemeleri (README.md)
- **Geliştirilmiş Modül Yapısı**: Yeni gelişmiş konuları içerecek şekilde müfredat tablosu güncellendi
  - Bağlam Mühendisliği (5.14) ve Özel Taşıyıcı (5.15) girişleri eklendi
  - Tüm modüllerde tutarlı biçimlendirme ve navigasyon bağlantıları
  - Güncel içerik kapsamını yansıtacak şekilde açıklamalar güncellendi

### Dizin Yapısı İyileştirmeleri
- **Adlandırma Standartlaştırması**: "mcp transport" klasörü diğer gelişmiş konu klasörleriyle uyumlu olarak "mcp-transport" olarak yeniden adlandırıldı
- **İçerik Organizasyonu**: Tüm 05-AdvancedTopics klasörleri artık tutarlı adlandırma desenini (mcp-[konu]) takip ediyor

### Dokümantasyon Kalite Geliştirmeleri
- **MCP Spesifikasyon Uyumu**: Tüm yeni içerikler güncel MCP Spesifikasyonu 2025-06-18 referans alıyor
- **Çok Dilli Örnekler**: C#, TypeScript ve Python’da kapsamlı kod örnekleri
- **Kurumsal Odak**: Üretime hazır desenler ve Azure bulut entegrasyonu genelinde
- **Görsel Dokümantasyon**: Mimari ve akış görselleştirmeleri için Mermaid diyagramları

## 18 Ağustos 2025

### Dokümantasyon Kapsamlı Güncellemesi - MCP 2025-06-18 Standartları

#### MCP Güvenlik En İyi Uygulamaları (02-Security/) - Tam Modernizasyon
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: MCP Spesifikasyonu 2025-06-18 ile uyumlu tam yeniden yazım
  - **Zorunlu Gereksinimler**: Resmi spesifikasyondan açıkça belirtilmiş OLMASI/OLMAMASI GEREKEN gereksinimler, net görsel göstergelerle eklendi
  - **12 Temel Güvenlik Uygulaması**: 15 maddelik listeden kapsamlı güvenlik alanlarına yeniden yapılandırıldı
    - Dış kimlik sağlayıcı entegrasyonlu Token Güvenliği ve Kimlik Doğrulama
    - Kriptografik gereksinimlerle Oturum Yönetimi ve Taşıma Güvenliği
    - Microsoft Prompt Shields entegrasyonlu AI'ya Özgü Tehdit Koruması
    - En Az Ayrıcalık prensibiyle Erişim Kontrolü ve İzinler
    - Azure Content Safety entegrasyonlu İçerik Güvenliği ve İzleme
    - Kapsamlı bileşen doğrulamasıyla Tedarik Zinciri Güvenliği
    - PKCE uygulamalı OAuth Güvenliği ve Karışık Vekil Önleme
    - Otomatik yeteneklerle Olay Müdahalesi ve Kurtarma
    - Düzenleyici uyumlu Uyumluluk ve Yönetişim
    - Sıfır güven mimarisiyle Gelişmiş Güvenlik Kontrolleri
    - Kapsamlı çözümlerle Microsoft Güvenlik Ekosistemi Entegrasyonu
    - Uyarlanabilir uygulamalarla Sürekli Güvenlik Evrimi
  - **Microsoft Güvenlik Çözümleri**: Prompt Shields, Azure Content Safety, Entra ID ve GitHub Advanced Security için geliştirilmiş entegrasyon rehberi
  - **Uygulama Kaynakları**: Resmi MCP Dokümantasyonu, Microsoft Güvenlik Çözümleri, Güvenlik Standartları ve Uygulama Kılavuzları olarak kapsamlı kaynak bağlantıları kategorize edildi

#### Gelişmiş Güvenlik Kontrolleri (02-Security/) - Kurumsal Uygulama
- **MCP-SECURITY-CONTROLS-2025.md**: Kurumsal düzeyde güvenlik çerçevesi ile tamamen yenilendi
  - **9 Kapsamlı Güvenlik Alanı**: Temel kontrollerden detaylı kurumsal çerçeveye genişletildi
    - Microsoft Entra ID entegrasyonlu Gelişmiş Kimlik Doğrulama ve Yetkilendirme
    - Kapsamlı doğrulama ile Token Güvenliği ve Anti-Passthrough Kontrolleri
    - Ele geçirme önleyici Oturum Güvenliği Kontrolleri
    - Prompt enjeksiyonu ve araç zehirlenmesi önleyici AI'ya Özgü Güvenlik Kontrolleri
    - OAuth proxy güvenliği ile Karışık Vekil Saldırısı Önleme
    - Sandbox ve izolasyon ile Araç Çalıştırma Güvenliği
    - Bağımlılık doğrulaması ile Tedarik Zinciri Güvenlik Kontrolleri
    - SIEM entegrasyonlu İzleme ve Tespit Kontrolleri
    - Otomatik yeteneklerle Olay Müdahalesi ve Kurtarma
  - **Uygulama Örnekleri**: Detaylı YAML yapılandırma blokları ve kod örnekleri eklendi
  - **Microsoft Çözümleri Entegrasyonu**: Azure güvenlik servisleri, GitHub Advanced Security ve kurumsal kimlik yönetimi kapsamlı şekilde ele alındı

#### Gelişmiş Konular Güvenliği (05-AdvancedTopics/mcp-security/) - Üretime Hazır Uygulama
- **README.md**: Kurumsal güvenlik uygulaması için tamamen yeniden yazıldı
  - **Mevcut Spesifikasyon Uyumu**: MCP Spesifikasyon 2025-06-18 ile zorunlu güvenlik gereksinimleri güncellendi
  - **Gelişmiş Kimlik Doğrulama**: Microsoft Entra ID entegrasyonu, kapsamlı .NET ve Java Spring Security örnekleriyle
  - **AI Güvenlik Entegrasyonu**: Microsoft Prompt Shields ve Azure Content Safety uygulaması, detaylı Python örnekleriyle
  - **Gelişmiş Tehdit Azaltma**: Kapsamlı uygulama örnekleri
    - PKCE ve kullanıcı onayı doğrulaması ile Karışık Vekil Saldırısı Önleme
    - Hedef doğrulaması ve güvenli token yönetimi ile Token Passthrough Önleme
    - Kriptografik bağlama ve davranış analizi ile Oturum Ele Geçirme Önleme
  - **Kurumsal Güvenlik Entegrasyonu**: Azure Application Insights izleme, tehdit tespit hatları ve tedarik zinciri güvenliği
  - **Uygulama Kontrol Listesi**: Zorunlu ve önerilen güvenlik kontrolleri ile Microsoft güvenlik ekosistemi avantajları net şekilde belirtildi

### Dokümantasyon Kalitesi ve Standart Uyumu
- **Spesifikasyon Referansları**: Tüm referanslar güncel MCP Spesifikasyon 2025-06-18 olarak güncellendi
- **Microsoft Güvenlik Ekosistemi**: Tüm güvenlik dokümantasyonunda geliştirilmiş entegrasyon rehberi
- **Pratik Uygulama**: Kurumsal desenlerle .NET, Java ve Python’da detaylı kod örnekleri eklendi
- **Kaynak Organizasyonu**: Resmi dokümantasyon, güvenlik standartları ve uygulama kılavuzları kapsamlı şekilde kategorize edildi
- **Görsel Göstergeler**: Zorunlu gereksinimler ve önerilen uygulamalar net şekilde işaretlendi


#### Temel Kavramlar (01-CoreConcepts/) - Tam Modernizasyon
- **Protokol Sürüm Güncellemesi**: Güncel MCP Spesifikasyon 2025-06-18 referanslı tarih bazlı sürüm (YYYY-AA-GG formatı) eklendi
- **Mimari İyileştirme**: Hosts, Clients ve Servers açıklamaları güncel MCP mimari desenlerine göre geliştirildi
  - Hosts artık birden fazla MCP istemci bağlantısını koordine eden AI uygulamaları olarak net tanımlandı
  - Clients, bire bir sunucu ilişkisini sürdüren protokol bağlayıcıları olarak tanımlandı
  - Servers, yerel ve uzak dağıtım senaryolarıyla geliştirildi
- **Primitive Yeniden Yapılandırma**: Sunucu ve istemci primitive’leri tamamen yenilendi
  - Sunucu Primitive’leri: Kaynaklar (veri kaynakları), Prompts (şablonlar), Araçlar (çalıştırılabilir fonksiyonlar) detaylı açıklama ve örneklerle
  - İstemci Primitive’leri: Örnekleme (LLM tamamlamaları), Elicitation (kullanıcı girdisi), Logging (hata ayıklama/izleme)
  - Güncel keşif (`*/list`), alma (`*/get`) ve yürütme (`*/call`) yöntem desenleriyle güncellendi
- **Protokol Mimarisi**: İki katmanlı mimari modeli tanıtıldı
  - Veri Katmanı: JSON-RPC 2.0 temelli yaşam döngüsü yönetimi ve primitive’ler
  - Taşıma Katmanı: STDIO (yerel) ve SSE destekli Streamable HTTP (uzak) taşıma mekanizmaları
- **Güvenlik Çerçevesi**: Açık kullanıcı onayı, veri gizliliği koruması, araç çalıştırma güvenliği ve taşıma katmanı güvenliği dahil kapsamlı güvenlik ilkeleri
- **İletişim Desenleri**: Başlatma, keşif, yürütme ve bildirim akışlarını gösteren protokol mesajları güncellendi
- **Kod Örnekleri**: Güncel MCP SDK desenlerini yansıtan çoklu dil örnekleri (.NET, Java, Python, JavaScript) yenilendi

#### Güvenlik (02-Security/) - Kapsamlı Güvenlik Yenilemesi  
- **Standart Uyumu**: MCP Spesifikasyon 2025-06-18 güvenlik gereksinimleriyle tam uyum sağlandı
- **Kimlik Doğrulama Evrimi**: Özel OAuth sunucularından dış kimlik sağlayıcı delege (Microsoft Entra ID) modeline geçiş belgelendi
- **AI'ya Özgü Tehdit Analizi**: Modern AI saldırı vektörleri kapsamı genişletildi
  - Gerçek dünya örnekleriyle detaylı prompt enjeksiyonu saldırı senaryoları
  - Araç zehirlenmesi mekanizmaları ve "rug pull" saldırı desenleri
  - Bağlam penceresi zehirlenmesi ve model karışıklığı saldırıları
- **Microsoft AI Güvenlik Çözümleri**: Microsoft güvenlik ekosistemi kapsamlı şekilde ele alındı
  - Gelişmiş tespit, vurgulama ve ayırıcı tekniklerle AI Prompt Shields
  - Azure Content Safety entegrasyon desenleri
  - Tedarik zinciri koruması için GitHub Advanced Security
- **Gelişmiş Tehdit Azaltma**: Detaylı güvenlik kontrolleri
  - MCP’ye özgü oturum ele geçirme saldırı senaryoları ve kriptografik oturum ID gereksinimleri
  - MCP proxy senaryolarında karışık vekil sorunları ve açık onay gereksinimleri
  - Zorunlu doğrulama kontrolleriyle token passthrough zafiyetleri
- **Tedarik Zinciri Güvenliği**: Temel modeller, embedding servisleri, bağlam sağlayıcılar ve üçüncü taraf API’leri dahil AI tedarik zinciri kapsamı genişletildi
- **Temel Güvenlik**: Sıfır güven mimarisi ve Microsoft güvenlik ekosistemi entegrasyonu geliştirildi
- **Kaynak Organizasyonu**: Resmi Dokümanlar, Standartlar, Araştırma, Microsoft Çözümleri ve Uygulama Kılavuzları olarak kapsamlı kaynak bağlantıları kategorize edildi

### Dokümantasyon Kalitesi İyileştirmeleri
- **Yapılandırılmış Öğrenme Hedefleri**: Spesifik, uygulanabilir sonuçlarla öğrenme hedefleri geliştirildi
- **Çapraz Referanslar**: İlgili güvenlik ve temel kavram konuları arasında bağlantılar eklendi
- **Güncel Bilgi**: Tüm tarih referansları ve spesifikasyon bağlantıları güncel standartlara göre yenilendi
- **Uygulama Rehberi**: Her iki bölümde de spesifik, uygulanabilir uygulama yönergeleri eklendi

## 16 Temmuz 2025

### README ve Navigasyon İyileştirmeleri
- README.md’de müfredat navigasyonu tamamen yeniden tasarlandı
- `<details>` etiketleri daha erişilebilir tablo tabanlı formata dönüştürüldü
- Yeni "alternative_layouts" klasöründe alternatif düzen seçenekleri oluşturuldu
- Kart tabanlı, sekmeli ve akordeon tarzı navigasyon örnekleri eklendi
- Depo yapısı bölümü tüm en son dosyaları içerecek şekilde güncellendi
- "Bu Müfredat Nasıl Kullanılır" bölümü net önerilerle geliştirildi
- MCP spesifikasyon bağlantıları doğru URL’lere yönlendirilecek şekilde güncellendi
- Müfredat yapısına Context Engineering bölümü (5.14) eklendi

### Çalışma Kılavuzu Güncellemeleri
- Çalışma kılavuzu mevcut depo yapısına uyacak şekilde tamamen revize edildi
- MCP İstemcileri ve Araçları ile Popüler MCP Sunucuları için yeni bölümler eklendi
- Görsel Müfredat Haritası tüm konuları doğru şekilde yansıtacak şekilde güncellendi
- Gelişmiş Konular açıklamaları tüm uzmanlık alanlarını kapsayacak şekilde geliştirildi
- Vaka Çalışmaları bölümü gerçek örneklerle güncellendi
- Bu kapsamlı değişiklik günlüğü eklendi

### Topluluk Katkıları (06-CommunityContributions/)
- Görüntü oluşturma için MCP sunucuları hakkında detaylı bilgi eklendi
- VSCode’da Claude kullanımı için kapsamlı bölüm eklendi
- Cline terminal istemcisi kurulumu ve kullanım talimatları eklendi
- MCP istemci bölümü tüm popüler istemci seçeneklerini içerecek şekilde güncellendi
- Katkı örnekleri daha doğru kod örnekleriyle geliştirildi

### Gelişmiş Konular (05-AdvancedTopics/)
- Tüm uzmanlık konu klasörleri tutarlı isimlendirme ile organize edildi
- Context engineering materyalleri ve örnekleri eklendi
- Foundry ajan entegrasyon dokümantasyonu eklendi
- Entra ID güvenlik entegrasyon dokümantasyonu geliştirildi

## 11 Haziran 2025

### İlk Oluşturma
- MCP for Beginners müfredatının ilk sürümü yayımlandı
- Tüm 10 ana bölüm için temel yapı oluşturuldu
- Navigasyon için Görsel Müfredat Haritası uygulandı
- Çoklu programlama dillerinde ilk örnek projeler eklendi

### Başlarken (03-GettingStarted/)
- İlk sunucu uygulama örnekleri oluşturuldu
- İstemci geliştirme rehberi eklendi
- LLM istemci entegrasyon talimatları dahil edildi
- VS Code entegrasyon dokümantasyonu eklendi
- Server-Sent Events (SSE) sunucu örnekleri uygulandı

### Temel Kavramlar (01-CoreConcepts/)
- İstemci-sunucu mimarisi detaylı şekilde açıklandı
- Ana protokol bileşenleri dokümante edildi
- MCP mesajlaşma desenleri belgelendi

## 23 Mayıs 2025

### Depo Yapısı
- Temel klasör yapısı ile depo başlatıldı
- Her ana bölüm için README dosyaları oluşturuldu
- Çeviri altyapısı kuruldu
- Görsel varlıklar ve diyagramlar eklendi

### Dokümantasyon
- Müfredat genel bakışını içeren ilk README.md oluşturuldu
- CODE_OF_CONDUCT.md ve SECURITY.md eklendi
- Yardım alma rehberi içeren SUPPORT.md kuruldu
- Ön çalışma kılavuzu yapısı oluşturuldu

## 15 Nisan 2025

### Planlama ve Çerçeve
- MCP for Beginners müfredatı için ilk planlama yapıldı
- Öğrenme hedefleri ve hedef kitle tanımlandı
- Müfredatın 10 bölümlük yapısı tasarlandı
- Örnekler ve vaka çalışmaları için kavramsal çerçeve geliştirildi
- Anahtar kavramlar için ilk prototip örnekler oluşturuldu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->