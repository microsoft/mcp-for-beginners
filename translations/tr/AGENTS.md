# AGENTS.md

## Proje Genel Bakış

**MCP for Beginners**, Model Context Protocol (MCP) öğrenimi için açık kaynaklı bir eğitim müfredatıdır. MCP, yapay zeka modelleri ile istemci uygulamaları arasındaki etkileşimler için standartlaştırılmış bir çerçevedir. Bu depo, birden fazla programlama dilinde uygulamalı kod örnekleriyle kapsamlı öğrenim materyalleri sunar.

### Temel Teknolojiler

- **Programlama Dilleri**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Çerçeveler ve SDK'lar**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Veritabanları**: pgvector uzantısı ile PostgreSQL
- **Bulut Platformları**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Yapı Araçları**: npm, Maven, pip, Cargo
- **Dokümantasyon**: Otomatik çok dilli çeviri ile Markdown (48+ dil)

### Mimari

- **11 Temel Modül (00-11)**: Temellerden ileri konulara kadar sıralı öğrenim yolu
- **Uygulamalı Laboratuvarlar**: Birden fazla dilde tam çözüm kodlarıyla pratik egzersizler
- **Örnek Projeler**: Çalışan MCP sunucu ve istemci uygulamaları
- **Çeviri Sistemi**: Çok dilli destek için otomatik GitHub Actions iş akışı
- **Görsel Varlıklar**: Çevrilmiş versiyonlarıyla merkezi görseller dizini

## Kurulum Komutları

Bu, dokümantasyon odaklı bir depodur. Çoğu kurulum, bireysel örnek projeler ve laboratuvarlar içinde gerçekleşir.

### Depo Kurulumu

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Örnek Projelerle Çalışma

Örnek projeler şu konumlarda bulunur:
- `03-GettingStarted/samples/` - Dile özgü örnekler
- `03-GettingStarted/01-first-server/solution/` - İlk sunucu uygulamaları
- `03-GettingStarted/02-client/solution/` - İstemci uygulamaları
- `11-MCPServerHandsOnLabs/` - Kapsamlı veritabanı entegrasyonu laboratuvarları

Her örnek proje kendi kurulum talimatlarını içerir:

#### TypeScript/JavaScript Projeleri
```bash
cd <project-directory>
npm install
npm start
```

#### Python Projeleri
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Java Projeleri
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Geliştirme İş Akışı

### Dokümantasyon Yapısı

- **Modüller 00-11**: Sıralı düzen içinde temel müfredat içeriği
- **translations/**: Dile özgü versiyonlar (otomatik oluşturulur, doğrudan düzenlemeyin)
- **translated_images/**: Yerelleştirilmiş görsel versiyonlar (otomatik oluşturulur)
- **images/**: Kaynak görseller ve diyagramlar

### Dokümantasyon Değişiklikleri Yapma

1. Yalnızca kök modül dizinlerindeki İngilizce markdown dosyalarını düzenleyin (00-11)
2. Gerekirse `images/` dizinindeki görselleri güncelleyin
3. co-op-translator GitHub Action otomatik olarak çevirileri oluşturacaktır
4. Çeviriler ana dalına yapılan push ile yeniden oluşturulur

### Çevirilerle Çalışma

- **Otomatik Çeviri**: GitHub Actions iş akışı tüm çevirileri yönetir
- `translations/` dizinindeki dosyaları MANUEL olarak düzenlemeyin
- Çeviri meta verileri her çevrilmiş dosyada gömülüdür
- Desteklenen diller: Arapça, Çince, Fransızca, Almanca, Hintçe, Japonca, Korece, Portekizce, Rusça, İspanyolca ve daha fazlası dahil 48+ dil

## Test Talimatları

### Dokümantasyon Doğrulama

Bu öncelikle bir dokümantasyon deposu olduğundan, testler şu konulara odaklanır:

1. **Bağlantı Doğrulama**: Tüm dahili bağlantıların çalıştığından emin olun
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Kod Örneği Doğrulama**: Kod örneklerinin derlenip çalıştığını test edin
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown Denetimi**: Biçimlendirme tutarlılığını kontrol edin
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Örnek Proje Testi

Her dile özgü örnek kendi test yaklaşımını içerir:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## Kod Stili Yönergeleri

### Dokümantasyon Stili

- Açık, başlangıç seviyesine uygun bir dil kullanın
- Uygun olduğunda birden fazla dilde kod örnekleri ekleyin
- Markdown en iyi uygulamalarını takip edin:
  - ATX tarzı başlıklar kullanın (`#` sözdizimi)
  - Dil tanımlayıcılarıyla çitlenmiş kod blokları kullanın
  - Görseller için açıklayıcı alt metin ekleyin
  - Satır uzunluklarını makul tutun (kesin bir sınır yok, ancak mantıklı olun)

### Kod Örneği Stili

#### TypeScript/JavaScript
- ES modüllerini kullanın (`import`/`export`)
- TypeScript sıkı mod kurallarını takip edin
- Tür açıklamaları ekleyin
- ES2022 hedefleyin

#### Python
- PEP 8 stil yönergelerini takip edin
- Uygun olduğunda tür ipuçları kullanın
- Fonksiyonlar ve sınıflar için docstring ekleyin
- Modern Python özelliklerini kullanın (3.8+)

#### Java
- Spring Boot kurallarını takip edin
- Java 21 özelliklerini kullanın
- Standart Maven proje yapısını takip edin
- Javadoc yorumları ekleyin

### Dosya Organizasyonu

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## Yapı ve Dağıtım

### Dokümantasyon Dağıtımı

Depo, GitHub Pages veya benzeri bir platform kullanarak dokümantasyon barındırır (uygulanabilir ise). Ana dalına yapılan değişiklikler şu işlemleri tetikler:

1. Çeviri iş akışı (`.github/workflows/co-op-translator.yml`)
2. Tüm İngilizce markdown dosyalarının otomatik çevirisi
3. Gerekirse görsel yerelleştirme

### Yapı Süreci Gerekmez

Bu depo öncelikle markdown dokümantasyonu içerir. Temel müfredat içeriği için derleme veya yapı adımı gerekmez.

### Örnek Proje Dağıtımı

Bireysel örnek projeler kendi dağıtım talimatlarını içerebilir:
- MCP sunucu dağıtım rehberi için `03-GettingStarted/09-deployment/` bölümüne bakın
- Azure Container Apps dağıtım örnekleri `11-MCPServerHandsOnLabs/` bölümünde

## Katkı Yönergeleri

### Pull Request Süreci

1. **Fork ve Klonlama**: Depoyu fork edin ve fork'unuzu yerel olarak klonlayın
2. **Bir Dal Oluşturun**: Açıklayıcı dal adları kullanın (ör. `fix/typo-module-3`, `add/python-example`)
3. **Değişiklik Yapın**: Yalnızca İngilizce markdown dosyalarını düzenleyin (çevirileri değil)
4. **Yerel Test Yapın**: Markdown'ın doğru şekilde görüntülendiğini doğrulayın
5. **PR Gönderin**: Açık PR başlıkları ve açıklamaları kullanın
6. **CLA**: Microsoft Katkı Lisans Sözleşmesini imzalayın

### PR Başlık Formatı

Açık, açıklayıcı başlıklar kullanın:
- `[Module XX] Kısa açıklama` modül spesifik değişiklikler için
- `[Samples] Açıklama` örnek kod değişiklikleri için
- `[Docs] Açıklama` genel dokümantasyon güncellemeleri için

### Katkı Sağlanabilecekler

- Dokümantasyon veya kod örneklerindeki hataların düzeltilmesi
- Ek dillerde yeni kod örnekleri
- Mevcut içeriğin açıklığının artırılması ve iyileştirilmesi
- Yeni vaka çalışmaları veya pratik örnekler
- Belirsiz veya yanlış içerik için sorun raporları

### Yapılmaması Gerekenler

- `translations/` dizinindeki dosyaları doğrudan düzenlemeyin
- `translated_images/` dizinini düzenlemeyin
- Büyük ikili dosyalar eklemeden önce tartışma yapın
- Çeviri iş akışı dosyalarını koordinasyon olmadan değiştirmeyin

## Ek Notlar

### Depo Bakımı

- **Değişiklik Günlüğü**: Tüm önemli değişiklikler `changelog.md` dosyasında belgelenir
- **Çalışma Kılavuzu**: Müfredat navigasyon genel görünümü için `study_guide.md` dosyasını kullanın
- **Sorun Şablonları**: Hata raporları ve özellik istekleri için GitHub sorun şablonlarını kullanın
- **Davranış Kuralları**: Tüm katkı sağlayıcılar Microsoft Açık Kaynak Davranış Kurallarına uymalıdır

### Öğrenim Yolu

Optimal öğrenim için modülleri sıralı olarak takip edin (00-11):
1. **00-02**: Temeller (Giriş, Temel Kavramlar, Güvenlik)
2. **03**: Uygulamalı uygulama ile başlangıç
3. **04-05**: Pratik uygulama ve ileri konular
4. **06-10**: Topluluk, en iyi uygulamalar ve gerçek dünya uygulamaları
5. **11**: Kapsamlı veritabanı entegrasyonu laboratuvarları (13 sıralı laboratuvar)

### Destek Kaynakları

- **Dokümantasyon**: https://modelcontextprotocol.io/
- **Spesifikasyon**: https://spec.modelcontextprotocol.io/
- **Topluluk**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord sunucusu
- **İlgili Kurslar**: Diğer Microsoft öğrenim yolları için README.md dosyasına bakın

### Yaygın Sorun Giderme

**S: PR'ım çeviri kontrolünden geçemiyor**
C: Yalnızca kök modül dizinlerindeki İngilizce markdown dosyalarını düzenlediğinizden emin olun, çevrilmiş versiyonları değil.

**S: Yeni bir dil nasıl eklenir?**
C: Dil desteği co-op-translator iş akışı ile yönetilir. Yeni diller eklemek için bir sorun açarak tartışma başlatın.

**S: Kod örnekleri çalışmıyor**
C: Belirli örneğin README'sindeki kurulum talimatlarını takip ettiğinizden emin olun. Doğru bağımlılık sürümlerinin yüklü olduğundan emin olun.

**S: Görseller görüntülenmiyor**
C: Görsel yollarının göreceli olduğundan ve ileri eğik çizgiler kullandığından emin olun. Görseller `images/` dizininde veya yerelleştirilmiş versiyonlar için `translated_images/` dizininde olmalıdır.

### Performans Dikkatleri

- Çeviri iş akışı tamamlanması birkaç dakika sürebilir
- Büyük görseller commit edilmeden önce optimize edilmelidir
- Bireysel markdown dosyalarını odaklı ve makul boyutta tutun
- Daha iyi taşınabilirlik için göreceli bağlantılar kullanın

### Proje Yönetimi

Bu proje Microsoft açık kaynak uygulamalarını takip eder:
- Kod ve dokümantasyon için MIT Lisansı
- Microsoft Açık Kaynak Davranış Kuralları
- Katkılar için CLA gereklidir
- Güvenlik sorunları: SECURITY.md yönergelerini takip edin
- Destek: Yardım kaynakları için SUPPORT.md dosyasına bakın

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.