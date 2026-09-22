# Hesap Makinesi LLM İstemcisi

> [!NOTE]
> Bu çözüm, kursun eski HTTP+SSE hesap makinesi servisine bağlanır ve
> MCP `2025-11-25` SDK API'lerini hedefler. Bu bir `2026-07-28` Streamable HTTP
> örneği değildir.

LangChain4j kullanarak MiniMax OpenAI uyumlu API üzerinden bir MCP (Model Context Protocol) hesap makinesi servisine nasıl bağlanılacağını gösteren bir Java uygulaması.

## Gereksinimler

- Java 21 veya daha yüksek sürüm
- Maven 3.6+ (veya dahil edilen Maven wrapper'ı kullanın)
- Bir MiniMax API anahtarı
- `http://localhost:8080` adresinde çalışan bir MCP hesap makinesi servisi

## API Anahtarını Alma

Bu uygulama MiniMax OpenAI uyumlu API'yi kullanır. Anahtarınızı ve uç noktayı almak için şu adımları izleyin:

### 1. Bir uç nokta seçin
1. Küresel uç nokta için `https://api.minimax.io/v1` kullanın
2. Çin uç noktası için `https://api.minimaxi.com/v1` kullanın

### 2. Bir API anahtarı oluşturun
1. MiniMax hesabınızdan MiniMax API anahtarı oluşturun
2. Anahtarı güvende bir yerde saklayın

### 3. Ortam Değişkenlerini Ayarlayın

#### Windows'ta (Komut İstemi):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows'ta (PowerShell):
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
   Veya Maven global olarak yüklüyse:
   ```cmd
   mvn clean install
   ```

3. **Ortam değişkenlerini ayarlayın** (yukarıdaki "API Anahtarını Alma" bölümüne bakınız)

4. **MCP Hesap Makinesi Servisini Başlatın**:
   Bölüm 1'in MCP hesap makinesi servisinin `http://localhost:8080/sse` adresinde çalıştığından emin olun. Bu, istemciyi başlatmadan önce çalışıyor olmalıdır.

## Uygulamayı Çalıştırma

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Uygulamanın Yaptıkları

Uygulama, hesap makinesi servisi ile üç temel etkileşimi gösterir:

1. **Toplama**: 24.5 ile 17.3'ün toplamını hesaplar
2. **Karekök**: 144'ün karekökünü hesaplar
3. **Yardım**: Mevcut hesap makinesi fonksiyonlarını gösterir

## Beklenen Çıktı

Başarıyla çalıştığında, aşağıdakine benzer çıktı görmelisiniz:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Sorun Giderme

### Yaygın Sorunlar

1. **"OPENAI_API_KEY ortam değişkeni ayarlanmadı"**
   - `OPENAI_API_KEY` ortam değişkenini ayarladığınızdan emin olun
   - Değişkeni ayarladıktan sonra terminal/komut istemcisini yeniden başlatın

2. **"localhost:8080 bağlantısı reddedildi"**
   - MCP hesap makinesi servisinin 8080 portunda çalıştığından emin olun
   - Başka bir servisin 8080 portunu kullanıp kullanmadığını kontrol edin

3. **"Kimlik doğrulama başarısız"**
   - API anahtarınızın geçerli olduğunu doğrulayın
   - `OPENAI_BASE_URL` değerinin kullanmak istediğiniz uç noktayla eşleştiğinden emin olun

4. **Maven derleme hataları**
   - Java 21 veya daha yüksek sürüm kullandığınızdan emin olun: `java -version`
   - Derlemeyi temizlemeyi deneyin: `mvnw clean`

### Hata Ayıklama

Hata ayıklama kaydını etkinleştirmek için aşağıdaki JVM argümanını çalıştırırken ekleyin:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigürasyon

Uygulama şu şekilde yapılandırılmıştır:
- Varsayılan olarak MiniMax-M3 kullanır; `MINIMAX_MODEL_ID` ayarlanarak `MiniMax-M3` veya `MiniMax-M2.7` seçilebilir
- `OPENAI_BASE_URL` ayarlanmışsa ona bağlanır; aksi takdirde `MINIMAX_REGION=cn_zh` ise `https://api.minimaxi.com/v1`, yoksa varsayılan olarak `https://api.minimax.io/v1` kullanılır
- MCP servisine `http://localhost:8080/sse` adresinden bağlanır
- İstekler için 60 saniyelik zaman aşımı kullanır

## Bağımlılıklar

Bu projede kullanılan ana bağımlılıklar:
- **LangChain4j**: Yapay zeka entegrasyonu ve araç yönetimi için
- **LangChain4j MCP**: Model Context Protocol desteği için
- **LangChain4j OpenAI resmi**: MiniMax OpenAI uyumlu API entegrasyonu için
- **Spring Boot**: Uygulama çerçevesi ve bağımlılık enjeksiyonu için

## Lisans

Bu proje Apache Lisansı 2.0 altında lisanslanmıştır - detaylar için [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) dosyasına bakınız.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->