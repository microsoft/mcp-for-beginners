# Temel Hesap Makinesi MCP Hizmeti

> [!NOTE]
> Bu örnek, eski HTTP+SSE taşıma yöntemi kullanmaktadır ve MCP `2025-11-25` ile uyumlu bir SDK'yı hedeflemektedir.
> Yeni uzak sunucular `2026-07-28` Streamable HTTP desteğini kullanmalıdır.








- SSE (Server-Sent Events) desteği
- Spring AI'nin `@Tool` açıklaması kullanılarak otomatik araç kaydı
- Temel hesap makinesi fonksiyonları:
  - Toplama, çıkarma, çarpma, bölme
  - Üs hesaplama ve karekök
  - Modül (kalan) ve mutlak değer
  - İşlem açıklamaları için yardım fonksiyonu






   - İki sayının toplanması
   - Bir sayının diğerinden çıkarılması
   - İki sayının çarpılması
   - Bir sayının diğerine bölünmesi (sıfıra bölme kontrolü ile)


   - Üs hesaplama (tabanın üste yükseltilmesi)
   - Karekök hesaplama (negatif sayı kontrolü ile)
   - Modül (kalan) hesaplama
   - Mutlak değer hesaplama


   - Mevcut tüm işlemleri açıklayan yerleşik yardım fonksiyonu






- `subtract(a, b)`: İkinci sayıyı birinciden çıkarır
- `multiply(a, b)`: İki sayıyı çarpar
- `divide(a, b)`: Birinci sayıyı ikinciye böler (sıfır kontrolü ile)
- `power(base, exponent)`: Bir sayının üssünü hesaplar
- `squareRoot(number)`: Karekökünü hesaplar (negatif sayı kontrolü ile)
- `modulus(a, b)`: Bölümünden kalan değeri hesaplar
- `absolute(number)`: Mutlak değeri hesaplar
- `help()`: Mevcut işlemler hakkında bilgi alır












   
   GitHub AI modellerini (phi-4 gibi) kullanmak için bir GitHub kişisel erişim token’ına ihtiyacınız vardır:


   
   b. "Generate new token" → "Generate new token (classic)" tıklayın
   
   c. Token’a açıklayıcı bir isim verin
   
   d. Aşağıdaki yetkileri seçin:
      - `repo` (Özel depolar üzerinde tam kontrol)
      - `read:org` (Organizasyon ve ekip üyeliğini okuma, organizasyon projelerini okuma)
      - `gist` (Gist oluşturma)


      - `user:email` (Kullanıcı e-posta adreslerine erişim (yalnızca okuma))
   
   e. "Generate token" butonuna tıklayın ve yeni token'ınızı kopyalayın
   
   f. Çevre değişkeni olarak ayarlayın:
      
      Windows'ta:
      ```
      set GITHUB_TOKEN=your-github-token
      ```
      
      macOS/Linux'ta:
      ```bash
      export GITHUB_TOKEN=your-github-token
      ```

   g. Kalıcı kurulum için, sistem ayarlarından çevre değişkenlerine ekleyin

2. LangChain4j GitHub bağımlılığını projenize ekleyin (zaten pom.xml içinde var):
   ```xml
   <dependency>
       <groupId>dev.langchain4j</groupId>
       <artifactId>langchain4j-github</artifactId>
       <version>${langchain4j.version}</version>
   </dependency>
   ```

3. Calculator sunucusunun `localhost:8080` adresinde çalıştığından emin olun

### LangChain4j İstemcisini Çalıştırma

Bu örnek şunları gösterir:
- Calculator MCP sunucusuna SSE protokolü üzerinden bağlanmak
- LangChain4j kullanarak calculator işlemlerini kullanan bir sohbet botu oluşturmak
- GitHub AI modelleri ile entegrasyon (şimdi phi-4 modeli kullanılıyor)

İstemci işlevselliği göstermek için aşağıdaki örnek sorguları gönderir:
1. İki sayının toplamını hesaplama
2. Bir sayının karekökünü bulma
3. Mevcut calculator işlemleri hakkında yardım bilgisi alma

Örneği çalıştırın ve AI modelinin sorulara nasıl calculator araçlarını kullanarak yanıt verdiğini görmek için konsol çıktısını kontrol edin.

### GitHub Model Yapılandırması

LangChain4j istemcisi GitHub'ın phi-4 modelini aşağıdaki ayarlarla kullanacak şekilde yapılandırılmıştır:

```java
ChatLanguageModel model = GitHubChatModel.builder()
    .apiKey(System.getenv("GITHUB_TOKEN"))
    .timeout(Duration.ofSeconds(60))
    .modelName("phi-4")
    .logRequests(true)
    .logResponses(true)
    .build();
```

Farklı GitHub modelleri kullanmak için `modelName` parametresini desteklenen başka bir modele değiştirmek yeterlidir (örneğin, "claude-3-haiku-20240307", "llama-3-70b-8192" vb.).

## Bağımlılıklar

Proje aşağıdaki temel bağımlılıkları gerektirir:

```xml
<!-- For MCP Server -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>

<!-- For LangChain4j integration -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-mcp</artifactId>
    <version>${langchain4j.version}</version>
</dependency>

<!-- For GitHub models support -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-github</artifactId>
    <version>${langchain4j.version}</version>
</dependency>
```

## Projeyi Derleme

Maven kullanarak projeyi derleyin:
```bash
./mvnw clean install -DskipTests
```

## Sunucuyu Çalıştırma

### Java Kullanarak

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### MCP Inspector Kullanarak

MCP Inspector, MCP servisleri ile etkileşimde bulunmak için kullanışlı bir araçtır. Bu calculator servisi ile kullanmak için:

1. **MCP Inspector'ı kurun ve yeni bir terminal penceresinde çalıştırın**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Uygulamanın gösterdiği URL'e tıklayarak web arayüzüne erişin** (genellikle http://localhost:6274)

3. **Bağlantıyı yapılandırın**:
   - Taşıma türünü "SSE" olarak ayarlayın
   - URL'yi çalışan sunucunuzun SSE uç noktasına ayarlayın: `http://localhost:8080/sse`
   - "Connect" butonuna tıklayın

4. **Araçları kullanın**:
   - Mevcut calculator işlemlerini görmek için "List Tools" butonuna tıklayın
   - Bir araç seçin ve işlemi yürütmek için "Run Tool" butonuna tıklayın

![MCP Inspector Screenshot](../../../../../../translated_images/tr/tool.c75a0b2380efcf1a.webp)

### Docker Kullanarak

Proje, konteyner tabanlı dağıtım için bir Dockerfile içerir:

1. **Docker imajını oluşturun**:
   ```bash
   docker build -t calculator-mcp-service .
   ```

2. **Docker konteynerini çalıştırın**:
   ```bash
   docker run -p 8080:8080 calculator-mcp-service
   ```

Bu şunları yapacaktır:
- Maven 3.9.9 ve Eclipse Temurin 24 JDK ile çok aşamalı bir Docker imajı oluşturur
- Optimize edilmiş bir konteyner imajı oluşturur
- Servisi 8080 portu üzerinde erişilebilir hale getirir
- Konteyner içinde MCP calculator servisini başlatır

Konteyner çalışmaya başladıktan sonra servise `http://localhost:8080` adresinden erişebilirsiniz.

## Sorun Giderme

### GitHub Token ile Yaygın Sorunlar


1. **Jeton İzin Sorunları**: 403 Forbidden hatası alırsanız, jetonunuzun ön koşullarda belirtilen doğru izinlere sahip olup olmadığını kontrol edin.

2. **Jeton Bulunamadı**: "No API key found" hatası alırsanız, GITHUB_TOKEN ortam değişkeninin doğru şekilde ayarlandığından emin olun.

3. **Oran Sınırlaması**: GitHub API'sinin oran sınırları vardır. Bir oran sınırı hatası (durum kodu 429) ile karşılaşırsanız, tekrar denemeden önce birkaç dakika bekleyin.

4. **Jetonun Süresi Dolması**: GitHub jetonlarının süresi dolabilir. Bir süre sonra kimlik doğrulama hataları alırsanız, yeni bir jeton oluşturun ve ortam değişkeninizi güncelleyin.

Daha fazla yardıma ihtiyacınız varsa, [LangChain4j dokümantasyonuna](https://github.com/langchain4j/langchain4j) veya [GitHub API dokümantasyonuna](https://docs.github.com/en/rest) bakın.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->