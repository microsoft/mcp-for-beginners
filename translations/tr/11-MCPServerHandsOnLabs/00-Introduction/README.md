# MCP Veritabanı Entegrasyonuna Giriş

## 🎯 Bu Laboratuvar Neleri Kapsıyor?

Bu giriş laboratuvarı, Model Context Protocol (MCP) sunucularını veritabanı entegrasyonu ile oluşturmanın kapsamlı bir özetini sunar. İş senaryosunu, teknik mimariyi ve gerçek dünya uygulamalarını, https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail adresindeki Zava Retail analitik kullanım örneği üzerinden anlayacaksınız.

## Genel Bakış

**Model Context Protocol (MCP)**, yapay zeka asistanlarının harici veri kaynaklarına gerçek zamanlı olarak güvenli bir şekilde erişmesini ve etkileşimde bulunmasını sağlar. Veritabanı entegrasyonu ile birleştirildiğinde, MCP veri odaklı yapay zeka uygulamaları için güçlü yetenekler sunar.

Bu öğrenme yolu, yapay zeka asistanlarını PostgreSQL aracılığıyla perakende satış verilerine bağlayan, satır düzeyinde güvenlik, anlamsal arama ve çok kiracılı veri erişimi gibi kurumsal desenleri uygulayan üretime hazır MCP sunucuları oluşturmayı öğretir.

## Öğrenme Hedefleri

Bu laboratuvarın sonunda şunları yapabileceksiniz:

- **Tanımlamak**: Model Context Protocol'ü ve veritabanı entegrasyonu için temel faydalarını
- **Belirlemek**: Veritabanları ile MCP sunucu mimarisinin temel bileşenlerini
- **Anlamak**: Zava Retail kullanım örneğini ve iş gereksinimlerini
- **Tanımak**: Güvenli, ölçeklenebilir veritabanı erişimi için kurumsal desenleri
- **Listelemek**: Bu öğrenme yolunda kullanılan araçlar ve teknolojiler

## 🧭 Zorluk: Yapay Zeka ve Gerçek Dünya Verileri

### Geleneksel Yapay Zeka Sınırlamaları

Modern yapay zeka asistanları son derece güçlüdür ancak gerçek dünya iş verileriyle çalışırken önemli sınırlamalarla karşılaşır:

| **Zorluk** | **Açıklama** | **İş Etkisi** |
|------------|--------------|---------------|
| **Statik Bilgi** | Sabit veri setleriyle eğitilmiş yapay zeka modelleri güncel iş verilerine erişemez | Güncel olmayan içgörüler, kaçırılan fırsatlar |
| **Veri Siloları** | Bilgiler veritabanlarında, API'lerde ve yapay zekanın erişemediği sistemlerde kilitli | Eksik analiz, parçalanmış iş akışları |
| **Güvenlik Kısıtlamaları** | Doğrudan veritabanı erişimi güvenlik ve uyumluluk sorunları yaratır | Sınırlı dağıtım, manuel veri hazırlığı |
| **Karmaşık Sorgular** | İş kullanıcılarının veri içgörülerini çıkarmak için teknik bilgiye ihtiyacı var | Azalan benimseme, verimsiz süreçler |

### MCP Çözümü

Model Context Protocol bu zorlukları şu şekilde çözer:

- **Gerçek Zamanlı Veri Erişimi**: Yapay zeka asistanları canlı veritabanlarını ve API'leri sorgular
- **Güvenli Entegrasyon**: Kimlik doğrulama ve izinlerle kontrol edilen erişim
- **Doğal Dil Arayüzü**: İş kullanıcıları sorularını sade bir İngilizce ile sorar
- **Standartlaştırılmış Protokol**: Farklı yapay zeka platformları ve araçlarıyla çalışır

## 🏪 Zava Retail ile Tanışın: Öğrenme Vaka Çalışmamız https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Bu öğrenme yolunda, **Zava Retail** için bir MCP sunucusu oluşturacağız. Zava Retail, birden fazla mağaza lokasyonuna sahip kurgusal bir DIY perakende zinciridir. Bu gerçekçi senaryo, kurumsal düzeyde MCP uygulamasını gösterir.

### İş Bağlamı

**Zava Retail** şu şekilde faaliyet gösterir:
- **Washington eyaletinde 8 fiziksel mağaza** (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 çevrimiçi mağaza** e-ticaret satışları için
- **Çeşitli ürün kataloğu**: araçlar, donanım, bahçe malzemeleri ve yapı malzemeleri
- **Çok seviyeli yönetim**: mağaza yöneticileri, bölge yöneticileri ve yöneticiler

### İş Gereksinimleri

Mağaza yöneticileri ve yöneticiler yapay zeka destekli analitiklere ihtiyaç duyar:

1. **Satış performansını analiz etmek** mağazalar ve zaman dilimleri arasında
2. **Stok seviyelerini takip etmek** ve yeniden stoklama ihtiyaçlarını belirlemek
3. **Müşteri davranışını anlamak** ve satın alma eğilimlerini analiz etmek
4. **Ürün içgörülerini keşfetmek** anlamsal arama ile
5. **Doğal dil sorguları ile raporlar oluşturmak**
6. **Veri güvenliğini sağlamak** rol tabanlı erişim kontrolü ile

### Teknik Gereksinimler

MCP sunucusu şunları sağlamalıdır:

- **Çok kiracılı veri erişimi**: Mağaza yöneticileri yalnızca kendi mağazalarının verilerini görür
- **Esnek sorgulama**: Karmaşık SQL işlemlerini destekler
- **Anlamsal arama**: Ürün keşfi ve önerileri için
- **Gerçek zamanlı veri**: Mevcut iş durumunu yansıtır
- **Güvenli kimlik doğrulama**: Satır düzeyinde güvenlik ile
- **Ölçeklenebilir mimari**: Birden fazla eşzamanlı kullanıcıyı destekler

## 🏗️ MCP Sunucu Mimari Genel Bakış

MCP sunucumuz, veritabanı entegrasyonu için optimize edilmiş katmanlı bir mimari uygular:

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code AI Client                       │
│                  (Natural Language Queries)                │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/SSE
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     MCP Server                             │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │   Tool Layer    │ │  Security Layer │ │  Config Layer │ │
│  │                 │ │                 │ │               │ │
│  │ • Query Tools   │ │ • RLS Context   │ │ • Environment │ │
│  │ • Schema Tools  │ │ • User Identity │ │ • Connections │ │
│  │ • Search Tools  │ │ • Access Control│ │ • Validation  │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ asyncpg
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                PostgreSQL Database                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │  Retail Schema  │ │   RLS Policies  │ │   pgvector    │ │
│  │                 │ │                 │ │               │ │
│  │ • Stores        │ │ • Store-based   │ │ • Embeddings  │ │
│  │ • Customers     │ │   Isolation     │ │ • Similarity  │ │
│  │ • Products      │ │ • Role Control  │ │   Search      │ │
│  │ • Orders        │ │ • Audit Logs    │ │               │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Azure OpenAI                              │
│               (Text Embeddings)                            │
└─────────────────────────────────────────────────────────────┘
```

### Temel Bileşenler

#### **1. MCP Sunucu Katmanı**
- **FastMCP Framework**: Modern Python MCP sunucu uygulaması
- **Araç Kaydı**: Tip güvenliği ile deklaratif araç tanımları
- **İstek Bağlamı**: Kullanıcı kimliği ve oturum yönetimi
- **Hata Yönetimi**: Güçlü hata yönetimi ve günlükleme

#### **2. Veritabanı Entegrasyon Katmanı**
- **Bağlantı Havuzu**: Verimli asyncpg bağlantı yönetimi
- **Şema Sağlayıcı**: Dinamik tablo şeması keşfi
- **Sorgu Yürütücü**: RLS bağlamı ile güvenli SQL yürütme
- **İşlem Yönetimi**: ACID uyumluluğu ve geri alma işlemleri

#### **3. Güvenlik Katmanı**
- **Satır Düzeyinde Güvenlik**: Çok kiracılı veri izolasyonu için PostgreSQL RLS
- **Kullanıcı Kimliği**: Mağaza yöneticisi kimlik doğrulama ve yetkilendirme
- **Erişim Kontrolü**: İnce ayarlı izinler ve denetim izleri
- **Girdi Doğrulama**: SQL enjeksiyon önleme ve sorgu doğrulama

#### **4. Yapay Zeka Geliştirme Katmanı**
- **Anlamsal Arama**: Ürün keşfi için vektör gömme
- **Azure OpenAI Entegrasyonu**: Metin gömme oluşturma
- **Benzerlik Algoritmaları**: pgvector kosin benzerlik araması
- **Arama Optimizasyonu**: İndeksleme ve performans ayarı

## 🔧 Teknoloji Yığını

### Temel Teknolojiler

| **Bileşen** | **Teknoloji** | **Amaç** |
|-------------|---------------|----------|
| **MCP Framework** | FastMCP (Python) | Modern MCP sunucu uygulaması |
| **Veritabanı** | PostgreSQL 17 + pgvector | İlişkisel veri ve vektör arama |
| **Yapay Zeka Hizmetleri** | Azure OpenAI | Metin gömme ve dil modelleri |
| **Konteynerizasyon** | Docker + Docker Compose | Geliştirme ortamı |
| **Bulut Platformu** | Microsoft Azure | Üretim dağıtımı |
| **IDE Entegrasyonu** | VS Code | Yapay zeka sohbeti ve geliştirme iş akışı |

### Geliştirme Araçları

| **Araç** | **Amaç** |
|----------|----------|
| **asyncpg** | Yüksek performanslı PostgreSQL sürücüsü |
| **Pydantic** | Veri doğrulama ve serileştirme |
| **Azure SDK** | Bulut hizmeti entegrasyonu |
| **pytest** | Test çerçevesi |
| **Docker** | Konteynerizasyon ve dağıtım |

### Üretim Yığını

| **Hizmet** | **Azure Kaynağı** | **Amaç** |
|------------|-------------------|----------|
| **Veritabanı** | Azure Database for PostgreSQL | Yönetilen veritabanı hizmeti |
| **Konteyner** | Azure Container Apps | Sunucusuz konteyner barındırma |
| **Yapay Zeka Hizmetleri** | Azure AI Foundry | OpenAI modelleri ve uç noktaları |
| **İzleme** | Application Insights | Gözlemlenebilirlik ve tanılama |
| **Güvenlik** | Azure Key Vault | Gizlilik ve yapılandırma yönetimi |

## 🎬 Gerçek Dünya Kullanım Senaryoları

Farklı kullanıcıların MCP sunucumuzla nasıl etkileşimde bulunduğunu keşfedelim:

### Senaryo 1: Mağaza Yöneticisi Performans İncelemesi

**Kullanıcı**: Sarah, Seattle Mağaza Yöneticisi  
**Hedef**: Geçen çeyreğin satış performansını analiz etmek

**Doğal Dil Sorgusu**:
> "2024'ün 4. çeyreğinde mağazam için en fazla gelir getiren ilk 10 ürünü göster"

**Ne Olur**:
1. VS Code Yapay Zeka Sohbeti sorguyu MCP sunucusuna gönderir
2. MCP sunucusu Sarah'ın mağaza bağlamını (Seattle) tanımlar
3. RLS politikaları verileri yalnızca Seattle mağazasıyla sınırlar
4. SQL sorgusu oluşturulur ve yürütülür
5. Sonuçlar biçimlendirilir ve Yapay Zeka Sohbetine geri gönderilir
6. Yapay zeka analiz ve içgörüler sağlar

### Senaryo 2: Anlamsal Arama ile Ürün Keşfi

**Kullanıcı**: Mike, Stok Yöneticisi  
**Hedef**: Müşteri talebine benzer ürünleri bulmak

**Doğal Dil Sorgusu**:
> "Dış mekan kullanımı için su geçirmez elektrik bağlantılarına benzer hangi ürünleri satıyoruz?"

**Ne Olur**:
1. Sorgu anlamsal arama aracı tarafından işlenir
2. Azure OpenAI gömme vektörü oluşturur
3. pgvector benzerlik araması yapar
4. İlgili ürünler alaka düzeyine göre sıralanır
5. Sonuçlar ürün detayları ve stok durumu içerir
6. Yapay zeka alternatifler ve paketleme fırsatları önerir

### Senaryo 3: Mağazalar Arası Analitik

**Kullanıcı**: Jennifer, Bölge Yöneticisi  
**Hedef**: Tüm mağazalar arasında performansı karşılaştırmak

**Doğal Dil Sorgusu**:
> "Son 6 ayda tüm mağazalar için kategori bazında satışları karşılaştır"

**Ne Olur**:
1. RLS bağlamı bölge yöneticisi erişimi için ayarlanır
2. Karmaşık çok mağazalı sorgu oluşturulur
3. Veriler mağaza lokasyonları arasında birleştirilir
4. Sonuçlar eğilimler ve karşılaştırmalar içerir
5. Yapay zeka içgörüler ve öneriler sunar

## 🔒 Güvenlik ve Çok Kiracılılık Derinlemesine İnceleme

Uygulamamız kurumsal düzeyde güvenliği önceliklendirir:

### Satır Düzeyinde Güvenlik (RLS)

PostgreSQL RLS veri izolasyonunu sağlar:

```sql
-- Store managers see only their store's data
CREATE POLICY store_manager_policy ON retail.orders
  FOR ALL TO store_managers
  USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_policy ON retail.orders
  FOR ALL TO regional_managers
  USING (store_id = ANY(get_user_store_list()));
```

### Kullanıcı Kimliği Yönetimi

Her MCP bağlantısı şunları içerir:
- **Mağaza Yöneticisi Kimliği**: RLS bağlamı için benzersiz tanımlayıcı
- **Rol Ataması**: İzinler ve erişim seviyeleri
- **Oturum Yönetimi**: Güvenli kimlik doğrulama jetonları
- **Denetim Günlüğü**: Tam erişim geçmişi

### Veri Koruma

Birden fazla güvenlik katmanı:
- **Bağlantı Şifreleme**: Tüm veritabanı bağlantıları için TLS
- **SQL Enjeksiyon Önleme**: Yalnızca parametreli sorgular
- **Girdi Doğrulama**: Kapsamlı istek doğrulama
- **Hata Yönetimi**: Hata mesajlarında hassas veri yok

## 🎯 Temel Çıkarımlar

Bu giriş bölümünü tamamladıktan sonra şunları anlamış olmalısınız:

✅ **MCP Değer Önerisi**: MCP'nin yapay zeka asistanlarını gerçek dünya verileriyle nasıl bağladığı  
✅ **İş Bağlamı**: Zava Retail'in gereksinimleri ve zorlukları  
✅ **Mimari Genel Bakış**: Temel bileşenler ve etkileşimleri  
✅ **Teknoloji Yığını**: Kullanılan araçlar ve çerçeveler  
✅ **Güvenlik Modeli**: Çok kiracılı veri erişimi ve koruma  
✅ **Kullanım Desenleri**: Gerçek dünya sorgu senaryoları ve iş akışları  

## 🚀 Sıradaki Adım

Daha derine inmeye hazır mısınız? Şunlarla devam edin:

**[Lab 01: Temel Mimari Kavramlar](../01-Architecture/README.md)**

MCP sunucu mimari desenleri, veritabanı tasarım ilkeleri ve perakende analitik çözümümüzü güçlendiren ayrıntılı teknik uygulama hakkında bilgi edinin.

## 📚 Ek Kaynaklar

### MCP Belgeleri
- [MCP Spesifikasyonu](https://modelcontextprotocol.io/docs/) - Resmi protokol belgeleri
- [MCP için Başlangıç Kılavuzu](https://aka.ms/mcp-for-beginners) - Kapsamlı MCP öğrenme rehberi
- [FastMCP Belgeleri](https://github.com/modelcontextprotocol/python-sdk) - Python SDK belgeleri

### Veritabanı Entegrasyonu
- [PostgreSQL Belgeleri](https://www.postgresql.org/docs/) - Tam PostgreSQL referansı
- [pgvector Kılavuzu](https://github.com/pgvector/pgvector) - Vektör uzantısı belgeleri
- [Satır Düzeyinde Güvenlik](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS rehberi

### Azure Hizmetleri
- [Azure OpenAI Belgeleri](https://docs.microsoft.com/azure/cognitive-services/openai/) - Yapay zeka hizmeti entegrasyonu
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Yönetilen veritabanı hizmeti
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Sunucusuz konteynerler

---

**Uyarı**: Bu, kurgusal perakende verilerini kullanan bir öğrenme egzersizidir. Benzer çözümleri üretim ortamlarında uygularken her zaman kuruluşunuzun veri yönetimi ve güvenlik politikalarını takip edin.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmemektedir.