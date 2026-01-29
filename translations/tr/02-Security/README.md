# MCP Güvenliği: AI Sistemleri için Kapsamlı Koruma

[![MCP Security Best Practices](../../../translated_images/tr/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Bu dersin videosunu izlemek için yukarıdaki resme tıklayın)_

Güvenlik, AI sistem tasarımının temelidir; bu nedenle ikinci bölümümüz olarak öncelik veriyoruz. Bu, Microsoft'un [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/) kapsamındaki **Secure by Design** (Tasarımda Güvenlik) ilkesine uygundur.

Model Context Protocol (MCP), AI destekli uygulamalara güçlü yeni yetenekler getirirken, geleneksel yazılım risklerinin ötesine geçen benzersiz güvenlik zorlukları da sunar. MCP sistemleri, güvenli kodlama, en az ayrıcalık, tedarik zinciri güvenliği gibi yerleşik güvenlik endişelerinin yanı sıra prompt enjeksiyonu, araç zehirlenmesi, oturum kaçırma, confused deputy saldırıları, token geçişi açıkları ve dinamik yetenek değişikliği gibi AI'ya özgü yeni tehditlerle karşı karşıyadır.

Bu ders, MCP uygulamalarındaki en kritik güvenlik risklerini inceler—kimlik doğrulama, yetkilendirme, aşırı izinler, dolaylı prompt enjeksiyonu, oturum güvenliği, confused deputy sorunları, token yönetimi ve tedarik zinciri açıklarını kapsar. Microsoft çözümleri olan Prompt Shields, Azure Content Safety ve GitHub Advanced Security gibi araçları kullanarak bu riskleri azaltmak için uygulanabilir kontroller ve en iyi uygulamaları öğreneceksiniz.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- **MCP'ye Özgü Tehditleri Tanımlama**: Prompt enjeksiyonu, araç zehirlenmesi, aşırı izinler, oturum kaçırma, confused deputy sorunları, token geçişi açıkları ve tedarik zinciri riskleri dahil MCP sistemlerindeki benzersiz güvenlik risklerini tanıyın
- **Güvenlik Kontrollerini Uygulama**: Güçlü kimlik doğrulama, en az ayrıcalık erişimi, güvenli token yönetimi, oturum güvenliği kontrolleri ve tedarik zinciri doğrulaması dahil etkili azaltma yöntemlerini uygulayın
- **Microsoft Güvenlik Çözümlerinden Yararlanma**: MCP iş yükü koruması için Microsoft Prompt Shields, Azure Content Safety ve GitHub Advanced Security'yi anlayın ve dağıtın
- **Araç Güvenliğini Doğrulama**: Araç meta verisi doğrulamasının önemini, dinamik değişikliklerin izlenmesini ve dolaylı prompt enjeksiyonu saldırılarına karşı savunmayı kavrayın
- **En İyi Uygulamaları Entegre Etme**: Yerleşik güvenlik temellerini (güvenli kodlama, sunucu sertleştirme, sıfır güven) MCP'ye özgü kontrollerle birleştirerek kapsamlı koruma sağlayın

# MCP Güvenlik Mimarisi ve Kontrolleri

Modern MCP uygulamaları, hem geleneksel yazılım güvenliği hem de AI'ya özgü tehditleri ele alan katmanlı güvenlik yaklaşımları gerektirir. Hızla gelişen MCP spesifikasyonu, güvenlik kontrollerini olgunlaştırmaya devam ederek kurumsal güvenlik mimarileri ve yerleşik en iyi uygulamalarla daha iyi entegrasyon sağlar.

[Microsoft Digital Defense Report](https://aka.ms/mddr) araştırması, **rapor edilen ihlallerin %98'inin sağlam güvenlik hijyeni ile önlenebileceğini** göstermektedir. En etkili koruma stratejisi, temel güvenlik uygulamalarını MCP'ye özgü kontrollerle birleştirmektir—kanıtlanmış temel güvenlik önlemleri genel güvenlik riskini azaltmada en etkili yöntemdir.

## Mevcut Güvenlik Durumu

> **Not:** Bu bilgiler **18 Aralık 2025** itibarıyla MCP güvenlik standartlarını yansıtmaktadır. MCP protokolü hızla gelişmeye devam etmekte olup, gelecekteki uygulamalar yeni kimlik doğrulama desenleri ve geliştirilmiş kontroller getirebilir. En güncel rehberlik için her zaman mevcut [MCP Spesifikasyonu](https://spec.modelcontextprotocol.io/), [MCP GitHub deposu](https://github.com/modelcontextprotocol) ve [güvenlik en iyi uygulamaları dokümantasyonu](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) başvurunuz.

### MCP Kimlik Doğrulama Evrimi

MCP spesifikasyonu, kimlik doğrulama ve yetkilendirme yaklaşımında önemli ölçüde evrilmiştir:

- **Orijinal Yaklaşım**: Erken spesifikasyonlar, geliştiricilerin özel kimlik doğrulama sunucuları uygulamasını gerektiriyordu; MCP sunucuları ise kullanıcı kimlik doğrulamasını doğrudan yöneten OAuth 2.0 Yetkilendirme Sunucuları olarak görev yapıyordu
- **Mevcut Standart (2025-11-25)**: Güncellenen spesifikasyon, MCP sunucularının kimlik doğrulamayı Microsoft Entra ID gibi harici kimlik sağlayıcılarına devretmesine izin vererek güvenlik duruşunu iyileştirir ve uygulama karmaşıklığını azaltır
- **Taşıma Katmanı Güvenliği**: Yerel (STDIO) ve uzak (Streamable HTTP) bağlantılar için uygun kimlik doğrulama desenleriyle güvenli taşıma mekanizmalarına gelişmiş destek

## Kimlik Doğrulama ve Yetkilendirme Güvenliği

### Mevcut Güvenlik Zorlukları

Modern MCP uygulamaları çeşitli kimlik doğrulama ve yetkilendirme zorluklarıyla karşı karşıyadır:

### Riskler ve Tehdit Vektörleri

- **Yanlış Yapılandırılmış Yetkilendirme Mantığı**: MCP sunucularındaki hatalı yetkilendirme uygulaması hassas verileri açığa çıkarabilir ve erişim kontrollerini yanlış uygulayabilir
- **OAuth Token İhlali**: Yerel MCP sunucu token hırsızlığı, saldırganların sunucuları taklit etmesine ve alt hizmetlere erişmesine olanak tanır
- **Token Geçişi Açıkları**: Yanlış token kullanımı güvenlik kontrollerinin atlanmasına ve hesap verebilirlik boşluklarına yol açar
- **Aşırı İzinler**: Gereğinden fazla yetkilendirilmiş MCP sunucuları en az ayrıcalık prensibini ihlal eder ve saldırı yüzeyini genişletir

#### Token Geçişi: Kritik Bir Anti-Desen

**Token geçişi, mevcut MCP yetkilendirme spesifikasyonunda ciddi güvenlik sonuçları nedeniyle açıkça yasaktır:**

##### Güvenlik Kontrolü Atlatma  
- MCP sunucuları ve alt API'ler, doğru token doğrulamasına bağlı kritik güvenlik kontrolleri (oran sınırlama, istek doğrulama, trafik izleme) uygular  
- İstemci ile API arasında doğrudan token kullanımı bu temel korumaları atlar ve güvenlik mimarisini zayıflatır

##### Hesap Verebilirlik ve Denetim Zorlukları  
- MCP sunucuları, yukarı akışta verilen tokenları kullanan istemcileri ayırt edemez, denetim izlerini bozar  
- Alt kaynak sunucu günlükleri, gerçek MCP sunucu aracıları yerine yanıltıcı istek kaynakları gösterir  
- Olay incelemesi ve uyumluluk denetimleri önemli ölçüde zorlaşır

##### Veri Sızdırma Riskleri  
- Doğrulanmamış token iddiaları, çalınan tokenlara sahip kötü niyetli aktörlerin MCP sunucularını veri sızdırma aracı olarak kullanmasına izin verir  
- Güven sınırı ihlalleri, yetkisiz erişim desenlerinin güvenlik kontrollerini atlamasına yol açar

##### Çoklu Hizmet Saldırı Vektörleri  
- Birden fazla hizmet tarafından kabul edilen ele geçirilmiş tokenlar, bağlı sistemler arasında yatay hareketliliğe olanak tanır  
- Token kökenleri doğrulanamadığında hizmetler arası güven varsayımları ihlal edilebilir

### Güvenlik Kontrolleri ve Azaltmalar

**Kritik Güvenlik Gereksinimleri:**

> **ZORUNLU**: MCP sunucuları, açıkça MCP sunucusu için verilmemiş herhangi bir tokenı **KABUL ETMEMELİDİR**

#### Kimlik Doğrulama ve Yetkilendirme Kontrolleri

- **Titiz Yetkilendirme İncelemesi**: MCP sunucu yetkilendirme mantığının kapsamlı denetimlerini yaparak yalnızca amaçlanan kullanıcılar ve istemcilerin hassas kaynaklara erişmesini sağlayın  
  - **Uygulama Rehberi**: [Azure API Management ile MCP Sunucuları için Kimlik Doğrulama Geçidi](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)  
  - **Kimlik Entegrasyonu**: [MCP Sunucu Kimlik Doğrulaması için Microsoft Entra ID Kullanımı](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Güvenli Token Yönetimi**: [Microsoft'un token doğrulama ve yaşam döngüsü en iyi uygulamalarını](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens) uygulayın  
  - Token hedef kitle iddialarının MCP sunucu kimliğiyle eşleştiğini doğrulayın  
  - Uygun token döndürme ve sona erme politikaları uygulayın  
  - Token tekrar oynatma saldırılarını ve yetkisiz kullanımı önleyin

- **Korunan Token Depolama**: Tokenları hem dinlenme hem de iletim sırasında şifreleyerek güvenli depolayın  
  - **En İyi Uygulamalar**: [Güvenli Token Depolama ve Şifreleme Kılavuzları](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Erişim Kontrolü Uygulaması

- **En Az Ayrıcalık Prensibi**: MCP sunucularına yalnızca amaçlanan işlevsellik için gereken minimum izinleri verin  
  - İzinlerin düzenli olarak gözden geçirilmesi ve güncellenmesi ile ayrıcalık artışını önleyin  
  - **Microsoft Dokümantasyonu**: [Güvenli En Az Ayrıcalıklı Erişim](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Rol Tabanlı Erişim Kontrolü (RBAC)**: İnce taneli rol atamaları uygulayın  
  - Rolleri belirli kaynaklar ve eylemlerle sıkı şekilde sınırlandırın  
  - Saldırı yüzeyini genişleten geniş veya gereksiz izinlerden kaçının

- **Sürekli İzin İzleme**: Sürekli erişim denetimi ve izleme uygulayın  
  - Anomaliler için izin kullanım desenlerini izleyin  
  - Aşırı veya kullanılmayan ayrıcalıkları hızlıca giderin

## AI'ya Özgü Güvenlik Tehditleri

### Prompt Enjeksiyonu ve Araç Manipülasyonu Saldırıları

Modern MCP uygulamaları, geleneksel güvenlik önlemlerinin tam olarak karşılayamadığı gelişmiş AI'ya özgü saldırı vektörleriyle karşı karşıyadır:

#### **Dolaylı Prompt Enjeksiyonu (Çapraz Alan Prompt Enjeksiyonu)**

**Dolaylı Prompt Enjeksiyonu**, MCP destekli AI sistemlerinde en kritik açıklardan biridir. Saldırganlar, AI sistemlerinin daha sonra meşru komutlar olarak işlediği dış içeriklere—belgeler, web sayfaları, e-postalar veya veri kaynakları—zararlı talimatlar gömer.

**Saldırı Senaryoları:**  
- **Belge Tabanlı Enjeksiyon**: İşlenen belgelerde gizlenmiş kötü niyetli talimatlar, AI'nın istenmeyen eylemler yapmasına neden olur  
- **Web İçeriği Sömürüsü**: Kazınan web sayfalarında gömülü promptlar AI davranışını manipüle eder  
- **E-posta Tabanlı Saldırılar**: E-postalardaki zararlı promptlar AI asistanlarının bilgi sızdırmasına veya yetkisiz işlemler yapmasına yol açar  
- **Veri Kaynağı Kontaminasyonu**: Kompromize edilmiş veritabanları veya API'ler AI sistemlerine bozuk içerik sağlar

**Gerçek Dünya Etkisi**: Bu saldırılar veri sızdırma, gizlilik ihlalleri, zararlı içerik üretimi ve kullanıcı etkileşimlerinin manipülasyonu ile sonuçlanabilir. Ayrıntılı analiz için bkz. [MCP'de Prompt Enjeksiyonu (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/tr/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Araç Zehirlenmesi Saldırıları**

**Araç Zehirlenmesi**, MCP araçlarını tanımlayan meta verilere yönelik saldırılardır; LLM'lerin araç açıklamalarını ve parametrelerini nasıl yorumladığını kötüye kullanır.

**Saldırı Mekanizmaları:**  
- **Meta Veri Manipülasyonu**: Saldırganlar, araç açıklamalarına, parametre tanımlarına veya kullanım örneklerine zararlı talimatlar enjekte eder  
- **Görünmez Talimatlar**: İnsan kullanıcılar tarafından görünmeyen ancak AI modelleri tarafından işlenen gizli promptlar  
- **Dinamik Araç Değişikliği ("Rug Pulls")**: Kullanıcılarca onaylanan araçlar, kullanıcı farkında olmadan kötü niyetli eylemler yapmak üzere sonradan değiştirilir  
- **Parametre Enjeksiyonu**: Model davranışını etkileyen araç parametre şemalarına gömülü zararlı içerik

**Barındırılan Sunucu Riskleri**: Uzaktan MCP sunucuları, araç tanımlarının ilk kullanıcı onayından sonra güncellenebilmesi nedeniyle risk taşır; önceden güvenli olan araçlar kötü niyetli hale gelebilir. Kapsamlı analiz için bkz. [Araç Zehirlenmesi Saldırıları (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/tr/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Ek AI Saldırı Vektörleri**

- **Çapraz Alan Prompt Enjeksiyonu (XPIA)**: Birden fazla alandan içerik kullanarak güvenlik kontrollerini aşan gelişmiş saldırılar  
- **Dinamik Yetenek Değişikliği**: Araç yeteneklerinde gerçek zamanlı değişiklikler, ilk güvenlik değerlendirmelerinden kaçabilir  
- **Kapsam Penceresi Zehirlenmesi**: Büyük kapsam pencerelerini manipüle ederek zararlı talimatları gizleyen saldırılar  
- **Model Karışıklığı Saldırıları**: Model sınırlamalarını kullanarak öngörülemez veya güvensiz davranışlar oluşturma

### AI Güvenlik Risklerinin Etkisi

**Yüksek Etkili Sonuçlar:**  
- **Veri Sızdırma**: Hassas kurumsal veya kişisel verilere yetkisiz erişim ve hırsızlık  
- **Gizlilik İhlalleri**: Kişisel tanımlanabilir bilgilerin (PII) ve gizli iş verilerinin açığa çıkması  
- **Sistem Manipülasyonu**: Kritik sistemler ve iş akışlarında istenmeyen değişiklikler  
- **Kimlik Bilgisi Hırsızlığı**: Kimlik doğrulama tokenları ve hizmet kimlik bilgilerinin ele geçirilmesi  
- **Yatay Hareketlilik**: Ele geçirilmiş AI sistemlerinin daha geniş ağ saldırıları için pivot olarak kullanılması

### Microsoft AI Güvenlik Çözümleri

#### **AI Prompt Shields: Enjeksiyon Saldırılarına Karşı Gelişmiş Koruma**

Microsoft **AI Prompt Shields**, doğrudan ve dolaylı prompt enjeksiyonu saldırılarına karşı çok katmanlı güvenlik savunması sağlar:

##### **Temel Koruma Mekanizmaları:**

1. **Gelişmiş Tespit ve Filtreleme**  
   - Makine öğrenimi algoritmaları ve NLP teknikleri, dış içerikteki zararlı talimatları tespit eder  
   - Belgeler, web sayfaları, e-postalar ve veri kaynaklarının gerçek zamanlı analizi  
   - Meşru ve zararlı prompt desenlerinin bağlamsal ayrımı

2. **Spotlight Teknikleri**  
   - Güvenilir sistem talimatları ile potansiyel olarak tehlikeli dış girdileri ayırt eder  
   - Metin dönüşüm yöntemleri, model alakasını artırırken zararlı içeriği izole eder  
   - AI sistemlerinin doğru talimat hiyerarşisini korumasına ve enjekte edilmiş komutları görmezden gelmesine yardımcı olur

3. **Ayırıcı ve Veri İşaretleme Sistemleri**  
   - Güvenilir sistem mesajları ile dış girdi metni arasında açık sınır tanımı  
   - Güvenilir ve güvensiz veri kaynakları arasındaki sınırları vurgulayan özel işaretleyiciler  
   - Talimat karışıklığını ve yetkisiz komut yürütmeyi önler

4. **Sürekli Tehdit İstihbaratı**  
   - Microsoft, ortaya çıkan saldırı desenlerini sürekli izler ve savunmaları günceller  
   - Yeni enjeksiyon teknikleri ve saldırı vektörleri için proaktif tehdit avcılığı  
   - Gelişen tehditlere karşı etkinliği korumak için düzenli güvenlik modeli güncellemeleri

5. **Azure Content Safety Entegrasyonu**  
   - Kapsamlı Azure AI Content Safety paketinin parçası  
   - Jailbreak denemeleri, zararlı içerik ve güvenlik politikası ihlalleri için ek tespit  
   - AI uygulama bileşenleri arasında birleşik güvenlik kontrolleri

**Uygulama Kaynakları**: [Microsoft Prompt Shields Dokümantasyonu](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/tr/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Gelişmiş MCP Güvenlik Tehditleri

### Oturum Kaçırma Açıkları

**Oturum kaçırma**, durum bilgisi tutan MCP uygulamalarında kritik bir saldırı vektörüdür; yetkisiz taraflar meşru oturum kimlik bilgilerini ele geçirip kötüye kullanarak istemcileri taklit eder ve yetkisiz işlemler yapar.

#### **Saldırı Senaryoları ve Riskler**

- **Oturum Kaçırma Prompt Enjeksiyonu**: Çalınan oturum kimlik bilgilerine sahip saldırganlar, oturum durumunu paylaşan sunuculara zararlı olaylar enjekte ederek zararlı eylemler tetikleyebilir veya hassas verilere erişebilir  
- **Doğrudan Taklit**: Çalınan oturum kimlik bilgileri, kimlik doğrulamayı atlayarak doğrudan MCP sunucu çağrılarına olanak tanır ve saldırganları meşru kullanıcı gibi gösterir  
- **Kompromize Edilmiş Devam Ettirilebilir Akışlar**: Saldırganlar istekleri erken sonlandırarak, meşru istemcilerin potansiyel olarak zararlı içerikle devam etmesine neden olabilir

#### **Oturum Yönetimi için Güvenlik Kontrolleri**

**Kritik Gereksinimler:**
- **Yetkilendirme Doğrulaması**: Yetkilendirmeyi uygulayan MCP sunucuları TÜM gelen istekleri doğrulamalı ve kimlik doğrulama için oturumlara GÜVENMEMELİDİR  
- **Güvenli Oturum Oluşturma**: Güvenli rastgele sayı üreteçleri ile oluşturulan kriptografik olarak güvenli, belirlenemez oturum kimlikleri kullanın  
- **Kullanıcıya Özel Bağlama**: Oturum kimliklerini `<user_id>:<session_id>` gibi formatlarla kullanıcıya özel bilgilerle bağlayarak kullanıcılar arası oturum kötüye kullanımını önleyin  
- **Oturum Yaşam Döngüsü Yönetimi**: Açıklık pencerelerini sınırlamak için uygun sona erdirme, döndürme ve geçersiz kılma uygulayın  
- **İletim Güvenliği**: Oturum kimliği yakalanmasını önlemek için tüm iletişimde HTTPS zorunludur  

### Karışık Vekil Problemi

**Karışık vekil problemi**, MCP sunucularının istemciler ile üçüncü taraf hizmetler arasında kimlik doğrulama vekili olarak hareket ettiği durumlarda ortaya çıkar ve statik istemci kimliği kötüye kullanımı yoluyla yetkilendirme atlatma fırsatları yaratır.

#### **Saldırı Mekanikleri ve Riskler**

- **Çerez Tabanlı Onay Atlatma**: Önceki kullanıcı kimlik doğrulaması, saldırganların kötü niyetli yetkilendirme istekleriyle oluşturulmuş yönlendirme URI'leri kullanarak istismar ettiği onay çerezleri oluşturur  
- **Yetkilendirme Kodu Hırsızlığı**: Mevcut onay çerezleri, yetkilendirme sunucularının onay ekranlarını atlayarak kodları saldırgan kontrolündeki uç noktalara yönlendirmesine neden olabilir  
- **Yetkisiz API Erişimi**: Çalınan yetkilendirme kodları, açık onay olmadan token değişimi ve kullanıcı taklidi yapılmasını sağlar  

#### **Azaltma Stratejileri**

**Zorunlu Kontroller:**  
- **Açık Onay Gereksinimleri**: Statik istemci kimlikleri kullanan MCP vekil sunucuları, her dinamik kayıtlı istemci için kullanıcı onayı ALMALIDIR  
- **OAuth 2.1 Güvenlik Uygulaması**: Tüm yetkilendirme isteklerinde PKCE (Kod Değişimi İçin Kanıt Anahtarı) dahil olmak üzere güncel OAuth güvenlik en iyi uygulamalarını takip edin  
- **Sıkı İstemci Doğrulaması**: İstismarları önlemek için yönlendirme URI'leri ve istemci kimliklerinin titiz doğrulamasını uygulayın  

### Token Geçişi Güvenlik Açıkları  

**Token geçişi**, MCP sunucularının istemci tokenlarını uygun doğrulama yapmadan kabul edip aşağı akış API'lerine iletmesiyle ortaya çıkan açıkça yanlış bir uygulamadır ve MCP yetkilendirme spesifikasyonlarını ihlal eder.

#### **Güvenlik Sonuçları**

- **Kontrol Atlatma**: İstemci ile API arasında doğrudan token kullanımı kritik oran sınırlama, doğrulama ve izleme kontrollerini atlar  
- **Denetim İzinin Bozulması**: Yukarı akışta verilen tokenlar istemci tanımlamasını imkansız hale getirir, olay inceleme yeteneklerini bozar  
- **Vekil Tabanlı Veri Sızdırma**: Doğrulanmamış tokenlar, kötü niyetli aktörlerin sunucuları yetkisiz veri erişimi için vekil olarak kullanmasına olanak tanır  
- **Güven Sınırı İhlalleri**: Token kökenleri doğrulanamadığında aşağı akış hizmetlerinin güven varsayımları ihlal edilebilir  
- **Çok Hizmetli Saldırı Yayılımı**: Birden fazla hizmette kabul edilen ele geçirilmiş tokenlar yatay hareketliliği sağlar  

#### **Gerekli Güvenlik Kontrolleri**

**Tartışmasız Gereksinimler:**  
- **Token Doğrulama**: MCP sunucuları, açıkça MCP sunucusu için verilmemiş tokenları KABUL ETMEMELİDİR  
- **Hedef Kitle Doğrulaması**: Token hedef kitle iddialarının MCP sunucusunun kimliğiyle eşleştiğini her zaman doğrulayın  
- **Uygun Token Yaşam Döngüsü**: Kısa ömürlü erişim tokenları ve güvenli döndürme uygulayın  

## AI Sistemleri için Tedarik Zinciri Güvenliği

Tedarik zinciri güvenliği, geleneksel yazılım bağımlılıklarının ötesine geçerek tüm AI ekosistemini kapsayacak şekilde evrilmiştir. Modern MCP uygulamaları, sistem bütünlüğünü tehlikeye atabilecek potansiyel açıklıkları önlemek için AI ile ilgili tüm bileşenleri titizlikle doğrulamalı ve izlemelidir.

### Genişletilmiş AI Tedarik Zinciri Bileşenleri

**Geleneksel Yazılım Bağımlılıkları:**  
- Açık kaynak kütüphaneler ve çerçeveler  
- Konteyner imajları ve temel sistemler  
- Geliştirme araçları ve derleme hatları  
- Altyapı bileşenleri ve hizmetler  

**AI'ya Özgü Tedarik Zinciri Öğeleri:**  
- **Temel Modeller**: Kaynak doğrulaması gereken çeşitli sağlayıcılardan önceden eğitilmiş modeller  
- **Embedding Hizmetleri**: Harici vektörleştirme ve anlamsal arama hizmetleri  
- **Bağlam Sağlayıcıları**: Veri kaynakları, bilgi tabanları ve belge depoları  
- **Üçüncü Taraf API'ler**: Harici AI hizmetleri, ML hatları ve veri işleme uç noktaları  
- **Model Artefaktları**: Ağırlıklar, yapılandırmalar ve ince ayarlı model varyantları  
- **Eğitim Veri Kaynakları**: Model eğitimi ve ince ayar için kullanılan veri setleri  

### Kapsamlı Tedarik Zinciri Güvenlik Stratejisi

#### **Bileşen Doğrulama ve Güven**  
- **Kaynak Doğrulaması**: Tüm AI bileşenlerinin kökeni, lisansı ve bütünlüğünü entegrasyondan önce doğrulayın  
- **Güvenlik Değerlendirmesi**: Modeller, veri kaynakları ve AI hizmetleri için zafiyet taramaları ve güvenlik incelemeleri yapın  
- **İtibar Analizi**: AI hizmet sağlayıcılarının güvenlik geçmişi ve uygulamalarını değerlendirin  
- **Uyumluluk Doğrulaması**: Tüm bileşenlerin kurumsal güvenlik ve düzenleyici gereksinimleri karşıladığından emin olun  

#### **Güvenli Dağıtım Hatları**  
- **Otomatik CI/CD Güvenliği**: Otomatik dağıtım hatlarında güvenlik taramalarını entegre edin  
- **Artefakt Bütünlüğü**: Dağıtılan tüm artefaktlar (kod, modeller, yapılandırmalar) için kriptografik doğrulama uygulayın  
- **Aşamalı Dağıtım**: Her aşamada güvenlik doğrulaması ile kademeli dağıtım stratejileri kullanın  
- **Güvenilir Artefakt Depoları**: Sadece doğrulanmış, güvenli artefakt kayıtlarından ve depolarından dağıtım yapın  

#### **Sürekli İzleme ve Müdahale**  
- **Bağımlılık Taraması**: Tüm yazılım ve AI bileşen bağımlılıkları için sürekli zafiyet izleme  
- **Model İzleme**: Model davranışı, performans sapması ve güvenlik anormalliklerinin sürekli değerlendirilmesi  
- **Hizmet Sağlığı Takibi**: Harici AI hizmetlerinin kullanılabilirlik, güvenlik olayları ve politika değişikliklerinin izlenmesi  
- **Tehdit İstihbaratı Entegrasyonu**: AI ve ML güvenlik risklerine özgü tehdit beslemelerinin dahil edilmesi  

#### **Erişim Kontrolü ve En Az Ayrıcalık**  
- **Bileşen Düzeyi İzinler**: Modeller, veriler ve hizmetlere iş gereksinimine göre erişimi kısıtlayın  
- **Hizmet Hesabı Yönetimi**: Minimum gerekli izinlere sahip özel hizmet hesapları uygulayın  
- **Ağ Segmentasyonu**: AI bileşenlerini izole edin ve hizmetler arası ağ erişimini sınırlandırın  
- **API Geçidi Kontrolleri**: Harici AI hizmetlerine erişimi kontrol etmek ve izlemek için merkezi API geçitleri kullanın  

#### **Olay Müdahalesi ve Kurtarma**  
- **Hızlı Müdahale Prosedürleri**: Ele geçirilmiş AI bileşenlerini yamalamak veya değiştirmek için belirlenmiş süreçler  
- **Kimlik Bilgisi Döndürme**: Sırlar, API anahtarları ve hizmet kimlik bilgileri için otomatik döndürme sistemleri  
- **Geri Alma Yeteneği**: AI bileşenlerinin önceki bilinen iyi sürümlerine hızlıca dönme imkanı  
- **Tedarik Zinciri İhlali Kurtarma**: Yukarı akış AI hizmeti ihlallerine yanıt için özel prosedürler  

### Microsoft Güvenlik Araçları ve Entegrasyonu

**GitHub Advanced Security**, şunları içeren kapsamlı tedarik zinciri koruması sağlar:  
- **Gizli Anahtar Taraması**: Depolarda kimlik bilgileri, API anahtarları ve tokenların otomatik tespiti  
- **Bağımlılık Taraması**: Açık kaynak bağımlılıkları ve kütüphaneler için zafiyet değerlendirmesi  
- **CodeQL Analizi**: Güvenlik açıkları ve kodlama sorunları için statik kod analizi  
- **Tedarik Zinciri İçgörüleri**: Bağımlılık sağlığı ve güvenlik durumu görünürlüğü  

**Azure DevOps & Azure Repos Entegrasyonu:**  
- Microsoft geliştirme platformlarında kesintisiz güvenlik taraması entegrasyonu  
- AI iş yükleri için Azure Pipelines'da otomatik güvenlik kontrolleri  
- Güvenli AI bileşen dağıtımı için politika uygulaması  

**Microsoft İç Uygulamaları:**  
Microsoft, tüm ürünlerinde kapsamlı tedarik zinciri güvenlik uygulamaları uygular. Kanıtlanmış yaklaşımlar hakkında bilgi edinin: [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).  

## Temel Güvenlik En İyi Uygulamaları

MCP uygulamaları, kuruluşunuzun mevcut güvenlik duruşunu devralır ve üzerine inşa eder. Temel güvenlik uygulamalarını güçlendirmek, AI sistemleri ve MCP dağıtımlarının genel güvenliğini önemli ölçüde artırır.

### Temel Güvenlik İlkeleri

#### **Güvenli Geliştirme Uygulamaları**  
- **OWASP Uyumu**: [OWASP Top 10](https://owasp.org/www-project-top-ten/) web uygulaması zafiyetlerine karşı koruma  
- **AI'ya Özgü Koruma**: [LLM'ler için OWASP Top 10](https://genai.owasp.org/download/43299/?tmstv=1731900559) kontrollerini uygulama  
- **Güvenli Gizli Yönetimi**: Tokenlar, API anahtarları ve hassas yapılandırma verileri için özel kasalar kullanma  
- **Uçtan Uca Şifreleme**: Tüm uygulama bileşenleri ve veri akışlarında güvenli iletişim sağlama  
- **Girdi Doğrulama**: Tüm kullanıcı girdileri, API parametreleri ve veri kaynaklarının titiz doğrulanması  

#### **Altyapı Sertleştirme**  
- **Çok Faktörlü Kimlik Doğrulama**: Tüm yönetici ve hizmet hesapları için zorunlu MFA  
- **Yama Yönetimi**: İşletim sistemleri, çerçeveler ve bağımlılıklar için otomatik ve zamanında yama uygulama  
- **Kimlik Sağlayıcı Entegrasyonu**: Kurumsal kimlik sağlayıcıları (Microsoft Entra ID, Active Directory) ile merkezi kimlik yönetimi  
- **Ağ Segmentasyonu**: MCP bileşenlerinin mantıksal izolasyonu ile yatay hareket potansiyelini sınırlama  
- **En Az Ayrıcalık İlkesi**: Tüm sistem bileşenleri ve hesaplar için minimum gerekli izinler  

#### **Güvenlik İzleme ve Tespit**  
- **Kapsamlı Kayıt Tutma**: MCP istemci-sunucu etkileşimleri dahil AI uygulama aktivitelerinin ayrıntılı kaydı  
- **SIEM Entegrasyonu**: Anomali tespiti için merkezi güvenlik bilgi ve olay yönetimi  
- **Davranışsal Analitik**: Sistem ve kullanıcı davranışındaki olağandışı desenleri tespit etmek için AI destekli izleme  
- **Tehdit İstihbaratı**: Harici tehdit beslemeleri ve ihlal göstergelerinin (IOC) entegrasyonu  
- **Olay Müdahalesi**: Güvenlik olaylarının tespiti, müdahalesi ve kurtarılması için iyi tanımlanmış prosedürler  

#### **Sıfır Güven Mimarisi**  
- **Asla Güvenme, Her Zaman Doğrula**: Kullanıcılar, cihazlar ve ağ bağlantılarının sürekli doğrulanması  
- **Mikro Segmentasyon**: Bireysel iş yükleri ve hizmetleri izole eden ayrıntılı ağ kontrolleri  
- **Kimlik Merkezli Güvenlik**: Ağ konumu yerine doğrulanmış kimliklere dayalı güvenlik politikaları  
- **Sürekli Risk Değerlendirmesi**: Mevcut bağlam ve davranışa göre dinamik güvenlik durumu değerlendirmesi  
- **Koşullu Erişim**: Risk faktörleri, konum ve cihaz güvenine göre uyarlanan erişim kontrolleri  

### Kurumsal Entegrasyon Desenleri

#### **Microsoft Güvenlik Ekosistemi Entegrasyonu**  
- **Microsoft Defender for Cloud**: Kapsamlı bulut güvenlik duruşu yönetimi  
- **Azure Sentinel**: AI iş yükü koruması için bulut yerel SIEM ve SOAR yetenekleri  
- **Microsoft Entra ID**: Koşullu erişim politikaları ile kurumsal kimlik ve erişim yönetimi  
- **Azure Key Vault**: Donanım güvenlik modülü (HSM) destekli merkezi gizli yönetimi  
- **Microsoft Purview**: AI veri kaynakları ve iş akışları için veri yönetişimi ve uyumluluk  

#### **Uyumluluk ve Yönetişim**  
- **Düzenleyici Uyum**: MCP uygulamalarının sektör spesifik uyumluluk gereksinimlerini (GDPR, HIPAA, SOC 2) karşılamasını sağlama  
- **Veri Sınıflandırması**: AI sistemleri tarafından işlenen hassas verilerin uygun kategorize edilmesi ve yönetimi  
- **Denetim İzleri**: Düzenleyici uyumluluk ve adli inceleme için kapsamlı kayıt tutma  
- **Gizlilik Kontrolleri**: AI sistem mimarisinde gizlilik-odaklı tasarım ilkelerinin uygulanması  
- **Değişiklik Yönetimi**: AI sistem değişikliklerinin güvenlik incelemeleri için resmi süreçler  

Bu temel uygulamalar, MCP'ye özgü güvenlik kontrollerinin etkinliğini artıran ve AI destekli uygulamalar için kapsamlı koruma sağlayan sağlam bir güvenlik tabanı oluşturur.

## Temel Güvenlik Çıkarımları

- **Katmanlı Güvenlik Yaklaşımı**: Temel güvenlik uygulamalarını (güvenli kodlama, en az ayrıcalık, tedarik zinciri doğrulaması, sürekli izleme) AI'ya özgü kontrollerle birleştirerek kapsamlı koruma sağlayın  
- **AI'ya Özgü Tehdit Manzarası**: MCP sistemleri, özel azaltımlar gerektiren prompt enjeksiyonu, araç zehirlenmesi, oturum kaçırma, karışık vekil problemleri, token geçişi açıkları ve aşırı izinler gibi benzersiz risklerle karşı karşıyadır  
- **Kimlik Doğrulama ve Yetkilendirme Mükemmelliği**: Harici kimlik sağlayıcıları (Microsoft Entra ID) kullanarak sağlam kimlik doğrulama uygulayın, uygun token doğrulamasını zorunlu kılın ve MCP sunucusu için açıkça verilmemiş tokenları asla kabul etmeyin  
- **AI Saldırı Önleme**: Dolaylı prompt enjeksiyonu ve araç zehirlenmesi saldırılarına karşı Microsoft Prompt Shields ve Azure Content Safety kullanarak savunun, araç meta verilerini doğrulayın ve dinamik değişiklikleri izleyin  
- **Oturum ve İletim Güvenliği**: Kullanıcı kimliklerine bağlı, kriptografik olarak güvenli, belirlenemez oturum kimlikleri kullanın, uygun oturum yaşam döngüsü yönetimi uygulayın ve kimlik doğrulama için asla oturum kullanmayın  
- **OAuth Güvenlik En İyi Uygulamaları**: Dinamik kayıtlı istemciler için açık kullanıcı onayı, PKCE ile doğru OAuth 2.1 uygulaması ve sıkı yönlendirme URI doğrulaması ile karışık vekil saldırılarını önleyin  
- **Token Güvenlik İlkeleri**: Token geçişi anti-patternlerinden kaçının, token hedef kitle iddialarını doğrulayın, kısa ömürlü tokenlar ve güvenli döndürme uygulayın, net güven sınırları koruyun  
- **Kapsamlı Tedarik Zinciri Güvenliği**: Tüm AI ekosistem bileşenlerini (modeller, embeddingler, bağlam sağlayıcıları, harici API'ler) geleneksel yazılım bağımlılıkları kadar titizlikle güvenlik açısından ele alın  
- **Sürekli Evrim**: Hızla gelişen MCP spesifikasyonlarını takip edin, güvenlik topluluğu standartlarına katkıda bulunun ve protokol olgunlaştıkça uyarlanabilir güvenlik duruşları sürdürün  
- **Microsoft Güvenlik Entegrasyonu**: Gelişmiş MCP dağıtım koruması için Microsoft’un kapsamlı güvenlik ekosisteminden (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) yararlanın  

## Kapsamlı Kaynaklar

### **Resmi MCP Güvenlik Dokümantasyonu**  
- [MCP Spesifikasyonu (Güncel: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP Güvenlik En İyi Uygulamaları](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP Yetkilendirme Spesifikasyonu](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  
- [MCP GitHub Deposu](https://github.com/modelcontextprotocol)  

### **Güvenlik Standartları ve En İyi Uygulamalar**  
- [OAuth 2.0 Güvenlik En İyi Uygulamaları (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 Web Uygulama Güvenliği](https://owasp.org/www-project-top-ten/)  
- [Büyük Dil Modelleri için OWASP Top 10](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- [Microsoft Dijital Savunma Raporu](https://aka.ms/mddr)  

### **AI Güvenlik Araştırmaları ve Analizleri**  
- [MCP'de Prompt Enjeksiyonu (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [Araç Zehirlenmesi Saldırıları (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)  
- [MCP Güvenlik Araştırma Brifingi (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Güvenlik Çözümleri**
- [Microsoft Prompt Shields Dokümantasyonu](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure İçerik Güvenliği Servisi](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Güvenliği](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Yönetimi En İyi Uygulamaları](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Gelişmiş Güvenlik](https://github.com/security/advanced-security)

### **Uygulama Kılavuzları ve Eğitimler**
- [Azure API Yönetimi MCP Kimlik Doğrulama Geçidi Olarak](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Kimlik Doğrulaması ile MCP Sunucuları](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Güvenli Token Depolama ve Şifreleme (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps ve Tedarik Zinciri Güvenliği**
- [Azure DevOps Güvenliği](https://azure.microsoft.com/products/devops)
- [Azure Repos Güvenliği](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Tedarik Zinciri Güvenliği Yolculuğu](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Ek Güvenlik Dokümantasyonu**

Kapsamlı güvenlik rehberliği için, bu bölümdeki uzmanlaşmış belgelere bakınız:

- **[MCP Güvenlik En İyi Uygulamaları 2025](./mcp-security-best-practices-2025.md)** - MCP uygulamaları için tam güvenlik en iyi uygulamaları
- **[Azure İçerik Güvenliği Uygulaması](./azure-content-safety-implementation.md)** - Azure İçerik Güvenliği entegrasyonu için pratik uygulama örnekleri  
- **[MCP Güvenlik Kontrolleri 2025](./mcp-security-controls-2025.md)** - MCP dağıtımları için en son güvenlik kontrolleri ve teknikleri
- **[MCP En İyi Uygulamalar Hızlı Referans](./mcp-best-practices.md)** - Temel MCP güvenlik uygulamaları için hızlı referans kılavuzu

---

## Sonraki Adım

Sonraki: [Bölüm 3: Başlarken](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->