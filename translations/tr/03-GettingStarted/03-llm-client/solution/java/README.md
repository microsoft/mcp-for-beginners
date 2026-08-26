# Hesap Makinesi LLM İstemcisi

LangChain4j kullanarak MCP (Model Context Protocol) hesap makinesi servisine MiniMax OpenAI uyumlu API üzerinden nasıl bağlanılacağını gösteren bir Java uygulaması.

## Gereksinimler

- Java 21 veya üzeri
- Maven 3.6+ (veya dahil edilen Maven sarmalayıcısını kullanabilirsiniz)
- Bir MiniMax API anahtarı
- `http://localhost:8080` adresinde çalışan bir MCP hesap makinesi servisi

## API Anahtarının Alınması

Bu uygulama MiniMax OpenAI uyumlu API'sini kullanmaktadır. Anahtarınızı ve uç noktanızı almak için şu adımları izleyin:

### 1. Bir uç nokta seçin
1. Küresel uç nokta için `https://api.minimax.io/v1` adresini kullanın
2. Çin uç noktası için `https://api.minimaxi.com/v1` adresini kullanın

### 2. Bir API anahtarı oluşturun
1. MiniMax hesabınızdan bir MiniMax API anahtarı oluşturun
2. Anahtarı güvenli bir yerde saklayın

### 3. Ortam Değişkenlerini Ayarlayın

#### Windows'da (Komut İstemi):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows'da (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### macOS/Linux'ta:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
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

3. **Ortam değişkenlerini ayarlayın** (yukarıdaki "API Anahtarının Alınması" bölümüne bakın)

4. **MCP Hesap Makinesi Servisini başlatın**:
   MCP hesap makinesi servisini `http://localhost:8080/sse` adresinde, bölüm 1'deki gibi çalıştırdığınızdan emin olun. Bu, istemciyi başlatmadan önce çalışıyor olmalıdır.

## Uygulamayı Çalıştırma

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Uygulamanın Yaptıkları

Uygulama, hesap makinesi servisi ile üç ana etkileşimi gösterir:

1. **Toplama**: 24.5 ve 17.3 sayılarının toplamını hesaplar
2. **Karekök**: 144 sayısının karekökünü hesaplar
3. **Yardım**: Kullanılabilir hesap makinesi fonksiyonlarını gösterir

## Beklenen Çıktı

Başarıyla çalıştırıldığında, benzer bir çıktı görmelisiniz:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Sorun Giderme

### Yaygın Sorunlar

1. **"OPENAI_API_KEY ortam değişkeni ayarlı değil"**
   - `OPENAI_API_KEY` ortam değişkenini ayarladığınızdan emin olun
   - Değişkeni ayarladıktan sonra terminalinizi/komut istemcinizi yeniden başlatın

2. **"localhost:8080 bağlantısı reddedildi"**
   - MCP hesap makinesi servisinin 8080 portunda çalıştığından emin olun
   - 8080 portunu kullanan başka bir servisin olup olmadığını kontrol edin

3. **"Kimlik doğrulama başarısız"**
   - API anahtarınızın geçerli olduğunu doğrulayın
   - `OPENAI_BASE_URL` değişkeninin kullanmak istediğiniz uç nokta ile eşleştiğini kontrol edin

4. **Maven derleme hataları**
   - Java 21 veya üzeri kullandığınızdan emin olun: `java -version`
   - Derlemeyi temizlemeyi deneyin: `mvnw clean`

### Hata Ayıklama

Hata ayıklama günlüklerini etkinleştirmek için, çalıştırırken şu JVM argümanını ekleyin:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Yapılandırma

Uygulama şu şekilde yapılandırılmıştır:
- Varsayılan olarak MiniMax-M3 kullanır veya `MINIMAX_MODEL_ID` ayarlandığında MiniMax-M2.7 kullanır
- `OPENAI_BASE_URL` ayarlanmışsa ona bağlanır; aksi takdirde `MINIMAX_REGION=cn_zh` ise `https://api.minimaxi.com/v1`, yoksa varsayılan olarak `https://api.minimax.io/v1` kullanır
- MCP servisine `http://localhost:8080/sse` adresinden bağlanır
- İstekler için 60 saniyelik zaman aşımı kullanır

## Bağımlılıklar

Bu projede kullanılan temel bağımlılıklar:
- **LangChain4j**: Yapay Zeka entegrasyonu ve araç yönetimi için
- **LangChain4j MCP**: Model Context Protocol desteği için
- **LangChain4j OpenAI resmi**: MiniMax OpenAI uyumlu API entegrasyonu için
- **Spring Boot**: Uygulama çatısı ve bağımlılık enjeksiyonu için

## Lisans

Bu proje Apache Lisans 2.0 altında lisanslanmıştır - ayrıntılar için [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) dosyasına bakınız.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->