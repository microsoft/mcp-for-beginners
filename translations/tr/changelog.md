# Değişiklik Günlüğü: Başlangıç Seviyesi MCP Müfredatı

Bu belge, Başlangıç Seviyesi Model Konteks Protokolü (MCP) müfredatında yapılan tüm önemli değişikliklerin kaydıdır. Değişiklikler ters kronolojik sırayla (en yeni değişiklikler önce) belgeye eklenmiştir.

## 11 Nisan 2026

### Yeni Ders, Dokümantasyon Düzeltmeleri ve Bağımlılık Güncellemeleri

#### Yeni Müfredat İçeriği Eklendi

**Modül 05 - İleri Konular**
- **Ders 5.17: MCP ile Rekabetçi Çoklu Ajan Muhakemesi** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Çoklu ajan sistemleri için rekabetçi tartışma modelini kapsayan yeni kapsamlı rehber
  - Mermaid mimari diyagramı: iki ajan → ortak MCP sunucusu → tartışma transkripti → hakem → karar
  - Python ve TypeScript ile yazılmış ortak MCP araç sunucusu (`web_search` + `run_python`)
  - Karşıt sistem istemleri (LEHİNDE / KARŞISINDA / Hakem) ile açık araç kullanım gereksinimleri
  - Turların yönetimi ve argümanların yönlendirilmesini Python, TypeScript ve C# ile gerçekleştiren tartışma yöneticisi
  - Orkestratör için gerçek araç çağrılarına bağlanan MCP `ClientSession` bağlantısı
  - Kullanım senaryoları tablosu (halüsinasyon tespiti, tehdit modelleme, API tasarımı incelemesi, olgusal doğrulama, teknoloji seçimi)
  - Güvenlik dikkate alınmaları: sandbox'lanmış yürütme, araç çağrılarının doğrulanması, hız sınırlaması, denetim kaydı
  - Üç uygulamalı senaryo içeren yapılandırılmış egzersiz (kod incelemesi, mimari karar, içerik denetimi)

#### Dokümantasyon Düzeltmeleri

**Modül 03 - Başlarken**
- **05-stdio-server/README.md**: Eksik TypeScript stdio sunucu örneği düzeltildi — Python ve .NET örnekleriyle uyumlu olması için eksik taşıyıcı örneklendirmesi (`new StdioServerTransport()`) ve `server.connect(transport)` çağrısı eklendi
- **14-sampling/README.md**: Yazım hatası düzeltildi — `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Müfredat Güncellemeleri

**Ana README.md**
- Müfredat tablosuna 5.17 girişi (MCP ile Rekabetçi Çoklu Ajan Muhakemesi) eklendi ve yeni derse doğrudan bağlantı sağlandı

**05-AdvancedTopics/README.md**
- Dersler tablosuna Ders 5.17 satırı eklendi

**study_guide.md**
- İleri Konuların zihin haritası ve açıklamasına Rekabetçi Çoklu Ajan Muhakemesi konusu eklendi

#### Kod ve Güvenlik Düzeltmeleri

**Modül 05 - Rekabetçi Ajanlar (`mcp-adversarial-agents`)**
- **Güvenlik düzeltmesi — komut enjeksiyonu**: TypeScript `run_python` aracında `execSync` kabuk interpolasyonu `execFile` + `promisify` ile değiştirildi, komut enjeksiyonu yüzeyi kaldırıldı (LLM tarafından kontrol edilen kod artık kabuk müdahalesi olmadan argüman olarak iletiliyor)
- **MCP araç döngüsü bağlantısı**: Python tartışma orkestratörü güncellendi; engelleyen eşzamanlı `Anthropic` yerine `AsyncAnthropic` istemcisi kullanıldı, her ajan dönüşüne canlı bir `ClientSession` doğrudan iletiliyor, her dönüşte `session.list_tools()` çağrısıyla araç tanımları alınıyor ve model nihai yanıtı verene kadar döngü içinde `session.call_tool()` ile `tool_use` blokları gönderiliyor

#### Bağımlılık Güncellemeleri

- Birçok pakette (`03-GettingStarted`, `04-PracticalImplementation`, `10-StreamliningAIWorkflows`) `hono` 4.12.12 sürümüne yükseltildi
- TypeScript paketlerinde `@hono/node-server` 1.19.11’den 1.19.13’e yükseltildi
- Python paketlerinde (10-StreamliningAIWorkflows laboratuvarları 3 ve 4) `cryptography` 46.0.5’ten 46.0.7’ye yükseltildi
- 10-StreamliningAIWorkflows denetleyicisinde `lodash` 4.17.23’ten 4.18.1’e yükseltildi

#### Çeviriler

- 48’den fazla dilde en güncel kaynak değişikliklerine göre çeviriler senkronize edildi (i18n güncellemesi)

---

## 5 Şubat 2026

### Depo Genelinde Doğrulama ve Navigasyon İyileştirmeleri

#### Yeni Müfredat İçeriği Eklendi

**Modül 03 - Başlarken**
- **12-mcp-hosts/README.md**: MCP host kurulumuna yönelik yeni kapsamlı rehber
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf yapılandırma örnekleri
  - Tüm önemli hostlar için JSON yapılandırma şablonları
  - Taşıyıcı türleri karşılaştırma tablosu (stdio, SSE/HTTP, WebSocket)
  - Yaygın bağlantı sorunlarının giderilmesi
  - Host yapılandırması için güvenlik en iyi uygulamaları

- **13-mcp-inspector/README.md**: MCP Denetleyicisi için yeni hata ayıklama rehberi
  - Kurulum yöntemleri (npx, npm global, kaynak koddan)
  - stdio ve HTTP/SSE üzerinden sunuculara bağlanma
  - Test araçları, kaynaklar ve istemler iş akışları
  - VS Code ile MCP Denetleyicisi entegrasyonu
  - Yaygın hata ayıklama senaryoları çözümleriyle

**Modül 04 - Pratik Uygulama**
- **pagination/README.md**: Yeni sayfalama uygulama rehberi
  - Python, TypeScript, Java’da imleç tabanlı sayfalama desenleri
  - İstemci tarafı sayfalama yönetimi
  - Opaque ve yapılandırılmış imleç tasarım stratejileri
  - Performans optimizasyonu önerileri

**Modül 05 - İleri Konular**
- **mcp-protocol-features/README.md**: Yeni protokol özellikleri derinlemesine inceleme
  - İlerleme bildirimleri uygulaması
  - İstek iptali desenleri
  - URI kalıplarıyla kaynak şablonları
  - Sunucu yaşam döngüsü yönetimi
  - Günlük seviyesi kontrolü
  - JSON-RPC kodları ile hata işleme desenleri

#### Navigasyon Düzeltmeleri (24+ dosyada güncelleme)

**Ana Modül README dosyaları**
 Artık hem ilk derse hem de sonraki modüle bağlantı sağlıyor

**02-Güvenlik Alt Dosyaları**
- Tüm 5 yardımcı güvenlik belgesinde "Sonraki Adım" navigasyonu eklendi:

**09-Vaka Çalışması Dosyaları**
- Tüm vaka çalışması dosyalarında ardışık navigasyon eklendi:

**10-StreamliningAI Laboratuvarları**
Modül 10 genel bakışı ve Modül 11'e "Sonraki Adım" bölümü eklendi

#### Kod ve İçerik Düzeltmeleri

**SDK ve Bağımlılık Güncellemeleri**
Boş openai sürümü `^4.95.0` olarak düzeltildi
SDK `^1.8.0`’den `>=1.26.0`’a güncellendi
MCP sürüm pinleri `>=1.26.0` olarak güncellendi

**Kod Düzeltmeleri**
Geçersiz model `gpt-4o-mini` → `gpt-4.1-mini` olarak düzeltildi

**İçerik Düzeltmeleri**
Kırık bağlantı `READMEmd` → `README.md` olarak düzeltildi, müfredat başlığı `Module 1-3` → `Module 0-3` olarak düzeltildi, büyük/küçük harf duyarlı yol düzeltildi
Bozuk çift Vaka Çalışması 5 içeriği kaldırıldı

**Yeni Başlayanlar için Rehberlik İyileştirmeleri**
Yeni başlayanlar için uygun tanıtım, öğrenme hedefleri ve önkoşullar eklendi

#### Müfredat Güncellemeleri

**Ana README.md**
- Müfredat tablosuna 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Sayfalama), 5.16 (Protokol Özellikleri) girişleri eklendi

**Modül README dosyaları**
Ders listesine 12 ve 13 numaralı dersler eklendi
Sayfalama bağlantısı ile Pratik Rehberler bölümü eklendi
Derslere 5.15 (Özel Taşıyıcı) ve 5.16 (Protokol Özellikleri) eklendi

**study_guide.md**
- Yeni konularla zihin haritası güncellendi: MCP Host Kurulumu, MCP Denetleyicisi, Sayfalama Stratejileri, Protokol Özellikleri Derinlemesine İnceleme

## 28 Ocak 2026

### MCP Şartnamesi 2025-11-25 Uyum İncelemesi

#### Temel Kavramlar Geliştirmesi (01-CoreConcepts/)
- **Yeni İstemci Primitifi - Roots**: Sunucuların dosya sistemi sınırlarını ve erişim izinlerini anlamasına olanak sağlayan Roots istemci primitifi için kapsamlı dokümantasyon eklendi
- **Araç Açıklamaları**: Daha iyi araç yürütme kararları için araç davranış açıklamaları (`readOnlyHint`, `destructiveHint`) dokümantasyonu eklendi
- **Sampling’de Araç Çağrısı**: Sampling dokümantasyonu güncellendi, sampling isteklerinde model tabanlı araç çağrıları için `tools` ve `toolChoice` parametreleri eklendi
- **URL Modu Tetikleme**: Sunucu kaynaklı dış web etkileşimleri için URL tabanlı tetiklemeye ilişkin dokümantasyon eklendi
- **Görevler (Deneysel)**: Dayanıklı yürütme paketleri ve ertelenmiş sonuç geri alımı için deneysel Görevler özelliği dokümantasyonu eklendi
- **Simge Desteği**: Araçların, kaynakların, kaynak şablonlarının ve istemlerin artık ek metadata olarak simgeler içerebileceği belirtildi

#### Dokümantasyon Güncellemeleri
- **README.md**: MCP Şartnamesi 2025-11-25 sürüm referansı ve tarih bazlı sürüm açıklaması eklendi
- **study_guide.md**: Müfredat haritası Güncellendi; Görevler ve Araç Açıklamaları Temel Kavramlar bölümüne eklendi; belge zaman damgası güncellendi

#### Şartname Uyum Doğrulaması
- **Protokol Sürümü**: Tüm dokümantasyonun güncel MCP Şartnamesi 2025-11-25’i referans verdiği doğrulandı
- **Mimari Uyum**: İki katmanlı mimari (Veri Katmanı + Taşıyıcı Katmanı) dokümantasyonunun doğruluğu kontrol edildi
- **Primitifler Dokümantasyonu**: Sunucu primitifi (Kaynaklar, İstemler, Araçlar) ve istemci primitifi (Sampling, Tetikleme, Günlükleme, Roots) doğrulandı
- **Taşıyıcı Mekanizmalar**: STDIO ve Akışlanabilir HTTP taşıyıcı dokümantasyonunun doğruluğu doğrulandı
- **Güvenlik Kılavuzu**: MCP Güvenlik En İyi Uygulamaları ile uyum sağlandığı onaylandı

#### Temel MCP 2025-11-25 Özellikleri Dokümante Edildi
- **OpenID Connect Keşfi**: OIDC ile kimlik doğrulama sunucusu keşfi
- **OAuth İstemci Kimliği Metadata Belgeleri**: Tavsiye edilen istemci kayıt mekanizması
- **JSON Şema 2020-12**: MCP şema tanımları varsayılan lehçesi
- **SDK Katman Sistemi**: SDK özellik desteği ve bakım gereksinimleri resmi hale getirildi
- **Yönetim Yapısı**: MCP yönetiminde Çalışma Grupları ve İlgi Grupları resmi hale getirildi

### Güvenlik Dokümantasyonu Büyük Güncelleme (02-Güvenlik/)

#### MCP Güvenlik Zirvesi Atölyesi (Sherpa) Entegrasyonu
- **Yeni Uygulamalı Eğitim Kaynağı**: [MCP Güvenlik Zirvesi Atölyesi (Sherpa)](https://azure-samples.github.io/sherpa/) tüm güvenlik dokümantasyonuna kapsamlı entegrasyon eklendi
- **Sefer Rotası Kapsamı**: Base Camp’den Summit’e tüm kamp kamp ilerleme rotası belgelenmiştir
- **OWASP Uyumu**: Tüm güvenlik kılavuzları şimdi OWASP MCP Azure Güvenlik Rehberi risklerine göre eşlendi

#### OWASP MCP Top 10 Entegrasyonu
- **Yeni Bölüm**: Ana Güvenlik README’sine OWASP MCP Top 10 Güvenlik Riskleri ve Azure azaltmaları tablosu eklendi
- **Risk Bazlı Dokümantasyon**: mcp-security-controls-2025.md dosyasına OWASP MCP risk referansları (MCP01-MCP08) eklendi
- **Referans Mimarisi**: OWASP MCP Azure Güvenlik Rehberi referans mimarisi ve uygulama desenlerine bağlantı sağlandı

#### Güncellenen Güvenlik Dosyaları
- **README.md**: Sherpa Atölyesi genel bakışı, sefer rotası tablosu, OWASP MCP Top 10 riskler özeti ve uygulamalı eğitim bölümü eklendi
- **mcp-security-controls-2025.md**: Başlık Şubat 2026’ya güncellendi, OWASP risk referansları (MCP01-MCP08) eklendi, şartname sürüm uyumsuzluğu giderildi
- **mcp-security-best-practices-2025.md**: Sherpa ve OWASP kaynaklar bölümü eklendi, zaman damgası güncellendi
- **mcp-best-practices.md**: Sherpa ve OWASP bağlantıları ile uygulamalı eğitim bölümü eklendi
- **azure-content-safety-implementation.md**: OWASP MCP06 referansı, Sherpa Kamp 3 uyumu ve ek kaynaklar bölümü eklendi

#### Yeni Kaynak Bağlantıları Eklendi
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Bireysel OWASP MCP risk sayfaları (MCP01-MCP10)

### Müfredat Genelinde MCP Şartnamesi 2025-11-25 Uyumu

#### Modül 03 - Başlarken
- **SDK Dokümantasyonu**: Go SDK resmi SDK listesine eklendi; tüm SDK referansları MCP Şartnamesi 2025-11-25’e göre güncellendi
- **Taşıyıcı Açıklaması**: STDIO ve HTTP Akış taşıyıcı açıklamaları netleştirildi, açık şartname referansları eklendi

#### Modül 04 - Pratik Uygulama
- **SDK Güncellemeleri**: Go SDK eklendi; SDK listesi şartname sürümü referansıyla güncellendi
- **Yetkilendirme Şartnamesi**: MCP Yetkilendirme şartnamesi bağlantısı güncel 2025-11-25 sürümüne değiştirildi

#### Modül 05 - İleri Konular
- **Yeni Özellikler**: MCP Şartnamesi 2025-11-25’in yeni özellikleri hakkında not eklendi (Görevler, Araç Açıklamaları, URL Modu Tetikleme, Roots)
- **Güvenlik Kaynakları**: Ek referanslara OWASP MCP Top 10 ve Sherpa atölyesi bağlantıları eklendi

#### Modül 06 - Topluluk Katkıları
- **SDK Listesi**: Swift ve Rust SDK’ları eklendi; şartname bağlantısı 2025-11-25 olarak güncellendi
- **Şartname Referansı**: MCP Şartnamesi doğrudan şartname URL’sine güncellendi

#### Modül 07 - Erken Benimsemekten Dersler
- **Kaynak Güncellemeleri**: Ek kaynaklara MCP Şartnamesi 2025-11-25 linki ve OWASP MCP Top 10 eklendi

#### Modül 08 - En İyi Uygulamalar
- **Şartname Sürümü**: MCP Şartnamesi referansı 2025-11-25 olarak güncellendi
- **Güvenlik Kaynakları**: Ek referanslara OWASP MCP Top 10 ve Sherpa atölyesi eklendi

#### Modül 10 - Yapay Zeka İş Akışlarının Kolaylaştırılması
- **Rozet Güncellemesi**: MCP sürüm rozeti SDK sürümü (1.9.3) yerine şartname sürümü (2025-11-25) olarak değiştirildi
- **Kaynak Bağlantıları**: MCP Şartnamesi bağlantısı güncellendi; OWASP MCP Top 10 eklendi

#### Modül 11 - MCP Sunucu Uygulamalı Laboratuvarları
- **Şartname Referansı**: MCP Şartnamesi bağlantısı 2025-11-25 sürümüne güncellendi
- **Güvenlik Kaynakları**: Resmi kaynaklara OWASP MCP Top 10 eklendi

## 18 Aralık 2025
### Güvenlik Dokümantasyonu Güncellemesi - MCP Spesifikasyonu 2025-11-25

#### MCP Güvenlik En İyi Uygulamaları (02-Security/mcp-best-practices.md) - Spesifikasyon Versiyonu Güncellemesi
- **Protokol Versiyon Güncellemesi**: En son MCP Spesifikasyonu 2025-11-25 (25 Kasım 2025 sürümü) referans alındı
  - Tüm spesifikasyon versiyon referansları 2025-06-18’den 2025-11-25’e güncellendi
  - Belge tarih referansları 18 Ağustos 2025’den 18 Aralık 2025’e güncellendi
  - Tüm spesifikasyon URL’lerinin güncel dokümantasyona işaret ettiği doğrulandı
- **İçerik Doğrulaması**: Güvenlik en iyi uygulamalarının en son standartlara göre kapsamlı doğrulaması yapıldı
  - **Microsoft Güvenlik Çözümleri**: Prompt Shields (önceden “Jailbreak risk tespiti”), Azure İçerik Güvenliği, Microsoft Entra ID ve Azure Key Vault için mevcut terim ve bağlantılar doğrulandı
  - **OAuth 2.1 Güvenliği**: En güncel OAuth güvenlik en iyi uygulamalarına uyumluluk teyit edildi
  - **OWASP Standartları**: LLM’ler için OWASP Top 10 referanslarının geçerliliği onaylandı
  - **Azure Servisleri**: Tüm Microsoft Azure dokümantasyon bağlantıları ve en iyi uygulamalar gözden geçirildi
- **Standartlara Uyum**: Referans verilen tüm güvenlik standartlarının güncelliği teyit edildi
  - NIST AI Risk Yönetimi Çerçevesi
  - ISO 27001:2022
  - OAuth 2.1 Güvenlik En İyi Uygulamaları
  - Azure güvenlik ve uyumluluk çerçeveleri
- **Uygulama Kaynakları**: Tüm uygulama rehberi bağlantıları ve kaynakları doğrulandı
  - Azure API Yönetimi kimlik doğrulama desenleri
  - Microsoft Entra ID entegrasyon rehberleri
  - Azure Key Vault gizli yönetimi
  - DevSecOps boru hatları ve izleme çözümleri

### Dokümantasyon Kalite Güvencesi
- **Spesifikasyon Uyumu**: Tüm zorunlu MCP güvenlik gereksinimlerinin (MUST/MUST NOT) en güncel spesifikasyonla uyumu sağlandı
- **Kaynak Güncelliği**: Microsoft dokümantasyonu, güvenlik standartları ve uygulama rehberleri için tüm dış bağlantılar doğrulandı
- **En İyi Uygulama Kapsamı**: Kimlik doğrulama, yetkilendirme, yapay zeka özgü tehditler, tedarik zinciri güvenliği ve kurumsal desenler kapsamının tamlığı teyit edildi

## 6 Ekim 2025

### Başlarken Bölüm Genişletmesi – Gelişmiş Sunucu Kullanımı & Basit Kimlik Doğrulama

#### Gelişmiş Sunucu Kullanımı (03-GettingStarted/10-advanced)
- **Yeni Bölüm Eklendi**: Hem normal hem de düşük seviye sunucu mimarilerini kapsayan kapsamlı gelişmiş MCP sunucu kullanımı rehberi sunuldu.
  - **Normal ve Düşük Seviyeli Sunucu Karşılaştırması**: Her iki yaklaşım için Python ve TypeScript örnekleri ile detaylı karşılaştırma.
  - **Handler Tabanlı Tasarım**: Ölçeklenebilir ve esnek sunucu uygulamaları için araç/kaynak/prompt yönetimi açıklaması.
  - **Pratik Desenler**: Gelişmiş özellikler ve mimari için düşük seviyeli sunucu desenlerinin kullanıldığı gerçek yaşam senaryoları.

#### Basit Kimlik Doğrulama (03-GettingStarted/11-simple-auth)
- **Yeni Bölüm Eklendi**: MCP sunucularında basit kimlik doğrulama uygulaması için adım adım rehber.
  - **Kimlik Doğrulama Kavramları**: Kimlik doğrulama ve yetkilendirme, kimlik bilgisi yönetimi konusunda net açıklamalar.
  - **Temel Kimlik Doğrulama Uygulaması**: Python (Starlette) ve TypeScript (Express) için middleware tabanlı kimlik doğrulama desenleri, kod örnekleri ile.
  - **Gelişmiş Güvenliğe Geçiş**: Basit kimlik doğrulamayla başlayıp OAuth 2.1 ve RBAC’a ilerleme rehberi ve gelişmiş güvenlik modüllerine referanslar.

Bu eklemeler, daha sağlam, güvenli ve esnek MCP sunucu uygulamaları geliştirmek için temel kavramlarla gelişmiş üretim desenleri arasında köprü kuran pratik ve uygulamalı rehberlik sağlar.

## 29 Eylül 2025

### MCP Sunucu Veritabanı Entegrasyon Laboratuvarları - Kapsamlı Uygulamalı Öğrenme Yolu

#### 11-MCPServerHandsOnLabs - Yeni Tam Veritabanı Entegrasyon Müfredatı
- **Tam 13 Laboratuvarlık Öğrenme Yolu**: PostgreSQL veritabanı entegrasyonlu üretim hazır MCP sunucuları oluşturmak için kapsamlı uygulamalı müfredat eklendi
  - **Gerçek Dünya Uygulaması**: Zava Retail analitik kullanım senaryosu ile kurumsal düzey desenler gösterildi
  - **Yapılandırılmış Öğrenme İlerleyişi**:
    - **Laboratuvarlar 00-03: Temeller** - Giriş, Temel Mimari, Güvenlik & Çok Kiracılık, Ortam Kurulumu
    - **Laboratuvarlar 04-06: MCP Sunucu İnşası** - Veritabanı Tasarımı & Şeması, MCP Sunucu Uygulaması, Araç Geliştirme  
    - **Laboratuvarlar 07-09: Gelişmiş Özellikler** - Semantik Arama Entegrasyonu, Test & Hata Ayıklama, VS Code Entegrasyonu
    - **Laboratuvarlar 10-12: Üretim & En İyi Uygulamalar** - Dağıtım Stratejileri, İzleme & Gözlemlenebilirlik, En İyi Uygulamalar & Optimizasyon
  - **Kurumsal Teknolojiler**: FastMCP çerçevesi, pgvector destekli PostgreSQL, Azure OpenAI gömme modelleri, Azure Container Apps, Application Insights
  - **Gelişmiş Özellikler**: Satır Seviyesi Güvenlik (RLS), semantik arama, çok kiracılı veri erişimi, vektör gömme, gerçek zamanlı izleme

#### Terminoloji Standardizasyonu - Modülden Laboratuvara Dönüşüm
- **Kapsamlı Dokümantasyon Güncellemesi**: 11-MCPServerHandsOnLabs içindeki tüm README dosyalarında "Modül" yerine "Laboratuvar" terimi sistematik olarak kullanıldı
  - **Bölüm Başlıkları**: Tüm 13 laboratuvarda “Bu Modülün Kapsadığı Konular” başlığı “Bu Laboratuvarın Kapsadığı Konular” olarak güncellendi
  - **İçerik Tanımı**: “Bu modül sunar...” ifadesi “Bu laboratuvar sunar...” olarak değiştirildi
  - **Öğrenme Hedefleri**: “Bu modülün sonunda...” ifadesi “Bu laboratuvarın sonunda...” olarak güncellendi
  - **Gezinim Bağlantıları**: Tüm çapraz referans ve navigasyonlarda “Modül XX:” yerine “Laboratuvar XX:” kullanımı sağlandı
  - **Tamamlama Takibi**: “Bu modül tamamlandıktan sonra...” yerine “Bu laboratuvar tamamlandıktan sonra...” olarak güncellendi
  - **Teknik Referanslar Korundu**: Yapılandırma dosyalarındaki Python modül referansları (örneğin `"module": "mcp_server.main"`) korundu

#### Çalışma Rehberi Geliştirmesi (study_guide.md)
- **Görsel Müfredat Haritası**: Kapsamlı laboratuvar yapısı görselleştirmesi ile “11. Veritabanı Entegrasyon Laboratuvarları” bölümü eklendi
- **Depo Yapısı**: Ondan on bir ana bölüme güncellendi ve 11-MCPServerHandsOnLabs detaylı şekilde tanımlandı
- **Öğrenme Yolu Rehberi**: 00-11 bölümlerini kapsayan gelişmiş gezinim talimatları sağlandı
- **Teknoloji Kapsamı**: FastMCP, PostgreSQL, Azure servisleri entegrasyonu detayları eklendi
- **Öğrenme Çıktıları**: Üretim hazır sunucu geliştirme, veritabanı entegrasyon desenleri ve kurumsal güvenlik vurgulandı

#### Ana README Yapılandırma Geliştirmesi
- **Laboratuvar Temelli Terminoloji**: 11-MCPServerHandsOnLabs içindeki ana README.md dosyasında tutarlı şekilde “Laboratuvar” yapısı kullanıldı
- **Öğrenme Yolu Organizasyonu**: Temel kavramlardan gelişmiş uygulamaya ve üretim dağıtımına kadar net ilerleyiş sağlandı
- **Gerçek Dünya Odaklılık**: Kurumsal düzey desenler ve teknolojiler ile pratik uygulamalı öğrenme ön planda

### Dokümantasyon Kalite ve Tutarlılık İyileştirmeleri
- **Uygulamalı Öğrenme Vurgusu**: Dokümantasyon boyunca pratik, laboratuvar tabanlı yaklaşım güçlendirildi
- **Kurumsal Desenler Vurgusu**: Üretim hazır uygulamalar ve kurumsal güvenlik hususları öne çıkarıldı
- **Teknoloji Entegrasyonu**: Modern Azure servisleri ve yapay zeka entegrasyon desenlerinin kapsamı genişletildi
- **Öğrenme İlerlemesi**: Basit kavramlardan üretim dağıtımına kadar net ve yapılandırılmış yol

## 26 Eylül 2025

### Vaka Çalışmaları Geliştirmesi - GitHub MCP Registry Entegrasyonu

#### Vaka Çalışmaları (09-CaseStudy/) - Ekosistem Geliştirme Odaklı
- **README.md**: Kapsamlı GitHub MCP Registry vaka çalışması ile büyük genişletme
  - **GitHub MCP Registry Vaka Çalışması**: Eylül 2025’teki GitHub MCP Registry lansmanını inceleyen kapsamlı vaka çalışması
    - **Sorun Analizi**: Parçalanmış MCP sunucu keşfi ve dağıtım zorluklarının detaylı incelenmesi
    - **Çözüm Mimarisı**: GitHub’ın merkezi kayıt yaklaşımı ve VS Code’un tek tıklamayla kurulumu
    - **İş Etkisi**: Geliştirici oryantasyonu ve verimlilikte ölçülebilir iyileşmeler
    - **Stratejik Değer**: Modüler ajan dağıtımı ve araçlar arası birlikte çalışabilirlik odaklılık
    - **Ekosistem Geliştirme**: Ajan temelli entegrasyon için temel platform pozisyonlandırması
  - **Zenginleştirilmiş Vaka Çalışması Yapısı**: Yedi vaka çalışmasının tamamı tutarlı biçimlendirme ve kapsamlı açıklamalarla güncellendi
    - Azure AI Seyahat Ajanları: Çok ajanlı orkestrasyon vurgusu
    - Azure DevOps Entegrasyonu: İş akışı otomasyon odaklılık
    - Gerçek Zamanlı Dokümantasyon Çekme: Python konsol istemcisi uygulaması
    - Etkileşimli Çalışma Planı Oluşturucu: Chainlit sohbet tabanlı web uygulaması
    - Editör İçi Dokümantasyon: VS Code ve GitHub Copilot entegrasyonu
    - Azure API Yönetimi: Kurumsal API entegrasyon desenleri
    - GitHub MCP Registry: Ekosistem geliştirme ve topluluk platformu
  - **Kapsamlı Sonuç**: MCP uygulamasının çeşitli boyutlarını kapsayan yedi vaka çalışmasını vurgulayan yeniden yazılmış sonuç bölümü
    - Kurumsal Entegrasyon, Çoklu Ajan Orkestrasyonu, Geliştirici Verimliliği
    - Ekosistem Geliştirme, Eğitimsel Uygulamalar sınıflandırması
    - Mimari desenler, uygulama stratejileri ve en iyi uygulamalar üzerine gelişmiş içgörüler
    - MCP’nin olgun, üretim hazır bir protokol olarak önemi vurgusu

#### Çalışma Rehberi Güncellemeleri (study_guide.md)
- **Görsel Müfredat Haritası**: Vaka Çalışmaları bölümüne GitHub MCP Registry dahil edilerek mindmap güncellendi
- **Vaka Çalışmaları Tanımı**: Genel açıklamalardan yedi kapsamlı vaka çalışmasının detaylı dökümüne yükseltildi
- **Depo Yapısı**: Bölüm 10, vaka çalışmaları kapsamının spesifik uygulama detaylarıyla güncellendi
- **Değişiklik Günlüğü Entegrasyonu**: 26 Eylül 2025 girdisi olarak GitHub MCP Registry eklemesi ve vaka çalışmaları geliştirmeleri eklendi
- **Tarih Güncellemeleri**: En son revizyon tarihi olarak 26 Eylül 2025 footer’da güncellendi

### Dokümantasyon Kalite İyileştirmeleri
- **Tutarlılık Artırma**: Yedi örnek vaka çalışmasının tümünde biçimlendirme ve yapı standartlaştırıldı
- **Kapsamlı Kapsama**: Vaka çalışmaları artık kurumsal, geliştirici verimliliği ve ekosistem geliştirme senaryolarını kapsıyor
- **Stratejik Konumlandırma**: MCP’nin ajan temelli sistem dağıtımı için temel platform olarak rolü güçlendirildi
- **Kaynak Entegrasyonu**: Ek kaynaklar arasında GitHub MCP Registry bağlantısı eklendi

## 15 Eylül 2025

### Gelişmiş Konular Genişletmesi - Özel Taşıyıcılar & Bağlam Mühendisliği

#### MCP Özel Taşıyıcılar (05-AdvancedTopics/mcp-transport/) - Yeni Gelişmiş Uygulama Rehberi
- **README.md**: Özel MCP taşıyıcı mekanizmaları için tam uygulama rehberi
  - **Azure Event Grid Taşıyıcısı**: Kapsamlı sunucusuz olay tabanlı taşıyıcı uygulaması
    - C#, TypeScript ve Python örnekleri, Azure Functions entegrasyonu ile
    - Ölçeklenebilir MCP çözümleri için olay tabanlı mimari desenler
    - Webhook alıcıları ve push tabanlı mesaj işleme
  - **Azure Event Hubs Taşıyıcısı**: Yüksek verimli akış taşıyıcı uygulaması
    - Düşük gecikmeli senaryolar için gerçek zamanlı akış yetenekleri
    - Bölümlendirme stratejileri ve kontrol noktası yönetimi
    - Mesaj toplama ve performans optimizasyonu
  - **Kurumsal Entegrasyon Desenleri**: Üretim hazır mimari örnekler
    - Çoklu Azure Functions arasında dağıtılmış MCP işleme
    - Birden fazla taşıyıcı türünü birleştiren hibrit taşıyıcı mimarileri
    - Mesaj dayanıklılığı, güvenilirlik ve hata yönetimi stratejileri
  - **Güvenlik & İzleme**: Azure Key Vault entegrasyonu ve gözlemlenebilirlik desenleri
    - Yönetilen kimlik doğrulama ve en az ayrıcalık erişimi
    - Application Insights telemetrisi ve performans izleme
    - Devre kesiciler ve hata toleransı desenleri
  - **Test Çerçeveleri**: Özel taşıyıcılar için kapsamlı test stratejileri
    - Test double ve mocking framework’leri ile birim testi
    - Azure Test Containers ile entegrasyon testi
    - Performans ve yük testi değerlendirmeleri

#### Bağlam Mühendisliği (05-AdvancedTopics/mcp-contextengineering/) - Yükselen Yapay Zeka Disiplini
- **README.md**: Bağlam mühendisliği olarak yükselen alanın kapsamlı incelemesi
  - **Temel İlkeler**: Kapsamlı bağlam paylaşımı, eylem karar farkındalığı ve bağlam penceresi yönetimi
  - **MCP Protokol Uyumu**: MCP tasarımının bağlam mühendisliği zorluklarını nasıl ele aldığı
    - Bağlam pencere sınırlamaları ve kademeli yükleme stratejileri
    - Alaka düzeyi belirleme ve dinamik bağlam getirme
    - Çok modlu bağlam işleme ve güvenlik hususları
  - **Uygulama Yaklaşımları**: Tek iş parçacıklı ve çoklu ajan mimarileri
    - Bağlam parçalama ve önceliklendirme teknikleri
    - Kademeli bağlam yükleme ve sıkıştırma stratejileri
    - Katmanlı bağlam yaklaşımları ve getirme optimizasyonu
  - **Ölçüm Çerçevesi**: Bağlam etkinliği değerlendirmesi için yeni metrikler
    - Girdi verimliliği, performans, kalite ve kullanıcı deneyimi değerlendirmeleri
    - Bağlam optimizasyonuna yönelik deneysel yaklaşımlar
    - Başarısızlık analizi ve iyileştirme yöntemleri

#### Müfredat Navigasyon Güncellemeleri (README.md)
- **Gelişmiş Modül Yapısı**: Müfredat tablosu yeni gelişmiş konuları içerecek şekilde güncellendi
  - Bağlam Mühendisliği (5.14) ve Özel Taşıyıcı (5.15) girişleri eklendi
  - Tüm modüllerde tutarlı biçimlendirme ve navigasyon bağlantıları
  - Mevcut içerik kapsamını yansıtan açıklamalar güncellendi

### Dizin Yapısı İyileştirmeleri
- **İsimlendirme Standardizasyonu**: "mcp transport" klasörü, diğer gelişmiş konu klasörleriyle uyum için "mcp-transport" olarak yeniden adlandırıldı
- **İçerik Organizasyonu**: Tüm 05-AdvancedTopics klasörleri artık tutarlı isimlendirme düzenini izliyor (mcp-[konu])

### Dokümantasyon Kalite İyileştirmeleri
- **MCP Spesifikasyon Uyumu**: Tüm yeni içerikler güncel MCP Spesifikasyonu 2025-06-18 referans alıyor
- **Çok Dilde Örnekler**: C#, TypeScript ve Python’da kapsamlı kod örnekleri sunuldu
- **Kurumsal Odak**: Tüm içerikte üretim hazır desenler ve Azure bulut entegrasyonu
- **Görsel Dokümantasyon**: Mimari ve akış görselleştirmeleri için Mermaid diyagramları

## 18 Ağustos 2025

### Dokümantasyon Kapsamlı Güncellemesi - MCP 2025-06-18 Standartları

#### MCP Güvenlik En İyi Uygulamaları (02-Security/) - Tam Modernizasyon
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: MCP Spesifikasyonu 2025-06-18 ile uyumlu tam yeniden yazım
  - **Zorunlu Gereksinimler**: Resmi spesifikasyondan açıkça belirtlenmiş MUTLAKA/MUTLAKA YAPILMAMASI gerekenler net görsel göstergelerle eklendi
  - **12 Temel Güvenlik Uygulaması**: 15 maddelik listeden kapsamlı güvenlik alanlarına yeniden yapılandırıldı
    - Dış kimlik sağlayıcı entegrasyonlu Token Güvenliği ve Kimlik Doğrulama
    - Kriptografik gereksinimlerle Oturum Yönetimi ve Taşıma Güvenliği
    - Microsoft Prompt Shields entegrasyonlu Yapay Zeka Özel Tehdit Koruması
    - En az ayrıcalık ilkesiyle Erişim Kontrolü ve İzinler
    - Azure Content Safety entegrasyonlu İçerik Güvenliği ve İzleme
    - Kapsamlı bileşen doğrulaması ile Tedarik Zinciri Güvenliği
    - PKCE uygulamalı OAuth Güvenliği ve Karışıklık (Confused Deputy) Önleme
    - Otomatikleşmiş yeteneklerle Olay Yanıtı ve Kurtarma
    - Düzenleyici uyumlu Uyum ve Yönetişim
    - Sıfır güven mimarisiyle Gelişmiş Güvenlik Kontrolleri
    - Kapsamlı çözümlerle Microsoft Güvenlik Ekosistem Entegrasyonu
    - Uyarlanabilir uygulamalarla Sürekli Güvenlik Evrimi
  - **Microsoft Güvenlik Çözümleri**: Prompt Shields, Azure Content Safety, Entra ID ve GitHub Advanced Security için geliştirilmiş entegrasyon rehberi
  - **Uygulama Kaynakları**: Resmi MCP Belgeleri, Microsoft Güvenlik Çözümleri, Güvenlik Standartları ve Uygulama Kılavuzları olarak kategorilendirilmiş kapsamlı kaynak bağlantıları

#### Gelişmiş Güvenlik Kontrolleri (02-Security/) - Kurumsal Uygulama
- **MCP-SECURITY-CONTROLS-2025.md**: Kurumsal sınıf güvenlik çerçevesiyle tam yenileme
  - **9 Kapsamlı Güvenlik Alanı**: Temel kontrollerden detaylı kurumsal çerçeveye genişletildi
    - Microsoft Entra ID entegrasyonlu Gelişmiş Kimlik Doğrulama ve Yetkilendirme
    - Kapsamlı doğrulamayla Token Güvenliği ve Geçiş Engelleme Kontrolleri
    - Ele geçirme önleme amaçlı Oturum Güvenliği Kontrolleri
    - Prompt enjeksiyonu ve araç zehirlenmesi önleme amaçlı AI Özel Güvenlik Kontrolleri
    - OAuth proxy güvenliği ile Karışıklık Saldırısı Önleme
    - Sandboxing ve izolasyonla Araç Çalıştırma Güvenliği
    - Bağımlılık doğrulamasıyla Tedarik Zinciri Güvenliği Kontrolleri
    - SIEM entegrasyonlu İzleme ve Tespit Kontrolleri
    - Otomatik yeteneklerle Olay Yanıtı ve Kurtarma
  - **Uygulama Örnekleri**: Ayrıntılı YAML konfigürasyon blokları ve kod örnekleri eklendi
  - **Microsoft Çözümleri Entegrasyonu**: Azure güvenlik hizmetleri, GitHub Advanced Security ve kurumsal kimlik yönetimi tam kapsam

#### Gelişmiş Konular Güvenliği (05-AdvancedTopics/mcp-security/) - Üretime Hazır Uygulama
- **README.md**: Kurumsal güvenlik uygulaması için tam yeniden yazım
  - **Mevcut Spesifikasyona Uyum**: MCP Spesifikasyonu 2025-06-18 ile güncellendi, zorunlu güvenlik gereksinimleri dahil
  - **Gelişmiş Kimlik Doğrulama**: Microsoft Entra ID entegrasyonu, kapsamlı .NET ve Java Spring Security örnekleriyle
  - **Yapay Zeka Güvenliği Entegrasyonu**: Microsoft Prompt Shields ve Azure Content Safety, ayrıntılı Python örnekleri ile uygulama
  - **Gelişmiş Tehdit Hafifletme**: Aşağıdakiler için kapsamlı uygulama örnekleri
    - PKCE ve kullanıcı onayı doğrulamalı Karışıklık Saldırısı Önleme
    - Hedef kontrolü ve güvenli token yönetimli Token Geçişi Engelleme
    - Kriptografik bağlama ve davranışsal analizli Oturum Ele Geçirme Önleme
  - **Kurumsal Güvenlik Entegrasyonu**: Azure Application Insights izleme, tehdit tespit hattı ve tedarik zinciri güvenliği
  - **Uygulama Kontrol Listesi**: Zorunlu ve önerilen güvenlik kontrolleri, Microsoft güvenlik ekosistemi faydaları net şekilde sunuldu

### Dokümantasyon Kalitesi ve Standartlara Uyum
- **Spesifikasyon Referansları**: Tüm referanslar güncel MCP Spesifikasyonu 2025-06-18 ile değiştirildi
- **Microsoft Güvenlik Ekosistemi**: Tüm güvenlik dökümantasyonunda güçlendirilmiş entegrasyon rehberi
- **Pratik Uygulama**: .NET, Java ve Python’da kurumsal desenlerle ayrıntılı kod örnekleri eklendi
- **Kaynak Organizasyonu**: Resmi dokümanlar, güvenlik standartları ve uygulama rehberleri kapsamlı şekilde kategorize edildi
- **Görsel Göstergeler**: Zorunlu gereksinimler ile önerilen uygulamalar net olarak işaretlendi


#### Temel Kavramlar (01-CoreConcepts/) - Tam Modernizasyon
- **Protokol Sürüm Güncellemesi**: Mevcut MCP Spesifikasyonu 2025-06-18 referanslı tarih bazlı versiyon (YYYY-AA-GG formatı) güncellemesi
- **Mimari İyileştirme**: Mevcut MCP mimari desenlerine uygun olarak Hosts, Clients ve Servers açıklamaları güçlendirildi
  - Hosts artık çoklu MCP istemci bağlantılarını yöneten Yapay Zeka uygulamaları olarak net tanımlandı
  - Clients, sunucuyla bire bir ilişkisi olan protokol bağlantıları olarak tanımlandı
  - Servers yerel ve uzak dağıtım senaryolarıyla iyileştirildi
- **Primitif Yeniden Yapılandırma**: Sunucu ve istemci primitiflerinde tam yenileme
  - Sunucu Primitifleri: Kaynaklar (veri kaynakları), Komutlar (şablonlar), Araçlar (çalıştırılabilir fonksiyonlar) detaylı açıklama ve örneklerle
  - İstemci Primitifleri: Örnekleme (LLM tamamlama), Girdi toplama (kullanıcı girişi), Kayıt (hata ayıklama/izleme)
  - Mevcut keşif (`*/list`), getirme (`*/get`) ve çağırma (`*/call`) metod desenleriyle güncellendi
- **Protokol Mimarisi**: İki katmanlı mimari modeli tanıtıldı
  - Veri Katmanı: Yaşam döngüsü yönetimi ve primitiflerle JSON-RPC 2.0 temeli
  - Taşıma Katmanı: STDIO (yerel) ve SSE destekli Streamable HTTP (uzak) taşıma mekanizmaları
- **Güvenlik Çerçevesi**: Açık kullanıcı onayı, veri gizliliği koruması, araç yürütme güvenliği ve taşıma katmanı güvenliği dahil kapsamlı prensipler
- **İletişim Desenleri**: Protokol mesajları başlatma, keşif, yürütme ve bildirim akışları olarak güncellendi
- **Kod Örnekleri**: Güncel MCP SDK desenleri yansıtılarak çoklu dil (.NET, Java, Python, JavaScript) örnekleri yenilendi

#### Güvenlik (02-Security/) - Kapsamlı Güvenlik Yenilemesi  
- **Standartlara Uyum**: MCP Spesifikasyonu 2025-06-18 güvenlik gereksinimleriyle tam uyum sağlandı
- **Kimlik Doğrulama Evrimi**: Özel OAuth sunucularından dış kimlik sağlayıcı (Microsoft Entra ID) yetkilendirmesine geçiş dokümante edildi
- **Yapay Zeka Özel Tehdit Analizi**: Modern AI saldırı vektörleri kapsamı güçlendirildi
  - Gerçek dünya örnekleriyle detaylı prompt enjeksiyonu saldırı senaryoları
  - Araç zehirlenmesi mekanizmaları ve "rug pull" saldırı modelleri
  - Bağlam penceresi zehirlenmesi ve model karışıklığı saldırıları
- **Microsoft AI Güvenlik Çözümleri**: Microsoft güvenlik ekosisteminin kapsamlı tanıtımı
  - Gelişmiş tespit, odaklama ve ayraç teknikleriyle AI Prompt Shields
  - Azure Content Safety entegrasyon desenleri
  - Tedarik zinciri koruması için GitHub Advanced Security
- **Gelişmiş Tehdit Hafifletme**: Ayrıntılı güvenlik kontrolleri
  - MCP’ye özgü oturum ele geçirme saldırıları ve kriptografik oturum ID gereksinimleri ile Oturum Ele Geçirme önleme
  - MCP proxy senaryolarında açık onay gereksinimleriyle Karışıklık Problemleri
  - Zorunlu doğrulama kontrolleri ile Token geçiş açıklıkları
- **Tedarik Zinciri Güvenliği**: Temel modeller, gömme servisleri, bağlam sağlayıcıları ve üçüncü taraf API’leri dahil genişletilmiş AI tedarik zinciri kapsamı
- **Temel Güvenlik**: Kurumsal güvenlik desenleri, sıfır güven mimarisi ve Microsoft güvenlik ekosistemi entegrasyonu güçlendirildi
- **Kaynak Organizasyonu**: Resmi Belgeler, Standartlar, Araştırma, Microsoft Çözümleri ve Uygulama Kılavuzları türlerine göre kategorize edilmiş kapsamlı kaynaklar

### Dokümantasyon Kalite İyileştirmeleri
- **Yapılandırılmış Öğrenme Hedefleri**: Özel ve uygulanabilir sonuçlarla güçlendirilmiş öğrenme hedefleri
- **Çapraz Referanslar**: İlgili güvenlik ve temel kavram konuları arasında bağlantılar eklendi
- **Güncel Bilgiler**: Tüm tarih referansları ve spesifikasyon bağlantıları güncel standartlara göre yenilendi
- **Uygulama Rehberliği**: Her iki bölümde de özel ve uygulanabilir uygulama kılavuzları eklendi

## 16 Temmuz 2025

### README ve Navigasyon İyileştirmeleri
- README.md içinde müfredat navigasyonu tamamen yenilendi
- `<details>` etiketleri daha erişilebilir tablo tabanlı formata dönüştürüldü
- Yeni "alternative_layouts" klasöründe alternatif düzen seçenekleri oluşturuldu
- Kart tabanlı, sekmeli ve akordeon tarzı navigasyon örnekleri eklendi
- Depo yapısı bölümü tüm en güncel dosyaları içerecek şekilde güncellendi
- "Bu Müfredat Nasıl Kullanılır" bölümü net önerilerle geliştirildi
- MCP spesifikasyon bağlantıları doğru URL’lere yönlendirilecek şekilde güncellendi
- Müfredata Context Engineering bölümü (5.14) eklendi

### Çalışma Rehberi Güncellemeleri
- Çalışma rehberi mevcut depo yapısına uygun şekilde tamamen revize edildi
- MCP İstemcileri ve Araçları ile Popüler MCP Sunucuları için yeni bölümler eklendi
- Görsel Müfredat Haritası tüm konuları doğru biçimde yansıtacak şekilde güncellendi
- Gelişmiş Konular açıklaması tüm uzmanlık alanlarını kapsayacak biçimde genişletildi
- Vaka Çalışmaları bölümü gerçek örneklerle güncellendi
- Bu kapsamlı değişiklik günlüğü eklendi

### Topluluk Katkıları (06-CommunityContributions/)
- Görüntü üretimi için MCP sunucuları hakkında ayrıntılı bilgiler eklendi
- VSCode’da Claude kullanımına kapsamlı bölüm eklendi
- Cline terminal istemci kurulum ve kullanım talimatları eklendi
- MCP istemci bölümü tüm popüler istemci seçeneklerini kapsayacak şekilde güncellendi
- Katkı örnekleri daha doğru kod örnekleriyle zenginleştirildi

### Gelişmiş Konular (05-AdvancedTopics/)
- Tüm uzmanlık konu klasörleri tutarlı isimlendirme ile düzenlendi
- Bağlam mühendisliği materyalleri ve örnekleri eklendi
- Foundry ajan entegrasyon dokümantasyonu eklendi
- Entra ID güvenlik entegrasyon dokümantasyonu geliştirildi

## 11 Haziran 2025

### İlk Oluşturma
- MCP for Beginners müfredatının ilk versiyonu yayınlandı
- 10 ana bölüm için temel yapı oluşturuldu
- Navigasyon için Görsel Müfredat Haritası uygulandı
- Birden çok programlama dilinde başlangıç proje örnekleri eklendi

### Başlarken (03-GettingStarted/)
- İlk sunucu uygulama örnekleri oluşturuldu
- İstemci geliştirme rehberliği eklendi
- LLM istemci entegrasyon talimatları dahil edildi
- VS Code entegrasyon dokümantasyonu eklendi
- Server-Sent Events (SSE) sunucu örnekleri uygulandı

### Temel Kavramlar (01-CoreConcepts/)
- İstemci-sunucu mimarisi detaylı olarak açıklandı
- Temel protokol bileşenleri dökümante edildi
- MCP mesajlaşma desenleri belgelendi

## 23 Mayıs 2025

### Depo Yapısı
- Temel klasör yapısıyla depo başlatıldı
- Her ana bölüm için README dosyaları oluşturuldu
- Çeviri altyapısı kuruldu
- Görsel varlıklar ve diyagramlar eklendi

### Dokümantasyon
- Müfredat genel bakışlı ilk README.md oluşturuldu
- CODE_OF_CONDUCT.md ve SECURITY.md eklendi
- Yardım alma rehberi SUPPORT.md oluşturuldu
- İlk çalışma rehberi yapısı oluşturuldu

## 15 Nisan 2025

### Planlama ve Çerçeve
- MCP for Beginners müfredatının ön planlaması yapıldı
- Öğrenme hedefleri ve hedef kitle tanımlandı
- Müfredatın 10 bölümlük yapısı tasarlandı
- Örnekler ve vaka çalışmaları için kavramsal çerçeve geliştirildi
- Anahtar kavramlar için ilk prototip örnekleri oluşturuldu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi tavsiye edilir. Bu çevirinin kullanılması sonucu ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->