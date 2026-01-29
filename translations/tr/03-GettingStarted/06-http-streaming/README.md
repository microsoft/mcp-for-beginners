# HTTPS Akışı ve Model Context Protocol (MCP)

Bu bölüm, HTTPS kullanarak Model Context Protocol (MCP) ile güvenli, ölçeklenebilir ve gerçek zamanlı akışın nasıl uygulanacağına dair kapsamlı bir rehber sunar. Akışın motivasyonunu, mevcut taşıma mekanizmalarını, MCP'de akışlı HTTP'nin nasıl uygulanacağını, güvenlik en iyi uygulamalarını, SSE'den geçişi ve kendi MCP akış uygulamalarınızı oluşturmak için pratik rehberliği kapsar.

## MCP'de Taşıma Mekanizmaları ve Akış

Bu bölüm, MCP'de mevcut taşıma mekanizmalarını ve bunların istemciler ile sunucular arasında gerçek zamanlı iletişim sağlama rolünü inceler.

### Taşıma Mekanizması Nedir?

Bir taşıma mekanizması, istemci ile sunucu arasında verilerin nasıl değiştirileceğini tanımlar. MCP, farklı ortamlar ve gereksinimlere uygun çeşitli taşıma türlerini destekler:

- **stdio**: Yerel ve CLI tabanlı araçlar için uygun olan standart giriş/çıkış. Basit ancak web veya bulut için uygun değil.
- **SSE (Sunucu Gönderimli Olaylar)**: Sunucuların HTTP üzerinden istemcilere gerçek zamanlı güncellemeler göndermesine olanak tanır. Web arayüzleri için iyi, ancak ölçeklenebilirlik ve esneklik açısından sınırlı.
- **Akışlı HTTP**: Bildirimleri destekleyen ve daha iyi ölçeklenebilirlik sağlayan modern HTTP tabanlı akış taşıması. Çoğu üretim ve bulut senaryosu için önerilir.

### Karşılaştırma Tablosu

Aşağıdaki karşılaştırma tablosuna göz atarak bu taşıma mekanizmaları arasındaki farkları anlayabilirsiniz:

| Taşıma           | Gerçek Zamanlı Güncellemeler | Akış     | Ölçeklenebilirlik | Kullanım Durumu          |
|-------------------|-----------------------------|----------|-------------------|--------------------------|
| stdio             | Hayır                       | Hayır    | Düşük             | Yerel CLI araçları       |
| SSE               | Evet                        | Evet     | Orta              | Web, gerçek zamanlı güncellemeler |
| Akışlı HTTP       | Evet                        | Evet     | Yüksek            | Bulut, çoklu istemci     |

> **İpucu:** Doğru taşıma seçimi performansı, ölçeklenebilirliği ve kullanıcı deneyimini etkiler. **Akışlı HTTP**, modern, ölçeklenebilir ve bulut uyumlu uygulamalar için önerilir.

Önceki bölümlerde gösterilen stdio ve SSE taşıma mekanizmalarını ve bu bölümde ele alınan akışlı HTTP taşımasını not edin.

## Akış: Kavramlar ve Motivasyon

Gerçek zamanlı iletişim sistemlerini etkili bir şekilde uygulamak için akışın temel kavramlarını ve motivasyonlarını anlamak önemlidir.

**Akış**, ağ programlamasında, tüm yanıtın hazır olmasını beklemek yerine verilerin küçük, yönetilebilir parçalar halinde veya bir olay dizisi olarak gönderilmesine ve alınmasına olanak tanıyan bir tekniktir. Bu özellikle şu durumlarda faydalıdır:

- Büyük dosyalar veya veri kümeleri.
- Gerçek zamanlı güncellemeler (ör. sohbet, ilerleme çubukları).
- Kullanıcıyı bilgilendirmek istediğiniz uzun süreli hesaplamalar.

Akış hakkında bilmeniz gerekenler:

- Veriler aşamalı olarak teslim edilir, hepsi bir kerede değil.
- İstemci, veriler geldikçe işleyebilir.
- Algılanan gecikmeyi azaltır ve kullanıcı deneyimini iyileştirir.

### Neden akış kullanılır?

Akış kullanmanın nedenleri şunlardır:

- Kullanıcılar hemen geri bildirim alır, sadece sonunda değil.
- Gerçek zamanlı uygulamalar ve duyarlı kullanıcı arayüzleri sağlar.
- Ağ ve işlem kaynaklarının daha verimli kullanımı.

### Basit Örnek: HTTP Akış Sunucusu ve İstemcisi

İşte akışın nasıl uygulanabileceğine dair basit bir örnek:

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

Bu örnek, sunucunun tüm mesajlar hazır olmadan önce istemciye bir dizi mesaj göndermesini gösterir.

**Nasıl çalışır:**

- Sunucu, her mesaj hazır olduğunda bir mesaj gönderir.
- İstemci, her parçayı geldikçe alır ve yazdırır.

**Gereksinimler:**

- Sunucu, bir akış yanıtı kullanmalıdır (ör. FastAPI'de `StreamingResponse`).
- İstemci, yanıtı bir akış olarak işlemelidir (`stream=True` requests içinde).
- Content-Type genellikle `text/event-stream` veya `application/octet-stream` olur.

#### Java

**Sunucu (Java, Spring Boot ve Sunucu Gönderimli Olaylar kullanarak):**

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

- `Flux` ile Spring Boot'un reaktif yığını kullanılır.
- `ServerSentEvent`, olay türleriyle yapılandırılmış olay akışı sağlar.
- `WebClient` ve `bodyToFlux()` reaktif akış tüketimini etkinleştirir.
- `delayElements()` olaylar arasındaki işlem süresini simüle eder.
- Olaylar, istemci işlemesi için türlere (`info`, `result`) sahip olabilir.

### Karşılaştırma: Klasik Akış vs MCP Akışı

Akışın "klasik" bir şekilde nasıl çalıştığı ile MCP'de nasıl çalıştığı arasındaki farklar şu şekilde gösterilebilir:

| Özellik              | Klasik HTTP Akışı            | MCP Akışı (Bildirimler)          |
|----------------------|------------------------------|----------------------------------|
| Ana yanıt            | Parçalı                     | Tek, sonunda                    |
| İlerleme güncellemeleri | Veri parçaları olarak gönderilir | Bildirimler olarak gönderilir   |
| İstemci gereksinimleri | Akışı işlemeli              | Mesaj işleyici uygulamalı       |
| Kullanım durumu       | Büyük dosyalar, AI token akışları | İlerleme, günlükler, gerçek zamanlı geri bildirim |

### Gözlemlenen Temel Farklar

Ek olarak, bazı temel farklar şunlardır:

- **İletişim Deseni:**
  - Klasik HTTP akışı: Verileri parçalı transfer kodlaması ile basitçe gönderir.
  - MCP akışı: JSON-RPC protokolü ile yapılandırılmış bir bildirim sistemi kullanır.

- **Mesaj Formatı:**
  - Klasik HTTP: Yeni satırlarla düz metin parçaları.
  - MCP: Meta verilerle yapılandırılmış LoggingMessageNotification nesneleri.

- **İstemci Uygulaması:**
  - Klasik HTTP: Akış yanıtlarını işleyen basit istemci.
  - MCP: Farklı türdeki mesajları işlemek için bir mesaj işleyiciye sahip daha sofistike istemci.

- **İlerleme Güncellemeleri:**
  - Klasik HTTP: İlerleme, ana yanıt akışının bir parçasıdır.
  - MCP: İlerleme, ana yanıtın sonunda gelirken ayrı bildirim mesajlarıyla gönderilir.

### Öneriler

Klasik akış (yukarıda gösterilen `/stream` uç noktası gibi) uygulamak ile MCP üzerinden akış seçmek arasında seçim yaparken bazı önerilerimiz var:

- **Basit akış ihtiyaçları için:** Klasik HTTP akışı, temel akış ihtiyaçları için daha basit ve yeterlidir.
- **Karmaşık, etkileşimli uygulamalar için:** MCP akışı, daha zengin meta veriler ve bildirimler ile nihai sonuçların ayrılması için daha yapılandırılmış bir yaklaşım sunar.
- **AI uygulamaları için:** MCP'nin bildirim sistemi, kullanıcıları ilerleme hakkında bilgilendirmek istediğiniz uzun süreli AI görevleri için özellikle kullanışlıdır.

## MCP'de Akış

Tamam, şimdiye kadar klasik akış ile MCP'deki akış arasındaki farklar ve öneriler gördünüz. Şimdi MCP'de akışı nasıl kullanabileceğinizi detaylı bir şekilde inceleyelim.

MCP çerçevesinde akışın nasıl çalıştığını anlamak, uzun süreli işlemler sırasında kullanıcılara gerçek zamanlı geri bildirim sağlayan duyarlı uygulamalar oluşturmak için önemlidir.

MCP'de akış, ana yanıtı parçalara ayırmakla ilgili değil, işlem sırasında istemciye **bildirimler** göndermekle ilgilidir. Bu bildirimler ilerleme güncellemeleri, günlükler veya diğer olayları içerebilir.

### Nasıl çalışır?

Ana sonuç hala tek bir yanıt olarak gönderilir. Ancak, bildirimler işlem sırasında ayrı mesajlar olarak gönderilebilir ve böylece istemciyi gerçek zamanlı olarak güncelleyebilir. İstemci, bu bildirimleri işleyip görüntüleyebilmelidir.

## Bildirim Nedir?

"Bildirim" dedik, MCP bağlamında bu ne anlama geliyor?

Bildirim, uzun süreli bir işlem sırasında ilerleme, durum veya diğer olaylar hakkında istemciyi bilgilendirmek için sunucudan istemciye gönderilen bir mesajdır. Bildirimler, şeffaflığı ve kullanıcı deneyimini artırır.

Örneğin, istemci, sunucu ile ilk el sıkışma yapıldıktan sonra bir bildirim göndermelidir.

Bir bildirim şu şekilde bir JSON mesajı olarak görünür:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Bildirimler MCP'de ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging) olarak adlandırılan bir konuya aittir.

Günlük kaydını çalıştırmak için sunucunun bunu bir özellik/yetenek olarak etkinleştirmesi gerekir:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Kullanılan SDK'ya bağlı olarak, günlük kaydı varsayılan olarak etkinleştirilmiş olabilir veya sunucu yapılandırmanızda bunu açıkça etkinleştirmeniz gerekebilir.

Farklı bildirim türleri vardır:

| Seviye     | Açıklama                     | Örnek Kullanım Durumu           |
|------------|------------------------------|----------------------------------|
| debug      | Ayrıntılı hata ayıklama bilgileri | Fonksiyon giriş/çıkış noktaları |
| info       | Genel bilgilendirme mesajları | İşlem ilerleme güncellemeleri   |
| notice     | Normal ancak önemli olaylar  | Yapılandırma değişiklikleri     |
| warning    | Uyarı koşulları              | Kullanımdan kaldırılmış özellik |
| error      | Hata koşulları               | İşlem hataları                  |
| critical   | Kritik koşullar              | Sistem bileşeni hataları        |
| alert      | Hemen harekete geçilmeli     | Veri bozulması tespit edildi    |
| emergency  | Sistem kullanılamaz durumda | Tam sistem arızası              |

## MCP'de Bildirimlerin Uygulanması

MCP'de bildirimleri uygulamak için hem sunucu hem de istemci tarafını gerçek zamanlı güncellemeleri işleyebilecek şekilde ayarlamanız gerekir. Bu, uygulamanızın uzun süreli işlemler sırasında kullanıcılara anında geri bildirim sağlamasına olanak tanır.

### Sunucu Tarafı: Bildirim Gönderme

Öncelikle sunucu tarafıyla başlayalım. MCP'de, istekleri işlerken bildirimler gönderebilen araçlar tanımlarsınız. Sunucu, istemciye mesaj göndermek için bağlam nesnesini (genellikle `ctx`) kullanır.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Yukarıdaki örnekte, `process_files` aracı her dosyayı işlerken istemciye üç bildirim gönderir. `ctx.info()` yöntemi, bilgilendirme mesajları göndermek için kullanılır.

Ek olarak, bildirimleri etkinleştirmek için sunucunuzun bir akış taşıması (ör. `streamable-http`) kullanması ve istemcinizin bildirimleri işlemek için bir mesaj işleyici uygulaması gerekir. İşte sunucuyu `streamable-http` taşımasını kullanacak şekilde ayarlamanın yolu:

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

Bu .NET örneğinde, `ProcessFiles` aracı `Tool` özniteliği ile süslenmiştir ve her dosyayı işlerken istemciye üç bildirim gönderir. `ctx.Info()` yöntemi, bilgilendirme mesajları göndermek için kullanılır.

.NET MCP sunucunuzda bildirimleri etkinleştirmek için bir akış taşıması kullandığınızdan emin olun:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### İstemci Tarafı: Bildirim Alma

İstemci, gelen bildirimleri işlemek ve görüntülemek için bir mesaj işleyici uygulamalıdır.

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

Yukarıdaki kodda, `message_handler` işlevi gelen mesajın bir bildirim olup olmadığını kontrol eder. Eğer öyleyse, bildirimi yazdırır; değilse, bunu normal bir sunucu mesajı olarak işler. Ayrıca, `ClientSession` gelen bildirimleri işlemek için `message_handler` ile başlatılır.

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

Bu .NET örneğinde, `MessageHandler` işlevi gelen mesajın bir bildirim olup olmadığını kontrol eder. Eğer öyleyse, bildirimi yazdırır; değilse, bunu normal bir sunucu mesajı olarak işler. `ClientSession`, `ClientSessionOptions` aracılığıyla mesaj işleyici ile başlatılır.

Bildirimleri etkinleştirmek için sunucunuzun bir akış taşıması (ör. `streamable-http`) kullandığından ve istemcinizin bildirimleri işlemek için bir mesaj işleyici uyguladığından emin olun.

## İlerleme Bildirimleri ve Senaryolar

Bu bölüm, MCP'deki ilerleme bildirimleri kavramını, neden önemli olduklarını ve Streamable HTTP kullanarak nasıl uygulanacaklarını açıklar. Ayrıca, anlayışınızı pekiştirmek için pratik bir görev bulacaksınız.

İlerleme bildirimleri, uzun süreli işlemler sırasında sunucudan istemciye gönderilen gerçek zamanlı mesajlardır. Tüm işlem bitene kadar beklemek yerine, sunucu istemciyi mevcut durum hakkında güncel tutar. Bu, şeffaflığı artırır, kullanıcı deneyimini iyileştirir ve hata ayıklamayı kolaylaştırır.

**Örnek:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Neden İlerleme Bildirimleri Kullanılır?

İlerleme bildirimleri birkaç nedenle önemlidir:

- **Daha iyi kullanıcı deneyimi:** Kullanıcılar, iş ilerledikçe güncellemeleri görür, sadece sonunda değil.
- **Gerçek zamanlı geri bildirim:** İstemciler ilerleme çubukları veya günlükler görüntüleyebilir, uygulamayı duyarlı hale getirir.
- **Daha kolay hata ayıklama ve izleme:** Geliştiriciler ve kullanıcılar bir işlemin yavaş veya takılıp kaldığı yeri görebilir.

### İlerleme Bildirimleri Nasıl Uygulanır?

İşte MCP'de ilerleme bildirimlerini nasıl uygulayabileceğiniz:

- **Sunucuda:** Her öğe işlendiğinde bildirim göndermek için `ctx.info()` veya `ctx.log()` kullanın. Bu, ana sonuç hazır olmadan önce istemciye bir mesaj gönderir.
- **İstemcide:** Gelen bildirimleri dinleyen ve görüntüleyen bir mesaj işleyici uygulayın. Bu işleyici, bildirimler ile nihai sonucu ayırt eder.

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

HTTP tabanlı taşıma mekanizmalarıyla MCP sunucuları uygularken, güvenlik birinci derecede önemli bir konu haline gelir ve birden fazla saldırı vektörüne karşı koruma mekanizmaları gerektirir.

### Genel Bakış

MCP sunucularını HTTP üzerinden açarken güvenlik kritik öneme sahiptir. Akışlı HTTP, yeni saldırı yüzeyleri sunar ve dikkatli yapılandırma gerektirir.

### Temel Noktalar

- **Origin Başlığı Doğrulaması**: DNS yeniden bağlama saldırılarını önlemek için her zaman `Origin` başlığını doğrulayın.
- **Yerel Sunucu Bağlama**: Yerel geliştirme için sunucuları `localhost`a bağlayarak genel internete maruz bırakmayın.
- **Kimlik Doğrulama**: Üretim dağıtımları için kimlik doğrulama (ör. API anahtarları, OAuth) uygulayın.
- **CORS**: Erişimi kısıtlamak için Çapraz Kaynak Paylaşımı (CORS) politikalarını yapılandırın.
- **HTTPS**: Trafiği şifrelemek için üretimde HTTPS kullanın.

### En İyi Uygulamalar

- Gelen istekleri doğrulamadan asla güvenmeyin.
- Tüm erişim ve hataları kaydedin ve izleyin.
- Güvenlik açıklarını yamalamak için düzenli olarak bağımlılıkları güncelleyin.

### Zorluklar

- Geliştirme kolaylığı ile güvenlik arasında denge kurmak.
- Çeşitli istemci ortamlarıyla uyumluluğu sağlamak.

## SSE'den Akışlı HTTP'ye Geçiş

Sunucu Gönderimli Olaylar (SSE) kullanan uygulamalar için, Streamable HTTP'ye geçiş, MCP uygulamalarınız için gelişmiş yetenekler ve daha iyi uzun vadeli sürdürülebilirlik sağlar.

### Neden Yükseltmeli?
SSE'den Streamable HTTP'ye geçiş yapmanız için iki güçlü neden vardır:

- Streamable HTTP, SSE'ye kıyasla daha iyi ölçeklenebilirlik, uyumluluk ve daha zengin bildirim desteği sunar.
- Yeni MCP uygulamaları için önerilen taşıma yöntemidir.

### Geçiş Adımları

MCP uygulamalarınızda SSE'den Streamable HTTP'ye geçiş yapmak için şu adımları izleyin:

- **Sunucu kodunu güncelleyin** ve `mcp.run()` içinde `transport="streamable-http"` kullanın.
- **İstemci kodunu güncelleyin** ve SSE istemcisi yerine `streamablehttp_client` kullanın.
- **Bir mesaj işleyici uygulayın** ve istemcide bildirimleri işleyin.
- **Mevcut araçlar ve iş akışlarıyla uyumluluğu test edin.**

### Uyumluluğu Korumak

Geçiş sürecinde mevcut SSE istemcileriyle uyumluluğu korumanız önerilir. İşte bazı stratejiler:

- Farklı uç noktalarda hem SSE hem de Streamable HTTP'yi destekleyebilirsiniz.
- İstemcileri yeni taşıma yöntemine kademeli olarak geçirin.

### Zorluklar

Geçiş sırasında şu zorlukları ele aldığınızdan emin olun:

- Tüm istemcilerin güncellendiğinden emin olmak
- Bildirim teslimatındaki farklılıkları yönetmek

## Güvenlik Hususları

HTTP tabanlı taşıma yöntemleri (örneğin, Streamable HTTP) kullanırken güvenlik en öncelikli konu olmalıdır. MCP sunucuları uygularken, çeşitli saldırı vektörlerine karşı dikkatli olunmalı ve koruma mekanizmaları uygulanmalıdır.

### Genel Bakış

MCP sunucularını HTTP üzerinden açarken güvenlik kritik bir öneme sahiptir. Streamable HTTP, yeni saldırı yüzeyleri sunar ve dikkatli bir yapılandırma gerektirir.

İşte bazı önemli güvenlik hususları:

- **Origin Başlığı Doğrulaması**: DNS yeniden bağlama saldırılarını önlemek için her zaman `Origin` başlığını doğrulayın.
- **Localhost Bağlantısı**: Yerel geliştirme için sunucuları `localhost`a bağlayarak genel internete maruz kalmalarını önleyin.
- **Kimlik Doğrulama**: Üretim ortamlarında API anahtarları veya OAuth gibi kimlik doğrulama yöntemlerini uygulayın.
- **CORS**: Erişimi kısıtlamak için Cross-Origin Resource Sharing (CORS) politikalarını yapılandırın.
- **HTTPS**: Trafiği şifrelemek için üretim ortamında HTTPS kullanın.

### En İyi Uygulamalar

MCP akış sunucunuzda güvenliği sağlarken şu en iyi uygulamaları takip edin:

- Gelen istekleri doğrulamadan asla güvenmeyin.
- Tüm erişim ve hataları kaydedin ve izleyin.
- Güvenlik açıklarını gidermek için bağımlılıkları düzenli olarak güncelleyin.

### Zorluklar

MCP akış sunucularında güvenlik uygularken karşılaşabileceğiniz bazı zorluklar:

- Güvenlik ile geliştirme kolaylığı arasında denge kurmak
- Çeşitli istemci ortamlarıyla uyumluluğu sağlamak

### Görev: Kendi Akış MCP Uygulamanızı Oluşturun

**Senaryo:**
Bir MCP sunucusu ve istemcisi oluşturun. Sunucu, bir öğe listesini (örneğin, dosyalar veya belgeler) işler ve işlenen her öğe için bir bildirim gönderir. İstemci, her bildirimi geldiği anda görüntülemelidir.

**Adımlar:**

1. Bir listeyi işleyen ve her öğe için bildirim gönderen bir sunucu aracı uygulayın.
2. Bildirimleri gerçek zamanlı olarak görüntülemek için bir mesaj işleyici içeren bir istemci uygulayın.
3. Hem sunucuyu hem de istemciyi çalıştırarak uygulamanızı test edin ve bildirimleri gözlemleyin.

[Çözüm](./solution/README.md)

## Daha Fazla Okuma ve Sırada Ne Var?

MCP akışıyla yolculuğunuza devam etmek ve bilginizi genişletmek için bu bölüm, daha fazla kaynak ve daha gelişmiş uygulamalar oluşturmak için önerilen sonraki adımları sunar.

### Daha Fazla Okuma

- [Microsoft: HTTP Akışına Giriş](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: ASP.NET Core'da CORS](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Akış Talepleri](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Sırada Ne Var?

- Gerçek zamanlı analiz, sohbet veya işbirlikçi düzenleme için akış kullanan daha gelişmiş MCP araçları oluşturmayı deneyin.
- Canlı kullanıcı arayüzü güncellemeleri için MCP akışını frontend çerçeveleri (React, Vue, vb.) ile entegre etmeyi keşfedin.
- Sıradaki konu: [VSCode için AI Araç Setini Kullanma](../07-aitk/README.md)

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.