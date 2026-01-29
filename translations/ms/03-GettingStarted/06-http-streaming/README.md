# Penstriman HTTPS dengan Protokol Model Context (MCP)

Bab ini menyediakan panduan menyeluruh untuk melaksanakan penstriman yang selamat, boleh diskala, dan masa nyata menggunakan Protokol Model Context (MCP) dengan HTTPS. Ia merangkumi motivasi untuk penstriman, mekanisme pengangkutan yang tersedia, cara melaksanakan HTTP boleh distrim dalam MCP, amalan terbaik keselamatan, migrasi daripada SSE, dan panduan praktikal untuk membina aplikasi MCP penstriman anda sendiri.

## Mekanisme Pengangkutan dan Penstriman dalam MCP

Bahagian ini meneroka pelbagai mekanisme pengangkutan yang tersedia dalam MCP dan peranannya dalam membolehkan keupayaan penstriman untuk komunikasi masa nyata antara klien dan pelayan.

### Apakah Mekanisme Pengangkutan?

Mekanisme pengangkutan menentukan cara data ditukar antara klien dan pelayan. MCP menyokong pelbagai jenis pengangkutan untuk memenuhi keperluan dan persekitaran yang berbeza:

- **stdio**: Input/output standard, sesuai untuk alat tempatan dan berasaskan CLI. Mudah tetapi tidak sesuai untuk web atau awan.
- **SSE (Server-Sent Events)**: Membolehkan pelayan menghantar kemas kini masa nyata kepada klien melalui HTTP. Baik untuk UI web, tetapi terhad dari segi skalabiliti dan fleksibiliti.
- **HTTP boleh distrim**: Pengangkutan penstriman moden berasaskan HTTP, menyokong pemberitahuan dan skalabiliti yang lebih baik. Disyorkan untuk kebanyakan senario pengeluaran dan awan.

### Jadual Perbandingan

Lihat jadual perbandingan di bawah untuk memahami perbezaan antara mekanisme pengangkutan ini:

| Pengangkutan       | Kemas Kini Masa Nyata | Penstriman | Skalabiliti | Kes Penggunaan           |
|--------------------|-----------------------|------------|-------------|--------------------------|
| stdio              | Tidak                | Tidak      | Rendah      | Alat CLI tempatan        |
| SSE                | Ya                   | Ya         | Sederhana   | Web, kemas kini masa nyata |
| HTTP boleh distrim | Ya                   | Ya         | Tinggi      | Awan, pelbagai klien     |

> **Tip:** Memilih pengangkutan yang betul memberi kesan kepada prestasi, skalabiliti, dan pengalaman pengguna. **HTTP boleh distrim** disyorkan untuk aplikasi moden, boleh diskala, dan bersedia untuk awan.

Perhatikan pengangkutan stdio dan SSE yang telah anda pelajari dalam bab sebelumnya dan bagaimana HTTP boleh distrim adalah pengangkutan yang dibincangkan dalam bab ini.

## Penstriman: Konsep dan Motivasi

Memahami konsep asas dan motivasi di sebalik penstriman adalah penting untuk melaksanakan sistem komunikasi masa nyata yang berkesan.

**Penstriman** adalah teknik dalam pengaturcaraan rangkaian yang membolehkan data dihantar dan diterima dalam bahagian kecil yang boleh diurus atau sebagai urutan peristiwa, bukannya menunggu keseluruhan respons sedia. Ini amat berguna untuk:

- Fail atau set data yang besar.
- Kemas kini masa nyata (contohnya, sembang, bar kemajuan).
- Pengiraan jangka panjang di mana anda ingin memastikan pengguna dimaklumkan.

Berikut adalah perkara yang perlu anda ketahui tentang penstriman pada tahap tinggi:

- Data dihantar secara progresif, bukan sekaligus.
- Klien boleh memproses data sebaik sahaja ia tiba.
- Mengurangkan latensi yang dirasakan dan meningkatkan pengalaman pengguna.

### Mengapa menggunakan penstriman?

Sebab-sebab menggunakan penstriman adalah seperti berikut:

- Pengguna mendapat maklum balas serta-merta, bukan hanya pada penghujungnya.
- Membolehkan aplikasi masa nyata dan UI yang responsif.
- Penggunaan sumber rangkaian dan pengiraan yang lebih cekap.

### Contoh Mudah: Pelayan & Klien Penstriman HTTP

Berikut adalah contoh mudah bagaimana penstriman boleh dilaksanakan:

#### Python

**Pelayan (Python, menggunakan FastAPI dan StreamingResponse):**

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

**Klien (Python, menggunakan requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Contoh ini menunjukkan pelayan menghantar siri mesej kepada klien apabila ia tersedia, bukannya menunggu semua mesej sedia.

**Bagaimana ia berfungsi:**

- Pelayan menghasilkan setiap mesej apabila ia sedia.
- Klien menerima dan mencetak setiap bahagian apabila ia tiba.

**Keperluan:**

- Pelayan mesti menggunakan respons penstriman (contohnya, `StreamingResponse` dalam FastAPI).
- Klien mesti memproses respons sebagai aliran (`stream=True` dalam requests).
- Content-Type biasanya `text/event-stream` atau `application/octet-stream`.

#### Java

**Pelayan (Java, menggunakan Spring Boot dan Server-Sent Events):**

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

**Klien (Java, menggunakan Spring WebFlux WebClient):**

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

**Nota Pelaksanaan Java:**

- Menggunakan tumpukan reaktif Spring Boot dengan `Flux` untuk penstriman.
- `ServerSentEvent` menyediakan penstriman acara berstruktur dengan jenis acara.
- `WebClient` dengan `bodyToFlux()` membolehkan penggunaan penstriman reaktif.
- `delayElements()` mensimulasikan masa pemprosesan antara acara.
- Acara boleh mempunyai jenis (`info`, `result`) untuk pengendalian klien yang lebih baik.

### Perbandingan: Penstriman Klasik vs Penstriman MCP

Perbezaan antara cara penstriman berfungsi secara "klasik" berbanding cara ia berfungsi dalam MCP boleh digambarkan seperti berikut:

| Ciri                 | Penstriman HTTP Klasik         | Penstriman MCP (Pemberitahuan)      |
|----------------------|--------------------------------|-------------------------------------|
| Respons utama        | Berpecah                      | Tunggal, pada penghujungnya         |
| Kemas kini kemajuan  | Dihantar sebagai bahagian data | Dihantar sebagai pemberitahuan      |
| Keperluan klien      | Mesti memproses aliran         | Mesti melaksanakan pengendali mesej |
| Kes penggunaan       | Fail besar, aliran token AI    | Kemajuan, log, maklum balas masa nyata |

### Perbezaan Utama yang Diperhatikan

Selain itu, berikut adalah beberapa perbezaan utama:

- **Corak Komunikasi:**
  - Penstriman HTTP klasik: Menggunakan pengekodan pemindahan berpecah mudah untuk menghantar data dalam bahagian.
  - Penstriman MCP: Menggunakan sistem pemberitahuan berstruktur dengan protokol JSON-RPC.

- **Format Mesej:**
  - HTTP klasik: Bahagian teks biasa dengan baris baru.
  - MCP: Objek LoggingMessageNotification berstruktur dengan metadata.

- **Pelaksanaan Klien:**
  - HTTP klasik: Klien mudah yang memproses respons penstriman.
  - MCP: Klien yang lebih canggih dengan pengendali mesej untuk memproses pelbagai jenis mesej.

- **Kemas Kini Kemajuan:**
  - HTTP klasik: Kemajuan adalah sebahagian daripada aliran respons utama.
  - MCP: Kemajuan dihantar melalui mesej pemberitahuan berasingan sementara respons utama datang pada penghujungnya.

### Cadangan

Terdapat beberapa perkara yang kami cadangkan apabila memilih antara melaksanakan penstriman klasik (sebagai titik akhir yang kami tunjukkan kepada anda di atas menggunakan `/stream`) berbanding memilih penstriman melalui MCP.

- **Untuk keperluan penstriman mudah:** Penstriman HTTP klasik lebih mudah dilaksanakan dan mencukupi untuk keperluan penstriman asas.
- **Untuk aplikasi interaktif yang kompleks:** Penstriman MCP menyediakan pendekatan yang lebih berstruktur dengan metadata yang lebih kaya dan pemisahan antara pemberitahuan dan hasil akhir.
- **Untuk aplikasi AI:** Sistem pemberitahuan MCP amat berguna untuk tugas AI jangka panjang di mana anda ingin memastikan pengguna dimaklumkan tentang kemajuan.

## Penstriman dalam MCP

Baiklah, anda telah melihat beberapa cadangan dan perbandingan setakat ini mengenai perbezaan antara penstriman klasik dan penstriman dalam MCP. Mari kita perincikan bagaimana anda boleh memanfaatkan penstriman dalam MCP.

Memahami bagaimana penstriman berfungsi dalam rangka kerja MCP adalah penting untuk membina aplikasi responsif yang memberikan maklum balas masa nyata kepada pengguna semasa operasi jangka panjang.

Dalam MCP, penstriman bukan tentang menghantar respons utama dalam bahagian, tetapi tentang menghantar **pemberitahuan** kepada klien semasa alat sedang memproses permintaan. Pemberitahuan ini boleh merangkumi kemas kini kemajuan, log, atau peristiwa lain.

### Bagaimana ia berfungsi

Hasil utama masih dihantar sebagai satu respons tunggal. Walau bagaimanapun, pemberitahuan boleh dihantar sebagai mesej berasingan semasa pemprosesan dan dengan itu mengemas kini klien dalam masa nyata. Klien mesti dapat mengendalikan dan memaparkan pemberitahuan ini.

## Apakah itu Pemberitahuan?

Kami menyebut "Pemberitahuan", apakah maksudnya dalam konteks MCP?

Pemberitahuan ialah mesej yang dihantar dari pelayan kepada klien untuk memaklumkan tentang kemajuan, status, atau peristiwa lain semasa operasi jangka panjang. Pemberitahuan meningkatkan ketelusan dan pengalaman pengguna.

Sebagai contoh, klien sepatutnya menghantar pemberitahuan sebaik sahaja jabat tangan awal dengan pelayan dibuat.

Pemberitahuan kelihatan seperti mesej JSON berikut:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Pemberitahuan tergolong dalam topik dalam MCP yang dirujuk sebagai ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Untuk membolehkan log berfungsi, pelayan perlu mengaktifkannya sebagai ciri/keupayaan seperti berikut:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Bergantung pada SDK yang digunakan, log mungkin diaktifkan secara lalai, atau anda mungkin perlu mengaktifkannya secara eksplisit dalam konfigurasi pelayan anda.

Terdapat pelbagai jenis pemberitahuan:

| Tahap     | Penerangan                     | Kes Penggunaan Contoh           |
|-----------|--------------------------------|----------------------------------|
| debug     | Maklumat penyahpepijatan terperinci | Titik masuk/keluar fungsi       |
| info      | Mesej maklumat umum            | Kemas kini kemajuan operasi     |
| notice    | Peristiwa biasa tetapi penting | Perubahan konfigurasi           |
| warning   | Keadaan amaran                 | Penggunaan ciri usang           |
| error     | Keadaan ralat                  | Kegagalan operasi               |
| critical  | Keadaan kritikal               | Kegagalan komponen sistem       |
| alert     | Tindakan mesti diambil segera | Pengesanan kerosakan data       |
| emergency | Sistem tidak boleh digunakan   | Kegagalan sistem sepenuhnya     |

## Melaksanakan Pemberitahuan dalam MCP

Untuk melaksanakan pemberitahuan dalam MCP, anda perlu menyediakan kedua-dua bahagian pelayan dan klien untuk mengendalikan kemas kini masa nyata. Ini membolehkan aplikasi anda memberikan maklum balas segera kepada pengguna semasa operasi jangka panjang.

### Bahagian Pelayan: Menghantar Pemberitahuan

Mari kita mulakan dengan bahagian pelayan. Dalam MCP, anda mentakrifkan alat yang boleh menghantar pemberitahuan semasa memproses permintaan. Pelayan menggunakan objek konteks (biasanya `ctx`) untuk menghantar mesej kepada klien.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Dalam contoh di atas, alat `process_files` menghantar tiga pemberitahuan kepada klien semasa ia memproses setiap fail. Kaedah `ctx.info()` digunakan untuk menghantar mesej maklumat.

Selain itu, untuk membolehkan pemberitahuan, pastikan pelayan anda menggunakan pengangkutan penstriman (seperti `streamable-http`) dan klien anda melaksanakan pengendali mesej untuk memproses pemberitahuan. Berikut adalah cara anda boleh menyediakan pelayan untuk menggunakan pengangkutan `streamable-http`:

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

Dalam contoh .NET ini, alat `ProcessFiles` dihiasi dengan atribut `Tool` dan menghantar tiga pemberitahuan kepada klien semasa ia memproses setiap fail. Kaedah `ctx.Info()` digunakan untuk menghantar mesej maklumat.

Untuk membolehkan pemberitahuan dalam pelayan MCP .NET anda, pastikan anda menggunakan pengangkutan penstriman:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Bahagian Klien: Menerima Pemberitahuan

Klien mesti melaksanakan pengendali mesej untuk memproses dan memaparkan pemberitahuan apabila ia tiba.

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

Dalam kod di atas, fungsi `message_handler` memeriksa sama ada mesej yang masuk adalah pemberitahuan. Jika ya, ia mencetak pemberitahuan; jika tidak, ia memprosesnya sebagai mesej pelayan biasa. Perhatikan juga bagaimana `ClientSession` dimulakan dengan `message_handler` untuk mengendalikan pemberitahuan yang masuk.

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

Dalam contoh .NET ini, fungsi `MessageHandler` memeriksa sama ada mesej yang masuk adalah pemberitahuan. Jika ya, ia mencetak pemberitahuan; jika tidak, ia memprosesnya sebagai mesej pelayan biasa. `ClientSession` dimulakan dengan pengendali mesej melalui `ClientSessionOptions`.

Untuk membolehkan pemberitahuan, pastikan pelayan anda menggunakan pengangkutan penstriman (seperti `streamable-http`) dan klien anda melaksanakan pengendali mesej untuk memproses pemberitahuan.

## Pemberitahuan Kemajuan & Senario

Bahagian ini menerangkan konsep pemberitahuan kemajuan dalam MCP, mengapa ia penting, dan cara melaksanakannya menggunakan HTTP boleh distrim. Anda juga akan menemui tugasan praktikal untuk memperkukuh pemahaman anda.

Pemberitahuan kemajuan ialah mesej masa nyata yang dihantar dari pelayan kepada klien semasa operasi jangka panjang. Daripada menunggu keseluruhan proses selesai, pelayan terus mengemas kini klien tentang status semasa. Ini meningkatkan ketelusan, pengalaman pengguna, dan memudahkan penyahpepijatan.

**Contoh:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Mengapa Menggunakan Pemberitahuan Kemajuan?

Pemberitahuan kemajuan penting atas beberapa sebab:

- **Pengalaman pengguna yang lebih baik:** Pengguna melihat kemas kini semasa kerja berlangsung, bukan hanya pada penghujungnya.
- **Maklum balas masa nyata:** Klien boleh memaparkan bar kemajuan atau log, menjadikan aplikasi terasa responsif.
- **Penyahpepijatan dan pemantauan yang lebih mudah:** Pembangun dan pengguna boleh melihat di mana proses mungkin perlahan atau tersekat.

### Cara Melaksanakan Pemberitahuan Kemajuan

Berikut adalah cara anda boleh melaksanakan pemberitahuan kemajuan dalam MCP:

- **Pada pelayan:** Gunakan `ctx.info()` atau `ctx.log()` untuk menghantar pemberitahuan semasa setiap item diproses. Ini menghantar mesej kepada klien sebelum hasil utama sedia.
- **Pada klien:** Laksanakan pengendali mesej yang mendengar dan memaparkan pemberitahuan apabila ia tiba. Pengendali ini membezakan antara pemberitahuan dan hasil akhir.

**Contoh Pelayan:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Contoh Klien:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Pertimbangan Keselamatan

Apabila melaksanakan pelayan MCP dengan pengangkutan berasaskan HTTP, keselamatan menjadi keutamaan yang memerlukan perhatian teliti terhadap pelbagai vektor serangan dan mekanisme perlindungan.

### Gambaran Keseluruhan

Keselamatan adalah kritikal apabila mendedahkan pelayan MCP melalui HTTP. HTTP boleh distrim memperkenalkan permukaan serangan baharu dan memerlukan konfigurasi yang teliti.

### Perkara Utama

- **Pengesahan Header Origin**: Sentiasa sahkan header `Origin` untuk mengelakkan serangan pengikatan semula DNS.
- **Pengikatan Localhost**: Untuk pembangunan tempatan, ikat pelayan kepada `localhost` untuk mengelakkan pendedahan kepada internet awam.
- **Pengesahan**: Laksanakan pengesahan (contohnya, kunci API, OAuth) untuk penggunaan pengeluaran.
- **CORS**: Konfigurasikan dasar Perkongsian Sumber Asal Silang (CORS) untuk mengehadkan akses.
- **HTTPS**: Gunakan HTTPS dalam pengeluaran untuk menyulitkan trafik.

### Amalan Terbaik

- Jangan sekali-kali mempercayai permintaan masuk tanpa pengesahan.
- Log dan pantau semua akses dan ralat.
- Kemas kini kebergantungan secara berkala untuk menampal kerentanan keselamatan.

### Cabaran

- Mengimbangi keselamatan dengan kemudahan pembangunan.
- Memastikan keserasian dengan pelbagai persekitaran klien.

## Meningkat Taraf dari SSE ke HTTP Boleh Distrim

Untuk aplikasi yang kini menggunakan Server-Sent Events (SSE), migrasi ke HTTP boleh distrim menyediakan keupayaan yang dipertingkatkan dan kemampanan jangka panjang yang lebih baik untuk pelaksanaan MCP anda.

### Mengapa Meningkat Taraf?
Terdapat dua sebab utama untuk menaik taraf daripada SSE kepada Streamable HTTP:

- Streamable HTTP menawarkan skalabiliti yang lebih baik, keserasian yang lebih luas, dan sokongan pemberitahuan yang lebih kaya berbanding SSE.
- Ia adalah pengangkutan yang disyorkan untuk aplikasi MCP baharu.

### Langkah Migrasi

Berikut adalah cara anda boleh bermigrasi daripada SSE kepada Streamable HTTP dalam aplikasi MCP anda:

- **Kemas kini kod pelayan** untuk menggunakan `transport="streamable-http"` dalam `mcp.run()`.
- **Kemas kini kod klien** untuk menggunakan `streamablehttp_client` sebagai ganti klien SSE.
- **Laksanakan pengendali mesej** dalam klien untuk memproses pemberitahuan.
- **Uji keserasian** dengan alat dan aliran kerja sedia ada.

### Mengekalkan Keserasian

Adalah disyorkan untuk mengekalkan keserasian dengan klien SSE sedia ada semasa proses migrasi. Berikut adalah beberapa strategi:

- Anda boleh menyokong kedua-dua SSE dan Streamable HTTP dengan menjalankan kedua-dua pengangkutan pada titik akhir yang berbeza.
- Migrasikan klien secara beransur-ansur kepada pengangkutan baharu.

### Cabaran

Pastikan anda menangani cabaran berikut semasa migrasi:

- Memastikan semua klien dikemas kini
- Menangani perbezaan dalam penghantaran pemberitahuan

## Pertimbangan Keselamatan

Keselamatan harus menjadi keutamaan utama apabila melaksanakan mana-mana pelayan, terutamanya apabila menggunakan pengangkutan berasaskan HTTP seperti Streamable HTTP dalam MCP.

Apabila melaksanakan pelayan MCP dengan pengangkutan berasaskan HTTP, keselamatan menjadi kebimbangan utama yang memerlukan perhatian teliti terhadap pelbagai vektor serangan dan mekanisme perlindungan.

### Gambaran Keseluruhan

Keselamatan adalah kritikal apabila mendedahkan pelayan MCP melalui HTTP. Streamable HTTP memperkenalkan permukaan serangan baharu dan memerlukan konfigurasi yang teliti.

Berikut adalah beberapa pertimbangan keselamatan utama:

- **Pengesahan Header Origin**: Sentiasa sahkan header `Origin` untuk mengelakkan serangan DNS rebinding.
- **Pengikatan Localhost**: Untuk pembangunan tempatan, ikat pelayan kepada `localhost` untuk mengelakkan pendedahan kepada internet awam.
- **Pengesahan**: Laksanakan pengesahan (contohnya, kunci API, OAuth) untuk penyebaran produksi.
- **CORS**: Konfigurasikan dasar Cross-Origin Resource Sharing (CORS) untuk mengehadkan akses.
- **HTTPS**: Gunakan HTTPS dalam produksi untuk menyulitkan trafik.

### Amalan Terbaik

Selain itu, berikut adalah beberapa amalan terbaik yang perlu diikuti semasa melaksanakan keselamatan dalam pelayan penstriman MCP anda:

- Jangan sekali-kali mempercayai permintaan masuk tanpa pengesahan.
- Log dan pantau semua akses dan ralat.
- Kemas kini kebergantungan secara berkala untuk menampal kerentanan keselamatan.

### Cabaran

Anda akan menghadapi beberapa cabaran semasa melaksanakan keselamatan dalam pelayan penstriman MCP:

- Mengimbangi keselamatan dengan kemudahan pembangunan
- Memastikan keserasian dengan pelbagai persekitaran klien

### Tugasan: Bina Aplikasi MCP Penstriman Anda Sendiri

**Senario:**
Bina pelayan dan klien MCP di mana pelayan memproses senarai item (contohnya, fail atau dokumen) dan menghantar pemberitahuan untuk setiap item yang diproses. Klien harus memaparkan setiap pemberitahuan sebaik sahaja ia diterima.

**Langkah-langkah:**

1. Laksanakan alat pelayan yang memproses senarai dan menghantar pemberitahuan untuk setiap item.
2. Laksanakan klien dengan pengendali mesej untuk memaparkan pemberitahuan secara masa nyata.
3. Uji pelaksanaan anda dengan menjalankan kedua-dua pelayan dan klien, dan perhatikan pemberitahuan.

[Solution](./solution/README.md)

## Bacaan Lanjut & Apa Seterusnya?

Untuk meneruskan perjalanan anda dengan penstriman MCP dan mengembangkan pengetahuan anda, bahagian ini menyediakan sumber tambahan dan langkah seterusnya yang disyorkan untuk membina aplikasi yang lebih maju.

### Bacaan Lanjut

- [Microsoft: Pengenalan kepada Penstriman HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS dalam ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Permintaan Penstriman](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Apa Seterusnya?

- Cuba bina alat MCP yang lebih maju yang menggunakan penstriman untuk analitik masa nyata, sembang, atau penyuntingan kolaboratif.
- Terokai integrasi penstriman MCP dengan rangka kerja frontend (React, Vue, dll.) untuk kemas kini UI secara langsung.
- Seterusnya: [Menggunakan AI Toolkit untuk VSCode](../07-aitk/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.