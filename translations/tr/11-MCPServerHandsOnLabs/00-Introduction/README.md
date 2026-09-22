# MCP Veritabanı Entegrasyonuna Giriş

> [!NOTE]
> Bu öğrenme yolundaki şemalar veya kodlar HTTP/SSE veya başlatma
> seçeneklerini kullandığında örneğin MCP `2025-11-25` bağımlılıklarını yansıtır. Yeni
> uygulamalarda, `2026-07-28` durumsuz istekleri ve Akışlanabilir HTTP kullanın.

## 🎯 Bu Laboratuvar Ne Kapsar

Bu giriş laboratuvarı, Veritabanı entegrasyonlu Model Context Protocol (MCP) sunucuları oluşturmanın kapsamlı bir genel bakışını sunar. İş gereksinimlerini, teknik mimariyi ve gerçek dünya uygulamalarını https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail adresindeki Zava Retail analiz kullanım durumu aracılığıyla anlayacaksınız.

## Genel Bakış

**Model Context Protocol (MCP)**, yapay zeka asistanlarının harici veri kaynaklarına güvenli ve gerçek zamanlı erişimini ve etkileşimini sağlar. Veritabanı entegrasyonu ile birleştiğinde, MCP veri odaklı yapay zeka uygulamaları için güçlü olanaklar sunar.

Bu öğrenme yolu, yapay zeka asistanlarını PostgreSQL üzerinden perakende satış verilerine bağlayan, Row Level Security, anlamsal arama ve çok kiracılı veri erişimi gibi kurumsal desenleri uygulayan üretime hazır MCP sunucuları oluşturmayı öğretir.

## Öğrenme Hedefleri

Bu laboratuvar sonunda şunları yapabileceksiniz:

- **Model Context Protocol’ü** ve veritabanı entegrasyonundaki temel faydalarını tanımlamak
- Veritabanlı bir MCP sunucu mimarisinin **ana bileşenlerini tanımlamak**
- Zava Retail kullanım durumu ve iş gereksinimlerini **anlamak**
- Güvenli ve ölçeklenebilir veritabanı erişimi için kurumsal desenleri **tanımak**
- Bu öğrenme yolunda kullanılan araçlar ve teknolojileri **listelemek**

## 🧭 Zorluk: Yapay Zeka Gerçek Veriyle Buluşuyor

### Geleneksel Yapay Zeka Sınırlamaları

Günümüz yapay zeka asistanları inanılmaz güçlüdür fakat gerçek dünya iş verileriyle çalışırken önemli sınırlamalarla karşılaşırlar:

| **Zorluk** | **Açıklama** | **İş Etkisi** |
|---------------|-----------------|-------------------|
| **Statik Bilgi** | Sabit veri setleri üzerinde eğitilen modeller güncel iş verisine erişemez | Eski bilgiler, kaçırılan fırsatlar |
| **Veri Adaçayı** | Veritabanları, API’ler ve sistemlerde kilitli bilgiye AI erişimi yok | Eksik analiz, parçalanmış iş akışları |
| **Güvenlik Kısıtlamaları** | Doğrudan veritabanı erişimi güvenlik ve uyumluluk endişeleri yaratır | Kısıtlı dağıtım, manuel veri hazırlama |
| **Karmaşık Sorgular** | İş kullanıcıları veri içgörüsü çıkarmak için teknik bilgiye ihtiyaç duyar | Azalan benimseme, verimsiz süreçler |

### MCP Çözümü

Model Context Protocol bu zorlukları şu şekilde ele alır:

- **Gerçek Zamanlı Veri Erişimi**: Yapay zeka asistanları canlı veritabanları ve API’lere sorgu gönderir
- **Güvenli Entegrasyon**: Kimlik doğrulama ve izinlerle kontrol edilen erişim
- **Doğal Dil Arayüzü**: İş kullanıcıları sorularını sade İngilizce ile sorar
- **Standardize Protokol**: Farklı yapay zeka platformları ve araçları arasında çalışır

## 🏪 Tanışın: Zava Retail - Öğrenme Vaka Çalışmamız https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Bu öğrenme yolunda, birden fazla mağaza konumuna sahip kurgusal bir DIY perakende zinciri olan **Zava Retail** için bir MCP sunucusu oluşturacağız. Bu gerçekçi senaryo, kurumsal sınıf MCP uygulamasını gösterir.

### İş Bağlamı

**Zava Retail** aşağıdaki şekilde faaliyet gösterir:
- Washington eyaletinde **8 fiziksel mağaza** (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- E-ticaret satışları için **1 online mağaza**
- Aletler, donanım, bahçe malzemeleri ve yapı malzemeleri dahil **çeşitli ürün kataloğu**
- Mağaza yöneticileri, bölge yöneticileri ve yöneticilerden oluşan **çok katmanlı yönetim**

### İş Gereksinimleri

Mağaza yöneticileri ve yöneticiler yapay zeka destekli analizlere ihtiyaç duyar:

1. Mağazalar ve zaman dilimleri arasında **satış performansını analiz etmek**
2. **Envanter seviyelerini takip etmek** ve yeniden stoklama ihtiyaçlarını belirlemek
3. **Müşteri davranışı ve satın alma kalıplarını anlamak**
4. Anlamsal arama yoluyla **ürün içgörüleri keşfetmek**
5. Doğal dil sorgularıyla **raporlar oluşturmak**
6. Rol tabanlı erişim kontrolü ile **veri güvenliğini sağlamak**

### Teknik Gereksinimler

MCP sunucusu şunları sağlamalıdır:

- Mağaza yöneticilerinin yalnızca kendi mağazalarının verilerini görebildiği **çok kiracılı veri erişimi**
- Karmaşık SQL işlemlerini destekleyen **esnek sorgulama**
- Ürün keşfi ve önerileri için **anlamsal arama**
- Güncel iş durumunu yansıtan **gerçek zamanlı veri**
- Satır düzeyi güvenlik ile **güvenli kimlik doğrulama**
- Çoklu eş zamanlı kullanıcıları destekleyen **ölçeklenebilir mimari**

## 🏗️ MCP Sunucu Mimarisi Genel Bakış

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

### Ana Bileşenler

#### **1. MCP Sunucu Katmanı**
- **FastMCP Framework**: Modern Python MCP sunucu uygulaması
- **Araç Kaydı**: Tip güvenliği ile tanımlayıcı araç tanımları
- **İstek Bağlamı**: Kullanıcı kimliği ve oturum yönetimi
- **Hata Yönetimi**: Sağlam hata yönetimi ve kayıt tutma

#### **2. Veritabanı Entegrasyon Katmanı**
- **Bağlantı Havuzu**: Verimli asyncpg bağlantı yönetimi
- **Şema Sağlayıcı**: Dinamik tablo şeması keşfi
- **Sorgu Yürütücü**: RLS bağlamıyla güvenli SQL yürütme
- **İşlem Yönetimi**: ACID uyumluluğu ve geri alma işlemleri

#### **3. Güvenlik Katmanı**
- **Satır Düzeyi Güvenlik**: Çok kiracılı veri izolasyonu için PostgreSQL RLS
- **Kullanıcı Kimliği**: Mağaza yöneticisi kimlik doğrulama ve yetkilendirme
- **Erişim Kontrolü**: Ayrıntılı izinler ve denetim kayıtları
- **Girdi Doğrulama**: SQL enjeksiyonu önleme ve sorgu doğrulama

#### **4. Yapay Zeka Geliştirme Katmanı**
- **Anlamsal Arama**: Ürün keşfi için vektör gömme
- **Azure OpenAI Entegrasyonu**: Metin gömme oluşturma
- **Benzerlik Algoritmaları**: pgvector kosinüs benzerlik araması
- **Arama Optimizasyonu**: İndeksleme ve performans ayarı

## 🔧 Teknoloji Yığını

### Temel Teknolojiler

| **Bileşen** | **Teknoloji** | **Amaç** |
|---------------|----------------|-------------|
| **MCP Framework** | FastMCP (Python) | Modern MCP sunucu uygulaması |
| **Veritabanı** | PostgreSQL 17 + pgvector | Vektör aramalı ilişkisel veri |
| **Yapay Zeka Servisleri** | Azure OpenAI | Metin gömmeleri ve dil modelleri |
| **Konteynerleştirme** | Docker + Docker Compose | Geliştirme ortamı |
| **Bulut Platformu** | Microsoft Azure | Üretim dağıtımı |
| **IDE Entegrasyonu** | VS Code | Yapay zeka sohbeti ve geliştirme iş akışı |

### Geliştirme Araçları

| **Araç** | **Amaç** |
|----------|-------------|
| **asyncpg** | Yüksek performanslı PostgreSQL sürücüsü |
| **Pydantic** | Veri doğrulama ve serileştirme |
| **Azure SDK** | Bulut servisi entegrasyonu |
| **pytest** | Test çerçevesi |
| **Docker** | Konteynerleştirme ve dağıtım |

### Üretim Yığını

| **Hizmet** | **Azure Kaynağı** | **Amaç** |
|-------------|-------------------|-------------|
| **Veritabanı** | Azure Database for PostgreSQL | Yönetilen veritabanı servisi |
| **Konteyner** | Azure Container Apps | Sunucusuz konteyner barındırma |
| **Yapay Zeka Servisleri** | Microsoft Foundry | OpenAI modelleri ve uç noktalar |
| **İzleme** | Application Insights | Gözlemlenebilirlik ve teşhis |
| **Güvenlik** | Azure Key Vault | Gizli bilgiler ve yapılandırma yönetimi |

## 🎬 Gerçek Dünya Kullanım Senaryoları

Farklı kullanıcıların MCP sunucumuzla nasıl etkileştiğini keşfedelim:

### Senaryo 1: Mağaza Müdürü Performans İncelemesi

**Kullanıcı**: Sarah, Seattle Mağaza Müdürü  
**Amaç**: Son çeyrek satış performansını analiz etmek

**Doğal Dil Sorgusu**:
> "2024 4. çeyreğinde mağazamın gelirine göre ilk 10 ürünü göster"

**Ne Olur**:
1. VS Code AI Sohbet MCP sunucusuna sorguyu gönderir
2. MCP sunucu Sarah'nın mağaza bağlamını (Seattle) tanımlar
3. RLS politikaları yalnızca Seattle mağazasına ait verileri filtreler
4. SQL sorgusu oluşturulur ve yürütülür
5. Sonuçlar biçimlendirilip AI sohbetine gönderilir
6. Yapay zeka analiz ve içgörüler sunar

### Senaryo 2: Anlamsal Arama ile Ürün Keşfi

**Kullanıcı**: Mike, Envanter Müdürü  
**Amaç**: Bir müşteri talebine benzer ürünleri bulmak

**Doğal Dil Sorgusu**:
> "Dış mekanda kullanılan su geçirmez elektrik bağlantı parçaları gibi ürünlerimiz nelerdir?"

**Ne Olur**:
1. Sorgu anlamsal arama aracı tarafından işlenir
2. Azure OpenAI gömme vektörü oluşturur
3. pgvector benzerlik araması yapar
4. Alakalı ürünler önem sırasına göre sıralanır
5. Sonuçlar ürün detayları ve bulunabilirlik içerir
6. AI alternatifler ve paketleme fırsatları önerir

### Senaryo 3: Mağazalar Arası Analiz

**Kullanıcı**: Jennifer, Bölge Müdürü  
**Amaç**: Tüm mağazalar arasında performans karşılaştırması

**Doğal Dil Sorgusu**:
> "Son 6 ayda tüm mağazalar için kategori bazlı satışları karşılaştır"

**Ne Olur**:
1. RLS bağlamı bölge müdürü erişimi için ayarlanır
2. Karmaşık çok mağaza sorgusu oluşturulur
3. Veriler mağaza konumları arasında toplanır
4. Sonuçlar trendler ve karşılaştırmalar içerir
5. Yapay zeka içgörüler ve öneriler sunar

## 🔒 Güvenlik ve Çok Kiracılık Derinlemesine

Uygulamamız kurumsal sınıf güvenliği önceliklendirir:

### Satır Düzeyi Güvenlik (RLS)

PostgreSQL RLS veri izolasyonunu garantiler:

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
- **Mağaza Müdürü ID’si**: RLS bağlamında benzersiz tanımlayıcı
- **Rol Ataması**: İzinler ve erişim seviyeleri
- **Oturum Yönetimi**: Güvenli kimlik doğrulama belirteçleri
- **Denetim Kaydı**: Tam erişim geçmişi

### Veri Koruma

Birden çok güvenlik katmanı:
- **Bağlantı Şifreleme**: Tüm veritabanı bağlantılarında TLS
- **SQL Enjeksiyon Önleme**: Yalnızca parametreli sorgular
- **Girdi Doğrulama**: Kapsamlı istek doğrulama
- **Hata Yönetimi**: Hata mesajlarında hassas veri yok

## 🎯 Temel Çıkarımlar

Bu giriş tamamlandıktan sonra şunları anlamış olmalısınız:

✅ **MCP Değer Önerisi**: MCP’nin yapay zeka asistanları ile gerçek veri arasındaki köprüsü  
✅ **İş Bağlamı**: Zava Retail’in gereksinimleri ve zorlukları  
✅ **Mimari Genel Bakış**: Ana bileşenler ve etkileşimleri  
✅ **Teknoloji Yığını**: Bu öğrenme yolunda kullanılan araç ve çerçeveler  
✅ **Güvenlik Modeli**: Çok kiracılı veri erişimi ve koruma  
✅ **Kullanım Desenleri**: Gerçek dünya sorgu senaryoları ve iş akışları  

## 🚀 Sonraki Adım

Daha derine inmeye hazır mısınız? Şununla devam edin:

**[Laboratuvar 01: Temel Mimari Kavramlar](../01-Architecture/README.md)**

MCP sunucu mimarisi desenlerini, veritabanı tasarım ilkelerini ve perakende analiz çözümümüzü güçlendiren ayrıntılı teknik uygulamayı öğrenin.

## 📚 Ek Kaynaklar

### MCP Dokümantasyonu
- [MCP Spesifikasyonu](https://modelcontextprotocol.io/docs/) - Resmi protokol dokümantasyonu
- [Yeni Başlayanlar için MCP](https://aka.ms/mcp-for-beginners) - Kapsamlı MCP öğrenme rehberi
- [FastMCP Dokümantasyonu](https://github.com/modelcontextprotocol/python-sdk) - Python SDK dokümanları

### Veritabanı Entegrasyonu
- [PostgreSQL Dokümantasyonu](https://www.postgresql.org/docs/) - Tam PostgreSQL referansı
- [pgvector Kılavuzu](https://github.com/pgvector/pgvector) - Vektör eklentisi dokümantasyonu
- [Satır Düzeyi Güvenlik](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS kılavuzu

### Azure Servisleri
- [Azure OpenAI Dokümantasyonu](https://docs.microsoft.com/azure/cognitive-services/openai/) - Yapay zeka servis entegrasyonu
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Yönetilen veritabanı servisi
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Sunucusuz konteynerler

---

**Feragatname**: Bu öğrenme egzersizi kurgusal perakende verileri kullanmaktadır. Benzer çözümleri üretim ortamlarında uygularken daima kuruluşunuzun veri yönetimi ve güvenlik politikalarına uyun.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->