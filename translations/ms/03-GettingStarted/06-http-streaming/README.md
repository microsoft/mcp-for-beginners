# Penstriman HTTPS dengan Protokol Konteks Model (MCP)

Bab ini menyediakan panduan komprehensif untuk melaksanakan penstriman yang selamat, boleh diskalakan, dan masa nyata dengan Protokol Konteks Model (MCP) menggunakan HTTPS. Ia meliputi motivasi untuk penstriman, mekanisme pengangkutan yang tersedia, cara melaksanakan HTTP yang boleh distrim dalam MCP, amalan terbaik keselamatan, migrasi dari SSE, dan panduan praktikal untuk membina aplikasi MCP penstriman anda sendiri.

> **Melihat ke depan:** pelajaran ini menerangkan Streamable HTTP di bawah **Spesifikasi MCP 2025-11-25**, di mana sesi ditubuhkan semasa `initialize` dan dipautkan dengan header `Mcp-Session-Id`. Calon pelepasan `2026-07-28` menghapuskan jabat tangan dan ID sesi sepenuhnya, menjadikan setiap permintaan berdikari dan boleh dihantar ke mana-mana contoh pelayan tanpa sesi melekat. Lihat [Apa Yang Berubah dalam MCP: Calon Pelepasan 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) untuk butiran.

## Mekanisme Pengangkutan dan Penstriman dalam MCP

Bahagian ini meneroka pelbagai mekanisme pengangkutan yang tersedia dalam MCP dan peranan mereka dalam membolehkan keupayaan penstriman untuk komunikasi masa nyata antara klient dan pelayan.

### Apakah Mekanisme Pengangkutan?

Mekanisme pengangkutan menentukan cara data ditukar antara klient dan pelayan. MCP menyokong pelbagai jenis pengangkutan untuk menyesuaikan dengan persekitaran dan keperluan yang berbeza:

- **stdio**: Input/output standard, sesuai untuk alat berasaskan tempatan dan CLI. Mudah tetapi tidak sesuai untuk web atau awan.
- **SSE (Server-Sent Events)**: Membolehkan pelayan menolak kemas kini masa nyata kepada klient melalui HTTP. Baik untuk UI web, tetapi terhad dari segi kebolehskaalan dan fleksibiliti. Bermula Spesifikasi MCP 2025-06-18, pengangkutan SSE (Server-Sent Events) standalone sudah dipencilkan dan digantikan oleh pengangkutan "Streamable HTTP".
- **Streamable HTTP**: Pengangkutan penstriman berasaskan HTTP moden, menyokong pemberitahuan dan kebolehskaalan yang lebih baik. Disyorkan untuk kebanyakan senario produksi dan awan.

### Jadual Perbandingan

Lihat jadual perbandingan di bawah untuk memahami perbezaan antara mekanisme pengangkutan ini:

| Pengangkutan      | Kemas Kini Masa Nyata | Penstriman | Kebolehskaalan | Kes Penggunaan          |
|-------------------|----------------------|------------|----------------|-------------------------|
| stdio             | Tidak                | Tidak      | Rendah         | Alat CLI tempatan       |
| SSE               | Ya                   | Ya         | Sederhana      | Web, kemas kini masa nyata |
| Streamable HTTP   | Ya                   | Ya         | Tinggi         | Awan, multi-klient      |

> **Petua:** Memilih pengangkutan yang betul memberi kesan kepada prestasi, kebolehskaalan, dan pengalaman pengguna. **Streamable HTTP** disyorkan untuk aplikasi moden, boleh diskalakan, dan sedia untuk awan.

Perhatikan pengangkutan stdio dan SSE yang telah anda pelajari dalam bab sebelumnya dan bagaimana streamable HTTP adalah pengangkutan yang dibincangkan dalam bab ini.

## Penstriman: Konsep dan Motivasi

Memahami konsep asas dan motivasi di sebalik penstriman adalah penting untuk melaksanakan sistem komunikasi masa nyata yang berkesan.

**Penstriman** adalah teknik dalam pengaturcaraan rangkaian yang membenarkan data dihantar dan diterima dalam potongan kecil yang boleh diurus atau sebagai urutan peristiwa, bukannya menunggu keseluruhan tindak balas tersedia. Ini sangat berguna untuk:

- Fail atau set data yang besar.
- Kemas kini masa nyata (contoh: sembang, bar kemajuan).
- Pengiraan jangka panjang di mana anda mahu sentiasa memaklumkan pengguna.

Berikut adalah apa yang anda perlu tahu tentang penstriman secara umum:

- Data dihantar secara berperingkat, bukan sekaligus.
- Klien boleh memproses data sebaik tiba.
- Mengurangkan kelewatan yang dirasai dan meningkatkan pengalaman pengguna.

### Mengapa menggunakan penstriman?

Sebab-sebab menggunakan penstriman adalah seperti berikut:

- Pengguna mendapat maklum balas dengan segera, bukan hanya di akhir.
- Membolehkan aplikasi masa nyata dan UI responsif.
- Penggunaan sumber rangkaian dan pengiraan yang lebih cekap.

### Contoh Ringkas: Server & Klien Penstriman HTTP

Berikut adalah contoh ringkas bagaimana penstriman boleh dilaksanakan:

#### Python

**Server (Python, menggunakan FastAPI dan StreamingResponse):**

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

Contoh ini menunjukkan server menghantar satu siri mesej kepada klien sebaik ia tersedia, bukannya menunggu semua mesej siap.

**Bagaimana ia berfungsi:**

- Server menghasilkan setiap mesej sebaik ia siap.
- Klien menerima dan mencetak setiap bahagian sebaik tiba.

**Keperluan:**

- Server mesti menggunakan respon penstriman (contohnya, `StreamingResponse` dalam FastAPI).
- Klien mesti memproses respon sebagai aliran (`stream=True` dalam requests).
- Content-Type biasanya `text/event-stream` atau `application/octet-stream`.

#### Java

**Server (Java, menggunakan Spring Boot dan Server-Sent Events):**

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

- Menggunakan stack reaktif Spring Boot dengan `Flux` untuk penstriman
- `ServerSentEvent` menyediakan penstriman acara berstruktur dengan jenis acara
- `WebClient` dengan `bodyToFlux()` membenarkan penggunaan penstriman reaktif
- `delayElements()` mensimulasikan masa pemprosesan antara acara
- Acara boleh mempunyai jenis (`info`, `result`) untuk pengendalian klien yang lebih baik

### Perbandingan: Penstriman Klasik vs Penstriman MCP

Perbezaan antara bagaimana penstriman berfungsi secara "klasik" berbanding bagaimana ia berfungsi dalam MCP boleh digambarkan seperti berikut:

| Ciri                   | Penstriman HTTP Klasik       | Penstriman MCP (Pemberitahuan)    |
|------------------------|------------------------------|-----------------------------------|
| Respon utama           | Terbahagi                    | Tunggal, di akhir                 |
| Kemas kini progres     | Dihantar sebagai potongan data | Dihantar sebagai pemberitahuan    |
| Keperluan klien        | Mesti memproses aliran       | Mesti melaksanakan pengendali mesej |
| Kes penggunaan         | Fail besar, aliran token AI   | Progres, log, maklum balas masa nyata |

### Perbezaan Utama Dapatan

Selain itu, berikut adalah beberapa perbezaan utama:

- **Corak Komunikasi:**
  - Penstriman HTTP klasik: Menggunakan pengkodean pemindahan berpotongan mudah untuk menghantar data dalam potongan
  - Penstriman MCP: Menggunakan sistem pemberitahuan berstruktur dengan protokol JSON-RPC

- **Format Mesej:**
  - HTTP klasik: Potongan teks biasa dengan baris baru
  - MCP: Objek LoggingMessageNotification berstruktur dengan metadata

- **Pelaksanaan Klien:**
  - HTTP klasik: Klien mudah yang memproses respon penstriman
  - MCP: Klien lebih maju dengan pengendali mesej untuk memproses jenis mesej berbeza

- **Kemas Kini Progres:**
  - HTTP klasik: Progres adalah sebahagian daripada aliran respon utama
  - MCP: Progres dihantar melalui mesej pemberitahuan berasingan sementara respon utama datang di akhir

### Cadangan

Ada beberapa perkara yang kami cadangkan apabila memilih antara melaksanakan penstriman klasik (sebagai titik akhir yang kami tunjukkan di atas menggunakan `/stream`) versus memilih penstriman melalui MCP.

- **Untuk keperluan penstriman mudah:** Penstriman HTTP klasik lebih mudah dilaksanakan dan mencukupi untuk keperluan penstriman asas.

- **Untuk aplikasi interaktif dan kompleks:** Penstriman MCP menyediakan pendekatan yang lebih berstruktur dengan metadata yang lebih kaya dan pemisahan antara pemberitahuan dan hasil akhir.

- **Untuk aplikasi AI:** Sistem pemberitahuan MCP amat berguna untuk tugas AI jangka panjang di mana anda mahu sentiasa memaklumkan pengguna tentang progres.

## Penstriman dalam MCP

Jadi, anda telah melihat beberapa cadangan dan perbandingan setakat ini mengenai perbezaan antara penstriman klasik dan penstriman dalam MCP. Mari kita terokai dengan lebih terperinci bagaimana anda boleh memanfaatkan penstriman dalam MCP.

Memahami bagaimana penstriman berfungsi dalam rangka kerja MCP adalah penting untuk membina aplikasi responsif yang menyediakan maklum balas masa nyata kepada pengguna semasa operasi jangka panjang.

Dalam MCP, penstriman bukan tentang menghantar respon utama dalam potongan, tetapi tentang menghantar **pemberitahuan** kepada klien semasa alat memproses permintaan. Pemberitahuan ini boleh merangkumi kemas kini progres, log, atau acara lain.

### Bagaimana ia berfungsi

Hasil utama masih dihantar sebagai satu respon tunggal. Namun, pemberitahuan boleh dihantar sebagai mesej berasingan semasa pemprosesan dan dengan itu mengemas kini klien dalam masa nyata. Klien mesti dapat mengendalikan dan memaparkan pemberitahuan ini.

## Apakah Pemberitahuan?

Kami menyebut "Pemberitahuan", apa maksudnya dalam konteks MCP?

Pemberitahuan adalah mesej yang dihantar dari pelayan ke klien untuk memaklumkan tentang progres, status, atau acara lain semasa operasi jangka panjang. Pemberitahuan meningkatkan ketelusan dan pengalaman pengguna.

Contohnya, klien sepatutnya menghantar pemberitahuan sebaik jabat tangan awal dengan pelayan dibuat.

Pemberitahuan kelihatan seperti ini sebagai mesej JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Pemberitahuan tergolong dalam topik dalam MCP dirujuk sebagai ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Notis pemansuhan:** calon pelepasan spesifikasi MCP `2026-07-28` menandakan primitif Logging sebagai dipansuhkan demi `stderr` untuk pengangkutan stdio dan OpenTelemetry untuk pengamatan berstruktur. Logging terus berfungsi dalam `2025-11-25` dan sekurang-kurangnya setahun selepas mana-mana pemansuhan rasmi. Lihat [Apa Yang Berubah dalam MCP: Calon Pelepasan 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Untuk mengaktifkan logging, pelayan perlu membolehkan ia sebagai ciri/keupayaan seperti ini:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Bergantung pada SDK yang digunakan, logging mungkin diaktifkan secara lalai, atau anda mungkin perlu mengaktifkannya secara eksplisit dalam konfigurasi pelayan anda.

Terdapat pelbagai jenis pemberitahuan:

| Tahap      | Penerangan                    | Contoh Kes Penggunaan             |
|-----------|------------------------------|---------------------------------|
| debug     | Maklumat debugging terperinci | Titik masuk/keluar fungsi        |
| info      | Mesej maklumat umum           | Kemas kini progres operasi       |
| notice    | Acara normal tapi penting     | Perubahan konfigurasi            |
| warning   | Keadaan amaran                | Penggunaan ciri yang dipansuhkan |
| error     | Keadaan ralat                | Kegagalan operasi                |
| critical  | Keadaan kritikal              | Kegagalan komponen sistem        |
| alert     | Tindakan mesti diambil segera | Pengesanan kerosakan data        |
| emergency | Sistem tidak boleh digunakan  | Kegagalan sistem sepenuhnya      |

## Melaksanakan Pemberitahuan dalam MCP

Untuk melaksanakan pemberitahuan dalam MCP, anda perlu menyediakan kedua-dua pihak pelayan dan klien untuk mengendalikan kemas kini masa nyata. Ini membolehkan aplikasi anda memberikan maklum balas segera kepada pengguna semasa operasi jangka panjang.

### Pihak pelayan: Menghantar Pemberitahuan

Mari mulakan dengan pihak pelayan. Dalam MCP, anda mentakrifkan alat yang boleh menghantar pemberitahuan semasa memproses permintaan. Pelayan menggunakan objek konteks (biasanya `ctx`) untuk menghantar mesej kepada klien.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Dalam contoh di atas, alat `process_files` menghantar tiga pemberitahuan kepada klien semasa memproses setiap fail. Kaedah `ctx.info()` digunakan untuk menghantar mesej informasi.

Selain itu, untuk mengaktifkan pemberitahuan, pastikan pelayan anda menggunakan pengangkutan penstriman (seperti `streamable-http`) dan klien anda melaksanakan pengendali mesej untuk memproses pemberitahuan. Berikut adalah cara anda boleh menyediakan pelayan menggunakan pengangkutan `streamable-http`:

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

Dalam contoh .NET ini, alat `ProcessFiles` dihias dengan atribut `Tool` dan menghantar tiga pemberitahuan kepada klien semasa memproses setiap fail. Kaedah `ctx.Info()` digunakan untuk menghantar mesej informasi.

Untuk mengaktifkan pemberitahuan dalam pelayan MCP .NET anda, pastikan anda menggunakan pengangkutan penstriman:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Pihak klien: Menerima Pemberitahuan

Klien mesti melaksanakan pengendali mesej untuk memproses dan memaparkan pemberitahuan sebaik ia tiba.

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

Dalam kod di atas, fungsi `message_handler` memeriksa jika mesej yang datang adalah pemberitahuan. Jika ya, ia mencetak pemberitahuan; jika tidak, ia memprosesnya sebagai mesej pelayan biasa. Juga perhatikan bagaimana `ClientSession` diinisialisasi dengan `message_handler` untuk mengendalikan pemberitahuan yang masuk.

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

Dalam contoh .NET ini, fungsi `MessageHandler` memeriksa jika mesej yang datang adalah pemberitahuan. Jika ya, ia mencetak pemberitahuan; jika tidak, ia memprosesnya sebagai mesej pelayan biasa. `ClientSession` diinisialisasi dengan pengendali mesej melalui `ClientSessionOptions`.

Untuk mengaktifkan pemberitahuan, pastikan pelayan anda menggunakan pengangkutan penstriman (seperti `streamable-http`) dan klien anda melaksanakan pengendali mesej untuk memproses pemberitahuan.

## Pemberitahuan Progres & Senario

Bahagian ini menerangkan konsep pemberitahuan progres dalam MCP, mengapa ia penting, dan bagaimana melaksanakannya menggunakan Streamable HTTP. Anda juga akan menemui tugasan praktikal untuk mengukuhkan pemahaman anda.

Pemberitahuan progres adalah mesej masa nyata yang dihantar dari pelayan kepada klien semasa operasi jangka panjang. Sebaliknya daripada menunggu keseluruhan proses selesai, pelayan sentiasa mengemas kini klien tentang status semasa. Ini meningkatkan ketelusan, pengalaman pengguna, dan memudahkan penyahpepijatan.

**Contoh:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Mengapa Menggunakan Pemberitahuan Progres?

Pemberitahuan progres penting atas beberapa sebab:

- **Pengalaman pengguna yang lebih baik:** Pengguna melihat kemas kini semasa kerja berjalan, bukan hanya di akhir.
- **Maklum balas masa nyata:** Klien boleh memaparkan bar kemajuan atau log, menjadikan aplikasi terasa responsif.
- **Penyahpepijatan dan pemantauan lebih mudah:** Pembangun dan pengguna boleh melihat di mana proses mungkin perlahan atau tersekat.

### Cara Melaksanakan Pemberitahuan Progres

Berikut cara anda boleh melaksanakan pemberitahuan progres dalam MCP:

- **Di pelayan:** Gunakan `ctx.info()` atau `ctx.log()` untuk menghantar pemberitahuan semasa setiap item diproses. Ini menghantar mesej kepada klien sebelum hasil utama siap.
- **Di klien:** Laksanakan pengendali mesej yang mendengar dan memaparkan pemberitahuan sebaik ia sampai. Pengendali ini membezakan antara pemberitahuan dan hasil akhir.

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

Keselamatan harus menjadi keutamaan apabila melaksanakan mana-mana pelayan, terutamanya apabila menggunakan pengangkut berasaskan HTTP seperti Streamable HTTP dalam MCP.

Apabila melaksanakan pelayan MCP dengan pengangkut berasaskan HTTP, keselamatan menjadi satu perkara penting yang memerlukan perhatian teliti terhadap pelbagai vektor serangan dan mekanisme perlindungan.

### Gambaran Keseluruhan

Keselamatan adalah kritikal apabila mendedahkan pelayan MCP melalui HTTP. Streamable HTTP memperkenalkan permukaan serangan baru dan memerlukan konfigurasi yang berhati-hati.

Berikut adalah beberapa pertimbangan keselamatan utama:

- **Pengesahan Kepala Origin**: Sentiasa sahkan kepala `Origin` untuk mengelakkan serangan DNS rebinding.
- **Pengikatan Localhost**: Untuk pembangunan tempatan, ikat pelayan ke `localhost` agar tidak terdedah kepada internet awam.
- **Pengesahan**: Laksanakan pengesahan (contoh: kekunci API, OAuth) untuk penggunaan produksi.
- **CORS**: Konfigurasikan polisi Cross-Origin Resource Sharing (CORS) untuk mengehadkan akses.
- **HTTPS**: Gunakan HTTPS dalam produksi untuk menyulitkan trafik.

### Amalan Terbaik

Di samping itu, berikut adalah beberapa amalan terbaik yang perlu diikuti apabila melaksanakan keselamatan dalam pelayan streaming MCP anda:

- Jangan sesekali mempercayai permintaan yang masuk tanpa pengesahan.
- Log dan pantau semua akses dan kesilapan.
- Kemas kini secara berkala pergantungan untuk membaiki kelemahan keselamatan.

### Cabaran

Anda akan menghadapi beberapa cabaran apabila melaksanakan keselamatan dalam pelayan streaming MCP:

- Mengimbangi keselamatan dengan kemudahan pembangunan
- Memastikan keserasian dengan pelbagai persekitaran klien


## Naik Taraf dari SSE ke Streamable HTTP

Bagi aplikasi yang kini menggunakan Server-Sent Events (SSE), beralih ke Streamable HTTP menyediakan kemampuan yang lebih baik dan kemampanan jangka panjang yang lebih baik untuk pelaksanaan MCP anda.

### Kenapa Naik Taraf?

Terdapat dua sebab utama untuk naik taraf dari SSE ke Streamable HTTP:

- Streamable HTTP menawarkan skala lebih baik, keserasian, dan sokongan pemberitahuan yang lebih kaya daripada SSE.
- Ia ialah pengangkut yang disyorkan untuk aplikasi MCP baru.

### Langkah Migrasi

Berikut adalah cara anda boleh migrasi dari SSE ke Streamable HTTP dalam aplikasi MCP anda:

- **Kemas kini kod pelayan** untuk menggunakan `transport="streamable-http"` dalam `mcp.run()`.
- **Kemas kini kod klien** untuk menggunakan `streamablehttp_client` dan bukan klien SSE.
- **Laksanakan pengendal pesanan** dalam klien untuk memproses pemberitahuan.
- **Uji keserasian** dengan alat dan aliran kerja sedia ada.

### Menyelenggara Keserasian

Disyorkan untuk mengekalkan keserasian dengan klien SSE sedia ada semasa proses migrasi. Berikut adalah beberapa strategi:

- Anda boleh menyokong kedua-dua SSE dan Streamable HTTP dengan menjalankan kedua-dua pengangkut pada titik akhir yang berbeza.
- Secara beransur-ansur migrasi klien ke pengangkut baru.

### Cabaran

Pastikan anda menangani cabaran berikut semasa migrasi:

- Memastikan semua klien dikemas kini
- Mengendalikan perbezaan dalam penghantaran pemberitahuan

### Tugasan: Bina Aplikasi Streaming MCP Anda Sendiri

**Senario:**
Bina pelayan dan klien MCP di mana pelayan memproses senarai item (contohnya, fail atau dokumen) dan menghantar pemberitahuan untuk setiap item yang diproses. Klien perlu memaparkan setiap pemberitahuan sebaik sahaja ia diterima.

**Langkah-langkah:**

1. Laksanakan alat pelayan yang memproses senarai dan menghantar pemberitahuan untuk setiap item.
2. Laksanakan klien dengan pengendali mesej untuk memaparkan pemberitahuan secara masa nyata.
3. Uji pelaksanaan anda dengan menjalankan kedua-dua pelayan dan klien, dan perhatikan pemberitahuan tersebut.

[Penyelesaian](./solution/README.md)

## Bacaan Lanjut & Apa Seterusnya?

Untuk meneruskan perjalanan anda dengan streaming MCP dan memperluas pengetahuan anda, bahagian ini menyediakan sumber tambahan dan langkah seterusnya yang dicadangkan untuk membina aplikasi yang lebih maju.

### Bacaan Lanjut

- [Microsoft: Pengenalan kepada Streaming HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS dalam ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Permintaan Streaming](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Apa Seterusnya?

- Cuba bina alat MCP yang lebih maju yang menggunakan streaming untuk analitik masa nyata, sembang, atau penyuntingan kolaboratif.
- Terokai integrasi streaming MCP dengan rangka kerja frontend (React, Vue, dll.) untuk kemaskini UI secara langsung.
- Seterusnya: [Menggunakan AI Toolkit untuk VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->