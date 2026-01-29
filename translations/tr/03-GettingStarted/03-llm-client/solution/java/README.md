# Calculator LLM Client

LangChain4j kullanarak MCP (Model Context Protocol) hesap makinesi servisine GitHub Models entegrasyonu ile nasıl bağlanılacağını gösteren bir Java uygulaması.

## Gereksinimler

- Java 21 veya üzeri
- Maven 3.6+ (veya dahil edilen Maven wrapper'ı kullanabilirsiniz)
- GitHub Models erişimi olan bir GitHub hesabı
- `http://localhost:8080` adresinde çalışan bir MCP hesap makinesi servisi

## GitHub Token'ını Alma

Bu uygulama GitHub Models kullanır ve bu da bir GitHub kişisel erişim tokenı gerektirir. Tokenınızı almak için şu adımları izleyin:

### 1. GitHub Models'a Erişim
1. [GitHub Models](https://github.com/marketplace/models) sayfasına gidin
2. GitHub hesabınızla giriş yapın
3. Henüz erişiminiz yoksa GitHub Models için erişim talep edin

### 2. Kişisel Erişim Tokenı Oluşturma
1. [GitHub Ayarları → Geliştirici ayarları → Kişisel erişim tokenları → Tokenlar (klasik)](https://github.com/settings/tokens) sayfasına gidin
2. "Generate new token" → "Generate new token (classic)" seçeneğine tıklayın
3. Tokenınıza açıklayıcı bir isim verin (örneğin, "MCP Calculator Client")
4. Gerekirse süresini ayarlayın
5. Aşağıdaki izinleri seçin:
   - `repo` (özel depolara erişim için)
   - `user:email`
6. "Generate token" butonuna tıklayın
7. **Önemli**: Tokenı hemen kopyalayın - bir daha göremeyeceksiniz!

### 3. Ortam Değişkenini Ayarlama

#### Windows (Komut İstemi) için:
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windows (PowerShell) için:
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linux için:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Kurulum ve Yükleme

1. **Projeyi klonlayın veya proje dizinine gidin**

2. **Bağımlılıkları yükleyin**:
   ```cmd
   mvnw clean install
   ```
   Ya da Maven global olarak yüklüyse:
   ```cmd
   mvn clean install
   ```

3. **Ortam değişkenini ayarlayın** (yukarıdaki "GitHub Token'ını Alma" bölümüne bakın)

4. **MCP Calculator Servisini Başlatın**:
   1. bölümdeki MCP hesap makinesi servisini `http://localhost:8080/sse` adresinde çalıştırdığınızdan emin olun. İstemciyi başlatmadan önce servis çalışıyor olmalı.

## Uygulamayı Çalıştırma

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Uygulamanın Yaptıkları

Uygulama hesap makinesi servisi ile üç temel etkileşimi gösterir:

1. **Toplama**: 24.5 ile 17.3'ün toplamını hesaplar
2. **Karekök**: 144'ün karekökünü hesaplar
3. **Yardım**: Kullanılabilir hesap makinesi fonksiyonlarını gösterir

## Beklenen Çıktı

Başarıyla çalıştığında aşağıdakine benzer bir çıktı görmelisiniz:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Sorun Giderme

### Yaygın Sorunlar

1. **"GITHUB_TOKEN ortam değişkeni ayarlanmadı"**
   - `GITHUB_TOKEN` ortam değişkenini ayarladığınızdan emin olun
   - Değişkeni ayarladıktan sonra terminal/komut istemcisini yeniden başlatın

2. **"localhost:8080 bağlantısı reddedildi"**
   - MCP hesap makinesi servisinin 8080 portunda çalıştığından emin olun
   - Başka bir servisin 8080 portunu kullanmadığını kontrol edin

3. **"Kimlik doğrulama başarısız"**
   - GitHub tokenınızın geçerli ve doğru izinlere sahip olduğunu doğrulayın
   - GitHub Models erişiminizin olduğundan emin olun

4. **Maven derleme hataları**
   - Java 21 veya üzeri kullandığınızdan emin olun: `java -version`
   - Derlemeyi temizlemeyi deneyin: `mvnw clean`

### Hata Ayıklama

Hata ayıklama kayıtlarını etkinleştirmek için uygulamayı çalıştırırken aşağıdaki JVM argümanını ekleyin:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigürasyon

Uygulama şu şekilde yapılandırılmıştır:
- GitHub Models ile `gpt-4.1-nano` modelini kullanır
- MCP servisine `http://localhost:8080/sse` adresinden bağlanır
- İstekler için 60 saniyelik zaman aşımı uygular
- Hata ayıklama için istek/yanıt kayıtlarını etkinleştirir

## Bağımlılıklar

Bu projede kullanılan temel bağımlılıklar:
- **LangChain4j**: AI entegrasyonu ve araç yönetimi için
- **LangChain4j MCP**: Model Context Protocol desteği için
- **LangChain4j GitHub Models**: GitHub Models entegrasyonu için
- **Spring Boot**: Uygulama çatısı ve bağımlılık yönetimi için

## Lisans

Bu proje Apache License 2.0 altında lisanslanmıştır - detaylar için [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) dosyasına bakınız.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.