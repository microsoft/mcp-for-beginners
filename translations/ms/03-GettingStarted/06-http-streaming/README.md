# Penstriman HTTPS dengan Protokol Konteks Model (MCP)

Bab ini menyediakan panduan komprehensif untuk melaksanakan penstriman yang selamat, boleh skala, dan masa nyata dengan Protokol Konteks Model (MCP) menggunakan HTTPS. Ia merangkumi motivasi untuk penstriman, mekanisme pengangkutan yang tersedia, cara melaksanakan HTTP yang boleh distrim dalam MCP, amalan terbaik keselamatan, migrasi dari SSE, dan panduan praktikal untuk membina aplikasi MCP penstriman anda sendiri.

> [!WARNING]
> Contoh pelaksanaan dalam pelajaran ini menyasarkan **Spesifikasi MCP
> `2025-11-25`** dan menunjukkan tanda tangan warisan `initialize`,
> `Mcp-Session-Id`, GET aliran acara, dan model sambungan semula. MCP `2026-07-28`
> mengalih keluar ciri-ciri tersebut. Permintaan HTTP Boleh Distrim semasa adalah
> permintaan POST yang berdiri sendiri dengan pengepala `MCP-Protocol-Version` dan `Mcp-Method`,
> serta `Mcp-Name` jika perlu. Lihat
> [Apa yang Berubah dalam MCP: Spesifikasi 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> sebelum menggunakan contoh-contoh ini dalam pelaksanaan baru.

## Mekanisme Pengangkutan dan Penstriman dalam MCP

Bahagian ini meneroka mekanisme pengangkutan berbeza yang tersedia dalam MCP dan peranannya dalam membolehkan keupayaan penstriman untuk komunikasi masa nyata antara klien dan pelayan.

### Apa itu Mekanisme Pengangkutan?

Mekanisme pengangkutan mentakrifkan bagaimana data ditukar antara klien dan pelayan. MCP menyokong pelbagai jenis pengangkutan untuk menyesuaikan dengan persekitaran dan keperluan yang berbeza:

- **stdio**: Input/output standard, sesuai untuk alat tempatan dan berasaskan CLI. Mudah tetapi tidak sesuai untuk web atau awan.
- **HTTP+SSE**: Pengangkutan jauh warisan, telah dihentikan dalam MCP `2025-03-26`
    dan digantikan dengan HTTP Boleh Distrim. Jangan gunakan untuk pelaksanaan baru.
- **HTTP Boleh Distrim**: Pengangkutan berasaskan HTTP moden, menyokong pemberitahuan dan penskalaan lebih baik. Disyorkan untuk kebanyakan senario pengeluaran dan awan.

### Jadual Perbandingan

Lihat jadual perbandingan di bawah untuk memahami perbezaan antara mekanisme pengangkutan ini:

| Pengangkutan | Status | Pemberitahuan | Kegunaan tipikal |
|---|---|---|---|
| stdio | Semasa | Ya | Proses anak tempatan |
| HTTP+SSE | Dihentikan | Ya | Pelaksanaan jauh warisan |
| HTTP Boleh Distrim | Semasa | Ya | Pelayan jauh dan awan |

> **Tip:** Pemilihan pengangkutan yang betul memberi kesan kepada prestasi, penskalaan, dan pengalaman pengguna. **HTTP Boleh Distrim** disyorkan untuk aplikasi moden, boleh skala, dan sedia awan.

Pengangkutan standard adalah stdio dan HTTP Boleh Distrim. HTTP+SSE muncul hanya dalam
contoh lama.

## Penstriman: Konsep dan Motivasi

Memahami konsep asas dan motivasi di sebalik penstriman adalah penting untuk melaksanakan sistem komunikasi masa nyata yang berkesan.

**Penstriman** adalah teknik dalam pengaturcaraan rangkaian yang membolehkan data dihantar dan diterima dalam potongan kecil yang boleh diurus atau sebagai satu urutan acara, bukannya menunggu keseluruhan respons siap. Ini amat berguna untuk:

- Fail atau set data yang besar.
- Kemas kini masa nyata (contoh: sembang, bar kemajuan).
- Pengiraan jangka panjang di mana anda ingin memberitahu pengguna secara berterusan.

Berikut adalah yang anda perlu tahu tentang penstriman pada tahap tinggi:

- Data dihantar secara berperingkat, bukan sekaligus.
- Klien boleh memproses data sewaktu ia sampai.
- Mengurangkan latensi yang dirasai dan memperbaiki pengalaman pengguna.

### Mengapa guna penstriman?

Sebab menggunakan penstriman adalah seperti berikut:

- Pengguna mendapat maklum balas segera, bukan hanya di akhir
- Membolehkan aplikasi masa nyata dan UI yang responsif
- Penggunaan sumber rangkaian dan pengkomputeran lebih cekap

### Contoh Ringkas: Pelayan & Klien Penstriman HTTP

Berikut contoh ringkas bagaimana penstriman boleh dilaksanakan:

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

Contoh ini menunjukkan pelayan menghantar satu siri mesej kepada klien apabila ia tersedia, bukannya menunggu semua mesej siap.

**Bagaimana ia berfungsi:**

- Pelayan menghantar setiap mesej sewaktu siap.
- Klien menerima dan memaparkan setiap potongan sewaktu tiba.

**Keperluan:**

- Pelayan mesti menggunakan respons penstriman (contoh: `StreamingResponse` dalam FastAPI).
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

- Menggunakan rangka reaktif Spring Boot dengan `Flux` untuk penstriman
- `ServerSentEvent` menyediakan penstriman acara berstruktur dengan jenis acara
- `WebClient` dengan `bodyToFlux()` membolehkan penggunaan penstriman reaktif
- `delayElements()` mensimulasikan masa pemprosesan antara acara
- Acara boleh mempunyai jenis (`info`, `result`) untuk pengendalian klien yang lebih baik

### Perbandingan: Penstriman Klasik vs Penstriman MCP

Perbezaan antara bagaimana penstriman berfungsi secara "klasik" berbanding bagaimana ia berfungsi dalam MCP boleh digambarkan seperti berikut:

| Ciri                  | Penstriman HTTP Klasik        | Penstriman MCP (Pemberitahuan)    |
|-----------------------|-------------------------------|----------------------------------|
| Respons utama          | Potongan                      | Tunggal, di hujung                |
| Kemas kini kemajuan    | Dihantar sebagai potongan data| Dihantar sebagai pemberitahuan    |
| Keperluan klien       | Mesti memproses aliran        | Mesti laksanakan pengendal mesej |
| Kegunaan              | Fail besar, aliran token AI   | Kemajuan, log, maklum balas masa nyata |

### Perbezaan Utama Yang Diperhatikan

Selain itu, berikut adalah beberapa perbezaan utama:

- **Corak Komunikasi:**
  - Penstriman HTTP klasik: Menggunakan pengekodan penghantaran potongan mudah untuk menghantar data dalam potongan
  - Penstriman MCP: Menggunakan sistem pemberitahuan berstruktur dengan protokol JSON-RPC

- **Format Mesej:**
  - HTTP klasik: Potongan teks biasa dengan baris baru
  - MCP: Objek LoggingMessageNotification berstruktur dengan metadata

- **Pelaksanaan Klien:**
  - HTTP klasik: Klien mudah yang memproses respons penstriman
  - MCP: Klien lebih canggih dengan pengendal mesej untuk memproses jenis mesej berbeza

- **Kemas Kini Kemajuan:**
  - HTTP klasik: Kemajuan adalah sebahagian daripada aliran respons utama
  - MCP: Kemajuan dihantar melalui mesej pemberitahuan berasingan sementara respons utama datang di hujung

### Cadangan

Terdapat beberapa perkara yang kami cadangkan apabila memilih antara melaksanakan penstriman klasik (seperti titik akhir yang ditunjukkan di atas menggunakan `/stream`) berbanding memilih penstriman melalui MCP.

- **Untuk keperluan penstriman mudah:** Penstriman HTTP klasik lebih mudah untuk dilaksanakan dan mencukupi untuk keperluan penstriman asas.

- **Untuk aplikasi kompleks dan interaktif:** Penstriman MCP menyediakan pendekatan lebih berstruktur dengan metadata yang lebih kaya dan pemisahan antara pemberitahuan dan hasil akhir.

- **Untuk aplikasi AI:** Sistem pemberitahuan MCP sangat berguna untuk tugas AI jangka panjang di mana anda mahu memberi maklumat kemajuan kepada pengguna.

## Penstriman dalam MCP

Baik, jadi anda telah melihat beberapa cadangan dan perbandingan setakat ini tentang perbezaan antara penstriman klasik dan penstriman dalam MCP. Mari kita lihat dengan lebih terperinci bagaimana anda boleh memanfaatkan penstriman dalam MCP.

Memahami bagaimana penstriman berfungsi dalam kerangka MCP penting untuk membina aplikasi responsif yang menyediakan maklum balas masa nyata kepada pengguna semasa operasi jangka panjang.

Dalam MCP, penstriman bukanlah tentang menghantar respons utama secara potongan, tetapi tentang menghantar **pemberitahuan** kepada klien sewaktu alat sedang memproses permintaan. Pemberitahuan ini boleh merangkumi kemas kini kemajuan, log, atau acara lain.

### Bagaimana ia berfungsi

Hasil utama masih dihantar sebagai satu respons tunggal. Walau bagaimanapun, pemberitahuan boleh dihantar sebagai mesej berasingan semasa pemprosesan dan dengan itu mengemas kini klien secara masa nyata. Klien mesti mampu mengendalikan dan memaparkan pemberitahuan ini.

### Latihan pilihan: sambungkan ke pelayan MCP yang dihoskan

Anda juga boleh menggunakan HTTP Boleh Distrim tanpa menjalankan pelayan tempatan. Contoh ini
menyambung ke [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
mencari alatan, dan mencari dokumentasi MCP awam menggunakan SDK Python yang sama
seperti [klien tempatan](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Titik akhir tanpa nama Parallel tidak memerlukan akaun atau kunci API. Akses percuma adalah
had kadar. Menjalankan skrip ini menghantar pertanyaan carian, objektif, dan satu
pengecam sesi rawak ke Parallel. Perkhidmatan ini juga menawarkan `web_fetch`,
yang menghantar URL yang diminta dan sebarang konteks dibekalkan ke Parallel. Gunakan maklumat awam
untuk latihan ini; lihat [terma](https://parallel.ai/customer-terms)
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

Jangkakan penemuan termasuk `web_search` dan `web_fetch`, diikuti dengan respons carian
yang mengandungi URL sumber dan petikan. Keputusan boleh berbeza atau kosong.
Skrip memeriksa `isError` kerana alat boleh gagal walaupun permintaan HTTP
berjaya. Jika akses dibatasi kadar, tunggu sebelum cuba lagi. Gunakan semula
`session_id` yang sama jika anda melanjutkan skrip dengan panggilan carian atau ambil berkaitan.

HTTP Boleh Distrim membenarkan respons JSON dan SSE; pelayan ini boleh mengembalikan
hasil JSON lengkap tanpa pemberitahuan kemajuan. SDK mengendalikan
pengangkutan. Teruskan dengan contoh tempatan di bawah untuk belajar tentang pemberitahuan.
Skrip pilihan ini membuat satu carian jelas dan menutup sambungannya apabila
selesai. Jika anda kemudian mendedahkan alatan ini kepada ejen, ejen mungkin memanggil
mereka semasa kerjanya; anggap teks web yang diperoleh sebagai data yang tidak dipercayai.

## Apa itu Pemberitahuan?

Kami kata "Pemberitahuan", apa maksudnya dalam konteks MCP?

Pemberitahuan ialah mesej JSON-RPC yang tidak mempunyai `id` dan tidak
menerima respons. MCP menggunakan pemberitahuan untuk kemajuan, pembatalan, dan
acara sehala lain.

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

Logging adalah satu ciri yang menggunakan pemberitahuan; pemberitahuan itu sendiri adalah
jenis mesej JSON-RPC umum.

> **Dihentikan dalam MCP `2026-07-28`:** ciri Logging kekal tersedia
> untuk keserasian tetapi layak untuk penghapusan dalam semakan spesifikasi pertama
> yang dikeluarkan pada atau selepas 28 Julai 2027. Pelaksanaan baru harus menggunakan
> `stderr` dengan stdio atau OpenTelemetry untuk pemerhatian berstruktur.

Untuk pelaksanaan warisan `2025-11-25`, pelayan mengaktifkan keupayaan Logging
seperti berikut:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Bergantung pada SDK yang digunakan, logging mungkin diaktifkan secara lalai, atau anda mungkin perlu mengaktifkannya secara jelas dalam konfigurasi pelayan anda.

Terdapat jenis pemberitahuan berbeza:

| Tahap     | Penerangan                    | Contoh Kegunaan                |
|-----------|------------------------------|-------------------------------|
| debug     | Maklumat debugging terperinci | Titik masuk/keluar fungsi     |
| info      | Mesej maklumat umum           | Kemas kini kemajuan operasi   |
| notice    | Acara biasa tetapi penting    | Perubahan konfigurasi         |
| warning   | Keadaan amaran                | Penggunaan ciri usang         |
| error     | Keadaan ralat                | Kegagalan operasi             |
| critical  | Keadaan kritikal             | Kegagalan komponen sistem     |
| alert     | Tindakan mesti diambil segera | Pengesanan kerosakan data    |
| emergency | Sistem tidak dapat digunakan | Kegagalan sistem sepenuhnya  |

## Melaksanakan Pemberitahuan dalam MCP

Untuk melaksanakan pemberitahuan dalam MCP, anda perlu menyediakan kedua-dua bahagian pelayan dan klien untuk mengendalikan kemas kini masa nyata. Ini membolehkan aplikasi anda memberi maklum balas segera kepada pengguna semasa operasi jangka panjang.

### Bahagian Pelayan: Menghantar Pemberitahuan

Mari mulakan dengan bahagian pelayan. Dalam MCP, anda mendefinisikan alat yang boleh menghantar pemberitahuan semasa memproses permintaan. Pelayan menggunakan objek konteks (biasanya `ctx`) untuk menghantar mesej kepada klien.

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

Selain itu, untuk membolehkan pemberitahuan, pastikan pelayan anda menggunakan pengangkutan penstriman (seperti `streamable-http`) dan klien anda melaksanakan pengendal mesej untuk memproses pemberitahuan. Berikut cara anda boleh menyediakan pelayan untuk menggunakan pengangkutan `streamable-http`:

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

Dalam contoh .NET ini, alat `ProcessFiles` dihiasi dengan atribut `Tool` dan menghantar tiga pemberitahuan kepada klien semasa memproses setiap fail. Kaedah `ctx.Info()` digunakan untuk menghantar mesej maklumat.

Untuk mengaktifkan pemberitahuan dalam pelayan MCP .NET anda, pastikan anda menggunakan pengangkutan penstriman:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Bahagian Klien: Menerima Pemberitahuan

Klien mesti melaksanakan pengendal mesej untuk memproses dan memaparkan pemberitahuan sewaktu ia tiba.

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

Dalam kod sebelum ini, fungsi `message_handler` memeriksa sama ada mesej masuk ialah notifikasi. Jika ya, ia mencetak notifikasi tersebut; jika tidak, ia memprosesnya sebagai mesej pelayan biasa. Perhatikan juga bagaimana `ClientSession` diinisialisasi dengan `message_handler` untuk mengendalikan notifikasi yang masuk.

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

Dalam contoh .NET ini, fungsi `MessageHandler` memeriksa sama ada mesej masuk ialah notifikasi. Jika ya, ia mencetak notifikasi tersebut; jika tidak, ia memprosesnya sebagai mesej pelayan biasa. `ClientSession` diinisialisasi dengan penangan mesej melalui `ClientSessionOptions`.

Untuk mengaktifkan notifikasi, pastikan pelayan anda menggunakan pengangkutan penstriman (seperti `streamable-http`) dan klien anda melaksanakan penangan mesej untuk memproses notifikasi.

## Notifikasi & Senario Kemajuan

Bahagian ini menerangkan konsep notifikasi kemajuan dalam MCP, mengapa ia penting, dan bagaimana untuk melaksanakannya menggunakan Streamable HTTP. Anda juga akan menemui tugasan praktikal untuk mengukuhkan pemahaman anda.

Notifikasi kemajuan adalah mesej masa nyata yang dihantar dari pelayan ke klien semasa operasi yang memakan masa lama. Daripada menunggu keseluruhan proses selesai, pelayan memastikan klien dikemas kini tentang status semasa. Ini meningkatkan ketelusan, pengalaman pengguna, dan memudahkan penyahpepijatan.

**Contoh:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Mengapa Menggunakan Notifikasi Kemajuan?

Notifikasi kemajuan adalah penting atas beberapa sebab:

- **Pengalaman pengguna yang lebih baik:** Pengguna melihat kemas kini semasa kerja berjalan, bukan hanya pada penghujungnya.
- **Maklum balas masa nyata:** Klien boleh memaparkan bar kemajuan atau log, menjadikan aplikasi rasa responsif.
- **Penyahpepijatan dan pemantauan lebih mudah:** Pembangun dan pengguna boleh melihat di mana proses mungkin perlahan atau tersekat.

### Cara Melaksanakan Notifikasi Kemajuan

Berikut adalah cara anda boleh melaksanakan notifikasi kemajuan dalam MCP:

- **Di pelayan:** Gunakan `ctx.info()` atau `ctx.log()` untuk menghantar notifikasi semasa setiap item diproses. Ini menghantar mesej kepada klien sebelum hasil utama siap.
- **Di klien:** Laksanakan penangan mesej yang mendengar dan memaparkan notifikasi sebaik tiba. Penangan ini membezakan antara notifikasi dan hasil akhir.

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

Keselamatan harus menjadi keutamaan utama apabila melaksanakan mana-mana pelayan, terutamanya apabila menggunakan pengangkutan berasaskan HTTP seperti Streamable HTTP dalam MCP.

Semasa melaksanakan pelayan MCP dengan pengangkutan berasaskan HTTP, keselamatan menjadi keprihatinan utama yang memerlukan perhatian rapi terhadap pelbagai vektor serangan dan mekanisme perlindungan.

### Gambaran Keseluruhan

Keselamatan adalah kritikal ketika mendedahkan pelayan MCP melalui HTTP. Streamable HTTP memperkenalkan permukaan serangan baru dan memerlukan konfigurasi yang teliti.

Berikut adalah beberapa pertimbangan keselamatan utama:

- **Pengesahan Header Origin**: Sentiasa sahkan header `Origin` untuk mengelakkan serangan DNS rebinding.
- **Pengikatan Localhost**: Untuk pembangunan tempatan, pautkan pelayan ke `localhost` untuk mengelakkan pendedahan ke internet awam.
- **Pengesahan**: Laksanakan pengesahan (contoh, kekunci API, OAuth) untuk pengeluaran.
- **CORS**: Konfigurasikan polisi Perkongsian Sumber Rentas (CORS) untuk mengehadkan akses.
- **HTTPS**: Gunakan HTTPS dalam pengeluaran untuk menyulitkan trafik.

### Amalan Terbaik

Selain itu, berikut adalah beberapa amalan terbaik untuk diikuti semasa melaksanakan keselamatan dalam pelayan penstriman MCP anda:

- Jangan sesekali mempercayai permintaan masuk tanpa pengesahan.
- Log dan pantau semua akses dan ralat.
- Kemas kini secara berkala kebergantungan untuk menampal kelemahan keselamatan.

### Cabaran

Anda akan menghadapi beberapa cabaran semasa melaksanakan keselamatan dalam pelayan penstriman MCP:

- Mengimbangi keselamatan dengan kemudahan pembangunan
- Memastikan keserasian dengan pelbagai persekitaran klien


## Naik Taraf dari SSE ke Streamable HTTP

Untuk aplikasi yang kini menggunakan Server-Sent Events (SSE), migrasi ke Streamable HTTP menyediakan keupayaan yang dipertingkatkan dan ketahanan jangka panjang yang lebih baik untuk pelaksanaan MCP anda.

### Mengapa Naik Taraf?

Terdapat dua sebab kukuh untuk naik taraf dari SSE ke Streamable HTTP:

- Streamable HTTP menawarkan kebolehskalaan, keserasian, dan sokongan notifikasi yang lebih kaya berbanding SSE.
- Ia adalah pengangkutan yang disyorkan untuk aplikasi MCP baharu.

### Langkah-Langkah Migrasi

Berikut cara anda boleh migrasi dari SSE ke Streamable HTTP dalam aplikasi MCP anda:

- **Kemas kini kod pelayan** untuk menggunakan `transport="streamable-http"` dalam `mcp.run()`.
- **Kemas kini kod klien** untuk menggunakan `streamablehttp_client` menggantikan klien SSE.
- **Laksanakan penangan mesej** dalam klien untuk memproses notifikasi.
- **Uji keserasian** dengan alat dan alur kerja sedia ada.

### Menjaga Keserasian

Adalah disyorkan untuk mengekalkan keserasian dengan klien SSE yang sedia ada semasa proses migrasi. Berikut adalah beberapa strategi:

- Anda boleh menyokong kedua-dua SSE dan Streamable HTTP dengan menjalankan kedua-dua pengangkutan pada titik akhir yang berbeza.
- Migrasi klien secara berperingkat ke pengangkutan baharu.

### Cabaran

Pastikan anda mengatasi cabaran berikut semasa migrasi:

- Memastikan semua klien dikemas kini
- Menangani perbezaan dalam penghantaran notifikasi

### Tugasan: Bangunkan Aplikasi MCP Penstriman Anda Sendiri

**Senario:**
Bangunkan pelayan dan klien MCP di mana pelayan memproses senarai item (contohnya, fail atau dokumen) dan menghantar notifikasi untuk setiap item yang diproses. Klien harus memaparkan setiap notifikasi sebaik tiba.

**Langkah-Langkah:**

1. Laksanakan alat pelayan yang memproses senarai dan menghantar notifikasi untuk setiap item.
2. Laksanakan klien dengan penangan mesej untuk memaparkan notifikasi secara masa nyata.
3. Uji pelaksanaan anda dengan menjalankan kedua-dua pelayan dan klien, dan perhatikan notifikasi.

[Penyelesaian](./solution/README.md)

## Bacaan Lanjut & Apa Seterusnya?

Untuk meneruskan perjalanan anda dengan penstriman MCP dan mengembangkan pengetahuan anda, bahagian ini menyediakan sumber tambahan dan langkah seterusnya yang dicadangkan untuk membina aplikasi yang lebih maju.

### Bacaan Lanjut

- [Microsoft: Pengenalan kepada Penstriman HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS dalam ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Permintaan Python: Permintaan Penstriman](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Apa Seterusnya?

- Cuba bina alat MCP yang lebih maju yang menggunakan penstriman untuk analitik masa nyata, sembang, atau penyuntingan kolaboratif.
- Terokai integrasi penstriman MCP dengan rangka kerja frontend (React, Vue, dll.) untuk kemas kini UI secara langsung.
- Seterusnya: [Menggunakan Microsoft Foundry Toolkit untuk Visual Studio Code](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->