# Calculator HTTP Streaming Demo

Bu proje, Spring Boot WebFlux ile Server-Sent Events (SSE) kullanarak HTTP streaming’i gösterir. İki uygulamadan oluşur:

- **Calculator Server**: Hesaplamalar yapan ve sonuçları SSE ile yayınlayan reaktif bir web servisi
- **Calculator Client**: Streaming uç noktasını tüketen bir istemci uygulaması

## Gereksinimler

- Java 17 veya üzeri
- Maven 3.6 veya üzeri

## Proje Yapısı

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## Nasıl Çalışır

1. **Calculator Server** `/calculate` uç noktasını sunar:
   - Sorgu parametreleri alır: `a` (sayı), `b` (sayı), `op` (işlem)
   - Desteklenen işlemler: `add`, `sub`, `mul`, `div`
   - Hesaplama ilerlemesi ve sonucu Server-Sent Events olarak döner

2. **Calculator Client** sunucuya bağlanır ve:
   - `7 * 5` hesaplaması için istek yapar
   - Streaming yanıtını tüketir
   - Her olayı konsola yazdırır

## Uygulamaların Çalıştırılması

### Seçenek 1: Maven ile (Önerilen)

#### 1. Calculator Server’ı Başlatın

Bir terminal açın ve server dizinine gidin:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Sunucu `http://localhost:8080` adresinde çalışmaya başlayacaktır.

Aşağıdaki gibi bir çıktı görmelisiniz:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Calculator Client’ı Çalıştırın

**Yeni bir terminal** açın ve client dizinine gidin:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

İstemci sunucuya bağlanacak, hesaplamayı yapacak ve streaming sonuçlarını gösterecektir.

### Seçenek 2: Doğrudan Java ile

#### 1. Server’ı derleyip çalıştırın:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Client’ı derleyip çalıştırın:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Sunucuyu Manuel Test Etme

Sunucuyu web tarayıcısı veya curl ile de test edebilirsiniz:

### Web tarayıcısı ile:
Şurayı ziyaret edin: `http://localhost:8080/calculate?a=10&b=5&op=add`

### curl ile:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Beklenen Çıktı

İstemci çalıştırıldığında aşağıdakine benzer streaming çıktısı görmelisiniz:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Desteklenen İşlemler

- `add` - Toplama (a + b)
- `sub` - Çıkarma (a - b)
- `mul` - Çarpma (a * b)
- `div` - Bölme (a / b, b = 0 ise NaN döner)

## API Referansı

### GET /calculate

**Parametreler:**
- `a` (zorunlu): Birinci sayı (double)
- `b` (zorunlu): İkinci sayı (double)
- `op` (zorunlu): İşlem (`add`, `sub`, `mul`, `div`)

**Yanıt:**
- Content-Type: `text/event-stream`
- Hesaplama ilerlemesi ve sonucu Server-Sent Events olarak döner

**Örnek İstek:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Örnek Yanıt:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Sorun Giderme

### Yaygın Sorunlar

1. **Port 8080 zaten kullanılıyor**
   - Port 8080’i kullanan diğer uygulamaları durdurun
   - Ya da `calculator-server/src/main/resources/application.yml` dosyasından sunucu portunu değiştirin

2. **Bağlantı reddedildi**
   - İstemciyi başlatmadan önce sunucunun çalıştığından emin olun
   - Sunucunun 8080 portunda başarıyla başladığını kontrol edin

3. **Parametre adı sorunları**
   - Bu proje Maven derleyici yapılandırmasında `-parameters` bayrağını içerir
   - Parametre bağlama sorunları yaşarsanız, projenin bu yapılandırmayla derlendiğinden emin olun

### Uygulamaları Durdurma

- Her uygulamanın çalıştığı terminalde `Ctrl+C` tuşlarına basın
- Ya da arka planda çalışıyorsa `mvn spring-boot:stop` komutunu kullanın

## Teknoloji Yığını

- **Spring Boot 3.3.1** - Uygulama çatısı
- **Spring WebFlux** - Reaktif web çatısı
- **Project Reactor** - Reaktif stream kütüphanesi
- **Netty** - Engellemesiz I/O sunucusu
- **Maven** - Derleme aracı
- **Java 17+** - Programlama dili

## Sonraki Adımlar

Kodu değiştirerek deneyin:
- Daha fazla matematiksel işlem ekleyin
- Geçersiz işlemler için hata yönetimi ekleyin
- İstek/yanıt loglaması ekleyin
- Kimlik doğrulama uygulayın
- Birim testleri ekleyin

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.