# Penstriman HTTPS dengan Protokol Konteks Model (MCP)

Bab ini menyediakan panduan menyeluruh untuk melaksanakan penstriman yang selamat, boleh diskalakan, dan masa nyata dengan Protokol Konteks Model (MCP) menggunakan HTTPS. Ia merangkumi motivasi untuk penstriman, mekanisme pengangkutan yang tersedia, cara melaksanakan HTTP yang boleh distrim dalam MCP, amalan keselamatan terbaik, migrasi daripada SSE, dan panduan praktikal untuk membina aplikasi MCP penstriman anda sendiri.

> [!WARNING]
> Contoh pelaksanaan dalam pelajaran ini menyasarkan **Spesifikasi MCP
> `2025-11-25`** dan menunjukkan jeda tangan `initialize` warisan,
> `Mcp-Session-Id`, GET aliran acara, dan model boleh disambung semula. MCP `2026-07-28`
> mengeluarkan ciri-ciri tersebut. Permintaan HTTP Boleh Distrim semasa adalah permintaan
> POST yang berdiri sendiri dengan tajuk `MCP-Protocol-Version` dan `Mcp-Method`, serta
> `Mcp-Name` apabila diperlukan. Lihat
> [Apa yang Berubah dalam MCP: Spesifikasi 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> sebelum menggunakan contoh ini dalam pelaksanaan baru.

## Mekanisme Pengangkutan dan Penstriman dalam MCP

Seksyen ini meneroka pelbagai mekanisme pengangkutan yang tersedia dalam MCP dan peranan mereka dalam membolehkan kebolehan penstriman untuk komunikasi masa nyata antara klien dan pelayan.

### Apakah Mekanisme Pengangkutan?

Mekanisme pengangkutan mentakrifkan bagaimana data dipertukarkan antara klien dan pelayan. MCP menyokong pelbagai jenis pengangkutan untuk sesuai dengan persekitaran dan keperluan yang berbeza:

- **stdio**: Input/output standard, sesuai untuk alat berasaskan tempatan dan CLI. Mudah tetapi tidak sesuai untuk web atau awan.
- **HTTP+SSE**: Pengangkutan jauh warisan, sudah tidak digunakan dalam MCP `2025-03-26`
    dan digantikan oleh Streamable HTTP. Jangan gunakan untuk pelaksanaan baru.
- **Streamable HTTP**: Pengangkutan penstriman berasaskan HTTP moden, menyokong notifikasi dan skala yang lebih baik. Disyorkan untuk kebanyakan senario produksi dan awan.

### Jadual Perbandingan

Lihat jadual perbandingan di bawah untuk memahami perbezaan antara mekanisme pengangkutan ini:

| Pengangkutan | Status | Notifikasi | Kegunaan tipikal |
|---|---|---|---|
| stdio | Semasa | Ya | Proses subtempatan |
| HTTP+SSE | Tidak digunakan | Ya | Pelaksanaan jauh warisan |
| Streamable HTTP | Semasa | Ya | Pelayan jauh dan awan |

> **Petua:** Memilih pengangkutan yang betul memberi impak kepada prestasi, skala, dan pengalaman pengguna. **Streamable HTTP** disyorkan untuk aplikasi moden, boleh diskalakan, dan sedia awan.

Pengangkutan standard ialah stdio dan Streamable HTTP. HTTP+SSE hanya muncul dalam
contoh lama sahaja.

## Penstriman: Konsep dan Motivasi

Memahami konsep asas dan motivasi di sebalik penstriman adalah penting untuk melaksanakan sistem komunikasi masa nyata yang berkesan.

**Penstriman** adalah teknik dalam pengaturcaraan rangkaian yang membolehkan data dihantar dan diterima dalam bahagian kecil yang boleh diurus atau sebagai urutan acara, bukannya menunggu keseluruhan respons siap. Ini sangat berguna untuk:

- Fail besar atau set data.
- Kemas kini masa nyata (contohnya, chat, bar kemajuan).
- Pengiraan lama di mana anda mahu terus memaklumkan pengguna.

Berikut adalah perkara yang perlu anda tahu mengenai penstriman pada tahap tinggi:

- Data dihantar secara berperingkat, bukan sekaligus.
- Klien boleh memproses data apabila ia sampai.
- Mengurangkan kelewatan yang dirasai dan memperbaiki pengalaman pengguna.

### Kenapa guna penstriman?

Sebab-sebab menggunakan penstriman adalah seperti berikut:

- Pengguna mendapat maklum balas segera, bukan hanya di akhir
- Membolehkan aplikasi masa nyata dan UI responsif
- Penggunaan sumber rangkaian dan pengiraan yang lebih cekap

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

Contoh ini menunjukkan pelayan menghantar satu siri mesej kepada klien apabila tersedia, bukan menunggu semua mesej siap.

**Cara ia berfungsi:**

- Pelayan menghantar setiap mesej apabila ia sudah siap.
- Klien menerima dan mencetak setiap bahagian apabila ia sampai.

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

- Menggunakan stack reaktif Spring Boot dengan `Flux` untuk penstriman
- `ServerSentEvent` menyediakan penstriman acara berstruktur dengan jenis acara
- `WebClient` dengan `bodyToFlux()` membolehkan penggunaan penstriman reaksif
- `delayElements()` mensimulasikan masa pemprosesan antara acara
- Acara boleh mempunyai jenis (`info`, `result`) untuk pengendalian klien yang lebih baik

### Perbandingan: Penstriman Klasik vs Penstriman MCP

Perbezaan cara penstriman berfungsi dalam cara "klasik" berbanding bagaimana ia berfungsi dalam MCP boleh digambarkan seperti berikut:

| Ciri                   | Penstriman HTTP Klasik        | Penstriman MCP (Notifikasi)       |
|------------------------|-------------------------------|-------------------------------------|
| Respons utama           | Berbahagian                   | Tunggal, di akhir                 |
| Kemas kini kemajuan     | Dihantar sebagai bahagian data| Dihantar sebagai notifikasi       |
| Keperluan klien        | Mesti memproses aliran         | Mesti melaksanakan pengendal mesej |
| Kes penggunaan          | Fail besar, aliran token AI    | Kemajuan, log, maklum balas masa nyata |

### Perbezaan Utama yang Diperhatikan

Selain itu, berikut adalah beberapa perbezaan utama:

- **Corak Komunikasi:**
  - Penstriman HTTP klasik: Menggunakan pengkodingan penghantaran berbahagian mudah untuk menghantar data dalam bahagian
  - Penstriman MCP: Menggunakan sistem notifikasi berstruktur dengan protokol JSON-RPC

- **Format Mesej:**
  - HTTP klasik: Bahagian teks biasa dengan baris baru
  - MCP: Objek Notifikasi LoggingMessage berstruktur dengan metadata

- **Pelaksanaan Klien:**
  - HTTP klasik: Klien mudah yang memproses respons penstriman
  - MCP: Klien lebih kompleks dengan pengendal mesej untuk memproses jenis mesej berbeza

- **Kemas Kini Kemajuan:**
  - HTTP klasik: Kemajuan adalah sebahagian daripada aliran respons utama
  - MCP: Kemajuan dihantar melalui mesej notifikasi berasingan manakala respons utama sampai di akhir

### Cadangan

Terdapat beberapa perkara yang kami cadangkan apabila memilih antara melaksanakan penstriman klasik (sebagai titik akhir yang kami tunjukkan di atas menggunakan `/stream`) berbanding memilih penstriman melalui MCP.

- **Untuk keperluan penstriman mudah:** Penstriman HTTP klasik lebih mudah dilaksanakan dan mencukupi untuk keperluan penstriman asas.


- **Untuk aplikasi kompleks dan interaktif:** Penstriman MCP menyediakan pendekatan yang lebih tersusun dengan metadata yang lebih kaya dan pemisahan antara pemberitahuan dan keputusan akhir.

- **Untuk aplikasi AI:** Sistem pemberitahuan MCP amat berguna untuk tugas AI yang berjalan lama di mana anda ingin memastikan pengguna sentiasa maklum tentang kemajuan.

## Penstriman dalam MCP

Baik, jadi anda sudah melihat beberapa cadangan dan perbandingan setakat ini mengenai perbezaan antara penstriman klasik dan penstriman dalam MCP. Mari kita terokai secara terperinci bagaimana anda boleh memanfaatkan penstriman dalam MCP.

Memahami bagaimana penstriman berfungsi dalam rangka kerja MCP adalah penting untuk membina aplikasi responsif yang memberikan maklum balas masa nyata kepada pengguna semasa operasi yang berjalan lama.

Dalam MCP, penstriman bukan tentang menghantar respon utama secara bersegmen, tetapi tentang menghantar **pemberitahuan** kepada klien semasa alat memproses permintaan. Pemberitahuan ini boleh termasuk kemas kini kemajuan, log, atau acara lain.

### Cara ia berfungsi

Keputusan utama masih dihantar sebagai satu respon tunggal. Namun, pemberitahuan boleh dihantar sebagai mesej berasingan semasa pemprosesan dan dengan itu mengemas kini klien secara masa nyata. Klien mesti boleh mengendalikan dan memaparkan pemberitahuan ini.

### Latihan pilihan: sambung ke pelayan MCP yang dihoskan

Anda juga boleh menggunakan Streamable HTTP tanpa menjalankan pelayan tempatan. Contoh ini
menyambung ke [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
mengesan alatan, dan mencari dokumentasi MCP awam menggunakan SDK
Python yang sama seperti [klien tempatan](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Titik laluan tanpa nama Parallel tidak memerlukan akaun atau kunci API. Akses percuma adalah
terhad pada kadar. Menjalankan skrip ini menghantar pertanyaan carian, objektif, dan
pengecam sesi rawak kepada Parallel. Perkhidmatan juga menawarkan `web_fetch`,
yang menghantar URL yang diminta dan sebarang konteks yang diberikan kepada Parallel. Gunakan
maklumat awam untuk latihan ini; lihat [terma](https://parallel.ai/customer-terms)
dan [dasar privasi](https://parallel.ai/privacy-policy).

Dengan Python 3.10 atau lebih baru dan persekitaran maya diaktifkan, pasang SDK:

```sh
python -m pip install "mcp>=1.10,<2"
```

Simpan ini sebagai `hosted_search.py` dan jalankan `python hosted_search.py`:

```python
import asyncio
from uuid import uuid4

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main() -> None:
    session_id = str(uuid4())
    async with streamablehttp_client("https://search.parallel.ai/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Available tools:", [tool.name for tool in tools.tools])

            result = await session.call_tool(
                "web_search",
                {
                    "objective": "Find the official MCP Streamable HTTP documentation",
                    "search_queries": ["MCP Streamable HTTP documentation"],
                    "session_id": session_id,
                },
            )
            if result.isError:
                raise RuntimeError(f"Search tool failed: {result.content}")
            for block in result.content:
                if block.type == "text":
                    print(block.text)


async def run() -> None:
    await asyncio.wait_for(main(), timeout=60)


if __name__ == "__main__":
    asyncio.run(run())
```

Jangkaan penemuan termasuk `web_search` dan `web_fetch`, diikuti oleh respons carian
yang mengandungi URL sumber dan petikan. Keputusan boleh berbeza atau kosong.
Skrip memeriksa `isError` kerana alat boleh gagal walaupun permintaan HTTP
berjaya. Jika akses dihadkan pada kadar, tunggu sebelum mencuba lagi. Gunakan semula
`session_id` yang sama jika anda melanjutkan skrip dengan panggilan carian atau fetch berkaitan.

Streamable HTTP membenarkan kedua-dua respons JSON dan SSE; pelayan ini boleh mengembalikan
keputusan JSON lengkap tanpa pemberitahuan kemajuan. SDK mengendalikan
pengangkutan. Teruskan dengan contoh tempatan di bawah untuk belajar tentang pemberitahuan.
Skrip pilihan ini membuat satu carian eksplisit dan menutup sambungannya apabila
selesai. Jika anda kemudian pendedahkan alatan ini kepada agen, agen mungkin akan memanggil
mereka semasa kerjanya; anggap teks web yang diperoleh sebagai data yang tidak boleh dipercayai.

## Apakah Pemberitahuan?

Kami sebut "Pemberitahuan", apa maksudnya dalam konteks MCP?

Pemberitahuan adalah mesej JSON-RPC yang tidak mempunyai `id` dan tidak
menerima respons. MCP menggunakan pemberitahuan untuk kemajuan, pembatalan, dan
acara satu hala lain.

Dalam MCP `2025-11-25`, klien menghantar `notifications/initialized` selepas
jabat tangan inisialisasi. MCP `2026-07-28` tidak mempunyai jabat tangan inisialisasi, jadi
pemberitahuan ini adalah tingkah laku warisan.

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

Logging adalah satu ciri yang menggunakan pemberitahuan; pemberitahuan sendiri adalah
jenis mesej JSON-RPC umum.

> **Tamat tempoh dalam MCP `2026-07-28`:** ciri Logging kekal tersedia
> untuk keserasian tetapi layak untuk dikeluarkan dalam semakan spesifikasi pertama
> yang dikeluarkan pada atau selepas 28 Julai 2027. Pelaksanaan baru harus menggunakan
> `stderr` dengan stdio atau OpenTelemetry untuk kebolehlihatan berstruktur.

Untuk pelaksanaan warisan `2025-11-25`, pelayan mengaktifkan kemampuan Logging
seperti berikut:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Bergantung pada SDK yang digunakan, logging mungkin diaktifkan secara lalai, atau anda mungkin perlu mengaktifkannya secara eksplisit dalam konfigurasi pelayan anda.

Terdapat jenis pemberitahuan yang berbeza:

| Tahap     | Penerangan                    | Contoh Kes Penggunaan               |
|-----------|------------------------------|------------------------------------|
| debug     | Maklumat pengesanan terperinci | Titik masuk/keluar fungsi          |
| info      | Mesej maklumat umum          | Kemas kini kemajuan operasi        |
| notice    | Acara normal tetapi penting  | Perubahan konfigurasi              |
| warning   | Keadaan amaran               | Penggunaan ciri yang tidak disarankan |
| error     | Keadaan ralat                | Kegagalan operasi                  |
| critical  | Keadaan kritikal             | Kegagalan komponen sistem          |
| alert     | Tindakan mesti diambil segera | Pengesanan kerosakan data          |
| emergency | Sistem tidak boleh digunakan | Kegagalan sistem sepenuhnya        |

## Melaksanakan Pemberitahuan dalam MCP

Untuk melaksanakan pemberitahuan dalam MCP, anda perlu menyediakan kedua-dua pihak pelayan dan klien untuk mengendalikan kemas kini masa nyata. Ini membolehkan aplikasi anda memberikan maklum balas segera kepada pengguna semasa operasi yang berjalan lama.

### Pihak pelayan: Menghantar Pemberitahuan

Mari mulakan dengan pihak pelayan. Dalam MCP, anda mentakrif alat yang boleh menghantar pemberitahuan semasa memproses permintaan. Pelayan menggunakan objek konteks (biasanya `ctx`) untuk menghantar mesej kepada klien.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Dalam contoh sebelumnya, alat `process_files` menghantar tiga pemberitahuan kepada klien semasa memproses setiap fail. Kaedah `ctx.info()` digunakan untuk menghantar mesej maklumat.

Selain itu, untuk mengaktifkan pemberitahuan, pastikan pelayan anda menggunakan pengangkutan penstriman (seperti `streamable-http`) dan klien anda melaksanakan pengendali mesej untuk memproses pemberitahuan. Berikut ialah cara anda boleh menetapkan pelayan untuk menggunakan pengangkutan `streamable-http`:

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

Dalam contoh .NET ini, alat `ProcessFiles` dihias dengan atribut `Tool` dan menghantar tiga pemberitahuan kepada klien semasa memproses setiap fail. Kaedah `ctx.Info()` digunakan untuk menghantar mesej maklumat.

Untuk mengaktifkan pemberitahuan dalam pelayan MCP .NET anda, pastikan anda menggunakan pengangkutan penstriman:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Pihak klien: Menerima Pemberitahuan

Klien mesti melaksanakan pengendali mesej untuk memproses dan memaparkan pemberitahuan semasa ia tiba.

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

Dalam kod sebelumnya, fungsi `message_handler` menyemak jika mesej yang masuk adalah pemberitahuan. Jika ya, ia mencetak pemberitahuan; jika tidak, ia memprosesnya sebagai mesej pelayan biasa. Juga ambil perhatian bagaimana `ClientSession` diinisialisasi dengan `message_handler` untuk mengendalikan pemberitahuan yang masuk.

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


Dalam contoh .NET ini, fungsi `MessageHandler` memeriksa sama ada mesej yang masuk adalah notifikasi. Jika ya, ia mencetak notifikasi itu; jika tidak, ia memprosesnya sebagai mesej pelayan biasa. `ClientSession` diinisialisasi dengan pengendali mesej melalui `ClientSessionOptions`.

Untuk membolehkan notifikasi, pastikan pelayan anda menggunakan pengangkutan penstriman (seperti `streamable-http`) dan klien anda mengimplimentasikan pengendali mesej untuk memproses notifikasi.

## Notifikasi Kemajuan & Senario

Bahagian ini menerangkan konsep notifikasi kemajuan dalam MCP, mengapa ia penting, dan bagaimana untuk melaksanakannya menggunakan Streamable HTTP. Anda juga akan menemui tugasan praktikal untuk mengukuhkan pemahaman anda.

Notifikasi kemajuan adalah mesej masa nyata yang dihantar dari pelayan ke klien semasa operasi yang berjalan lama. Daripada menunggu keseluruhan proses selesai, pelayan memaklumkan klien tentang status semasa. Ini meningkatkan ketelusan, pengalaman pengguna, dan memudahkan penyahpepijatan.

**Contoh:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Mengapa Gunakan Notifikasi Kemajuan?

Notifikasi kemajuan adalah penting untuk beberapa sebab:

- **Pengalaman pengguna yang lebih baik:** Pengguna melihat kemas kini semasa kerja sedang dijalankan, bukan hanya pada akhirnya.
- **Maklum balas masa nyata:** Klien boleh memaparkan bar kemajuan atau log, menjadikan aplikasi rasa responsif.
- **Mudah untuk penyahpepijatan dan pemantauan:** Pembangun dan pengguna dapat melihat di mana proses mungkin lambat atau tersekat.

### Cara Melaksanakan Notifikasi Kemajuan

Berikut adalah cara anda boleh melaksanakan notifikasi kemajuan dalam MCP:

- **Pada pelayan:** Gunakan `ctx.info()` atau `ctx.log()` untuk menghantar notifikasi setiap kali item diproses. Ini menghantar mesej kepada klien sebelum keputusan utama siap.
- **Pada klien:** Laksanakan pengendali mesej yang mendengar dan memaparkan notifikasi semasa ia tiba. Pengendali ini membezakan antara notifikasi dan keputusan akhir.

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

Keselamatan harus menjadi keutamaan apabila melaksanakan sebarang pelayan, terutamanya apabila menggunakan pengangkutan berasaskan HTTP seperti Streamable HTTP dalam MCP.

Apabila melaksanakan pelayan MCP dengan pengangkutan berasaskan HTTP, keselamatan menjadi perkara utama yang memerlukan perhatian teliti terhadap pelbagai vektor serangan dan mekanisme perlindungan.

### Gambaran Keseluruhan

Keselamatan adalah penting apabila mendedahkan pelayan MCP melalui HTTP. Streamable HTTP memperkenalkan permukaan serangan baru dan memerlukan konfigurasi teliti.

Berikut adalah beberapa pertimbangan keselamatan utama:

- **Pengesahan Header Origin**: Sentiasa sahkan header `Origin` bagi mengelakkan serangan DNS rebinding.
- **Pengikatan Localhost**: Untuk pembangunan tempatan, kaitkan pelayan ke `localhost` supaya tidak didedahkan ke internet awam.
- **Pengesahan**: Laksanakan pengesahan (contoh, kunci API, OAuth) untuk penyebaran pengeluaran.
- **CORS**: Tetapkan polisi Cross-Origin Resource Sharing (CORS) untuk mengehadkan akses.
- **HTTPS**: Gunakan HTTPS dalam pengeluaran untuk menyulitkan trafik.

### Amalan Terbaik

Selain itu, berikut adalah beberapa amalan terbaik yang harus diikuti semasa melaksanakan keselamatan dalam pelayan penstriman MCP anda:

- Jangan sekali-kali percaya pada permintaan masuk tanpa pengesahan.
- Log dan pantau semua akses dan ralat.
- Kemas kini kebergantungan secara berkala untuk menampal kelemahan keselamatan.

### Cabaran

Anda akan menghadapi beberapa cabaran apabila melaksanakan keselamatan dalam pelayan penstriman MCP:

- Menyeimbangkan keselamatan dengan kemudahan pembangunan
- Memastikan keserasian dengan pelbagai persekitaran klien


## Meningkatkan dari SSE ke Streamable HTTP

Untuk aplikasi yang kini menggunakan Server-Sent Events (SSE), migrasi ke Streamable HTTP menyediakan keupayaan yang dipertingkat dan kelestarian jangka panjang yang lebih baik untuk pelaksanaan MCP anda.

### Mengapa Meningkatkan?

Terdapat dua sebab kukuh untuk meningkatkan dari SSE ke Streamable HTTP:

- Streamable HTTP menawarkan skala lebih baik, keserasian, dan sokongan notifikasi yang lebih kaya berbanding SSE.
- Ia adalah pengangkutan yang disyorkan untuk aplikasi MCP baru.

### Langkah Migrasi

Berikut adalah cara anda boleh migrasi dari SSE ke Streamable HTTP dalam aplikasi MCP anda:

- **Kemas kini kod pelayan** untuk menggunakan `transport="streamable-http"` dalam `mcp.run()`.
- **Kemas kini kod klien** untuk menggunakan `streamablehttp_client` menggantikan klien SSE.
- **Implimentasikan pengendali mesej** dalam klien untuk memproses notifikasi.
- **Uji keserasian** dengan alat dan aliran kerja sedia ada.

### Mengekalkan Keserasian

Adalah disarankan untuk mengekalkan keserasian dengan klien SSE sedia ada semasa proses migrasi. Berikut adalah beberapa strategi:

- Anda boleh menyokong kedua-dua SSE dan Streamable HTTP dengan menjalankan kedua-dua pengangkutan pada titik akhir berbeza.
- Migrasi klien secara berperingkat ke pengangkutan baru.

### Cabaran

Pastikan anda menangani cabaran berikut semasa migrasi:

- Memastikan semua klien dikemas kini
- Mengendalikan perbezaan dalam penghantaran notifikasi

### Tugasan: Bina Aplikasi MCP Penstriman Anda Sendiri

**Senario:**
Bina pelayan dan klien MCP di mana pelayan memproses senarai item (contoh, fail atau dokumen) dan menghantar notifikasi untuk setiap item yang diproses. Klien harus memaparkan setiap notifikasi semasa tiba.

**Langkah:**

1. Laksanakan alat pelayan yang memproses senarai dan menghantar notifikasi untuk setiap item.
2. Laksanakan klien dengan pengendali mesej untuk memaparkan notifikasi secara masa nyata.
3. Uji pelaksanaan anda dengan menjalankan kedua-dua pelayan dan klien, dan perhatikan notifikasi.

[Penyelesaian](./solution/README.md)

## Bacaan Lanjut & Apa Seterusnya?

Untuk meneruskan perjalanan anda dengan penstriman MCP dan mengembangkan pengetahuan anda, bahagian ini menyediakan sumber tambahan dan langkah seterusnya yang disyorkan untuk membina aplikasi yang lebih maju.

### Bacaan Lanjut

- [Microsoft: Pengenalan kepada Penstriman HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS dalam ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Permintaan Penstriman](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Apa Seterusnya?

- Cuba bina alat MCP yang lebih maju yang menggunakan penstriman untuk analitis masa nyata, sembang, atau penyuntingan kolaboratif.
- Terokai integrasi penstriman MCP dengan rangka kerja frontend (React, Vue, dll.) untuk kemas kini UI langsung.
- Seterusnya: [Menggunakan AI Toolkit untuk VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->