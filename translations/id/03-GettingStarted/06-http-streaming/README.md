# Streaming HTTPS dengan Model Context Protocol (MCP)

Bab ini memberikan panduan komprehensif untuk mengimplementasikan streaming yang aman, skalabel, dan real-time dengan Model Context Protocol (MCP) menggunakan HTTPS. Bab ini membahas motivasi untuk streaming, mekanisme transport yang tersedia, cara mengimplementasikan HTTP yang dapat distreaming di MCP, praktik terbaik keamanan, migrasi dari SSE, dan panduan praktis untuk membangun aplikasi MCP streaming Anda sendiri.

> [!WARNING]
> Contoh implementasi dalam pelajaran ini ditujukan untuk **Spesifikasi MCP
> `2025-11-25`** dan menunjukkan handshake `initialize` warisan,
> `Mcp-Session-Id`, stream event GET, dan model resumabilitas. MCP `2026-07-28`
> menghapus fitur-fitur tersebut. Permintaan Streamable HTTP saat ini adalah permintaan POST mandiri
> dengan header `MCP-Protocol-Version` dan `Mcp-Method`, plus
> `Mcp-Name` jika diperlukan. Lihat
> [Perubahan di MCP: Spesifikasi 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> sebelum menggunakan contoh ini dalam implementasi baru.

## Mekanisme Transport dan Streaming di MCP

Bagian ini mengeksplorasi berbagai mekanisme transport yang tersedia di MCP dan perannya dalam memungkinkan kemampuan streaming untuk komunikasi real-time antara klien dan server.

### Apa itu Mekanisme Transport?

Mekanisme transport mendefinisikan bagaimana data dipertukarkan antara klien dan server. MCP mendukung beberapa jenis transport untuk menyesuaikan dengan lingkungan dan kebutuhan yang berbeda:

- **stdio**: Input/output standar, cocok untuk alat lokal dan berbasis CLI. Sederhana tapi tidak cocok untuk web atau cloud.
- **HTTP+SSE**: Transport jarak jauh warisan, sudah tidak digunakan di MCP `2025-03-26`
    dan digantikan oleh Streamable HTTP. Jangan gunakan untuk implementasi baru.
- **Streamable HTTP**: Transport streaming berbasis HTTP modern, mendukung notifikasi dan skalabilitas lebih baik. Direkomendasikan untuk kebanyakan skenario produksi dan cloud.

### Tabel Perbandingan

Lihat tabel perbandingan di bawah untuk memahami perbedaan antara mekanisme transport ini:

| Transport | Status | Notifikasi | Penggunaan khas |
|---|---|---|---|
| stdio | Saat ini | Ya | Proses lokal |
| HTTP+SSE | Tidak digunakan | Ya | Implementasi jarak jauh warisan |
| Streamable HTTP | Saat ini | Ya | Server jarak jauh dan cloud |

> **Tip:** Memilih transport yang tepat berdampak pada performa, skalabilitas, dan pengalaman pengguna. **Streamable HTTP** direkomendasikan untuk aplikasi modern, skalabel, dan siap cloud.

Transport standar adalah stdio dan Streamable HTTP. HTTP+SSE hanya muncul pada
contoh lama.

## Streaming: Konsep dan Motivasi

Memahami konsep dasar dan motivasi di balik streaming sangat penting untuk mengimplementasikan sistem komunikasi real-time yang efektif.

**Streaming** adalah teknik dalam pemrograman jaringan yang memungkinkan data dikirim dan diterima dalam potongan kecil yang dapat dikelola atau sebagai urutan peristiwa, daripada menunggu seluruh respons selesai. Ini sangat berguna untuk:

- File besar atau kumpulan data besar.
- Pembaruan real-time (misalnya, obrolan, bar kemajuan).
- Perhitungan berjalan lama dimana Anda ingin menjaga pengguna tetap diberi informasi.

Berikut adalah yang perlu Anda ketahui tentang streaming secara garis besar:

- Data dikirim secara bertahap, tidak sekaligus.
- Klien dapat memproses data saat tiba.
- Mengurangi latensi yang dirasakan dan meningkatkan pengalaman pengguna.

### Mengapa menggunakan streaming?

Alasan menggunakan streaming adalah sebagai berikut:

- Pengguna mendapatkan umpan balik segera, tidak hanya di akhir
- Memungkinkan aplikasi real-time dan UI yang responsif
- Pemanfaatan sumber daya jaringan dan komputasi yang lebih efisien

### Contoh Sederhana: Server & Klien Streaming HTTP

Berikut contoh sederhana bagaimana streaming dapat diimplementasikan:

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

Contoh ini menunjukkan server mengirim serangkaian pesan ke klien saat tersedia, daripada menunggu semua pesan siap.

**Cara kerjanya:**

- Server menghasilkan setiap pesan saat sudah siap.
- Klien menerima dan mencetak setiap potongan saat tiba.

**Persyaratan:**

- Server harus menggunakan response streaming (misalnya, `StreamingResponse` di FastAPI).
- Klien harus memproses response sebagai stream (`stream=True` di requests).
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

**Catatan Implementasi Java:**

- Menggunakan stack reaktif Spring Boot dengan `Flux` untuk streaming
- `ServerSentEvent` menyediakan streaming event terstruktur dengan tipe event
- `WebClient` dengan `bodyToFlux()` memungkinkan konsumsi streaming reaktif
- `delayElements()` mensimulasikan waktu proses antar event
- Event dapat memiliki tipe (`info`, `result`) untuk penanganan klien yang lebih baik

### Perbandingan: Streaming Klasik vs Streaming MCP

Perbedaan bagaimana streaming bekerja secara "klasik" versus di MCP dapat digambarkan seperti ini:

| Fitur                 | Streaming HTTP Klasik         | Streaming MCP (Notifikasi)          |
|-----------------------|-------------------------------|------------------------------------|
| Respons utama          | Chunked                       | Tunggal, di akhir                  |
| Pembaruan kemajuan    | Dikirim sebagai potongan data | Dikirim sebagai notifikasi         |
| Persyaratan klien     | Harus memproses stream         | Harus mengimplementasikan handler pesan |
| Kasus penggunaan      | File besar, stream token AI    | Kemajuan, log, umpan balik real-time |

### Perbedaan Kunci yang Diamati

Selain itu, berikut beberapa perbedaan kunci:

- **Pola Komunikasi:**
  - Streaming HTTP klasik: Menggunakan enkoding transfer chunked sederhana untuk mengirim data dalam potongan
  - Streaming MCP: Menggunakan sistem notifikasi terstruktur dengan protokol JSON-RPC

- **Format Pesan:**
  - HTTP klasik: Potongan teks polos dengan baris baru
  - MCP: Objek LoggingMessageNotification terstruktur dengan metadata

- **Implementasi Klien:**
  - HTTP klasik: Klien sederhana yang memproses respons streaming
  - MCP: Klien lebih canggih dengan handler pesan untuk memproses tipe pesan berbeda

- **Pembaruan Kemajuan:**
  - HTTP klasik: Kemajuan adalah bagian dari stream respons utama
  - MCP: Kemajuan dikirim melalui pesan notifikasi terpisah sementara respons utama datang di akhir

### Rekomendasi

Ada beberapa hal yang kami rekomendasikan ketika memilih antara mengimplementasikan streaming klasik (seperti endpoint yang kami tunjukkan di atas menggunakan `/stream`) versus memilih streaming melalui MCP.

- **Untuk kebutuhan streaming sederhana:** Streaming HTTP klasik lebih mudah diimplementasikan dan cukup untuk kebutuhan streaming dasar.


- **Untuk aplikasi yang kompleks dan interaktif:** Streaming MCP menyediakan pendekatan yang lebih terstruktur dengan metadata yang lebih kaya dan pemisahan antara notifikasi dan hasil akhir.

- **Untuk aplikasi AI:** Sistem notifikasi MCP sangat berguna untuk tugas AI yang berjalan lama di mana Anda ingin terus memberi informasi kepada pengguna tentang kemajuan.

## Streaming di MCP

Baik, jadi Anda telah melihat beberapa rekomendasi dan perbandingan sejauh ini tentang perbedaan antara streaming klasik dan streaming di MCP. Mari kita bahas secara detail bagaimana tepatnya Anda dapat memanfaatkan streaming di MCP.

Memahami bagaimana streaming bekerja dalam kerangka MCP sangat penting untuk membangun aplikasi yang responsif yang memberikan umpan balik waktu nyata kepada pengguna selama operasi yang berjalan lama.

Dalam MCP, streaming bukan tentang mengirim respons utama dalam potongan, tetapi tentang mengirim **notifikasi** ke klien saat alat sedang memproses permintaan. Notifikasi ini bisa berisi pembaruan kemajuan, log, atau acara lainnya.

### Cara kerjanya

Hasil utama masih dikirim sebagai respons tunggal. Namun, notifikasi dapat dikirim sebagai pesan terpisah selama pemrosesan dan dengan demikian memperbarui klien secara waktu nyata. Klien harus dapat menangani dan menampilkan notifikasi ini.

### Latihan opsional: terhubung ke server MCP yang dihosting

Anda juga dapat menggunakan Streamable HTTP tanpa menjalankan server lokal. Contoh ini
terhubung ke [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
menemukan alat-alatnya, dan mencari dokumentasi MCP publik menggunakan
SDK Python yang sama seperti [klien lokal](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Endpoint anonim Parallel tidak memerlukan akun atau kunci API. Akses gratis
dibatasi kecepatannya. Menjalankan skrip ini mengirimkan kueri pencarian, tujuan, dan
pengenal sesi acak ke Parallel. Layanan ini juga menawarkan `web_fetch`,
yang mengirim URL yang diminta dan konteks yang disediakan ke Parallel. Gunakan informasi publik
untuk latihan ini; lihat [ketentuannya](https://parallel.ai/customer-terms)
dan [kebijakan privasinya](https://parallel.ai/privacy-policy).

Dengan Python 3.10 atau versi lebih baru dan lingkungan virtual diaktifkan, instal SDK:

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

Harapkan penemuan mencakup `web_search` dan `web_fetch`, diikuti oleh respons pencarian
yang berisi URL sumber dan kutipan. Hasil dapat bervariasi atau kosong.
Skrip memeriksa `isError` karena alat dapat gagal meskipun permintaan HTTP
berhasil. Jika akses dibatasi kecepatannya, tunggu sebelum mencoba lagi. Gunakan kembali
`session_id` yang sama jika Anda memperluas skrip dengan panggilan pencarian atau fetch terkait.

Streamable HTTP memperbolehkan respons JSON dan SSE; server ini dapat mengembalikan
hasil JSON lengkap tanpa notifikasi kemajuan. SDK menangani
transportasi. Lanjutkan dengan contoh lokal di bawah untuk mempelajari tentang notifikasi.
Skrip opsional ini melakukan satu pencarian eksplisit dan menutup koneksinya saat
selesai. Jika nanti Anda mengekspos alat ini ke agen, agen mungkin memanggil
alat tersebut selama kerjanya; anggap teks web yang diambil sebagai data yang tidak tepercaya.

## Apa itu Notifikasi?

Kami mengatakan "Notifikasi", apa artinya dalam konteks MCP?

Notifikasi adalah pesan JSON-RPC yang tidak memiliki `id` dan tidak
menerima respons. MCP menggunakan notifikasi untuk kemajuan, pembatalan, dan
acara satu arah lainnya.

Dalam MCP `2025-11-25`, klien mengirim `notifications/initialized` setelah
jabat tangan inisialisasi. MCP `2026-07-28` tidak memiliki jabat tangan inisialisasi, jadi
notifikasi ini adalah perilaku warisan.

Notifikasi terlihat seperti ini sebagai pesan JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Logging adalah salah satu fitur yang menggunakan notifikasi; notifikasi sendiri adalah
jenis pesan JSON-RPC umum.

> **Tidak digunakan lagi di MCP `2026-07-28`:** fitur Logging tetap tersedia
> untuk kompatibilitas tetapi berpotensi dihapus pada revisi spesifikasi pertama
> yang dirilis pada atau setelah 28 Juli 2027. Implementasi baru harus menggunakan
> `stderr` dengan stdio atau OpenTelemetry untuk observabilitas terstruktur.

Untuk implementasi warisan `2025-11-25`, server mengaktifkan kemampuan Logging
sebagai berikut:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Tergantung pada SDK yang digunakan, logging mungkin diaktifkan secara default, atau Anda mungkin perlu mengaktifkannya secara eksplisit dalam konfigurasi server Anda.

Ada berbagai jenis notifikasi:

| Level     | Deskripsi                      | Contoh Kasus Penggunaan         |
|-----------|-------------------------------|---------------------------------|
| debug     | Informasi debugging rinci      | Titik masuk/keluar fungsi       |
| info      | Pesan informasi umum           | Pembaruan kemajuan operasi      |
| notice    | Acara normal tapi signifikan   | Perubahan konfigurasi           |
| warning   | Kondisi peringatan             | Penggunaan fitur yang kedaluwarsa|
| error     | Kondisi kesalahan             | Kegagalan operasi               |
| critical  | Kondisi kritis                | Kegagalan komponen sistem       |
| alert     | Harus segera diambil tindakan  | Terdeteksi korupsi data         |
| emergency | Sistem tidak dapat digunakan   | Kegagalan sistem total          |

## Mengimplementasikan Notifikasi di MCP

Untuk mengimplementasikan notifikasi di MCP, Anda perlu menyiapkan sisi server dan klien untuk menangani pembaruan waktu nyata. Ini memungkinkan aplikasi Anda memberikan umpan balik langsung kepada pengguna selama operasi yang berjalan lama.

### Sisi server: Mengirim Notifikasi

Mari mulai dari sisi server. Dalam MCP, Anda mendefinisikan alat yang bisa mengirim notifikasi saat memproses permintaan. Server menggunakan objek konteks (biasanya `ctx`) untuk mengirim pesan ke klien.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Dalam contoh sebelumnya, alat `process_files` mengirim tiga notifikasi ke klien saat memproses setiap file. Metode `ctx.info()` digunakan untuk mengirim pesan informasional.

Selain itu, untuk mengaktifkan notifikasi, pastikan server Anda menggunakan transport streaming (seperti `streamable-http`) dan klien Anda mengimplementasikan pengelola pesan untuk memproses notifikasi. Berikut cara menyiapkan server untuk menggunakan transport `streamable-http`:

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

Dalam contoh .NET ini, alat `ProcessFiles` dihias dengan atribut `Tool` dan mengirim tiga notifikasi ke klien saat memproses setiap file. Metode `ctx.Info()` digunakan untuk mengirim pesan informasional.

Untuk mengaktifkan notifikasi di server MCP .NET Anda, pastikan Anda menggunakan transport streaming:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Sisi klien: Menerima Notifikasi

Klien harus mengimplementasikan pengelola pesan untuk memproses dan menampilkan notifikasi saat mereka tiba.

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

Dalam kode sebelumnya, fungsi `message_handler` memeriksa apakah pesan yang masuk adalah notifikasi. Jika iya, ia mencetak notifikasi tersebut; jika tidak, ia memprosesnya sebagai pesan server biasa. Juga diperhatikan bagaimana `ClientSession` diinisialisasi dengan `message_handler` untuk menangani notifikasi yang masuk.

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


Dalam contoh .NET ini, fungsi `MessageHandler` memeriksa apakah pesan yang masuk adalah notifikasi. Jika iya, itu mencetak notifikasi; jika tidak, memprosesnya sebagai pesan server biasa. `ClientSession` diinisialisasi dengan penangan pesan melalui `ClientSessionOptions`.

Untuk mengaktifkan notifikasi, pastikan server Anda menggunakan transport streaming (seperti `streamable-http`) dan klien Anda mengimplementasikan penangan pesan untuk memproses notifikasi.

## Notifikasi & Skenario Progres

Bagian ini menjelaskan konsep notifikasi progres dalam MCP, mengapa hal ini penting, dan cara mengimplementasikannya menggunakan Streamable HTTP. Anda juga akan menemukan tugas praktis untuk memperkuat pemahaman Anda.

Notifikasi progres adalah pesan waktu nyata yang dikirim dari server ke klien selama operasi yang berjalan lama. Alih-alih menunggu seluruh proses selesai, server terus memperbarui klien tentang status terkini. Ini meningkatkan transparansi, pengalaman pengguna, dan mempermudah debugging.

**Contoh:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Mengapa Menggunakan Notifikasi Progres?

Notifikasi progres penting karena beberapa alasan:

- **Pengalaman pengguna yang lebih baik:** Pengguna melihat pembaruan selama pekerjaan berjalan, bukan hanya di akhir.
- **Umpan balik waktu nyata:** Klien dapat menampilkan progress bar atau log, membuat aplikasi terasa responsif.
- **Mempermudah debugging dan pemantauan:** Pengembang dan pengguna dapat melihat di mana proses mungkin lambat atau terhenti.

### Cara Mengimplementasikan Notifikasi Progres

Berikut cara mengimplementasikan notifikasi progres di MCP:

- **Di server:** Gunakan `ctx.info()` atau `ctx.log()` untuk mengirim notifikasi saat setiap item diproses. Ini mengirim pesan ke klien sebelum hasil utama siap.
- **Di klien:** Implementasikan penangan pesan yang mendengarkan dan menampilkan notifikasi saat tiba. Penangan ini membedakan antara notifikasi dan hasil akhir.

**Contoh Server:**

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

## Pertimbangan Keamanan

Keamanan harus menjadi prioritas utama saat mengimplementasikan server apa pun, terutama saat menggunakan transport berbasis HTTP seperti Streamable HTTP di MCP.

Saat mengimplementasikan server MCP dengan transport berbasis HTTP, keamanan menjadi perhatian utama yang memerlukan perhatian cermat terhadap berbagai vektor serangan dan mekanisme perlindungan.

### Gambaran Umum

Keamanan sangat penting saat mengekspos server MCP melalui HTTP. Streamable HTTP memperkenalkan permukaan serangan baru dan memerlukan konfigurasi yang hati-hati.

Berikut adalah beberapa pertimbangan keamanan kunci:

- **Validasi Header Origin**: Selalu validasi header `Origin` untuk mencegah serangan DNS rebinding.
- **Binding Localhost**: Untuk pengembangan lokal, ikat server ke `localhost` agar tidak terekspos ke internet publik.
- **Autentikasi**: Implementasikan autentikasi (misalnya, kunci API, OAuth) untuk deployment produksi.
- **CORS**: Konfigurasikan kebijakan Cross-Origin Resource Sharing (CORS) untuk membatasi akses.
- **HTTPS**: Gunakan HTTPS pada produksi untuk mengenkripsi lalu lintas.

### Praktik Terbaik

Selain itu, berikut beberapa praktik terbaik yang harus diikuti saat mengimplementasikan keamanan di server streaming MCP Anda:

- Jangan pernah percaya permintaan masuk tanpa validasi.
- Catat dan pantau semua akses dan kesalahan.
- Rutin perbarui dependensi untuk menambal kerentanan keamanan.

### Tantangan

Anda akan menghadapi beberapa tantangan saat mengimplementasikan keamanan di server streaming MCP:

- Menyeimbangkan keamanan dengan kemudahan pengembangan
- Memastikan kompatibilitas dengan berbagai lingkungan klien


## Migrasi dari SSE ke Streamable HTTP

Untuk aplikasi yang saat ini menggunakan Server-Sent Events (SSE), migrasi ke Streamable HTTP memberikan kemampuan yang lebih baik dan keberlanjutan jangka panjang yang lebih baik untuk implementasi MCP Anda.

### Mengapa Upgrade?

Ada dua alasan kuat untuk upgrade dari SSE ke Streamable HTTP:

- Streamable HTTP menawarkan skalabilitas, kompatibilitas, dan dukungan notifikasi yang lebih kaya daripada SSE.
- Ini adalah transport yang direkomendasikan untuk aplikasi MCP baru.

### Langkah Migrasi

Berikut cara migrasi dari SSE ke Streamable HTTP dalam aplikasi MCP Anda:

- **Perbarui kode server** untuk menggunakan `transport="streamable-http"` di `mcp.run()`.
- **Perbarui kode klien** untuk menggunakan `streamablehttp_client` daripada klien SSE.
- **Implementasikan penangan pesan** di klien untuk memproses notifikasi.
- **Uji kompatibilitas** dengan alat dan alur kerja yang ada.

### Mempertahankan Kompatibilitas

Disarankan untuk mempertahankan kompatibilitas dengan klien SSE yang ada selama proses migrasi. Berikut beberapa strategi:

- Anda dapat mendukung SSE dan Streamable HTTP dengan menjalankan kedua transport di endpoint berbeda.
- Migrasi klien secara bertahap ke transport baru.

### Tantangan

Pastikan Anda mengatasi tantangan berikut selama migrasi:

- Memastikan semua klien diperbarui
- Menangani perbedaan dalam pengiriman notifikasi

### Tugas: Bangun Aplikasi Streaming MCP Sendiri

**Skenario:**
Bangun server dan klien MCP di mana server memproses daftar item (misalnya, file atau dokumen) dan mengirim notifikasi untuk setiap item yang diproses. Klien harus menampilkan setiap notifikasi saat tiba.

**Langkah-langkah:**

1. Implementasikan alat server yang memproses daftar dan mengirim notifikasi untuk setiap item.
2. Implementasikan klien dengan penangan pesan untuk menampilkan notifikasi secara real time.
3. Uji implementasi Anda dengan menjalankan server dan klien, dan amati notifikasinya.

[Solusi](./solution/README.md)

## Bacaan Lanjutan & Apa Selanjutnya?

Untuk melanjutkan perjalanan Anda dengan streaming MCP dan memperluas pengetahuan Anda, bagian ini menyediakan sumber daya tambahan dan langkah selanjutnya yang disarankan untuk membangun aplikasi yang lebih maju.

### Bacaan Lanjutan

- [Microsoft: Pengenalan HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS di ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Permintaan Streaming](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Apa Selanjutnya?

- Cobalah membangun alat MCP yang lebih maju yang menggunakan streaming untuk analitik waktu nyata, obrolan, atau pengeditan kolaboratif.
- Jelajahi integrasi streaming MCP dengan framework frontend (React, Vue, dll.) untuk pembaruan UI secara langsung.
- Selanjutnya: [Memanfaatkan AI Toolkit untuk VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->