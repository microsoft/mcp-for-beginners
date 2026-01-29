# 🚀 PostgreSQL ile MCP Sunucusu - Tam Öğrenme Kılavuzu

## 🧠 MCP Veritabanı Entegrasyonu Öğrenme Yolunun Genel Bakışı

Bu kapsamlı öğrenme kılavuzu, veritabanlarıyla entegre olan üretime hazır **Model Context Protocol (MCP) sunucuları** oluşturmayı, pratik bir perakende analitiği uygulaması üzerinden öğretir. **Satır Düzeyinde Güvenlik (RLS)**, **anlamsal arama**, **Azure AI entegrasyonu** ve **çok kiracılı veri erişimi** gibi kurumsal düzeydeki kalıpları öğreneceksiniz.

İster bir backend geliştirici, ister bir AI mühendisi veya veri mimarı olun, bu kılavuz, gerçek dünya örnekleri ve uygulamalı alıştırmalarla yapılandırılmış bir öğrenme deneyimi sunar. MCP sunucusunu adım adım öğrenmek için şu bağlantıyı takip edebilirsiniz: https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Resmi MCP Kaynakları

- 📘 [MCP Belgeleri](https://modelcontextprotocol.io/) – Ayrıntılı eğitimler ve kullanıcı kılavuzları
- 📜 [MCP Spesifikasyonu](https://modelcontextprotocol.io/docs/) – Protokol mimarisi ve teknik referanslar
- 🧑‍💻 [MCP GitHub Deposu](https://github.com/modelcontextprotocol) – Açık kaynak SDK'lar, araçlar ve kod örnekleri
- 🌐 [MCP Topluluğu](https://github.com/orgs/modelcontextprotocol/discussions) – Tartışmalara katılın ve topluluğa katkıda bulunun

## 🧭 MCP Veritabanı Entegrasyonu Öğrenme Yolu

### 📚 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail için Tam Öğrenme Yapısı

| Lab | Konu | Açıklama | Bağlantı |
|--------|-------|-------------|------|
| **Lab 1-3: Temeller** | | | |
| 00 | [MCP Veritabanı Entegrasyonuna Giriş](./00-Introduction/README.md) | MCP'nin veritabanı entegrasyonu ve perakende analitiği kullanım senaryosuna genel bakış | [Buradan Başlayın](./00-Introduction/README.md) |
| 01 | [Temel Mimari Kavramlar](./01-Architecture/README.md) | MCP sunucu mimarisi, veritabanı katmanları ve güvenlik kalıplarını anlama | [Öğren](./01-Architecture/README.md) |
| 02 | [Güvenlik ve Çok Kiracılılık](./02-Security/README.md) | Satır Düzeyinde Güvenlik, kimlik doğrulama ve çok kiracılı veri erişimi | [Öğren](./02-Security/README.md) |
| 03 | [Ortam Kurulumu](./03-Setup/README.md) | Geliştirme ortamı, Docker, Azure kaynaklarının kurulumu | [Kurulum](./03-Setup/README.md) |
| **Lab 4-6: MCP Sunucusunu İnşa Etme** | | | |
| 04 | [Veritabanı Tasarımı ve Şeması](./04-Database/README.md) | PostgreSQL kurulumu, perakende şema tasarımı ve örnek veri | [İnşa Et](./04-Database/README.md) |
| 05 | [MCP Sunucu Uygulaması](./05-MCP-Server/README.md) | Veritabanı entegrasyonu ile FastMCP sunucusunu oluşturma | [İnşa Et](./05-MCP-Server/README.md) |
| 06 | [Araç Geliştirme](./06-Tools/README.md) | Veritabanı sorgu araçları ve şema inceleme araçları oluşturma | [İnşa Et](./06-Tools/README.md) |
| **Lab 7-9: Gelişmiş Özellikler** | | | |
| 07 | [Anlamsal Arama Entegrasyonu](./07-Semantic-Search/README.md) | Azure OpenAI ve pgvector ile vektör gömme uygulaması | [Geliştir](./07-Semantic-Search/README.md) |
| 08 | [Test ve Hata Ayıklama](./08-Testing/README.md) | Test stratejileri, hata ayıklama araçları ve doğrulama yaklaşımları | [Test Et](./08-Testing/README.md) |
| 09 | [VS Code Entegrasyonu](./09-VS-Code/README.md) | VS Code MCP entegrasyonu ve AI Chat kullanımı yapılandırma | [Entegre Et](./09-VS-Code/README.md) |
| **Lab 10-12: Üretim ve En İyi Uygulamalar** | | | |
| 10 | [Dağıtım Stratejileri](./10-Deployment/README.md) | Docker dağıtımı, Azure Container Apps ve ölçeklendirme dikkate alınması gerekenler | [Dağıt](./10-Deployment/README.md) |
| 11 | [İzleme ve Gözlemlenebilirlik](./11-Monitoring/README.md) | Application Insights, günlük kaydı, performans izleme | [İzle](./11-Monitoring/README.md) |
| 12 | [En İyi Uygulamalar ve Optimizasyon](./12-Best-Practices/README.md) | Performans optimizasyonu, güvenlik güçlendirme ve üretim ipuçları | [Optimize Et](./12-Best-Practices/README.md) |

### 💻 Neler İnşa Edeceksiniz?

Bu öğrenme yolunun sonunda, aşağıdaki özelliklere sahip tam bir **Zava Perakende Analitiği MCP Sunucusu** oluşturmuş olacaksınız:

- **Çok tablolalı perakende veritabanı**: müşteri siparişleri, ürünler ve envanter
- **Satır Düzeyinde Güvenlik**: mağaza bazlı veri izolasyonu
- **Anlamsal ürün arama**: Azure OpenAI gömmeleri kullanarak
- **VS Code AI Chat entegrasyonu**: doğal dil sorguları için
- **Üretime hazır dağıtım**: Docker ve Azure ile
- **Kapsamlı izleme**: Application Insights ile

## 🎯 Öğrenme İçin Ön Koşullar

Bu öğrenme yolundan en iyi şekilde faydalanmak için aşağıdaki bilgilere sahip olmalısınız:

- **Programlama Deneyimi**: Python (tercih edilen) veya benzer dillerde temel bilgi
- **Veritabanı Bilgisi**: SQL ve ilişkisel veritabanları hakkında temel bilgi
- **API Kavramları**: REST API'ler ve HTTP kavramlarını anlama
- **Geliştirme Araçları**: Komut satırı, Git ve kod editörleri ile deneyim
- **Bulut Temelleri**: (Opsiyonel) Azure veya benzer bulut platformları hakkında temel bilgi
- **Docker Bilgisi**: (Opsiyonel) Konteynerleştirme kavramlarını anlama

### Gerekli Araçlar

- **Docker Desktop** - PostgreSQL ve MCP sunucusunu çalıştırmak için
- **Azure CLI** - Bulut kaynaklarını dağıtmak için
- **VS Code** - Geliştirme ve MCP entegrasyonu için
- **Git** - Versiyon kontrolü için
- **Python 3.8+** - MCP sunucusu geliştirme için

## 📚 Çalışma Kılavuzu ve Kaynaklar

Bu öğrenme yolu, etkili bir şekilde gezinmenize yardımcı olacak kapsamlı kaynaklar içerir:

### Çalışma Kılavuzu

Her laboratuvar şunları içerir:
- **Açık öğrenme hedefleri** - Neler başaracağınızı öğrenin
- **Adım adım talimatlar** - Ayrıntılı uygulama kılavuzları
- **Kod örnekleri** - Açıklamalı çalışan örnekler
- **Alıştırmalar** - Uygulamalı pratik fırsatları
- **Sorun giderme kılavuzları** - Yaygın sorunlar ve çözümleri
- **Ek kaynaklar** - Daha fazla okuma ve keşif

### Ön Koşul Kontrolü

Her laboratuvara başlamadan önce şunları bulacaksınız:
- **Gerekli bilgiler** - Önceden bilmeniz gerekenler
- **Kurulum doğrulama** - Ortamınızı nasıl doğrulayacağınız
- **Zaman tahminleri** - Tamamlama için beklenen süre
- **Öğrenme çıktıları** - Tamamladıktan sonra neler öğreneceğiniz

### Önerilen Öğrenme Yolları

Deneyim seviyenize göre yolunuzu seçin:

#### 🟢 **Başlangıç Yolu** (MCP'ye Yeni Başlayanlar)
1. Öncelikle [MCP for Beginners](https://aka.ms/mcp-for-beginners) 0-10'u tamamlayın
2. Temelleri pekiştirmek için 00-03 laboratuvarlarını tamamlayın
3. 04-06 laboratuvarlarını uygulamalı olarak takip edin
4. 07-09 laboratuvarlarını pratik kullanım için deneyin

#### 🟡 **Orta Seviye Yolu** (Biraz MCP Deneyimi)
1. Veritabanı ile ilgili kavramlar için 00-01 laboratuvarlarını gözden geçirin
2. Uygulama için 02-06 laboratuvarlarına odaklanın
3. Gelişmiş özellikler için 07-12 laboratuvarlarına derinlemesine dalın

#### 🔴 **İleri Seviye Yolu** (MCP'de Deneyimli)
1. Bağlam için 00-03 laboratuvarlarını hızlıca gözden geçirin
2. Veritabanı entegrasyonu için 04-09 laboratuvarlarına odaklanın
3. Üretim dağıtımı için 10-12 laboratuvarlarına yoğunlaşın

## 🛠️ Bu Öğrenme Yolunu Etkili Kullanma

### Sıralı Öğrenme (Önerilen)

Kapsamlı bir anlayış için laboratuvarları sırayla çalışın:

1. **Genel bakışı okuyun** - Neler öğreneceğinizi anlayın
2. **Ön koşulları kontrol edin** - Gerekli bilgilere sahip olduğunuzdan emin olun
3. **Adım adım kılavuzları takip edin** - Öğrenirken uygulayın
4. **Alıştırmaları tamamlayın** - Anlamanızı pekiştirin
5. **Ana noktaları gözden geçirin** - Öğrenme çıktılarınızı sağlamlaştırın

### Hedefe Yönelik Öğrenme

Belirli becerilere ihtiyacınız varsa:

- **Veritabanı Entegrasyonu**: 04-06 laboratuvarlarına odaklanın
- **Güvenlik Uygulaması**: 02, 08, 12 laboratuvarlarına yoğunlaşın
- **AI/Anlamsal Arama**: 07 laboratuvarına derinlemesine dalın
- **Üretim Dağıtımı**: 10-12 laboratuvarlarını inceleyin

### Uygulamalı Pratik

Her laboratuvar şunları içerir:
- **Çalışan kod örnekleri** - Kopyalayın, değiştirin ve deneyin
- **Gerçek dünya senaryoları** - Pratik perakende analitiği kullanım senaryoları
- **Aşamalı karmaşıklık** - Basitten karmaşığa doğru inşa etme
- **Doğrulama adımları** - Uygulamanızın çalıştığını doğrulayın

## 🌟 Topluluk ve Destek

### Yardım Alın

- **Azure AI Discord**: [Uzman desteği için katılın](https://discord.com/invite/ByRwuEEgH4)
- **GitHub Deposu ve Uygulama Örneği**: [Dağıtım Örneği ve Kaynaklar](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP Topluluğu**: [Daha geniş MCP tartışmalarına katılın](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Başlamaya Hazır mısınız?

**[Lab 00: MCP Veritabanı Entegrasyonuna Giriş](./00-Introduction/README.md)** ile yolculuğunuza başlayın.

---

*Bu kapsamlı, uygulamalı öğrenme deneyimi ile veritabanı entegrasyonu içeren üretime hazır MCP sunucuları oluşturmayı öğrenin.*

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.