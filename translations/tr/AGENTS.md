# AGENTS.md

## Proje Genel Bakış

**Yeni Başlayanlar için MCP**, Model Context Protocol (MCP) - AI modelleri ile istemci uygulamalar arasındaki etkileşimler için standart bir çerçeve olan MCP'yi öğrenmek için açık kaynaklı bir eğitim müfredatıdır. Bu depo, birden çok programlama dilinde pratik kod örnekleriyle kapsamlı öğrenme malzemeleri sunar.

### Temel Teknolojiler

- **Programlama Dilleri**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Çerçeveler ve SDK'lar**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Veritabanları**: pgvector eklentili PostgreSQL
- **Bulut Platformları**: Azure (Container Apps, OpenAI, İçerik Güvenliği, Application Insights)
- **Yapı Araçları**: npm, Maven, pip, Cargo
- **Dokümantasyon**: Otomatik çok dilli çeviri ile Markdown (48+ dil)

### Mimari

- **11 Temel Modül (00-11)**: Temel konulardan ileri seviyelere sıralı öğrenme yolu
- **Uygulamalı Laboratuvarlar**: Birden çok dilde tam çözüm kodlu pratik egzersizler
- **Örnek Projeler**: Çalışan MCP sunucu ve istemci uygulamaları
- **Çeviri Sistemi**: Çok dil desteği için otomatik GitHub Actions iş akışı
- **Görsel Varlıklar**: Çevrilmiş sürümleri ile merkezi resim dizini

## Kurulum Komutları

Bu, belge odaklı bir depodur. Çoğu kurulum bireysel örnek projeler ve laboratuvarlar içinde gerçekleşir.

### Depo Kurulumu

```bash
# Depoyu klonla
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Örnek Projelerle Çalışma

Örnek projeler aşağıdaki konumlardadır:
- `03-GettingStarted/samples/` - Dil spesifik örnekler
- `03-GettingStarted/01-first-server/solution/` - İlk sunucu uygulamaları
- `03-GettingStarted/02-client/solution/` - İstemci uygulamaları
- `11-MCPServerHandsOnLabs/` - Kapsamlı veritabanı entegrasyon laboratuvarları

Her örnek projenin kendi kurulum talimatları vardır:

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
# veya
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

### MCP 7-28 Hazırlığı

#### Depo hazırlık kontrol listesi

- [x] **Yeni katılımcılar için netlik**: Bu dosya depo amacını,
  yapısını, katkı kurallarını ve örnek kurulum yollarını tanımlar.
- [x] **Tam bayraklar ile build/test/lint komutları**:
  - Depo dokümantasyonu lint:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Depo doküman link kalıbı denetimi:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript örnek doğrulaması:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python örnek doğrulaması:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java örnek doğrulaması:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **MCP aracı olabilecek gerçekçi bir iş akışı**:
  `validate_curriculum_change`
- [x] **Girdi/çıktılar açıkça belirtilmiş** (aşağıdaki spesifikasyona bakınız).
- [x] **İzinler ve hata modları belgelenmiş** (aşağıdaki spesifikasyona bakınız).
- [x] **CI test edilebilirliği açık** (deterministik komutlar, açık
  çıkış kodları ve makine tarafından okunabilir çıktılar).

#### Aday MCP araç iş akışı: `validate_curriculum_change`

##### Amaç

Müfredat dokümantasyonu değişikliklerinin ve temsilci örnek kodların
birleşim öncesi sağlığını doğrulamak.

##### Girdiler

- `changed_paths: string[]` (zorunlu) - PR'de değişen göreli yollar.
- `run_docs_lint: boolean` (varsayılan `true`)
- `run_links_audit: boolean` (varsayılan `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (varsayılan tümü `false`)

##### Çıktılar

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### İzinler

- Sadece çalışma alanı dosyalarını okuyup araç tarafından oluşturulan çıktı dosyalarını yazmak (örneğin lint
  raporları, test logları); `translations/` veya
  `translated_images/` dizinlerine yazma yok.
- Yerel shell komutlarını çalıştırmak.
- Paket geri yükleme için isteğe bağlı ağ erişimi (`npm ci`,
  `python -m pip install`, `mvn` bağımlılık çözme).
- `translations/` veya
  `translated_images/` dizinlerini itme, birleştirme veya değiştirme izni yok.

##### Hata modları

- `E_NO_INPUT_PATHS`: `changed_paths` boş.
- `E_INVALID_PATH`: giriş yolu depo kökünün dışına çıkıyor.
- `E_LINT_FAILED`: markdown lint sıfır olmayan çıkış verdi.
- `E_LINK_AUDIT_FAILED`: link denetimi komutu sıfır olmayan çıkış verdi.
- `E_SAMPLE_TEST_FAILED`: örnek test/derleme sıfır olmayan çıkış verdi.
- `E_TIMEOUT`: komut ayarlanmış zaman aşımını aştı.

##### Önerilen CI sözleşmesi

Doğrulamayı otomatikleştirmek için, şu ayarlarda bir CI işi yapılandırın:

- `*.md`, örnek kod veya bu dosyayı etkileyen pull requestlerde tetiklenir.
- Yukarıda listelenen tam komutları çalıştırır.
- Logları çıktı olarak saklar.
- Herhangi bir sıfır olmayan çıkış kodunda işi başarısız kılar.

#### Bu repodan bir MCP sunucusu yayımlarsanız

- [ ] MCP 7-28 taslak değişiklik günlüğünü okuyun:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Sunucunuzu SDK beta sürümlerine karşı çalıştırın:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Oturum ve el sıkışma varsayımlarını kaldırın; her isteği
  kendi başına bağımsız ele alın:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Ham HTTP istekleri için `Mcp-Method` ve `Mcp-Name` başlıklarını gönderin:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Sert kodlanmış hata kodlarını denetleyin (`missing resource` `-32002` 'den `-32602`'ye taşındı).
- [ ] Kullanımdan kaldırılan kökler, örnekleme ve
  kayıt için bayrak işaretleyin ve göç planlayın:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Deneysel `2025-11-25` Görevler (Tasks) API'sinden geçiş yapın:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] OAuth ve OpenID Connect sertleştirmesi için yetkilendirmeyi gözden geçirin:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Dokümantasyon Yapısı

- **Modüller 00-11**: Sıralı sırayla temel müfredat içeriği
- **translations/**: Dil spesifik sürümler (otomatik oluşturuluyor, doğrudan düzenlemeyin)
- **translated_images/**: Yerelleştirilmiş resim sürümleri (otomatik oluşturuluyor)
- **images/**: Kaynak resimler ve diyagramlar

### Dokümantasyon Değişiklikleri Yapma

1. Sadece kök modül dizinlerindeki (00-11) İngilizce markdown dosyalarını düzenleyin
2. Gerekirse `images/` dizinindeki resimleri güncelleyin
3. co-op-translator GitHub Action otomatik olarak çeviriler oluşturacaktır
4. Ana dala push edildiğinde çeviriler yeniden oluşturulur

### Çevirilerle Çalışma

- **Otomatik Çeviri**: GitHub Actions iş akışı tüm çevirileri yönetir
- `translations/` dizinindeki dosyaları elle düzenlemeyin
- Çeviri meta verileri her çevrilmiş dosyada gömülüdür
- Desteklenen diller: Arapça, Çince, Fransızca, Almanca, Hintçe, Japonca, Korece, Portekizce, Rusça, İspanyolca ve daha fazlası dahil 48+ dil

## Test Talimatları

### Dokümantasyon Doğrulaması

Bu öncelikle bir dokümantasyon deposu olduğundan, testler şunlara odaklanır:

1. **Link Desen Denetimi**: İnceleme için Markdown linklerini listele

   ```bash
   # Markdown bağlantılarını listele (desen denetimi)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Kod Örneği Doğrulaması**: Kod örneklerinin derlenip çalıştığını test et

   ```bash
   # Belirli örneğe gidin ve testlerini çalıştırın
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown Linting**: Format tutarlılığını kontrol et

   ```bash
   # Gerekirse markdownlint kullanın
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Örnek Proje Testi

Her dil spesifik örnek kendine özgü test yaklaşımına sahiptir:

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

## Kod Stili Rehberi

### Dokümantasyon Stili

- Açık, yeni başlayan dostu dil kullanın
- Uygun yerlerde çoklu dillerde kod örnekleri ekleyin
- Markdown en iyi uygulamalarına uyun:
  - ATX stil başlıklar (`#` sözdizimi) kullanın
  - Dil tanımlayıcıları ile çitli kod blokları kullanın
  - Görseller için açıklayıcı alt metin ekleyin
  - Satır uzunluklarını makul tutun (sabit sınır yok, ama makul olun)

### Kod Örneği Stili

#### TypeScript/JavaScript
- ES modülleri (`import`/`export`) kullanın
- TypeScript sıkı mod kurallarına uyun
- Tür açıklamaları ekleyin
- Hedef ES2022

#### Python
- PEP 8 stil yönergelerine uyun
- Uygun yerlerde tip ipuçları kullanın
- Fonksiyon ve sınıflar için docstring ekleyin
- Modern Python özellikleri kullanın (3.8+)

#### Java
- Spring Boot yönergelerine uyun
- Java 21 özellikleri kullanın
- Standart Maven proje yapısına uyun
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

## Derleme ve Dağıtım

### Dokümantasyon Dağıtımı

Depo, dokümantasyon barındırmak için GitHub Pages veya benzer bir yapı kullanır (uygunsa). Ana dalda yapılan değişiklikler şunları tetikler:

1. Çeviri iş akışı (`.github/workflows/co-op-translator.yml`)
2. Tüm İngilizce markdown dosyalarının otomatik çevirisi
3. Gerekirse görsel yerelleştirmesi

### Derleme Süreci Gerekmez

Bu depo öncelikle markdown dokümantasyonu içerir. Temel müfredat içeriği için derleme veya build adımı gerektirmez.

### Örnek Proje Dağıtımı

Bireysel örnek projelerin dağıtım talimatları olabilir:
- MCP sunucu dağıtımı için `03-GettingStarted/09-deployment/` dizinine bakın
- Azure Container Apps dağıtım örnekleri `11-MCPServerHandsOnLabs/` içinde

## Katkı Rehberi

### Pull Request Süreci

1. **Fork ve Klonlama**: Depoyu çatallayın ve yerel olarak kopyalayın
2. **Bir Dal Oluşturma**: Anlamlı dal adları kullanın (ör. `fix/typo-module-3`, `add/python-example`)
3. **Değişiklik Yapma**: Sadece İngilizce markdown dosyalarını düzenleyin (çeviriler değil)
4. **Yerel Test**: Markdown'ın doğru render edildiğini doğrulayın
5. **PR Gönderme**: Net PR başlıkları ve açıklamaları kullanın
6. **CLA**: İstendiğinde Microsoft Katılımcı Lisans Anlaşmasını imzalayın

### PR Başlık Formatı

Açık ve açıklayıcı başlıklar kullanın:
- Modül spesifik değişiklikler için `[Module XX] Kısa açıklama`
- Örnek kod değişiklikleri için `[Samples] Açıklama`
- Genel dokümantasyon güncellemeleri için `[Docs] Açıklama`

### Ne Katkıda Bulunmalı

- Dokümantasyon veya kod örneklerindeki hata düzeltmeleri
- Ek dillerde yeni kod örnekleri
- Mevcut içeriği açıklama ve iyileştirmeler
- Yeni vaka çalışmaları veya pratik örnekler
- Belirsiz veya yanlış içerik için sorun bildirimleri

### Ne Yapmamalı

- `translations/` dizinindeki dosyaları doğrudan düzenlemeyin
- `translated_images/` dizinini düzenlemeyin
- Büyük ikili dosyalar eklemeden önce tartışın
- Çeviri iş akışı dosyalarını koordinasyon olmadan değiştirmeyin

## Ek Notlar

### Depo Bakımı

- **Değişiklik Günlüğü**: Tüm önemli değişiklikler `changelog.md` içinde belgelenir
- **Çalışma Rehberi**: Müfredat navigasyonu için `study_guide.md` kullanın
- **Sorun Şablonları**: Hata raporları ve özellik talepleri için GitHub sorun şablonları kullanın
- **Davranış Kuralları**: Tüm katkıda bulunanlar Microsoft Açık Kaynak Davranış Kuralları'nı takip etmelidir

### Öğrenme Yolu

Optimal öğrenme için modülleri sıralı takip edin (00-11):
1. **00-02**: Temeller (Giriş, Temel Kavramlar, Güvenlik)
2. **03**: Uygulamalı başlangıç
3. **04-05**: Pratik uygulamalar ve ileri konular
4. **06-10**: Topluluk, en iyi uygulamalar ve gerçek dünya uygulamaları
5. **11**: Kapsamlı veritabanı entegrasyon laboratuvarları (13 sıralı laboratuvar)

### Destek Kaynakları

- **Dokümantasyon**: https://modelcontextprotocol.io/
- **Spesifikasyon**: https://spec.modelcontextprotocol.io/
- **Topluluk**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord sunucusu
- **İlgili Kurslar**: Diğer Microsoft öğrenme yolları için README.md'ye bakın

### Ortak Sorun Giderme

**S: PR'im çeviri denetiminde hata veriyor**
C: Sadece kök modül dizinlerindeki İngilizce markdown dosyalarını düzenlediğinizden emin olun, çevrilmiş sürümler değil.

**S: Yeni bir dil nasıl eklerim?**
C: Dil desteği co-op-translator iş akışıyla yönetilir. Yeni dillerin eklenmesini tartışmak için bir sorun açın.

**S: Kod örnekleri çalışmıyor**

C: Belirli örneğin README dosyasındaki kurulum talimatlarını takip ettiğinizden emin olun. Doğru bağımlılık sürümlerinin yüklü olduğunu kontrol edin.

**S: Resimler görüntülenmiyor**
C: Resim yollarının göreli ve ileri eğik çizgi kullanılarak yazıldığını doğrulayın. Resimler `images/` dizininde veya yerelleştirilmiş sürümler için `translated_images/` dizininde olmalıdır.

### Performans Dikkate Alınması Gerekenler

- Çeviri iş akışı tamamlanması birkaç dakika sürebilir
- Büyük resimler commit yapmadan önce optimize edilmelidir
- Bireysel markdown dosyaları odaklı ve makul boyutta olmalıdır
- Daha iyi taşınabilirlik için göreli bağlantılar kullanın

### Proje Yönetimi

Bu proje Microsoft açık kaynak uygulamalarını takip eder:
- Kod ve dokümantasyon için MIT Lisansı
- Microsoft Açık Kaynak Davranış Kuralları
- Katkılar için CLA gereklidir
- Güvenlik sorunları: SECURITY.md yönergelerini takip edin
- Destek: Yardım kaynakları için SUPPORT.md dosyasına bakın

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->