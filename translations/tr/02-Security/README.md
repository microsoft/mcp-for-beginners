# MCP Güvenliği: AI Sistemleri için Kapsamlı Koruma

[![MCP Güvenliği En İyi Uygulamalar](../../../translated_images/tr/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Bu dersin videosunu görüntülemek için yukarıdaki resme tıklayın)_

Güvenlik, AI sistemi tasarımının temelidir, bu yüzden ikinci bölüm olarak öncelik veriyoruz. Bu, Microsoft'un [Güvenli Gelecek Girişimi](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/)'ndaki **Tasarımda Güvenlik** prensibi ile uyumludur.

Model Context Protocol (MCP), AI destekli uygulamalara güçlü yeni yetenekler katarken geleneksel yazılım risklerinin ötesine geçen benzersiz güvenlik zorlukları sunar. MCP sistemleri, sağlam kodlama, en az ayrıcalık, tedarik zinciri güvenliği gibi yerleşik güvenlik sorunlarının yanı sıra prompt enjeksiyonu, araç zehirlenmesi, oturum kaçırma, karışmış temsilci saldırıları, token geçiş açıklıkları ve dinamik yetenek değişiklikleri gibi yeni AI özgü tehditlerle karşı karşıyadır.

Bu ders, MCP uygulamalarındaki en kritik güvenlik risklerini keşfeder—kimlik doğrulama, yetkilendirme, aşırı izinler, dolaylı prompt enjeksiyonu, oturum güvenliği, karışmış temsilci sorunları, token yönetimi ve tedarik zinciri açıklıkları kapsar. Bu riskleri en aza indirmek için uygulanabilir kontroller ve en iyi uygulamaları öğrenirken Prompt Shields, Azure Content Safety ve GitHub Advanced Security gibi Microsoft çözümlerinin MCP dağıtımınızı nasıl güçlendirdiğini keşfedeceksiniz.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- **MCP Özgü Tehditleri Belirleme**: MCP sistemlerindeki benzersiz güvenlik risklerini tanıyın; prompt enjeksiyonu, araç zehirlenmesi, aşırı izinler, oturum kaçırma, karışmış temsilci sorunları, token geçiş açıklıkları ve tedarik zinciri riskleri dahil
- **Güvenlik Kontrolleri Uygulama**: Güçlü kimlik doğrulama, en az ayrıcalık erişimi, güvenli token yönetimi, oturum güvenlik kontrolleri ve tedarik zinciri doğrulaması gibi etkili hafifletmeleri uygulayın
- **Microsoft Güvenlik Çözümlerini Kullanma**: MCP iş yükü koruması için Microsoft Prompt Shields, Azure Content Safety ve GitHub Advanced Security çözümlerini anlayın ve devreye alın
- **Araç Güvenliğini Doğrulama**: Araç meta veri doğrulamanın önemini, dinamik değişikliklerin izlenmesini ve dolaylı prompt enjeksiyonu saldırılarına karşı savunmayı kavrayın
- **En İyi Uygulamaları Entegre Etme**: Yerleşik güvenlik temellerini (güvenli kodlama, sunucu sertleştirme, sıfır güven) MCP özgü kontrollerle birleştirerek kapsamlı koruma sağlayın

# MCP Güvenlik Mimarisi ve Kontrolleri

Modern MCP uygulamaları, hem geleneksel yazılım güvenliğini hem de AI özgü tehditleri ele alan katmanlı güvenlik yaklaşımları gerektirir. Hızla gelişen MCP spesifikasyonu, güvenlik kontrollerini olgunlaştırmaya ve kurumsal güvenlik mimarileri ile yerleşik en iyi uygulamalarla daha iyi entegrasyon sağlamaya devam ediyor.

[Microsoft Dijital Savunma Raporu](https://aka.ms/mddr) araştırmaları, **rapor edilen ihlallerin %98'inin güçlü güvenlik hijyeniyle önlenebileceğini** göstermektedir. En etkili koruma stratejisi, temel güvenlik uygulamalarını MCP özgü kontrollerle birleştirmektir—kanıtlanmış temel güvenlik tedbirleri, genel güvenlik riskini azaltmada en etkili yöntem olmaya devam eder.

## Mevcut Güvenlik Manzarası

> **Not:** Bu bölüm, yerleşik MCP güvenlik kontrollerini
> mevcut **MCP Spesifikasyonu 2026-07-28** yetkilendirme rehberiyle birleştirir. 
> Her zaman güncel [MCP Spesifikasyonuna](https://modelcontextprotocol.io/specification/2026-07-28/),
> [MCP GitHub deposuna](https://github.com/modelcontextprotocol) ve
> [güvenlik en iyi uygulamaları dokümantasyonuna](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> başvurunuz.

> **Yetkilendirme güncellemesi:** MCP `2026-07-28`, istemcilerin
> yetkilendirme yanıtlarındaki `iss` parametresini (RFC 9207) doğrulamasını ve
> kayıtlı kimlik bilgilerini yetkilendirme sunucusuna bağlamasını şart koşar.
> Dinamik İstemci Kaydı kullanımdan kalktı; yeni uygulamalar İstemci Kimliği Meta Veri Belgelerini kullanmalıdır.
> Tüm yetkilendirme değişiklikleri için [MCP'deki Değişiklikler: 2026-07-28 Spesifikasyonu](../01-CoreConcepts/mcp-2026-07-28.md)
> başlığına bakınız.

## 🏔️ MCP Güvenlik Zirvesi Atölyesi (Sherpa)

**Pratik güvenlik eğitimi** için, Microsoft Azure'daki MCP sunucularını güvenceye alma konusunda kapsamlı ve rehberli bir yolculuk olan **MCP Güvenlik Zirvesi Atölyesi**ni (Sherpa) şiddetle tavsiye ederiz.

### Atölye Genel Bakış

[MCP Güvenlik Zirvesi Atölyesi](https://azure-samples.github.io/sherpa/) kanıtlanmış "güvenlik açıklarını keşfet → istismar et → düzelt → doğrula" metodolojisiyle pratik, uygulanabilir güvenlik eğitimi sunar. Şunları yapacaksınız:

- **Hataları Kendiniz Deneyimleyin**: Kasıtlı olarak güvensiz sunucuları istismar ederek güvenlik açıklarını ilk elden deneyimleyin
- **Azure Yerel Güvenliğini Kullanın**: Azure Entra ID, Key Vault, API Yönetimi ve AI İçerik Güvenliğini kullanın
- **Derin Savunmayı Takip Edin**: Kapsamlı güvenlik katmanları inşa eden kamplardan geçin
- **OWASP Standartlarını Uygulayın**: Her teknik [OWASP MCP Azure Güvenlik Kılavuzu](https://microsoft.github.io/mcp-azure-security-guide/) ile eşleşir
- **Çalışan Kod Alın**: Çalışır ve test edilmiş uygulamalar edinin

### Yolculuk Rotaları

| Kamp | Odak | Kapsanan OWASP Riskleri |
|------|-------|----------------------|
| **Temel Kamp** | MCP temelleri ve kimlik doğrulama güvenlik açıkları | MCP01, MCP07 |
| **1. Kamp: Kimlik** | OAuth 2.1, Azure Yönetilen Kimlik, Key Vault | MCP01, MCP02, MCP07 |
| **2. Kamp: Ağ Geçidi** | API Yönetimi, Özel Uç Noktalar, yönetişim | MCP02, MCP06, MCP07, MCP09 |
| **3. Kamp: Giriş/Çıkış Güvenliği** | Prompt enjeksiyonu, PII koruması, içerik güvenliği | MCP03, MCP05, MCP06, MCP10 |
| **4. Kamp: İzleme** | Günlük Analitiği, gösterge panoları, tehdit tespiti | MCP04, MCP08 |
| **Zirve** | Kırmızı Takım / Mavi Takım entegrasyon testi | Tümü |

**Başlayın:** [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP İlk 10 Güvenlik Riski

[OWASP MCP Azure Güvenlik Kılavuzu](https://microsoft.github.io/mcp-azure-security-guide/) MCP uygulamaları için en kritik on güvenlik riskini detaylandırır:

| Risk | Açıklama | Azure Hafifletmesi |
|------|-------------|-------------------|
| **MCP01** | Token Yanlış Yönetimi & Gizli Bilgi Açığa Çıkması | Azure Key Vault, Yönetilen Kimlik |
| **MCP02** | Kapsam Kayması Yoluyla Ayrıcalık Artışı | RBAC, Koşullu Erişim |
| **MCP03** | Araç Zehirlenmesi | Araç doğrulama, bütünlük doğrulama |
| **MCP04** | Yazılım Tedarik Zinciri Saldırıları & Bağımlılık Manipülasyonu | GitHub Advanced Security, bağımlılık taraması |
| **MCP05** | Komut Enjeksiyonu & Çalıştırma | Girdi doğrulama, korumalı ortam |
| **MCP06** | Niyet Akışının Altüst Edilmesi | Azure AI İçerik Güvenliği, Prompt Shields |
| **MCP07** | Yetersiz Kimlik Doğrulama & Yetkilendirme | Azure Entra ID, PKCE ile OAuth 2.1 |
| **MCP08** | Denetim ve Telemetri Eksikliği | Azure Monitor, Application Insights |
| **MCP09** | Gölge MCP Sunucuları | API Merkezi yönetişimi, ağ izolasyonu |
| **MCP10** | Bağlam Enjeksiyonu & Aşırı Paylaşım | Veri sınıflandırması, minimal maruz kalma |

### MCP Kimlik Doğrulamasının Evrimi

MCP spesifikasyonu, kimlik doğrulama ve yetkilendirme yaklaşımında önemli ölçüde evrilmiştir:

- **Orijinal Yaklaşım**: İlk spesifikasyonlarda, geliştiriciler özel kimlik doğrulama sunucuları uygulamak zorundaydı; MCP sunucuları doğrudan kullanıcı kimlik doğrulamasını yöneten OAuth 2.0 Yetkilendirme Sunucusu olarak hareket ediyordu
- **Güncel Standart (`2026-07-28`)**: MCP sunucuları, Microsoft Entra ID gibi dış kimlik sağlayıcılarına kimlik doğrulamasını devredebilir. Ayrıca istemciler güncel issuer doğrulama ve kimlik bilgisi bağlama gereksinimlerini uygulamalıdır.
-  
-  
- **Taşıma Katmanı Güvenliği**: Hem yerel (STDIO) hem de uzak (Akışlı HTTP) bağlantılar için uygun kimlik doğrulama kalıplarıyla güvenli taşıma mekanizmalarına geliştirilmiş destek

## Kimlik Doğrulama ve Yetkilendirme Güvenliği

### Güncel Güvenlik Zorlukları

Modern MCP uygulamaları, çeşitli kimlik doğrulama ve yetkilendirme zorluklarıyla karşı karşıyadır:

### Riskler ve Tehdit Vektörleri

- **Yanlış Yapılandırılmış Yetkilendirme Mantığı**: MCP sunucularındaki hatalı yetkilendirme uygulaması hassas verilerin açığa çıkmasına ve erişim kontrollerinin yanlış uygulanmasına yol açabilir
- **OAuth Token İhlali**: Yerel MCP sunucu token hırsızlığı, saldırganların sunucu taklidi yapmasına ve bağlı hizmetlere erişmesine olanak tanır
- **Token Geçiş Açıkları**: Yanlış token işlemleri güvenlik kontrollerinin atlanmasına ve sorumluluk boşluklarına neden olur
- **Aşırı İzinler**: Fazla ayrıcalıklı MCP sunucuları en az ayrıcalık prensiplerini ihlal eder ve saldırı yüzeyini genişletir

#### Token Geçişi: Kritik Bir Anti-Model

Mevcut MCP yetkilendirme spesifikasyonunda, şiddetli güvenlik etkileri nedeniyle **token geçişi açıkça yasaklanmıştır**:

##### Güvenlik Kontrolü Atlatma
- MCP sunucuları ve bağlı API'ler, oran sınırlama, talep doğrulama, trafik izleme gibi kritik güvenlik kontrolleri uygular; bunlar doğru token doğrulama gerektirir
- Doğrudan istemci-API token kullanımı bu temel korumaları atlayarak güvenlik mimarisini zayıflatır

##### Sorumluluk ve Denetim Zorlukları  
- MCP sunucuları, yukarı akıştan verilen tokenları kullanan istemcileri ayırt edemez, bu denetim izlerini kırar
- Bağlı kaynak sunucu günlükleri gerçek MCP sunucu aracılarını değil, yanıltıcı istek kaynaklarını gösterir
- Olay inceleme ve uyumluluk denetimleri önemli ölçüde zorlaşır

##### Veri Çıkarma Riskleri
- Doğrulanmamış token talepleri, kötü niyetli aktörlerin çalınan tokenlarla MCP sunucularını veri çıkarma için vekil olarak kullanmasına imkan verir
- Güven sınırı ihlalleri, amaçlanan güvenlik kontrollerini aşan yetkisiz erişim desenlerine yol açar

##### Çoklu Hizmet Saldırı Vektörleri
- Kabul edilen ele geçirilmiş tokenlar, bağlı sistemler arasında yatay hareketliliği mümkün kılar
- Token kaynakları doğrulanamadığında servisler arası güven varsayımları ihlal edilebilir

### Güvenlik Kontrolleri ve Hafifletmeler

**Kritik Güvenlik Gereksinimleri:**

> **ZORUNLU**: MCP sunucuları, açıkça MCP sunucusu için verilmemiş herhangi bir tokenı  




- **Titiz Yetkilendirme İncelemesi**: Sadece amaçlanan kullanıcılar ve istemcilerin hassas kaynaklara erişebilmesini sağlamak için MCP sunucu yetkilendirme mantığının kapsamlı denetimlerini yapın
  - **Uygulama Rehberi**: [MCP Sunucuları için Kimlik Doğrulama Geçidi olarak Azure API Yönetimi](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)


- **Güvenli Token Yönetimi**: [Microsoft'un token doğrulama ve yaşam döngüsü en iyi uygulamalarını](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens) uygulayın
  - Token hedef kitle beyanlarının MCP sunucu kimliği ile uyuşmasını doğrulayın
  - Doğru token rotasyonu ve sona erme politikalarını uygulayın


- **Korunan Token Depolaması**: Hem beklemede hem aktarma sırasında tokenların şifrelenerek güvenli depolanması




- **En Az Ayrıcalık Prensibi**: MCP sunucularına yalnızca gereken minimum izinleri verin
  - Ayrıcalık kaymasını önlemek için düzenli izin incelemeleri ve güncellemeleri yapın


- **Rol Tabanlı Erişim Kontrolü (RBAC)**: Ayrıntılı rol atamaları yapın
  - Roller belirli kaynaklara ve işlemlere sıkı şekilde sınırlandırılmalı


- **Sürekli İzin İzleme**: Sürekli erişim denetimi ve izleme uygulayın
  - İzin kullanım desenlerini anormallik için izleyin












**Saldırı Senaryoları:**
- **Belge Tabanlı Enjeksiyon**: İşlenen belgelerde gizlenmiş kötü niyetli talimatlar, istenmeyen AI işlemlerini tetikler
- **Web İçeriği İstismarı**: İstismar edilmiş web sayfalarında gömülü promptlar, AI davranışını kazıma sırasında manipüle eder
- **E-posta Tabanlı Saldırılar**: E-postalardaki zararlı promptlar, AI asistanlarının bilgi sızdırmasına veya yetkisiz işlemler yapmasına neden olur










**Saldırı Mekanizmaları:**
- **Meta Veri Manipülasyonu**: Saldırganlar araç tanımları, parametre tanımları veya kullanım örneklerine zararlı talimatlar enjekte eder
- **Görünmez Talimatlar**: İnsan kullanıcılar tarafından görünmeyen ama AI modelleri tarafından işlenen araç meta verilerindeki gizli promptlar
- **Dinamik Araç Değişiklikleri ("Rug Pulls")**: Kullanıcılarca onaylanan araçlar, sonradan kullanıcı fark etmeden kötü amaçlı işlemler yapmak üzere değiştirilir


**Barındırılan Sunucu Riskleri**: Uzaktan MCP sunucuları, araç tanımları ilk kullanıcı onayından sonra güncellenebildiği için artırılmış riskler sunar ve bu durum daha önce güvenli olan araçların kötü amaçlı hale gelmesine neden olabilir. Kapsamlı analiz için bkz. [Araç Zehirleme Saldırıları (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Araç Enjeksiyonu Saldırısı Diyagramı](../../../translated_images/tr/tool-injection.3b0b4a6b24de6bef.webp)

#### **Ek AI Saldırı Vektörleri**

- **Çapraz Alan İstem Enjeksiyonu (XPIA)**: Güvenlik kontrollerini aşmak için birden çok alanın içeriğini kullanan karmaşık saldırılar
- **Dinamik Yetenek Değişikliği**: Başlangıçtaki güvenlik değerlendirmelerinden kaçan araç yeteneklerinde gerçek zamanlı değişiklikler
- **Bağlam Penceresi Zehirlenmesi**: Kötü amaçlı talimatları gizlemek için büyük bağlam pencerelerini manipüle eden saldırılar
- **Model Karışıklığı Saldırıları**: Öngörülemeyen veya güvensiz davranışlar yaratmak için model sınırlamalarının sömürülmesi


### AI Güvenlik Riski Etkisi

**Yüksek Etkili Sonuçlar:**
- **Veri Dışa Aktarımı**: Yetkisiz erişim ve hassas kurumsal veya kişisel verilerin çalınması
- **Gizlilik İhlalleri**: Kişisel olarak tanımlanabilir bilgilerin (PII) ve gizli iş verilerinin açığa çıkması  
- **Sistem Manipülasyonu**: Kritik sistemler ve iş akışlarında istenmeyen değişiklikler
- **Kimlik Bilgisi Hırsızlığı**: Kimlik doğrulama belirteçleri ve hizmet kimlik bilgilerinin ele geçirilmesi
- **Yanal Hareket**: Ele geçirilmiş AI sistemlerinin daha geniş ağ saldırıları için dayanak olarak kullanılması

### Microsoft AI Güvenlik Çözümleri

#### **AI İstem Kalkanları: Enjeksiyon Saldırılarında Gelişmiş Koruma**

Microsoft **AI İstem Kalkanları**, doğrudan ve dolaylı istem enjeksiyonu saldırılarına çoklu güvenlik katmanlarıyla kapsamlı savunma sağlar:

##### **Temel Koruma Mekanizmaları:**

1. **Gelişmiş Algılama ve Filtreleme**
   - Makine öğrenimi algoritmaları ve NLP teknikleri, dış içerikteki kötü amaçlı talimatları algılar
   - Gömülü tehditler için belgelerin, web sayfalarının, e-postaların ve veri kaynaklarının gerçek zamanlı analizi
   - Meşru ve kötü amaçlı istem kalıplarının bağlamsal olarak anlaşılması

2. **Spotlight Teknikleri**  
   - Güvenilen sistem talimatları ile potansiyel olarak ele geçirilmiş dış girdiler arasında ayrım yapar
   - Kötü amaçlı içeriği izole ederken model alaka düzeyini artıran metin dönüştürme yöntemleri
   - AI sistemlerinin doğru talimat hiyerarşisini korumasına ve enjeksiyon komutlarını görmezden gelmesine yardımcı olur

3. **Ayraç ve Veri İşaretleme Sistemleri**
   - Güvenilen sistem mesajları ile dış girdi metni arasında açık sınır tanımı
   - Güvenilen ve güvenilmeyen veri kaynaklarının sınırlarını vurgulayan özel işaretler
   - Talimat karışıklığını ve yetkisiz komut yürütmeyi önler

4. **Sürekli Tehdit İstihbaratı**
   - Microsoft sürekli olarak ortaya çıkan saldırı modellerini izler ve savunmaları günceller
   - Yeni enjeksiyon teknikleri ve saldırı vektörleri için proaktif tehdit avcılığı
   - Evrimleşen tehditlere karşı etkinliği sürdürmek için düzenli güvenlik modeli güncellemeleri

5. **Azure İçerik Güvenliği Entegrasyonu**
   - Kapsamlı Azure AI İçerik Güvenliği paketi parçası
   - Jailbreak girişimleri, zararlı içerik ve güvenlik politikası ihlalleri için ek algılama
   - AI uygulama bileşenleri arasında birleştirilmiş güvenlik kontrolleri

**Uygulama Kaynakları**: [Microsoft İstem Kalkanları Belgeleri](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft İstem Kalkanları Koruması](../../../translated_images/tr/prompt-shield.ff5b95be76e9c78c.webp)


## Gelişmiş MCP Güvenlik Tehditleri

### Oturum Çalma Açıkları

**Oturum çalma**, durumsal MCP uygulamalarında yetkisiz tarafların meşru oturum kimliklerini ele geçirip kötüye kullanarak istemcileri taklit edip yetkisiz işlemler gerçekleştirmesi kritik bir saldırı vektörüdür.

#### **Saldırı Senaryoları ve Riskler**

- **Oturum Çalma İstem Enjeksiyonu**: Çalınan oturum kimlikleri ile saldırganlar, oturum durumunu paylaşan sunuculara kötü amaçlı olaylar enjekte ederek zararlı eylemler tetikleyebilir veya hassas verilere erişebilir
- **Doğrudan Taklit**: Çalınan oturum kimlikleri, kimlik doğrulamayı atlayarak saldırganların meşru kullanıcı olarak doğrudan MCP sunucu çağrıları yapmasına olanak tanır
- **Ele Geçirilmiş Devam Ettirilebilir Akışlar**: Saldırganlar istekleri erken sonlandırabilir ve meşru istemcilerin potansiyel olarak kötü amaçlı içeriklerle devam etmesine neden olabilir

#### **Oturum Yönetimi İçin Güvenlik Kontrolleri**

**Kritik Gereksinimler:**
- **Yetkilendirme Doğrulama**: Yetkilendirme uygulayan MCP sunucuları TÜM gelen istekleri doğrulamalı ve kimlik doğrulama için oturumlara güvenMEMELİDİR
- **Güvenli Oturum Üretimi**: Güvenli rastgele sayı üreteçleri ile kriptografik olarak güvenli, belirlenemez oturum kimlikleri kullanılmalıdır
- **Kullanıcıya Özel Bağlama**: Oturum kimlikleri, `<user_id>:<session_id>` gibi formatlarda kullanıcıya özgü bilgilere bağlanmalı, kullanıcılar arası oturum kötüye kullanımını önlemeli
- **Oturum Yaşam Döngüsü Yönetimi**: Kısıtlı saldırı pencereleri için uygun sona erdirme, döndürme ve geçersiz kılma uygulanmalı
- **İletim Güvenliği**: Oturum kimliği yakalanmasını önlemek için tüm iletişimde HTTPS zorunlu

### Karışmış Vekil Sorunu

**Karışmış vekil sorunu**, MCP sunucularının istemciler ile üçüncü taraf hizmetler arasında kimlik doğrulama vekili olarak hareket ettiği durumlarda ortaya çıkar ve statik istemci kimliklerinin sömürülmesiyle yetkilendirme baypası fırsatları yaratır.

#### **Saldırı Mekanikleri ve Riskler**

- **Çerez Tabanlı Onay Atlama**: Önceki kullanıcı kimlik doğrulaması, saldırganların özel yönlendirme URI’leri ile kötü amaçlı yetkilendirme istekleri yaparak sömürdüğü onay çerezleri oluşturur
- **Yetkilendirme Kodu Hırsızlığı**: Mevcut onay çerezleri, yetkilendirme sunucusunun onay ekranlarını atlamasına ve kodları saldırgan kontrolündeki uç noktalara yönlendirmesine neden olabilir  
- **Yetkisiz API Erişimi**: Çalınan yetkilendirme kodları, açık onay olmadan belirteç değişimi ve kullanıcı taklitlerine olanak sağlar

#### **Azaltma Stratejileri**

**Zorunlu Kontroller:**
- **Açık Onay Gereksinimleri**: Statik istemci kimlikleri kullanan MCP vekil sunucuları, her dinamik kayıtlı istemci için kullanıcı onayı ALMALIDIR
- **OAuth 2.1 Güvenlik Uygulaması**: Tüm yetkilendirme isteklerinde PKCE (Kod Değişim Anahtarı Kanıtı) de dahil olmak üzere güncel OAuth güvenlik en iyi uygulamalarına uyulmalıdır
- **Sıkı İstemci Doğrulama**: Kötüye kullanımı önlemek için yönlendirme URI’leri ve istemci tanımlayıcılarının sıkı doğrulaması uygulanmalıdır

### Belirteç Doğrudan Geçiş Açıkları  

**Belirteç doğrudan geçiş**, MCP sunucularının istemci belirteçlerini uygun doğrulama olmadan kabul edip alt API’lere iletmesiyle MCP yetkilendirme spesifikasyonlarını ihlal eden net bir karşıt örüntüdür.

#### **Güvenlik Etkileri**

- **Kontrol Atlatma**: İstemciden API’lere doğrudan belirteç kullanımı, kritik hız limitleme, doğrulama ve izleme kontrollerini atlar
- **Denetim İzinin Bozulması**: Yukarı akışta verilen belirteçler, istemci tanımlamasını imkânsız kılar ve olay soruşturma yeteneklerini bozar
- **Vekil Tabanlı Veri Dışa Aktarımı**: Doğrulanmamış belirteçler sayesinde kötü niyetli aktörler, sunucuları yetkisiz veri erişimi için vekil olarak kullanabilir
- **Güven Sınırı İhlalleri**: Aşağı akış hizmetlerinin güven varsayımları, belirteç kökenleri doğrulanamadığında ihlal edilebilir
- **Çok Hizmetli Saldırı Yayılımı**: Çok sayıda hizmette kabul edilen ele geçirilmiş belirteçler, yanal hareketliliğe olanak sağlar

#### **Gerekli Güvenlik Kontrolleri**

**Tartışılmaz Gereksinimler:**
- **Belirteç Doğrulama**: MCP sunucuları, açıkça MCP sunucusu için verilmemiş belirteçleri KABUL ETMEMELİDİR
- **Hedef Kitle Doğrulaması**: Belirteç hedef kitlesi iddialarının MCP sunucu kimliğiyle eşleştiği her zaman doğrulanmalıdır
- **Uygun Belirteç Yaşam Döngüsü**: Kısa ömürlü erişim belirteçleri güvenli döndürme uygulamalarıyla kullanılmalıdır


## AI Sistemleri İçin Tedarik Zinciri Güvenliği

Tedarik zinciri güvenliği, geleneksel yazılım bağımlılıklarının ötesine geçerek tüm AI ekosistemini kapsar. Modern MCP uygulamaları, sistem bütünlüğünü tehlikeye atabilecek her AI ile ilgili bileşeni titizlikle doğrulamalı ve izlemelidir.

### Genişletilmiş AI Tedarik Zinciri Bileşenleri

**Geleneksel Yazılım Bağımlılıkları:**
- Açık kaynak kütüphaneler ve çerçeveler
- Konteyner görüntüleri ve temel sistemler  
- Geliştirme araçları ve derleme hatları
- Altyapı bileşenleri ve hizmetler

**AI’ye Özgü Tedarik Zinciri Öğeleri:**
- **Temel Modeller**: Köken doğrulaması gerektiren çeşitli sağlayıcılardan önceden eğitilmiş modeller
- **Gömme Hizmetleri**: Harici vektörleştirme ve anlamsal arama servisleri
- **Bağlam Sağlayıcıları**: Veri kaynakları, bilgi tabanları ve belge depoları  
- **Üçüncü Taraf API’ler**: Harici AI hizmetleri, ML boru hatları ve veri işleme uç noktaları
- **Model Eserleri**: Ağırlıklar, yapılandırmalar ve ince ayarlı model varyantları
- **Eğitim Veri Kaynakları**: Model eğitimi ve ince ayar için kullanılan veri setleri

### Kapsamlı Tedarik Zinciri Güvenlik Stratejisi

#### **Bileşen Doğrulama ve Güven**
- **Köken Doğrulaması**: Tüm AI bileşenlerinin kökeni, lisansı ve bütünlüğü bütünleştirmeden önce doğrulanmalıdır
- **Güvenlik Değerlendirmesi**: Modeller, veri kaynakları ve AI hizmetleri için güvenlik açık taramaları ve incelemeleri yapılmalıdır
- **Reputasyon Analizi**: AI hizmet sağlayıcılarının güvenlik geçmişi ve uygulamaları değerlendirilmelidir
- **Uyumluluk Doğrulaması**: Tüm bileşenlerin organizasyonel güvenlik ve düzenleyici gereksinimleri karşılaması sağlanmalıdır

#### **Güvenli Dağıtım Boru Hatları**  
- **Otomatik CI/CD Güvenliği**: Otomatik dağıtım boru hatlarında güvenlik taraması entegre edilmelidir
- **Eser Bütünlüğü**: Tüm dağıtılan eserler (kod, modeller, yapılandırmalar) için kriptografik doğrulama uygulanmalıdır
- **Aşamalı Dağıtım**: Her aşamada güvenlik doğrulaması ile aşamalı dağıtım stratejileri kullanılmalıdır
- **Güvenilir Eser Depoları**: Yalnızca doğrulanmış, güvenli eser kayıt ve depolarından dağıtım yapılmalıdır

#### **Sürekli İzleme ve Müdahale**
- **Bağımlılık Taraması**: Tüm yazılım ve AI bileşen bağımlılıkları için sürekli güvenlik açığı takibi
- **Model İzleme**: Model davranışı, performans kayması ve güvenlik anomalilerinin sürekli değerlendirilmesi
- **Hizmet Sağlığı Takibi**: Harici AI hizmetlerinin kullanılabilirlik, güvenlik olayları ve politika değişikliklerinin izlenmesi
- **Tehdit İstihbaratı Entegrasyonu**: AI ve ML güvenlik risklerine özgü tehdit beslemelerinin dahil edilmesi

#### **Erişim Denetimi ve En Az Ayrıcalık**
- **Bileşen Düzeyinde İzinler**: Modeller, veriler ve hizmetlere erişim iş gereksinimlerine göre kısıtlanmalıdır
- **Hizmet Hesabı Yönetimi**: Minimum gerekli izinlere sahip özel hizmet hesapları uygulanmalıdır
- **Ağ Segmentasyonu**: AI bileşenleri izole edilmeli ve hizmetler arası ağ erişimi sınırlandırılmalıdır
- **API Geçidi Kontrolleri**: Harici AI hizmetlerine erişimi kontrol ve izlemek için merkezi API geçitleri kullanılmalıdır

#### **Olay Müdahalesi ve Kurtarma**
- **Hızlı Müdahale Prosedürleri**: Ele geçirilmiş AI bileşenlerinin yamalanması veya değiştirilmesi için belirlenmiş süreçler
- **Kimlik Bilgisi Döndürme**: Sırlar, API anahtarları ve hizmet kimlik bilgilerinin otomatik döndürülmesi sistemleri
- **Geri Alma Yeteneği**: AI bileşenlerinin önceki bilinen iyi sürümlerine hızlı dönüş imkanı
- **Tedarik Zinciri İhlali Kurtarma**: Yukarı akış AI hizmeti ihlallerine yanıt için özel prosedürler

### Microsoft Güvenlik Araçları ve Entegrasyon

**GitHub Advanced Security**, kapsamlı tedarik zinciri koruması sağlar:
- **Gizli Taraması**: Depolarda kimlik bilgileri, API anahtarları ve belirteçlerin otomatik tespiti
- **Bağımlılık Taraması**: Açık kaynak bağımlılıkları ve kütüphaneler için güvenlik açığı değerlendirmesi
- **CodeQL Analizi**: Güvenlik açıkları ve kodlama sorunları için statik kod analizi
- **Tedarik Zinciri İçgörüleri**: Bağımlılık sağlığı ve güvenlik durumu görünürlüğü

**Azure DevOps ve Azure Repos Entegrasyonu:**
- Microsoft geliştirme platformları genelinde sorunsuz güvenlik taraması entegrasyonu
- AI iş yükleri için Azure Pipelines içinde otomatik güvenlik kontrolleri
- Güvenli AI bileşen dağıtımı için politika uygulaması

**Microsoft İç Uygulamaları:**
Microsoft, tüm ürünlerde kapsamlı tedarik zinciri güvenlik uygulamaları uygular. Kanıtlanmış yaklaşımlar hakkında bilgi için bkz. [Microsoft'ta Yazılım Tedarik Zincirini Güvenceye Alma Yolculuğu](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Temel Güvenlik En İyi Uygulamaları

MCP uygulamaları, kuruluşunuzun mevcut güvenlik duruşundan miras alır ve üzerine inşa eder. Temel güvenlik uygulamalarının güçlendirilmesi, AI sistemleri ve MCP dağıtımlarının genel güvenliğini önemli ölçüde artırır.

### Temel Güvenlik Temelleri

#### **Güvenli Geliştirme Uygulamaları**
- **OWASP Uyumluluğu**: [OWASP Top 10](https://owasp.org/www-project-top-ten/) web uygulama güvenlik açıklarına karşı koruma
- **AI’ye Özgü Koruyucular**: [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) için kontroller uygulama
- **Güvenli Sırlar Yönetimi**: Belirteçler, API anahtarları ve hassas yapılandırma verileri için adanmış kasalar kullanma
- **Uçtan Uca Şifreleme**: Tüm uygulama bileşenleri ve veri akışları boyunca güvenli iletişim uygulama
- **Girdi Doğrulama**: Tüm kullanıcı girdileri, API parametreleri ve veri kaynaklarının titiz doğrulaması

#### **Altyapı Sertleştirme**
- **Çok Faktörlü Kimlik Doğrulama**: Tüm yönetim ve hizmet hesapları için zorunlu MFA
- **Yama Yönetimi**: İşletim sistemleri, çerçeveler ve bağımlılıklar için otomatik ve zamanında yama uygulaması  
- **Kimlik Sağlayıcı Entegrasyonu**: Kurumsal kimlik sağlayıcıları (Microsoft Entra ID, Active Directory) üzerinden merkezi kimlik yönetimi
- **Ağ Segmentasyonu**: Yanal hareketi sınırlandırmak için MCP bileşenlerinin mantıksal izolasyonu
- **En Az Ayrıcalık İlkesi**: Tüm sistem bileşenleri ve hesaplar için minimal gerekli izinler

#### **Güvenlik İzleme ve Algılama**
- **Kapsamlı Kayıt Tutma**: MCP istemci-sunucu etkileşimleri dahil olmak üzere AI uygulama aktivitelerinin detaylı kaydı
- **SIEM Entegrasyonu**: Anomali tespiti için merkezi güvenlik bilgi ve olay yönetimi
- **Davranışsal Analitik**: Sistem ve kullanıcı davranışındaki alışılmadık kalıpları tespit için AI destekli izleme
- **Tehdit İstihbaratı**: Harici tehdit beslemeleri ve ihlal göstergelerinin (IOC) entegrasyonu
- **Olay Müdahalesi**: Güvenlik olaylarının tespiti, müdahalesi ve kurtarılması için iyi tanımlanmış prosedürler

#### **Sıfır Güven Mimarisi**
- **Asla Güvenme, Her Zaman Doğrula**: Kullanıcılar, aygıtlar ve ağ bağlantılarının sürekli doğrulanması
- **Mikro-Segmentasyon**: Bireysel iş yükleri ve hizmetleri izole eden ayrıntılı ağ kontrolleri
- **Kimlik Merkezli Güvenlik**: Ağ konumu yerine doğrulanmış kimliklere dayalı güvenlik politikaları
- **Sürekli Risk Değerlendirmesi**: Mevcut bağlam ve davranışa dayalı dinamik güvenlik durumu değerlendirmesi
- **Koşullu Erişim**: Risk faktörleri, konum ve cihaz güvenine göre uyarlanan erişim kontrolleri

### Kurumsal Entegrasyon Şablonları

#### **Microsoft Güvenlik Ekosistemi Entegrasyonu**
- **Microsoft Defender for Cloud**: Kapsamlı bulut güvenlik duruş yönetimi
- **Azure Sentinel**: AI iş yükü koruması için bulut tabanlı SIEM ve SOAR yetenekleri
- **Microsoft Entra ID**: Koşullu erişim politikaları ile kurumsal kimlik ve erişim yönetimi
- **Azure Key Vault**: Donanım güvenlik modülü (HSM) destekli merkezi gizli yönetimi
- **Microsoft Purview**: AI veri kaynakları ve iş akışları için veri yönetişimi ve uyumluluk

#### **Uyumluluk ve Yönetişim**
- **Düzenleyici Uyum**: MCP uygulamalarının endüstri özel uyumluluk gereksinimlerini karşılamasını sağlamak (GDPR, HIPAA, SOC 2)

- **Veri Sınıflandırması**: AI sistemleri tarafından işlenen hassas verilerin uygun kategorize edilmesi ve işlenmesi
- **Denetim İzleri**: Düzenleyici uyumluluk ve adli inceleme için kapsamlı kayıt tutma
- **Gizlilik Kontrolleri**: AI sistem mimarisinde gizlilik-ilkeleri tasarımının uygulanması
- **Değişiklik Yönetimi**: AI sistemi değişikliklerinin güvenlik incelemeleri için resmi süreçler

Bu temel uygulamalar, MCP’ye özgü güvenlik kontrollerinin etkinliğini artıran ve AI destekli uygulamalar için kapsamlı koruma sağlayan sağlam bir güvenlik temeli oluşturur.

## Temel Güvenlik Çıkarımları

- **Katmanlı Güvenlik Yaklaşımı**: Temel güvenlik uygulamalarını (güvenli kodlama, en az ayrıcalık, tedarik zinciri doğrulaması, sürekli izleme) AI’ya özgü kontrollerle birleştirerek kapsamlı koruma sağlama

- **AI’ye Özgü Tehdit Manzarası**: MCP sistemleri; istem enjekte etme, araç zehirleme, oturum kaçırma, kafası karışık vekil sorunları, belirteç geçişi açıklıkları ve aşırı izinler dahil benzersiz risklerle karşı karşıyadır ve özel önlemler gerektirir

- **Kimlik Doğrulama ve Yetkilendirme Mükemmelliği**: Dış kimlik sağlayıcıları (Microsoft Entra ID) kullanarak sağlam kimlik doğrulama uygulayın, doğru belirteç doğrulamasını zorunlu kılın ve MCP sunucunuz için açıkça verilmemiş belirteçleri asla kabul etmeyin

- **AI Saldırı Önleme**: Dolaylı istem enjekte etme ve araç zehirleme saldırılarına karşı Microsoft Prompt Shields ve Azure Content Safety’yi devreye alın, araç meta verilerini doğrulayın ve dinamik değişiklikleri izleyin

- **Oturum ve Taşıma Güvenliği**: Kullanıcı kimliklerine bağlı, kriptografik olarak güvenli, deterministik olmayan oturum kimlikleri kullanın, uygun oturum yaşam döngüsü yönetimini uygulayın ve oturumları asla kimlik doğrulamada kullanmayın

- **OAuth Güvenliği En İyi Uygulamaları**: Dinamik olarak kayıtlı istemciler için açık kullanıcı onayıyla kafası karışık vekil saldırılarını önleyin, PKCE ile doğru OAuth 2.1 uygulayın ve yönlendirme URI doğrulamasında sıkı kurallar uygulayın  

- **Belirteç Güvenlik İlkeleri**: Belirteç geçişi anti-pattern’lerinden kaçının, belirteç alıcı beyanlarını doğrulayın, kısa ömürlü belirteçler ve güvenli döndürme uygulayın ve net güven sınırları koruyun

- **Kapsamlı Tedarik Zinciri Güvenliği**: Tüm AI ekosistemi bileşenlerini (modeller, gömme yapılar, bağlam sağlayıcıları, dış API'ler) geleneksel yazılım bağımlılıkları kadar yüksek güvenlik dikkat ve özeniyle ele alın

- **Sürekli Evrim**: Hızla gelişen MCP spesifikasyonlarını takip edin, güvenlik topluluğu standartlarına katkıda bulunun ve protokol olgunlaştıkça uyarlanabilir güvenlik duruşlarını sürdürün

- **Microsoft Güvenlik Entegrasyonu**: Microsoft'un kapsamlı güvenlik ekosisteminden yararlanın (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) MCP dağıtım korumasını artırmak için

## Kapsamlı Kaynaklar

### **Resmi MCP Güvenlik Dokümantasyonu**
- [MCP Spesifikasyonu (Güncel: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Güvenlik En İyi Uygulamaları](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Yetkilendirme Spesifikasyonu](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub Deposu](https://github.com/modelcontextprotocol)

### **OWASP MCP Güvenlik Kaynakları**
- [OWASP MCP Azure Güvenlik Rehberi](https://microsoft.github.io/mcp-azure-security-guide/) - Azure uygulama rehberi ile kapsamlı OWASP MCP İlk 10
- [OWASP MCP İlk 10](https://owasp.org/www-project-mcp-top-10/) - Resmi OWASP MCP güvenlik riskleri
- [MCP Güvenlik Zirvesi Atölyesi (Sherpa)](https://azure-samples.github.io/sherpa/) - Azure üzerinde MCP için uygulamalı güvenlik eğitimi

### **Güvenlik Standartları ve En İyi Uygulamalar**
- [OAuth 2.0 Güvenlik En İyi Uygulamaları (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP İlk 10 Web Uygulaması Güvenliği](https://owasp.org/www-project-top-ten/)
- [OWASP Büyük Dil Modelleri İçin İlk 10](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Dijital Savunma Raporu](https://aka.ms/mddr)

### **AI Güvenlik Araştırması ve Analizi**
- [MCP'de İstem Enjeksiyonu (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Araç Zehirleme Saldırıları (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Güvenlik Araştırması Bilgilendirmesi (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Güvenlik Çözümleri**
- [Microsoft Prompt Shields Dokümantasyonu](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Hizmeti](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Güvenliği](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Belirteç Yönetimi En İyi Uygulamaları](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Uygulama Kılavuzları ve Eğitimler**
- [Azure API Yönetimi MCP Kimlik Doğrulama Geçidi Olarak](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID ile MCP Sunucu Kimlik Doğrulaması](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Güvenli Belirteç Depolama ve Şifreleme (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps ve Tedarik Zinciri Güvenliği**
- [Azure DevOps Güvenliği](https://azure.microsoft.com/products/devops)
- [Azure Repos Güvenliği](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Tedarik Zinciri Güvenlik Yolculuğu](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Ek Güvenlik Dokümantasyonu**

Kapsamlı güvenlik rehberliği için, bu bölümdeki uzmanlaşmış belgelere başvurun:

- **[CIMD ve DCR Yetkilendirme Örneği](./samples/cimd-dcr-auth/README.md)** - Tercih edilen İstemci ID Meta Verileri Dökümanları ile kullanımdan kalkmış Dinamik İstemci Kaydı yedeğini karşılaştıran çalıştırılabilir TypeScript MCP `2026-07-28` kaynak sunucu
- **[MCP Güvenlik En İyi Uygulamaları](./mcp-security-best-practices.md)** - MCP uygulamaları için tam güvenlik en iyi uygulamalar
- **[Azure Content Safety Uygulaması](./azure-content-safety-implementation.md)** - Azure Content Safety entegrasyonu için pratik uygulama örnekleri  
- **[MCP Güvenlik Kontrolleri](./mcp-security-controls.md)** - MCP dağıtımları için en yeni güvenlik kontrolleri ve teknikleri
- **[MCP En İyi Uygulamalar Hızlı Referans](./mcp-best-practices.md)** - Temel MCP güvenlik uygulamaları için hızlı referans kılavuzu
- **[BlueHat 2026: AI’nin geleceğini güvence altına almak: Derinlemesine savunma desenleri ile MCP güvenliği](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Microsoft Güvenlik Müdahale Merkezi (MSRC) tarafından derinlemesine savunma desenleri

### **Uygulamalı Güvenlik Eğitimi**

- **[MCP Güvenlik Zirvesi Atölyesi (Sherpa)](https://azure-samples.github.io/sherpa/)** - Base Camp'ten Zirveye kadar ilerleyen kamplarla Azure'da MCP sunucularını güvence altına almak için kapsamlı uygulamalı atölye çalışması
- **[OWASP MCP Azure Güvenlik Rehberi](https://microsoft.github.io/mcp-azure-security-guide/)** - Tüm OWASP MCP İlk 10 riskleri için referans mimarisi ve uygulama rehberi

---

## Sonraki Adım

Sonraki: [Bölüm 3: Başlarken](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->