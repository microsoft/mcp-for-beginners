# Temel Hesap Makinesi MCP Servisi

Bu servis, Spring Boot ile WebFlux taşıma kullanarak Model Context Protocol (MCP) üzerinden temel hesap makinesi işlemleri sağlar. MCP uygulamalarını öğrenen yeni başlayanlar için basit bir örnek olarak tasarlanmıştır.

Daha fazla bilgi için [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) referans dokümantasyonuna bakabilirsiniz.


## Servisin Kullanımı

Servis, MCP protokolü aracılığıyla aşağıdaki API uç noktalarını sunar:

- `add(a, b)`: İki sayıyı toplar
- `subtract(a, b)`: İkinci sayıdan birincisini çıkarır
- `multiply(a, b)`: İki sayıyı çarpar
- `divide(a, b)`: Birinci sayıyı ikinciye böler (sıfır kontrolü ile)
- `power(base, exponent)`: Bir sayının kuvvetini hesaplar
- `squareRoot(number)`: Kare kökünü hesaplar (negatif sayı kontrolü ile)
- `modulus(a, b)`: Bölme işleminde kalanı hesaplar
- `absolute(number)`: Mutlak değeri hesaplar

## Bağımlılıklar

Proje aşağıdaki temel bağımlılıkları gerektirir:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

## Projeyi Derleme

Projeyi Maven ile derleyin:
```bash
./mvnw clean install -DskipTests
```

## Sunucuyu Çalıştırma

### Java Kullanarak

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### MCP Inspector Kullanarak

MCP Inspector, MCP servisleriyle etkileşimde bulunmak için faydalı bir araçtır. Bu hesap makinesi servisi ile kullanmak için:

1. **MCP Inspector'ı yükleyin ve yeni bir terminal penceresinde çalıştırın:**
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Uygulamanın gösterdiği URL'ye tıklayarak web arayüzüne erişin** (genellikle http://localhost:6274)

3. **Bağlantıyı yapılandırın:**
   - Taşıma türünü "SSE" olarak ayarlayın
   - URL'yi çalışan sunucunuzun SSE uç noktası olarak ayarlayın: `http://localhost:8080/sse`
   - "Connect" butonuna tıklayın

4. **Araçları kullanın:**
   - Mevcut hesap makinesi işlemlerini görmek için "List Tools" butonuna tıklayın
   - Bir aracı seçin ve işlemi çalıştırmak için "Run Tool" butonuna tıklayın

![MCP Inspector Ekran Görüntüsü](../../../../../../translated_images/tr/tool.40e180a7b0d0fe2067cf96435532b01f63f7f8619d6b0132355a04b426b669ac.png)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.