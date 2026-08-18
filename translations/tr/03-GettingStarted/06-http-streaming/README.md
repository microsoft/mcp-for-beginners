# Model Context Protocol (MCP) ile HTTPS Akışı

Bu bölüm, Model Context Protocol (MCP) kullanarak HTTPS üzerinden güvenli, ölçeklenebilir ve gerçek zamanlı akış uygulamak için kapsamlı bir rehber sunar. Akış motivasyonunu, mevcut taşıma mekanizmalarını, MCP'de akış yapılabilir HTTP'nin nasıl uygulanacağını, güvenlik en iyi uygulamalarını, SSE'den geçişi ve kendi akış MCP uygulamalarınızı oluşturmak için pratik rehberliği kapsar.

> **İleriye bakarken:** Bu ders, bir oturumun `initialize` sırasında kurulduğu ve `Mcp-Session-Id` başlığı ile sabitlendiği **MCP Spesifikasyonu 2025-11-25** altında Akış Yapılabilir HTTP'yi açıklar. `2026-07-28` sürüm adayı ise el sıkışmayı ve oturum kimliğini tamamen kaldırarak her isteğin kendi içinde bağımsız ve yapışkan oturum olmadan herhangi bir sunucu örneğine yönlendirilebilir olmasını sağlar. Ayrıntılar için [MCP'de Neler Değişiyor: 2026-07-28 Sürüm Adayı](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) sayfasına bakınız.

## MCP'de Taşıma Mekanizmaları ve Akış

Bu bölüm, MCP'de mevcut farklı taşıma mekanizmalarını ve istemci ile sunucu arasında gerçek zamanlı iletişimi mümkün kılan akış yeteneklerindeki rollerini inceler.

### Taşıma Mekanizması Nedir?

Bir taşıma mekanizması, istemci ile sunucu arasında verinin nasıl değiş tokuş edildiğini tanımlar. MCP, farklı ortamlar ve gereksinimler için çeşitli taşıma türlerini destekler:

- **stdio**: Standart giriş/çıkış, yerel ve CLI tabanlı araçlar için uygundur. Basittir ancak web veya bulut için uygun değildir.
- **SSE (Server-Sent Events)**: Sunucuların HTTP üzerinden istemcilere gerçek zamanlı güncellemeler göndermesine olanak tanır. Web kullanıcı arayüzleri için iyidir, ancak ölçeklenebilirlik ve esneklik açısından sınırlıdır. MCP Spesifikasyonu 2025-06-18 itibariyle bağımsız SSE taşıması kullanımdan kaldırılmış ve yerine "Akış Yapılabilir HTTP" taşıması getirilmiştir.
- **Akış Yapılabilir HTTP**: Bildirimleri destekleyen modern HTTP tabanlı akış taşıması, daha iyi ölçeklenebilirlik sunar. Çoğu üretim ve bulut senaryosu için önerilir.

### Karşılaştırma Tablosu

Bu taşıma mekanizmaları arasındaki farkları anlamak için aşağıdaki karşılaştırma tablosuna göz atın:

| Taşıma          | Gerçek Zamanlı Güncellemeler | Akış       | Ölçeklenebilirlik | Kullanım Alanı            |
|-----------------|------------------------------|------------|-------------------|--------------------------|
| stdio           | Hayır                        | Hayır      | Düşük             | Yerel CLI araçları       |
| SSE             | Evet                         | Evet       | Orta              | Web, gerçek zamanlı güncellemeler |
| Akış Yapılabilir HTTP | Evet                    | Evet       | Yüksek            | Bulut, çoklu istemci     |

> **İpucu:** Doğru taşıma seçimi performansı, ölçeklenebilirliği ve kullanıcı deneyimini etkiler. Modern, ölçeklenebilir ve bulut hazır uygulamalar için **Akış Yapılabilir HTTP** önerilir.

Önceki bölümlerde gösterilen stdio ve SSE taşıma yöntemlerini ve bu bölümde kapsanan akış yapılabilir HTTP'nin taşıma yöntemi olduğunu unutmayın.

## Akış: Kavramlar ve Motivasyon

Akışın temel kavramlarını ve motivasyonlarını anlamak, etkili gerçek zamanlı iletişim sistemleri uygulamak için gereklidir.

**Akış**, ağ programlamasında verinin tüm yanıtın hazır olmasını beklemek yerine küçük, yönetilebilir parçalarda veya olaylar dizisi olarak gönderilip alınmasına olanak tanıyan bir tekniktir. Bu özellikle şunlar için kullanışlıdır:

- Büyük dosyalar veya veri setleri.
- Gerçek zamanlı güncellemeler (ör. sohbet, ilerleme çubukları).
- Kullanıcıyı bilgilendirmek istediğiniz uzun süre çalışan hesaplamalar.

Akış hakkında bilmeniz gerekenler:

- Veri kademeli olarak iletilir, hepsi birden değil.
- İstemci veriyi geldiği gibi işleyebilir.
- Algılanan gecikmeyi azaltır ve kullanıcı deneyimini iyileştirir.

### Neden akış kullanılır?

Akış kullanmanın sebepleri şunlardır:

- Kullanıcılar sadece sonunda değil, anında geri bildirim alır.
- Gerçek zamanlı uygulamalar ve duyarlı kullanıcı arayüzleri sağlar.
- Ağ ve hesaplama kaynaklarını daha verimli kullanır.

### Basit Örnek: HTTP Akış Sunucu ve İstemcisi

İşte akış uygulamayı gösteren basit bir örnek:

#### Python

**Sunucu (Python, FastAPI ve StreamingResponse kullanarak):**

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

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Bu örnek, sunucunun tüm mesajların hazır olmasını beklemek yerine, mesajlar hazır oldukça istemciye göndermesini gösterir.

**Nasıl çalışır:**

- Sunucu her mesajı hazır oldukça verir.
- İstemci gelen her parçayı alır ve yazdırır.

**Gereksinimler:**

- Sunucu akış yapabilir yanıt (örneğin FastAPI’de `StreamingResponse`) kullanmalıdır.
- İstemci yanıtı akış olarak işlemelidir (`requests`’te `stream=True`).
- İçerik türü genellikle `text/event-stream` veya `application/octet-stream` olur.

#### Java

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

- Akış için `Flux` kullanan Spring Boot reaktif yığını
- `ServerSentEvent` olay türleriyle yapılandırılmış olay akışı sağlar
- `WebClient` ve `bodyToFlux()` reaktif akış tüketimini sağlar
- `delayElements()` olaylar arasında işleme süresi simüle eder
- Olaylar (`info`, `result`) türlerine sahip olabilir, istemci için daha iyi işlem yapılır

### Karşılaştırma: Klasik Akış ile MCP Akışı

Klasik akış ve MCP akışının nasıl farklı çalıştığını şöyle gösterebiliriz:

| Özellik                | Klasik HTTP Akışı            | MCP Akışı (Bildirimler)         |
|------------------------|------------------------------|--------------------------------|
| Ana yanıt              | Parçalı (chunked)            | Tek, sonunda                   |
| İlerleme güncellemeleri| Veri parçaları olarak gönderilir | Bildirimler olarak gönderilir      |
| İstemci gereksinimleri  | Akışı işlemeli               | Mesaj işleyici uygulamalı      |
| Kullanım alanı          | Büyük dosyalar, AI token akışları | İlerleme, günlükler, gerçek zamanlı geri bildirim |

### Gözlemlenen Temel Farklar

Ayrıca, bazı temel farklar şunlardır:

- **İletişim Deseni:**
  - Klasik HTTP akışı: Basit parçalı aktarım kodlaması kullanır
  - MCP akışı: JSON-RPC protokolü ile yapılandırılmış bildirim sistemi kullanır

- **Mesaj Formatı:**
  - Klasik HTTP: Yeni satırlarla bölünmüş düz metin parçaları
  - MCP: Meta veriye sahip yapılandırılmış LoggingMessageNotification nesneleri

- **İstemci Uygulaması:**
  - Klasik HTTP: Akış yanıtları işleyen basit istemci
  - MCP: Farklı mesaj türlerini işlemek için mesaj işleyici olan daha gelişmiş istemci

- **İlerleme Güncellemeleri:**
  - Klasik HTTP: İlerleme ana yanıt akışının parçasıdır
  - MCP: İlerleme, ana yanıt sonunda gelirken ayrı bildirim mesajlarıyla gönderilir

### Öneriler

Klasik akışı (yukarıda `/stream` kullanarak gösterildiği gibi) veya MCP akışını uygulama arasında seçim yaparken bazı önerilerimiz var.

- **Basit akış ihtiyaçları için:** Klasik HTTP akışı uygulaması daha basittir ve temel akış ihtiyaçları için yeterlidir.

- **Karmaşık, etkileşimli uygulamalar için:** MCP akışı, bildirimler ve sonuçlar arasında net ayrım ile daha yapılandırılmış bir yaklaşım sunar.

- **AI uygulamaları için:** MCP'nin bildirim sistemi, kullanıcıları ilerleme hakkında bilgilendirmek istediğiniz uzun süreli AI görevleri için özellikle kullanışlıdır.

## MCP'de Akış

Şimdiye kadar klasik akış ile MCP akışı arasındaki farklara ve önerilere baktınız. MCP'de tam olarak nasıl akış yapabileceğinize detaylı bakalım.

MCP çerçevesi içinde akışın nasıl işlediğini anlamak, uzun süreli işlemler sırasında kullanıcılara gerçek zamanlı geri bildirim veren duyarlı uygulamalar geliştirmek için çok önemlidir.

MCP'de akış, ana yanıtı parçalara bölüp göndermek değil, bir aracın istekleri işlerken istemciye **bildirimler** göndermekle ilgilidir. Bu bildirimler ilerleme güncellemeleri, günlükler veya diğer olayları içerebilir.

### Nasıl çalışır

Ana sonuç yine tek bir yanıt olarak gönderilir. Ancak, işlem sırasında bildirimler ayrı mesajlar halinde gönderilerek istemci gerçek zamanlı olarak güncellenir. İstemci bu bildirimleri işleyip gösterebilmelidir.

## Bildirim (Notification) Nedir?

"Bildirim" dedik, MCP bağlamında ne anlama geliyor?

Bildirim, uzun süren bir işlem sırasında ilerleme, durum veya diğer olaylar hakkında bilgilendirmek için sunucudan istemciye gönderilen mesajdır. Bildirimler şeffaflığı ve kullanıcı deneyimini artırır.

Örneğin, istemci sunucu ile ilk el sıkışması tamamlandığında bir bildirim göndermelidir.

Bir bildirim JSON mesajı olarak şu şekildedir:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Bildirimler, MCP'de ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging) olarak adlandırılan bir konuya aittir.

> **Kaldırma bildirimi:** `2026-07-28` MCP spesifikasyon sürüm adayı, Logging özelliğini stdio taşıma için `stderr` ve yapılandırılmış gözlemlenebilirlik için OpenTelemetry lehine kullanımdan kaldırmayı işaret eder. Logging, `2025-11-25` sürümünde ve resmi kaldırmadan sonra en az bir yıl daha çalışmaya devam eder. Detaylar için [MCP'de Neler Değişiyor: 2026-07-28 Sürüm Adayı](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) sayfasına bakınız.

Logging'i etkinleştirmek için sunucu bunu özellik/yetenek olarak açmalıdır:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Kullanılan SDK'ya bağlı olarak logging varsayılan etkin olabilir veya sunucu yapılandırmanızda açıkça etkinleştirmeniz gerekebilir.

Farklı bildirim seviyeleri vardır:

| Seviye   | Açıklama                     | Örnek Kullanım Alanı          |
|---------|------------------------------|------------------------------|
| debug   | Detaylı hata ayıklama bilgisi | Fonksiyon giriş/çıkış noktaları |
| info    | Genel bilgilendirici mesajlar | İşlem ilerleme güncellemeleri  |
| notice  | Normal ama önemli olaylar      | Yapılandırma değişiklikleri    |
| warning | Uyarı durumu                  | Kullanımdan kaldırılmış özellik kullanımı |
| error   | Hata durumu                  | İşlem hataları                |
| critical| Kritik durumlar              | Sistem bileşeni hataları      |
| alert   | Acilen işlem yapılmalı        | Veri bozulması tespit edildi |
| emergency| Sistem kullanılamaz durumda   | Tam sistem hatası             |

## MCP'de Bildirimleri Uygulama

Bildirimleri MCP'de uygulamak için hem sunucu hem de istemci taraflarını gerçek zamanlı güncellemeleri işleyebilecek şekilde hazırlamanız gerekir. Bu, uygulamanızın uzun işlemler sırasında kullanıcılara anında geri bildirim sunmasını sağlar.

### Sunucu tarafı: Bildirim Gönderme

Sunucu tarafından başlayalım. MCP'de, istekleri işlerken bildirim gönderebilen araçları tanımlarsınız. Sunucu, istemciye mesaj göndermek için genellikle `ctx` olan context nesnesini kullanır.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Önceki örnekte, `process_files` aracı her dosyayı işledikçe istemciye üç bildirim gönderir. `ctx.info()` metodu bilgilendirici mesajlar göndermek için kullanılır.

Ayrıca, bildirimlerin etkinleşmesi için sunucunuzun `streamable-http` gibi akışla taşıma kullanması ve istemcinizin bildirimleri işlemek için mesaj işleyicisi uygulaması gerekir. Sunucunun `streamable-http` taşımayı kullanması şöyle ayarlanabilir:

```python
mcp.run(transport="streamable-http")
```

#### .NET

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

Bu .NET örneğinde, `ProcessFiles` aracı her dosyayı işlerken istemciye üç bildirim gönderir. `ctx.Info()` metodu bilgilendirici mesajlar göndermek için kullanılır.

.NET MCP sunucunuzda bildirimleri etkinleştirmek için akış taşıma kullandığınızdan emin olun:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### İstemci tarafı: Bildirim Alma

İstemci, gelen bildirimleri işleyip görüntülemek için mesaj işleyicisi uygulamalıdır.

#### Python

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

Önceki kodda, `message_handler` fonksiyonu gelen mesajın bildirim olup olmadığını kontrol eder. Bildirimse yazdırılır, değilse normal sunucu mesajı olarak işlenir. Ayrıca `ClientSession` gelen bildirimleri işlemek üzere `message_handler` ile başlatılır.

#### .NET

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

Bu .NET örneğinde, `MessageHandler` fonksiyonu gelen mesajın bildirim olup olmadığını kontrol eder. Bildirimse yazdırılır, değilse normal sunucu mesajı olarak işlenir. `ClientSession`, mesaj işleyici ile `ClientSessionOptions` üzerinden başlatılır.

Bildirimleri etkinleştirmek için sunucunuzun `streamable-http` gibi akış taşıma kullandığından ve istemcinizin bildirimleri işleyebilecek mesaj işleyicisi uyguladığından emin olun.

## İlerleme Bildirimleri ve Senaryolar

Bu bölümde MCP'de ilerleme bildirimlerinin kavramı, önemi ve Streamable HTTP kullanarak nasıl uygulanacağı açıklanır. Ayrıca anlayışınızı pekiştirmek için pratik bir görev bulunur.

İlerleme bildirimleri, uzun süren işlemler boyunca sunucudan istemciye gönderilen gerçek zamanlı mesajlardır. Tüm işlemin bitmesini beklemek yerine, sunucu istemciyi mevcut durum hakkında güncel tutar. Bu şeffaflığı, kullanıcı deneyimini artırır ve hata ayıklamayı kolaylaştırır.

**Örnek:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Neden İlerleme Bildirimleri Kullanılır?

İlerleme bildirimleri birkaç sebepten gereklidir:

- **Daha iyi kullanıcı deneyimi:** Kullanıcılar iş ilerledikçe güncelleme görür, yalnızca sonunda değil.
- **Gerçek zamanlı geri bildirim:** İstemciler ilerleme çubuğu veya günlük gösterebilir, uygulama daha duyarlı hissedilir.
- **Daha kolay hata ayıklama ve izleme:** Geliştiriciler ve kullanıcılar işlemin nerede yavaşladığını veya takıldığını görebilir.

### İlerleme Bildirimleri Nasıl Uygulanır

MCP'de ilerleme bildirimleri şöyle uygulanabilir:

- **Sunucu tarafında:** Her öğe işlendiğinde `ctx.info()` veya `ctx.log()` kullanarak bildirim gönderilir. Bu, ana sonuç hazır olmadan istemciye mesaj gönderir.
- **İstemci tarafında:** Gelen bildirimleri dinleyip gösteren bir mesaj işleyici uygulanır. Bu işleyici bildirimler ile nihai sonuçları ayırt eder.

**Sunucu Örneği:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**İstemci Örneği:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Güvenlik Hususları

Herhangi bir sunucu uygulaması geliştirirken, özellikle MCP'de Streamable HTTP gibi HTTP tabanlı taşıyıcılar kullanıldığında güvenlik öncelikli olmalıdır.

HTTP tabanlı taşıyıcılarla MCP sunucuları uygularken, güvenlik çok sayıda saldırı vektörüne ve koruma mekanizmasına dikkat gerektiren en önemli husustur.

### Genel Bakış

MCP sunucularını HTTP üzerinden erişime açarken güvenlik kritik öneme sahiptir. Streamable HTTP yeni saldırı yüzeyleri oluşturur ve dikkatli yapılandırma gerektirir.

İşte bazı önemli güvenlik hususları:

- **Origin Başlığı Doğrulama**: DNS rebinding saldırılarını önlemek için `Origin` başlığını her zaman doğrulayın.
- **Localhost Bağlama**: Yerel geliştirme için, sunucuları `localhost`'a bağlayarak genel internete açılmasını engelleyin.
- **Kimlik Doğrulama**: Üretim dağıtımlarında kimlik doğrulamayı (ör. API anahtarları, OAuth) uygulayın.
- **CORS**: Erişimi kısıtlamak için Çapraz Kaynak Paylaşımı (CORS) politikalarını yapılandırın.
- **HTTPS**: Trafiği şifrelemek için üretimde HTTPS kullanın.

### En İyi Uygulamalar

Ayrıca, MCP akış sunucunuzda güvenliği sağlarken şu en iyi uygulamaları izleyin:

- Gelen istekleri doğrulamadan asla güvenmeyin.
- Tüm erişim ve hataları kaydedin ve izleyin.
- Güvenlik açıklarını gidermek için bağımlılıkları düzenli olarak güncelleyin.

### Zorluklar

MCP akış sunucularında güvenlik uygularken bazı zorluklarla karşılaşacaksınız:

- Güvenlik ile geliştirme kolaylığı arasında denge kurmak
- Çeşitli istemci ortamlarıyla uyumluluğu sağlamak


## SSE'den Streamable HTTP'ye Geçiş

Şu anda Server-Sent Events (SSE) kullanan uygulamalar için Streamable HTTP'ye geçiş, MCP uygulamalarınızda gelişmiş yetenekler ve daha iyi uzun vadeli sürdürülebilirlik sunar.

### Neden Yükseltmeli?

SSE'den Streamable HTTP'ye geçiş için iki önemli neden vardır:

- Streamable HTTP, SSE'ye göre daha iyi ölçeklenebilirlik, uyumluluk ve zengin bildirim desteği sunar.
- Yeni MCP uygulamaları için önerilen taşıyıcıdır.

### Geçiş Adımları

MCP uygulamalarınızda SSE'den Streamable HTTP'ye nasıl geçiş yapabileceğiniz aşağıda açıklanmıştır:

- **Sunucu kodunu güncelleyin**: `mcp.run()` içinde `transport="streamable-http"` kullanın.
- **İstemci kodunu güncelleyin**: SSE istemcisi yerine `streamablehttp_client` kullanın.
- **İstemcide bir mesaj işleyici uygulayın**: Bildirimleri işlemek için.
- **Mevcut araçlar ve iş akışlarıyla uyumluluğu test edin**.

### Uyumluluğun Sürdürülmesi

Geçiş sürecinde mevcut SSE istemcileriyle uyumluluğu sürdürmek önerilir. İşte bazı stratejiler:

- Farklı uç noktalarda hem SSE hem Streamable HTTP taşıyıcılarını çalıştırarak her ikisini destekleyebilirsiniz.
- İstemcileri kademeli olarak yeni taşıyıcıya geçirin.

### Zorluklar

Geçiş sırasında aşağıdaki zorluklara dikkat edin:

- Tüm istemcilerin güncellendiğinden emin olmak
- Bildirim iletimindeki farklılıkları yönetmek

### Ödev: Kendi MCP Akış Uygulamanızı Oluşturun

**Senaryo:**
Bir MCP sunucusu ve istemcisi oluşturun; sunucu bir öğe listesini (ör. dosyalar veya belgeler) işler ve işlenen her öğe için bir bildirim gönderir. İstemci ise her bildirimi varır varmaz görüntülemelidir.

**Adımlar:**

1. Bir listeyi işleyip her öğe için bildirim gönderen bir sunucu aracı uygulayın.
2. Bildirimleri gerçek zamanlı göstermek için mesaj işleyiciye sahip bir istemci uygulayın.
3. Hem sunucu hem istemciyi çalıştırarak uygulamanızı test edin ve bildirimleri gözlemleyin.

[Çözüm](./solution/README.md)

## Daha Fazla Okuma ve Sonrası

MCP akış ile yolculuğunuza devam etmek ve bilginizi genişletmek için bu bölüm, daha gelişmiş uygulamalar oluşturmanız adına ek kaynaklar ve önerilen sonraki adımları sunar.

### Daha Fazla Okuma

- [Microsoft: HTTP Akışa Giriş](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: ASP.NET Core'da CORS](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Akış İstekleri](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Sonraki Adımlar

- Gerçek zamanlı analiz, sohbet veya ortak düzenleme için akış kullanan daha gelişmiş MCP araçları geliştirmeyi deneyin.
- Canlı UI güncellemeleri için MCP akışını frontend frameworkleri (React, Vue vb.) ile entegre etmeyi keşfedin.
- Sonraki: [VSCode İçin AI Araç Seti Kullanımı](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->