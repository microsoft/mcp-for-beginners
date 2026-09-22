# 🚀 MCP Sunucusu ile PostgreSQL - Tam Öğrenme Rehberi

## 🧠 MCP Veritabanı Entegrasyonu Öğrenme Yolunun Genel Görünümü

Bu kapsamlı öğrenme rehberi, pratik bir perakende analitiği uygulaması aracılığıyla veritabanlarıyla entegre olan üretime hazır **Model Context Protocol (MCP) sunucuları** oluşturmayı öğretir. **Satır Düzeyinde Güvenlik (RLS)**, **anlamsal arama**, **Azure AI entegrasyonu** ve **çok kiracılı veri erişimi** gibi kurumsal düzeydeki desenleri öğreneceksiniz.

İster bir arka uç geliştiricisi, AI mühendisi ya da veri mimarı olun, bu rehber aşağıdaki MCP sunucusu https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail ile gerçek dünya örnekleri ve uygulamalı egzersizler içeren yapılandırılmış öğrenim sunar.

## 🔗 Resmi MCP Kaynakları

- 📘 [MCP Dokümantasyonu](https://modelcontextprotocol.io/) – Detaylı eğitimler ve kullanıcı kılavuzları
- 📜 [MCP Spesifikasyonu (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Protokol mimarisi ve teknik referanslar
- 🧑‍💻 [MCP GitHub Deposu](https://github.com/modelcontextprotocol) – Açık kaynak SDK'lar, araçlar ve kod örnekleri
- 🌐 [MCP Topluluğu](https://github.com/orgs/modelcontextprotocol/discussions) – Tartışmalara katılın ve topluluğa katkıda bulunun
- 🔒 [OWASP MCP İlk 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Güvenlik en iyi uygulamaları ve risk azaltmaları


## 🧭 MCP Veritabanı Entegrasyonu Öğrenme Yolu

### 📚 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail için Tam Öğrenme Yapısı

| Laboratuvar | Konu | Açıklama | Bağlantı |
|--------|-------|-------------|------|
| **Laboratuvar 1-3: Temeller** | | | |
| 00 | [MCP Veritabanı Entegrasyonuna Giriş](./00-Introduction/README.md) | MCP'nin veritabanı entegrasyonu ve perakende analitiği kullanım durumu genel bakışı | [Buradan Başla](./00-Introduction/README.md) |
| 01 | [Temel Mimari Kavramlar](./01-Architecture/README.md) | MCP sunucu mimarisi, veritabanı katmanları ve güvenlik desenlerini anlama | [Öğren](./01-Architecture/README.md) |
| 02 | [Güvenlik ve Çok Kiracılık](./02-Security/README.md) | Satır Düzeyinde Güvenlik, kimlik doğrulama ve çok kiracılı veri erişimi | [Öğren](./02-Security/README.md) |
| 03 | [Ortam Kurulumu](./03-Setup/README.md) | Geliştirme ortamı, Docker, Azure kaynaklarının kurulumu | [Kurulum](./03-Setup/README.md) |
| **Laboratuvar 4-6: MCP Sunucusunu İnşa Etme** | | | |
| 04 | [Veritabanı Tasarımı ve Şema](./04-Database/README.md) | PostgreSQL kurulumu, perakende şeması tasarımı ve örnek veri | [İnşa Et](./04-Database/README.md) |
| 05 | [MCP Sunucu Uygulaması](./05-MCP-Server/README.md) | Veritabanı entegrasyonlu FastMCP sunucusunu oluşturma | [İnşa Et](./05-MCP-Server/README.md) |
| 06 | [Araç Geliştirme](./06-Tools/README.md) | Veritabanı sorgu araçları ve şema introspeksiyonunu oluşturma | [İnşa Et](./06-Tools/README.md) |
| **Laboratuvar 7-9: İleri Özellikler** | | | |
| 07 | [Anlamsal Arama Entegrasyonu](./07-Semantic-Search/README.md) | Azure OpenAI ve pgvector ile vektör gömme uygulaması | [İlerle](./07-Semantic-Search/README.md) |
| 08 | [Test ve Hata Ayıklama](./08-Testing/README.md) | Test stratejileri, hata ayıklama araçları ve doğrulama yöntemleri | [Test Et](./08-Testing/README.md) |
| 09 | [VS Code Entegrasyonu](./09-VS-Code/README.md) | VS Code MCP entegrasyonu ve AI Sohbet kullanımı yapılandırması | [Entegre Et](./09-VS-Code/README.md) |
| **Laboratuvar 10-12: Üretim ve En İyi Uygulamalar** | | | |
| 10 | [Dağıtım Stratejileri](./10-Deployment/README.md) | Docker dağıtımı, Azure Container Apps ve ölçeklendirme hususları | [Dağıt](./10-Deployment/README.md) |
| 11 | [İzleme ve Gözlemlenebilirlik](./11-Monitoring/README.md) | Application Insights, günlükleme, performans izleme | [İzle](./11-Monitoring/README.md) |
| 12 | [En İyi Uygulamalar ve Optimizasyon](./12-Best-Practices/README.md) | Performans optimizasyonu, güvenlik güçlendirmeleri ve üretim ipuçları | [Optimize Et](./12-Best-Practices/README.md) |

### 💻 Neler İnşa Edeceksiniz

Bu öğrenme yolunun sonunda, şu özelliklere sahip tam bir **Zava Perakende Analitiği MCP Sunucusu** oluşturmuş olacaksınız:

- **Müşteri siparişleri, ürünler ve stokların bulunduğu çok tablolu perakende veritabanı**
- **Mağaza bazında veri izolasyonu için Satır Düzeyinde Güvenlik**
- **Azure OpenAI gömme kullanarak anlamsal ürün araması**
- **Doğal dil sorguları için VS Code AI Chat entegrasyonu**
- **Docker ve Azure ile üretime hazır dağıtım**
- **Application Insights ile kapsamlı izleme**

## 🎯 Öğrenme İçin Ön Koşullar

Bu öğrenme yolundan en iyi şekilde yararlanmak için şu özelliklere sahip olmalısınız:

- **Programlama Deneyimi**: Tercihen Python veya benzeri diller hakkında bilgi
- **Veritabanı Bilgisi**: Temel SQL ve ilişkisel veritabanları anlayışı
- **API Kavramları**: REST API'leri ve HTTP kavramlarının anlaşılması
- **Geliştirme Araçları**: Komut satırı, Git ve kod editörleri deneyimi
- **Bulut Temelleri**: (İsteğe bağlı) Azure veya benzeri bulut platformları hakkında temel bilgi
- **Docker Bilgisi**: (İsteğe bağlı) Konteynerleştirme kavramları hakkında anlayış

### Gerekli Araçlar

- **Docker Desktop** - PostgreSQL ve MCP sunucusunu çalıştırmak için
- **Azure CLI** - Bulut kaynaklarının dağıtımı için
- **VS Code** - Geliştirme ve MCP entegrasyonu için
- **Git** - Versiyon kontrol için
- **Python 3.8+** - MCP sunucu geliştirme için

## 📚 Çalışma Rehberi ve Kaynaklar

Bu öğrenme yolu, etkili ilerlemeniz için kapsamlı kaynaklar içerir:

### Çalışma Rehberi

Her laboratuvarda:
- **Net öğrenme hedefleri** - Neler başaracağınız
- **Adım adım talimatlar** - Detaylı uygulama rehberleri
- **Kod örnekleri** - Açıklamalı çalışan örnekler
- **Egzersizler** - Uygulamalı pratik fırsatları
- **Sorun giderme rehberleri** - Yaygın sorunlar ve çözümleri
- **Ek kaynaklar** - Daha fazla okuma ve keşif

### Ön Koşul Kontrolü

Her laboratuvara başlamadan önce:
- **Gerekli bilgi** - Önceden bilmeniz gerekenler
- **Ortam doğrulaması** - Ortamınızı nasıl doğrulayacağınız
- **Zaman tahminleri** - Beklenen tamamlanma süresi
- **Öğrenme çıktıları** - Tamamlandıktan sonra neler bileceğiniz

### Önerilen Öğrenme Yolları

Deneyim seviyenize göre yolunuzu seçin:

#### 🟢 **Yeni Başlayanlar Yolu** (MCP’ye yeni)
1. Öncelikle [MCP for Beginners](https://aka.ms/mcp-for-beginners) 0-10 numaralarını tamamladığınızdan emin olun
2. Temellerinizi pekiştirmek için 00-03 laboratuvarlarını tamamlayın
3. Uygulama için 04-06 laboratuvarlarını takip edin
4. Pratik kullanım için 07-09 laboratuvarlarını deneyin

#### 🟡 **Orta Seviye Yolu** (Biraz MCP deneyimi)
1. Veritabanı kavramları için 00-01 laboratuvarlarını gözden geçirin
2. Uygulama için 02-06 laboratuvarlarına odaklanın
3. İleri özellikler için 07-12 laboratuvarlarını derinlemesine inceleyin

#### 🔴 **İleri Seviye Yolu** (MCP deneyimli)
1. Bağlam için 00-03 laboratuvarlarını hızlıca inceleyin
2. Veritabanı entegrasyonu için 04-09 laboratuvarlarına odaklanın
3. Üretime dağıtım için 10-12 laboratuvarlarını yoğunlaşın

## 🛠️ Bu Öğrenme Yolunu Etkili Kullanma

### Sıralı Öğrenme (Önerilen)

Tam anlayış için laboratuvarları sırayla çalışın:

1. **Genel bakışı okuyun** - Neler öğreneceğinizi anlayın
2. **Ön koşulları kontrol edin** - Gereken bilgiye sahip olduğunuzdan emin olun
3. **Adım adım rehberleri takip edin** - Öğrenirken uygulayın
4. **Egzersizleri tamamlayın** - Bilginizi pekiştirin
5. **Anahtar noktaları gözden geçirin** - Öğrenme çıktılarınızı sağlamlaştırın

### Hedefe Yönelik Öğrenme

Belirli becerilere ihtiyacınız varsa:

- **Veritabanı Entegrasyonu**: 04-06 laboratuvarlarına odaklanın
- **Güvenlik Uygulaması**: 02, 08, 12 laboratuvarlarına yoğunlaşın
- **AI/Anlamsal Arama**: 07 laboratuvarını derinlemesine inceleyin
- **Üretim Dağıtımı**: 10-12 laboratuvarlarını çalışın

### Uygulamalı Pratik

Her laboratuvarda:
- **Çalışan kod örnekleri** - Kopyalayın, değiştirin ve deneyin
- **Gerçek dünya senaryoları** - Pratik perakende analitiği kullanım durumları
- **Kademeli karmaşıklık** - Basitten ileriye doğru inşa etme
- **Doğrulama adımları** - Uygulamanızın çalıştığını doğrulayın

## 🌟 Topluluk ve Destek

### Yardım Alın

- **Azure AI Discord**: [Uzman desteği için katılın](https://discord.com/invite/ByRwuEEgH4)
- **GitHub Deposu ve Uygulama Örneği**: [Dağıtım Örneği ve Kaynaklar](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP Topluluğu**: [Genel MCP tartışmalarına katılın](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Başlamaya Hazır mısınız?

Yolculuğunuza **[Laboratuvar 00: MCP Veritabanı Entegrasyonuna Giriş](./00-Introduction/README.md)** ile başlayın

---

*Bu kapsamlı, uygulamalı öğrenme deneyimiyle üretime hazır MCP sunucuları veritabanı entegrasyonu ile inşa etmeyi ustaca öğrenin.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->