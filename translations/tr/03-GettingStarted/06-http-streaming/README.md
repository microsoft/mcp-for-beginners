<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "40b1bbffdb8ce6812bf6e701cad876b6",
  "translation_date": "2025-07-17T18:34:17+00:00",
  "source_file": "03-GettingStarted/06-http-streaming/README.md",
  "language_code": "tr"
}
-->
# Model Context Protocol (MCP) ile HTTPS Akışı

Bu bölüm, Model Context Protocol (MCP) kullanarak HTTPS üzerinden güvenli, ölçeklenebilir ve gerçek zamanlı akış uygulamanıza yönelik kapsamlı bir rehber sunar. Akışın motivasyonunu, mevcut taşıma mekanizmalarını, MCP’de akışa uygun HTTP’nin nasıl uygulanacağını, güvenlik en iyi uygulamalarını, SSE’den geçişi ve kendi akış tabanlı MCP uygulamalarınızı oluşturmak için pratik rehberliği kapsar.

## MCP’de Taşıma Mekanizmaları ve Akış

Bu bölüm, MCP’de mevcut farklı taşıma mekanizmalarını ve bunların istemciler ile sunucular arasında gerçek zamanlı iletişim için akış yeteneklerini nasıl sağladığını inceler.

### Taşıma Mekanizması Nedir?

Taşıma mekanizması, istemci ile sunucu arasında verinin nasıl değiş tokuş edildiğini tanımlar. MCP, farklı ortamlar ve gereksinimler için çeşitli taşıma türlerini destekler:

- **stdio**: Standart giriş/çıkış, yerel ve CLI tabanlı araçlar için uygundur. Basit ancak web veya bulut için uygun değildir.
- **SSE (Server-Sent Events)**: Sunucuların HTTP üzerinden istemcilere gerçek zamanlı güncellemeler göndermesine olanak tanır. Web arayüzleri için iyidir, ancak ölçeklenebilirlik ve esneklik açısından sınırlıdır.
- **Streamable HTTP**: Bildirimleri destekleyen ve daha iyi ölçeklenebilirlik sunan modern HTTP tabanlı akış taşıması. Çoğu üretim ve bulut senaryosu için önerilir.

### Karşılaştırma Tablosu

Aşağıdaki karşılaştırma tablosu, bu taşıma mekanizmaları arasındaki farkları anlamanıza yardımcı olur:

| Taşıma            | Gerçek Zamanlı Güncellemeler | Akış      | Ölçeklenebilirlik | Kullanım Alanı           |
|-------------------|------------------------------|-----------|-------------------|-------------------------|
| stdio             | Hayır                        | Hayır     | Düşük             | Yerel CLI araçları      |
| SSE               | Evet                         | Evet      | Orta              | Web, gerçek zamanlı güncellemeler |
| Streamable HTTP   | Evet                         | Evet      | Yüksek            | Bulut, çoklu istemci    |

> **Tip:** Doğru taşıma seçimi performans, ölçeklenebilirlik ve kullanıcı deneyimini etkiler. Modern, ölçeklenebilir ve bulut uyumlu uygulamalar için **Streamable HTTP** önerilir.

Önceki bölümlerde gösterilen stdio ve SSE taşıma mekanizmalarına ve bu bölümde ele alınan streamable HTTP taşımasına dikkat edin.

## Akış: Kavramlar ve Motivasyon

Akışın temel kavramlarını ve motivasyonlarını anlamak, etkili gerçek zamanlı iletişim sistemleri uygulamak için önemlidir.

**Akış**, ağ programlamasında verinin tamamının hazır olmasını beklemek yerine küçük, yönetilebilir parçalar veya olay dizisi halinde gönderilip alınmasına olanak tanıyan bir tekniktir. Bu özellikle şunlar için faydalıdır:

- Büyük dosyalar veya veri setleri.
- Gerçek zamanlı güncellemeler (örneğin, sohbet, ilerleme çubukları).
- Kullanıcıyı bilgilendirmek istediğiniz uzun süren hesaplamalar.

Akış hakkında bilmeniz gerekenler:

- Veri kademeli olarak iletilir, hepsi birden değil.
- İstemci veriyi geldikçe işleyebilir.
- Algılanan gecikmeyi azaltır ve kullanıcı deneyimini iyileştirir.

### Neden akış kullanılır?

Akış kullanmanın sebepleri şunlardır:

- Kullanıcılar sadece sonunda değil, hemen geri bildirim alır.
- Gerçek zamanlı uygulamalar ve duyarlı kullanıcı arayüzleri sağlar.
- Ağ ve hesaplama kaynaklarının daha verimli kullanımı.

### Basit Örnek: HTTP Akış Sunucusu ve İstemcisi

Akışın nasıl uygulanabileceğine dair basit bir örnek:

## Python

**Sunucu (Python, FastAPI ve StreamingResponse kullanarak):**

### Python

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

async def event_stream():
    for i in range(1, 6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```


**İstemci (Python, requests kullanarak):**

### Python

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```


Bu örnek, sunucunun tüm mesajlar hazır olana kadar beklemek yerine, mesajları hazır oldukça istemciye göndermesini gösterir.

**Nasıl çalışır:**
- Sunucu her mesajı hazır olduğunda gönderir.
- İstemci gelen her parçayı alır ve yazdırır.

**Gereksinimler:**
- Sunucu akış yanıtı kullanmalı (örneğin, FastAPI’de `StreamingResponse`).
- İstemci yanıtı akış olarak işlemeli (`requests`’te `stream=True`).
- İçerik türü genellikle `text/event-stream` veya `application/octet-stream` olur.

## Java

**Sunucu (Java, Spring Boot ve Server-Sent Events kullanarak):**

```java
@RestController
public class CalculatorController {

    @GetMapping(value = "/calculate", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> calculate(@RequestParam double a,
                                                   @RequestParam double b,
                                                   @RequestParam String op) {
        
        double result;
        switch (op) {
            case "add": result = a + b; break;
            case "sub": result = a - b; break;
            case "mul": result = a * b; break;
            case "div": result = b != 0 ? a / b : Double.NaN; break;
            default: result = Double.NaN;
        }

        return Flux.<ServerSentEvent<String>>just(
                    ServerSentEvent.<String>builder()
                        .event("info")
                        .data("Calculating: " + a + " " + op + " " + b)
                        .build(),
                    ServerSentEvent.<String>builder()
                        .event("result")
                        .data(String.valueOf(result))
                        .build()
                )
                .delayElements(Duration.ofSeconds(1));
    }
}
```

**İstemci (Java, Spring WebFlux WebClient kullanarak):**

```java
@SpringBootApplication
public class CalculatorClientApplication implements CommandLineRunner {

    private final WebClient client = WebClient.builder()
            .baseUrl("http://localhost:8080")
            .build();

    @Override
    public void run(String... args) {
        client.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/calculate")
                        .queryParam("a", 7)
                        .queryParam("b", 5)
                        .queryParam("op", "mul")
                        .build())
                .accept(MediaType.TEXT_EVENT_STREAM)
                .retrieve()
                .bodyToFlux(String.class)
                .doOnNext(System.out::println)
                .blockLast();
    }
}
```

**Java Uygulama Notları:**
- Spring Boot’un reaktif yığını `Flux` ile akış sağlar
- `ServerSentEvent` yapılandırılmış olay akışı ve olay türleri sunar
- `WebClient` ve `bodyToFlux()` reaktif akış tüketimini mümkün kılar
- `delayElements()` olaylar arasındaki işlem süresini simüle eder
- Olaylar, istemci tarafında daha iyi işleme için türlere (`info`, `result`) sahip olabilir

### Karşılaştırma: Klasik Akış vs MCP Akışı

Klasik akış ile MCP akışının nasıl farklı çalıştığını aşağıdaki tabloda görebilirsiniz:

| Özellik                | Klasik HTTP Akışı             | MCP Akışı (Bildirimler)           |
|------------------------|-------------------------------|----------------------------------|
| Ana yanıt              | Parçalı (chunked)             | Tek parça, sonunda gönderilir    |
| İlerleme güncellemeleri| Veri parçaları olarak gönderilir | Bildirimler olarak gönderilir    |
| İstemci gereksinimleri | Akışı işlemeli                | Mesaj işleyici uygulamalı         |
| Kullanım alanı         | Büyük dosyalar, AI token akışları | İlerleme, loglar, gerçek zamanlı geri bildirim |

### Gözlemlenen Temel Farklar

Ek olarak, bazı temel farklar:

- **İletişim Deseni:**
   - Klasik HTTP akışı: Basit parçalı transfer kodlaması kullanır
   - MCP akışı: JSON-RPC protokolü ile yapılandırılmış bildirim sistemi kullanır

- **Mesaj Formatı:**
   - Klasik HTTP: Yeni satırlarla ayrılmış düz metin parçaları
   - MCP: Meta veriler içeren yapılandırılmış LoggingMessageNotification nesneleri

- **İstemci Uygulaması:**
   - Klasik HTTP: Akış yanıtlarını işleyen basit istemci
   - MCP: Farklı mesaj türlerini işlemek için mesaj işleyici kullanan daha gelişmiş istemci

- **İlerleme Güncellemeleri:**
   - Klasik HTTP: İlerleme ana yanıt akışının parçası
   - MCP: İlerleme, ana yanıt sonunda gelirken ayrı bildirim mesajlarıyla gönderilir

### Öneriler

Klasik akış (örneğin yukarıda `/stream` ile gösterilen) ile MCP akışı arasında seçim yaparken bazı öneriler:

- **Basit akış ihtiyaçları için:** Klasik HTTP akışı daha basit ve temel akış ihtiyaçları için yeterlidir.

- **Karmaşık, etkileşimli uygulamalar için:** MCP akışı, zengin meta veriler ve bildirimler ile sonuçların ayrılması sayesinde daha yapılandırılmış bir yaklaşım sunar.

- **Yapay zeka uygulamaları için:** MCP’nin bildirim sistemi, uzun süren AI görevlerinde kullanıcıları ilerleme hakkında bilgilendirmek için özellikle faydalıdır.

## MCP’de Akış

Şimdiye kadar klasik akış ile MCP akışı arasındaki farklar ve öneriler hakkında bilgi edindiniz. MCP’de akışı nasıl kullanabileceğinize daha detaylı bakalım.

MCP çerçevesinde akış, ana yanıtı parçalara bölerek göndermek değil, bir araç isteği işlerken istemciye **bildirimler** göndermekle ilgilidir. Bu bildirimler ilerleme güncellemeleri, loglar veya diğer olayları içerebilir.

### Nasıl çalışır

Ana sonuç hâlâ tek bir yanıt olarak gönderilir. Ancak, işlem sırasında bildirimler ayrı mesajlar olarak gönderilerek istemci gerçek zamanlı olarak güncellenir. İstemci bu bildirimleri işleyip gösterebilmelidir.

## Bildirim Nedir?

“Bildirim” dedik, MCP bağlamında ne anlama gelir?

Bildirim, uzun süren bir işlem sırasında sunucudan istemciye ilerleme, durum veya diğer olaylar hakkında bilgi vermek için gönderilen mesajdır. Bildirimler şeffaflığı ve kullanıcı deneyimini artırır.

Örneğin, istemcinin sunucu ile ilk el sıkışma tamamlandığında bir bildirim göndermesi beklenir.

Bir bildirim JSON mesajı olarak şöyle görünür:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Bildirimler MCP’de ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging) adlı bir konuya aittir.

Logging’in çalışması için sunucunun bunu özellik/yetenek olarak etkinleştirmesi gerekir:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Kullanılan SDK’ya bağlı olarak, logging varsayılan olarak etkin olabilir veya sunucu yapılandırmanızda açıkça etkinleştirmeniz gerekebilir.

Farklı bildirim türleri vardır:

| Seviye    | Açıklama                      | Örnek Kullanım Durumu          |
|-----------|------------------------------|-------------------------------|
| debug     | Ayrıntılı hata ayıklama bilgisi | Fonksiyon giriş/çıkış noktaları |
| info      | Genel bilgilendirici mesajlar | İşlem ilerleme güncellemeleri  |
| notice    | Normal ama önemli olaylar     | Konfigürasyon değişiklikleri   |
| warning   | Uyarı durumları              | Kullanımdan kaldırılmış özellikler |
| error     | Hata durumları              | İşlem hataları                |
| critical  | Kritik durumlar             | Sistem bileşeni arızaları     |
| alert     | Hemen müdahale gerektirir  | Veri bozulması tespiti        |
| emergency | Sistem kullanılamaz durumda | Tam sistem arızası            |

## MCP’de Bildirimlerin Uygulanması

Bildirimleri MCP’de uygulamak için hem sunucu hem de istemci tarafını gerçek zamanlı güncellemeleri işleyebilecek şekilde ayarlamanız gerekir. Bu, uzun süren işlemler sırasında uygulamanızın kullanıcılara anlık geri bildirim sağlamasına olanak tanır.

### Sunucu tarafı: Bildirim Gönderme

Sunucu tarafıyla başlayalım. MCP’de, istekleri işlerken bildirim gönderebilen araçlar tanımlarsınız. Sunucu, istemciye mesaj göndermek için genellikle `ctx` olarak adlandırılan context nesnesini kullanır.

### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Yukarıdaki örnekte, `process_files` aracı her dosyayı işlerken istemciye üç bildirim gönderir. `ctx.info()` metodu bilgilendirici mesajlar göndermek için kullanılır.

Ayrıca, bildirimleri etkinleştirmek için sunucunuzun `streamable-http` gibi bir akış taşıması kullandığından ve istemcinizin bildirimleri işlemek için mesaj işleyici uyguladığından emin olun. Sunucuyu `streamable-http` taşımasını kullanacak şekilde nasıl ayarlayabileceğiniz aşağıda gösterilmiştir:

```python
mcp.run(transport="streamable-http")
```

### .NET

```csharp
[Tool("A tool that sends progress notifications")]
public async Task<TextContent> ProcessFiles(string message, ToolContext ctx)
{
    await ctx.Info("Processing file 1/3...");
    await ctx.Info("Processing file 2/3...");
    await ctx.Info("Processing file 3/3...");
    return new TextContent
    {
        Type = "text",
        Text = $"Done: {message}"
    };
}
```

Bu .NET örneğinde, `ProcessFiles` aracı `Tool` özniteliği ile işaretlenmiş ve her dosyayı işlerken istemciye üç bildirim gönderir. `ctx.Info()` metodu bilgilendirici mesajlar göndermek için kullanılır.

.NET MCP sunucunuzda bildirimleri etkinleştirmek için akış taşıması kullandığınızdan emin olun:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### İstemci tarafı: Bildirim Alma

İstemci, gelen bildirimleri işleyip göstermek için bir mesaj işleyici uygulamalıdır.

### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)

async with ClientSession(
   read_stream, 
   write_stream,
   logging_callback=logging_collector,
   message_handler=message_handler,
) as session:
```

Yukarıdaki kodda, `message_handler` fonksiyonu gelen mesajın bildirim olup olmadığını kontrol eder. Bildirimse yazdırır, değilse normal sunucu mesajı olarak işler. Ayrıca `ClientSession`’ın bildirimleri işlemek için `message_handler` ile başlatıldığına dikkat edin.

### .NET

```csharp
// Define a message handler
void MessageHandler(IJsonRpcMessage message)
{
    if (message is ServerNotification notification)
    {
        Console.WriteLine($"NOTIFICATION: {notification}");
    }
    else
    {
        Console.WriteLine($"SERVER MESSAGE: {message}");
    }
}

// Create and use a client session with the message handler
var clientOptions = new ClientSessionOptions
{
    MessageHandler = MessageHandler,
    LoggingCallback = (level, message) => Console.WriteLine($"[{level}] {message}")
};

using var client = new ClientSession(readStream, writeStream, clientOptions);
await client.InitializeAsync();

// Now the client will process notifications through the MessageHandler
```

Bu .NET örneğinde, `MessageHandler` fonksiyonu gelen mesajın bildirim olup olmadığını kontrol eder. Bildirimse yazdırır, değilse normal sunucu mesajı olarak işler. `ClientSession`, `ClientSessionOptions` aracılığıyla mesaj işleyici ile başlatılır.

Bildirimleri etkinleştirmek için sunucunuzun `streamable-http` gibi bir akış taşıması kullandığından ve istemcinizin bildirimleri işlemek için mesaj işleyici uyguladığından emin olun.

## İlerleme Bildirimleri ve Senaryolar

Bu bölüm, MCP’de ilerleme bildirimleri kavramını, neden önemli olduklarını ve Streamable HTTP kullanarak nasıl uygulanacağını açıklar. Ayrıca konuyu pekiştirmek için pratik bir görev içerir.

İlerleme bildirimleri, uzun süren işlemler sırasında sunucudan istemciye gerçek zamanlı gönderilen mesajlardır. Tüm işlem bitene kadar beklemek yerine, sunucu istemciyi mevcut durum hakkında güncel tutar. Bu şeffaflığı artırır, kullanıcı deneyimini iyileştirir ve hata ayıklamayı kolaylaştırır.

**Örnek:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Neden İlerleme Bildirimleri Kullanılır?

İlerleme bildirimleri şu nedenlerle önemlidir:

- **Daha iyi kullanıcı deneyimi:** Kullanıcılar iş ilerledikçe güncellemeleri görür, sadece sonunda değil.
- **Gerçek zamanlı geri bildirim:** İstemciler ilerleme çubukları veya loglar gösterebilir, uygulama daha duyarlı hissedilir.
- **Daha kolay hata ayıklama ve izleme:** Geliştiriciler ve kullanıcılar işlemin nerede yavaşladığını veya takıldığını görebilir.

### İlerleme Bildirimleri Nasıl Uygulanır?

MCP’de ilerleme bildirimlerini şöyle uygulayabilirsiniz:

- **Sunucu tarafında:** Her öğe işlenirken `ctx.info()` veya `ctx.log()` kullanarak bildirim gönderin. Bu, ana sonuç hazır olmadan önce istemciye mesaj gönderir.
- **İstemci tarafında:** Gelen bildirimleri dinleyen ve gösteren bir mesaj işleyici uygulayın. Bu işleyici bildirimler ile son sonucu ayırt eder.

**Sunucu Örneği:**

## Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```


**İstemci Örneği:**

### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```


## Güvenlik Hususları

HTTP tabanlı taşıma kullanan MCP sunucuları uygularken, güvenlik çok önemli bir konudur ve çeşitli saldırı vektörlerine karşı dikkatli önlemler alınmalıdır.

### Genel Bakış

MCP sunucularını HTTP üzerinden açarken güvenlik kritik öneme sahiptir. Streamable HTTP yeni saldırı yüzeyleri oluşturur ve dikkatli yapılandırma gerektirir.

### Temel Noktalar
- **Origin Header Doğrulaması:** DNS rebinding saldırılarını önlemek için `Origin` başlığını mutlaka doğrulayın.
- **Localhost Bağlama:** Yerel geliştirme için sunucuları `localhost`’a bağlayarak genel internete açılmasını engelleyin.
- **Kimlik Doğrulama:** Üretim ortamlarında API anahtarları, OAuth gibi kimlik doğrulama yöntemleri uygulayın.
- **CORS:** Erişimi kısıtlamak için Cross-Origin Resource Sharing (CORS) politikalarını yapılandırın.
- **HTTPS:** Trafiği şifrelemek için üretimde HTTPS kullanın.

### En İyi Uygulamalar
- Gelen istekleri doğrulamadan asla güvenmeyin.
- Tüm erişimleri ve hataları kaydedip izleyin.
- Güvenlik açıklarını gidermek için bağımlılıkları düzenli güncelleyin.

### Zorluklar
- Güvenlik ile geliştirme kolaylığı arasında denge kurmak
- Farklı istemci ortamlarıyla uyumluluğu sağlamak

## SSE’den Streamable HTTP’ye Geçiş

Şu anda Server-Sent Events (SSE) kullanan uygulamalar için Streamable HTTP’ye geçiş, MCP uygulamalarınızda gelişmiş yetenekler ve daha iyi uzun vadeli sürdürülebilirlik sağlar.
### Neden Yükseltme Yapmalısınız?

SSE'den Streamable HTTP'ye yükseltmek için iki önemli neden vardır:

- Streamable HTTP, SSE'ye kıyasla daha iyi ölçeklenebilirlik, uyumluluk ve daha zengin bildirim desteği sunar.
- Yeni MCP uygulamaları için önerilen taşıma yöntemidir.

### Geçiş Adımları

MCP uygulamalarınızda SSE'den Streamable HTTP'ye nasıl geçiş yapabileceğiniz aşağıda açıklanmıştır:

- **Sunucu kodunu güncelleyin** ve `mcp.run()` içinde `transport="streamable-http"` kullanın.
- **İstemci kodunu güncelleyin** ve SSE istemcisi yerine `streamablehttp_client` kullanın.
- **İstemcide bir mesaj işleyici uygulayın** ve bildirimleri işleyin.
- **Mevcut araçlar ve iş akışları ile uyumluluğu test edin.**

### Uyumluluğun Korunması

Geçiş sürecinde mevcut SSE istemcileriyle uyumluluğu korumanız önerilir. İşte bazı stratejiler:

- Farklı uç noktalarda her iki taşıma yöntemini de çalıştırarak hem SSE hem de Streamable HTTP'yi destekleyebilirsiniz.
- İstemcileri kademeli olarak yeni taşıma yöntemine geçirin.

### Zorluklar

Geçiş sırasında aşağıdaki zorlukları ele aldığınızdan emin olun:

- Tüm istemcilerin güncellenmesini sağlamak
- Bildirim iletimindeki farklılıkları yönetmek

## Güvenlik Hususları

Herhangi bir sunucu uygularken, özellikle MCP'de Streamable HTTP gibi HTTP tabanlı taşıma yöntemleri kullanıldığında güvenlik en öncelikli konu olmalıdır.

HTTP tabanlı taşıma yöntemleriyle MCP sunucuları uygularken, çok sayıda saldırı vektörüne ve koruma mekanizmasına dikkat etmek gerekir.

### Genel Bakış

MCP sunucularını HTTP üzerinden açarken güvenlik kritik öneme sahiptir. Streamable HTTP yeni saldırı yüzeyleri getirir ve dikkatli yapılandırma gerektirir.

İşte bazı önemli güvenlik hususları:

- **Origin Header Doğrulaması**: DNS yeniden bağlama saldırılarını önlemek için `Origin` başlığını her zaman doğrulayın.
- **Localhost Bağlama**: Yerel geliştirme için sunucuları `localhost`a bağlayarak genel internete açılmasını engelleyin.
- **Kimlik Doğrulama**: Üretim ortamlarında kimlik doğrulama (örneğin API anahtarları, OAuth) uygulayın.
- **CORS**: Erişimi kısıtlamak için Cross-Origin Resource Sharing (CORS) politikalarını yapılandırın.
- **HTTPS**: Trafiği şifrelemek için üretimde HTTPS kullanın.

### En İyi Uygulamalar

MCP streaming sunucunuzda güvenlik uygularken aşağıdaki en iyi uygulamaları takip edin:

- Gelen istekleri doğrulamadan asla güvenmeyin.
- Tüm erişim ve hataları kaydedin ve izleyin.
- Güvenlik açıklarını gidermek için bağımlılıkları düzenli olarak güncelleyin.

### Zorluklar

MCP streaming sunucularında güvenlik uygularken karşılaşacağınız bazı zorluklar:

- Güvenlik ile geliştirme kolaylığı arasında denge kurmak
- Çeşitli istemci ortamlarıyla uyumluluğu sağlamak

### Ödev: Kendi Streaming MCP Uygulamanızı Oluşturun

**Senaryo:**  
Sunucu, bir öğe listesi (örneğin dosyalar veya belgeler) işleyen ve her işlenen öğe için bildirim gönderen bir MCP sunucusu ve istemcisi oluşturun. İstemci, gelen her bildirimi anında göstermelidir.

**Adımlar:**

1. Bir listeyi işleyen ve her öğe için bildirim gönderen bir sunucu aracı uygulayın.
2. Bildirimleri gerçek zamanlı göstermek için mesaj işleyicisi olan bir istemci uygulayın.
3. Hem sunucu hem istemciyi çalıştırarak uygulamanızı test edin ve bildirimleri gözlemleyin.

[Solution](./solution/README.md)

## Daha Fazla Okuma & Sonraki Adımlar

MCP streaming yolculuğunuza devam etmek ve bilginizi genişletmek için bu bölüm, daha gelişmiş uygulamalar oluşturmak üzere ek kaynaklar ve önerilen sonraki adımları sunar.

### Daha Fazla Okuma

- [Microsoft: HTTP Streaming’e Giriş](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: ASP.NET Core’da CORS](https://learn.microsoft.com/en-us/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Sonraki Adımlar

- Gerçek zamanlı analiz, sohbet veya ortak düzenleme için streaming kullanan daha gelişmiş MCP araçları geliştirmeyi deneyin.
- MCP streaming’i canlı UI güncellemeleri için frontend framework’leri (React, Vue vb.) ile entegre etmeyi keşfedin.
- Sonraki: [VSCode için AI Toolkit Kullanımı](../07-aitk/README.md)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.