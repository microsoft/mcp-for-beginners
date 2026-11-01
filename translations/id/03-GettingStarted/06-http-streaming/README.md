# Streaming HTTPS dengan Model Context Protocol (MCP)

Bab ini memberikan panduan komprehensif untuk mengimplementasikan streaming yang aman, skalabel, dan real-time dengan Model Context Protocol (MCP) menggunakan HTTPS. Ini mencakup motivasi untuk streaming, mekanisme transport yang tersedia, cara mengimplementasikan HTTP yang dapat di-stream dalam MCP, praktik keamanan terbaik, migrasi dari SSE, dan panduan praktis untuk membangun aplikasi streaming MCP Anda sendiri.

> [!WARNING]
> Contoh implementasi dalam pelajaran ini menargetkan **Spesifikasi MCP
> `2025-11-25`** dan menunjukkan handshake legacy `initialize`,
> `Mcp-Session-Id`, GET event stream, dan model dapat dilanjutkan. MCP `2026-07-28`
> menghapus fitur-fitur tersebut. Permintaan HTTP yang dapat di-stream saat ini adalah permintaan POST mandiri
> dengan header `MCP-Protocol-Version` dan `Mcp-Method`, plus
> `Mcp-Name` jika diperlukan. Lihat
> [Perubahan dalam MCP: Spesifikasi 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> sebelum menggunakan contoh ini dalam implementasi baru.

## Mekanisme Transport dan Streaming dalam MCP

Bagian ini mengeksplorasi berbagai mekanisme transport yang tersedia dalam MCP dan perannya dalam memungkinkan kemampuan streaming untuk komunikasi real-time antara klien dan server.

### Apa itu Mekanisme Transport?

Mekanisme transport mendefinisikan bagaimana data dipertukarkan antara klien dan server. MCP mendukung berbagai jenis transport untuk menyesuaikan dengan lingkungan dan kebutuhan yang berbeda:

- **stdio**: Input/output standar, cocok untuk alat lokal dan berbasis CLI. Sederhana tetapi tidak cocok untuk web atau cloud.
- **HTTP+SSE**: Transport remote legacy, yang sudah usang dalam MCP `2025-03-26`
    dan digantikan oleh Streamable HTTP. Jangan gunakan untuk implementasi baru.
- **Streamable HTTP**: Transport streaming modern berbasis HTTP, mendukung notifikasi dan skala yang lebih baik. Direkomendasikan untuk sebagian besar skenario produksi dan cloud.

### Tabel Perbandingan

Lihat tabel perbandingan di bawah ini untuk memahami perbedaan antara mekanisme transport ini:

| Transport | Status | Notifikasi | Penggunaan tipikal |
|---|---|---|---|
| stdio | Saat ini | Ya | Subproses lokal |
| HTTP+SSE | Usang | Ya | Implementasi remote legacy |
| Streamable HTTP | Saat ini | Ya | Server remote dan cloud |

> **Tip:** Memilih transport yang tepat berdampak pada performa, skalabilitas, dan pengalaman pengguna. **Streamable HTTP** direkomendasikan untuk aplikasi modern, skalabel, dan siap cloud.

Transport standar adalah stdio dan Streamable HTTP. HTTP+SSE hanya muncul dalam
contoh lama saja.

## Streaming: Konsep dan Motivasi

Memahami konsep dasar dan motivasi di balik streaming sangat penting untuk mengimplementasikan sistem komunikasi real-time yang efektif.

**Streaming** adalah teknik dalam pemrograman jaringan yang memungkinkan data dikirim dan diterima dalam potongan-potongan kecil yang mudah dikelola atau sebagai rangkaian kejadian, alih-alih menunggu seluruh respons siap. Ini sangat berguna untuk:

- File atau dataset besar.
- Pembaruan real-time (misalnya, obrolan, bilah kemajuan).
- Perhitungan panjang yang ingin membuat pengguna tetap terinformasi.

Berikut yang perlu Anda ketahui tentang streaming secara garis besar:

- Data dikirim secara bertahap, bukan sekaligus.
- Klien dapat memproses data saat tiba.
- Mengurangi latensi yang dirasakan dan meningkatkan pengalaman pengguna.

### Mengapa menggunakan streaming?

Alasan menggunakan streaming adalah sebagai berikut:

- Pengguna mendapatkan umpan balik segera, bukan hanya di akhir
- Mendukung aplikasi real-time dan UI yang responsif
- Penggunaan sumber daya jaringan dan komputasi yang lebih efisien

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

Contoh ini menunjukkan server mengirim serangkaian pesan ke klien saat mereka tersedia, bukan menunggu semua pesan siap.

**Cara kerjanya:**

- Server menghasilkan setiap pesan saat sudah siap.
- Klien menerima dan mencetak setiap potongan saat tiba.

**Persyaratan:**

- Server harus menggunakan respons streaming (misalnya, `StreamingResponse` di FastAPI).
- Klien harus memproses respons sebagai stream (`stream=True` di requests).
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

- Menggunakan tumpukan reaktif Spring Boot dengan `Flux` untuk streaming
- `ServerSentEvent` menyediakan streaming event terstruktur dengan jenis event
- `WebClient` dengan `bodyToFlux()` memungkinkan konsumsi streaming reaktif
- `delayElements()` mensimulasikan waktu proses antar event
- Event dapat memiliki tipe (`info`, `result`) untuk penanganan klien yang lebih baik

### Perbandingan: Streaming Klasik vs Streaming MCP

Perbedaan bagaimana streaming bekerja secara "klasik" dibanding bagaimana cara kerjanya di MCP dapat digambarkan seperti ini:

| Fitur                  | Streaming HTTP Klasik          | Streaming MCP (Notifikasi)          |
|------------------------|-------------------------------|------------------------------------|
| Respon utama           | Potongan                      | Tunggal, di akhir                   |
| Pembaruan progres      | Dikirim sebagai potongan data | Dikirim sebagai notifikasi          |
| Persyaratan klien      | Harus memproses stream        | Harus mengimplementasikan handler pesan |
| Kasus penggunaan       | File besar, streaming token AI| Progres, log, umpan balik waktu nyata|

### Perbedaan Utama yang Diamati

Berikut beberapa perbedaan utama:

- **Polanya Komunikasi:**
  - Streaming HTTP klasik: Menggunakan enkoding transfer chunked sederhana untuk mengirim data dalam potongan
  - Streaming MCP: Menggunakan sistem notifikasi terstruktur dengan protokol JSON-RPC

- **Format Pesan:**
  - HTTP klasik: Potongan teks biasa dengan baris baru
  - MCP: Objek LoggingMessageNotification terstruktur dengan metadata

- **Implementasi Klien:**
  - HTTP klasik: Klien sederhana yang memproses respons streaming
  - MCP: Klien lebih canggih dengan handler pesan untuk memproses berbagai tipe pesan

- **Pembaruan Progres:**
  - HTTP klasik: Progres menjadi bagian dari stream respons utama
  - MCP: Progres dikirim lewat pesan notifikasi terpisah sedangkan respons utama datang di akhir

### Rekomendasi

Berikut beberapa hal yang kami rekomendasikan saat memilih antara implementasi streaming klasik (seperti endpoint yang kami tunjukkan di atas menggunakan `/stream`) dibanding memilih streaming lewat MCP.

- **Untuk kebutuhan streaming sederhana:** Streaming HTTP klasik lebih mudah diimplementasikan dan sudah cukup untuk kebutuhan dasar streaming.

- **Untuk aplikasi kompleks dan interaktif:** Streaming MCP memberikan pendekatan lebih terstruktur dengan metadata yang lebih kaya dan pemisahan antara notifikasi dan hasil akhir.

- **Untuk aplikasi AI:** Sistem notifikasi MCP sangat berguna untuk tugas AI yang berjalan lama dimana Anda ingin terus memberi tahu pengguna tentang progres.

## Streaming di MCP

Baik, jadi Anda sudah melihat beberapa rekomendasi dan perbandingan sejauh ini mengenai perbedaan antara streaming klasik dan streaming di MCP. Sekarang mari kita bahas secara rinci bagaimana Anda bisa memanfaatkan streaming di MCP.

Memahami bagaimana streaming bekerja dalam kerangka MCP sangat penting untuk membangun aplikasi responsif yang memberikan umpan balik waktu nyata kepada pengguna selama operasi yang berjalan lama.

Di MCP, streaming bukan tentang mengirim respons utama dalam potongan, tetapi tentang mengirim **notifikasi** ke klien saat sebuah alat memproses permintaan. Notifikasi ini dapat mencakup pembaruan progres, log, atau event lain.

### Cara kerjanya

Hasil utama masih dikirim sebagai respons tunggal. Namun, notifikasi dapat dikirim sebagai pesan terpisah selama pemrosesan dan dengan demikian memperbarui klien secara waktu nyata. Klien harus dapat menangani dan menampilkan notifikasi ini.

### Latihan opsional: sambungkan ke server MCP yang di-host

Anda juga bisa menggunakan Streamable HTTP tanpa menjalankan server lokal. Contoh ini
terhubung ke [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
menemukan alat-alatnya, dan mencari dokumentasi MCP publik menggunakan
SDK Python yang sama dengan [klien lokal](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Endpoint anonim Parallel tidak memerlukan akun atau kunci API. Akses gratis
memiliki batasan kecepatan. Menjalankan skrip ini mengirimkan kueri pencarian, tujuan, dan
pengenal sesi acak ke Parallel. Layanan ini juga menawarkan `web_fetch`,
yang mengirim URL yang diminta dan konteks yang disediakan ke Parallel. Gunakan informasi publik
untuk latihan ini; lihat [ketentuannya](https://parallel.ai/customer-terms)
dan [kebijakan privasinya](https://parallel.ai/privacy-policy).

Dengan Python 3.10 atau lebih baru dan lingkungan virtual aktif, pasang SDK:

```sh
python -m pip install "mcp>=1.10,<2"
```

Simpan sebagai `hosted_search.py` dan jalankan `python hosted_search.py`:

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
yang berisi URL sumber dan kutipan. Hasil bisa bervariasi atau kosong.
Skrip memeriksa `isError` karena alat bisa gagal meski permintaan HTTP berhasil.
Jika akses dibatasi kecepatannya, tunggu sebelum mencoba lagi. Gunakan kembali
`session_id` yang sama jika Anda memperluas skrip dengan panggilan pencarian atau pengambilan terkait.

Streamable HTTP memperbolehkan respons JSON dan SSE; server ini bisa mengembalikan
hasil JSON lengkap tanpa notifikasi progres. SDK menangani
transportasinya. Lanjutkan dengan contoh lokal di bawah untuk mempelajari tentang notifikasi.
Skrip opsional ini melakukan satu pencarian eksplisit dan menutup koneksi saat
selesai. Jika nanti Anda mengekspos alat-alat ini ke agen, agen mungkin memanggil
mereka selama pekerjaannya; perlakukan teks web yang diambil sebagai data yang tidak terpercaya.

## Apa itu Notifikasi?

Kami menyebut "Notifikasi", apa artinya dalam konteks MCP?

Notifikasi adalah pesan JSON-RPC yang tidak memiliki `id` dan tidak
menerima respons. MCP menggunakan notifikasi untuk progres, pembatalan, dan
peristiwa satu arah lainnya.

Dalam MCP `2025-11-25`, klien mengirim `notifications/initialized` setelah
handshake inisialisasi. MCP `2026-07-28` tidak memiliki handshake inisialisasi, jadi
notifikasi ini adalah perilaku warisan (legacy).

Suatu notifikasi terlihat seperti pesan JSON berikut:

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
tipe pesan JSON-RPC umum.

> **Tidak lagi digunakan di MCP `2026-07-28`:** fitur Logging tetap tersedia
> untuk kompatibilitas tetapi layak dihapus dalam revisi spesifikasi pertama
> yang dirilis pada atau setelah 28 Juli 2027. Implementasi baru harus menggunakan
> `stderr` dengan stdio atau OpenTelemetry untuk observabilitas terstruktur.

Untuk implementasi `2025-11-25` lama, server mengaktifkan kemampuan Logging
sebagai berikut:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Tergantung pada SDK yang digunakan, pencatatan mungkin diaktifkan secara default, atau Anda mungkin perlu mengaktifkannya secara eksplisit dalam konfigurasi server Anda.

Ada berbagai jenis notifikasi:

| Level     | Deskripsi                     | Contoh Kasus Penggunaan        |
|-----------|-------------------------------|---------------------------------|
| debug     | Informasi debugging terperinci | Titik masuk/keluar fungsi     |
| info      | Pesan informasional umum      | Pembaruan kemajuan operasi     |
| notice    | Peristiwa normal namun signifikan | Perubahan konfigurasi        |
| warning   | Kondisi peringatan            | Penggunaan fitur yang usang    |
| error     | Kondisi error                 | Kegagalan operasi              |
| critical  | Kondisi kritis                | Kegagalan komponen sistem       |
| alert     | Aksi harus diambil segera    | Terjadi deteksi korupsi data   |
| emergency | Sistem tidak dapat digunakan  | Kegagalan sistem total         |

## Mengimplementasikan Notifikasi di MCP

Untuk mengimplementasikan notifikasi di MCP, Anda perlu menyiapkan sisi server dan klien untuk menangani pembaruan waktu nyata. Ini memungkinkan aplikasi Anda memberikan umpan balik segera kepada pengguna selama operasi yang berjalan lama.

### Sisi Server: Mengirim Notifikasi

Mari mulai dengan sisi server. Di MCP, Anda mendefinisikan tools yang dapat mengirim notifikasi saat memproses permintaan. Server menggunakan objek context (biasanya `ctx`) untuk mengirim pesan ke klien.

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

Selain itu, untuk mengaktifkan notifikasi, pastikan server Anda menggunakan transportasi streaming (seperti `streamable-http`) dan klien Anda mengimplementasikan pengelola pesan untuk memproses notifikasi. Berikut cara mengatur server untuk menggunakan transportasi `streamable-http`:

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

Dalam contoh .NET ini, alat `ProcessFiles` diberi atribut `Tool` dan mengirim tiga notifikasi ke klien saat memproses setiap file. Metode `ctx.Info()` digunakan untuk mengirim pesan informasional.

Untuk mengaktifkan notifikasi di server MCP .NET Anda, pastikan Anda menggunakan transportasi streaming:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Sisi Klien: Menerima Notifikasi

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

Dalam kode sebelumnya, fungsi `message_handler` memeriksa apakah pesan yang masuk adalah notifikasi. Jika iya, ia mencetak notifikasi tersebut; jika tidak, ia memprosesnya sebagai pesan server biasa. Juga perhatikan bagaimana `ClientSession` diinisialisasi dengan `message_handler` untuk menangani notifikasi yang masuk.

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

Dalam contoh .NET ini, fungsi `MessageHandler` memeriksa apakah pesan yang masuk adalah notifikasi. Jika iya, ia mencetak notifikasi tersebut; jika tidak, ia memprosesnya sebagai pesan server biasa. `ClientSession` diinisialisasi dengan handler pesan melalui `ClientSessionOptions`.

Untuk mengaktifkan notifikasi, pastikan server Anda menggunakan transport streaming (seperti `streamable-http`) dan klien Anda mengimplementasikan handler pesan untuk memproses notifikasi.

## Notifikasi & Skenario Progres

Bagian ini menjelaskan konsep notifikasi progres dalam MCP, mengapa itu penting, dan cara mengimplementasikannya menggunakan Streamable HTTP. Anda juga akan menemukan tugas praktis untuk memperkuat pemahaman Anda.

Notifikasi progres adalah pesan waktu nyata yang dikirim dari server ke klien selama operasi yang berlangsung lama. Alih-alih menunggu seluruh proses selesai, server terus memperbarui klien tentang status saat ini. Ini meningkatkan transparansi, pengalaman pengguna, dan memudahkan debugging.

**Contoh:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Mengapa Menggunakan Notifikasi Progres?

Notifikasi progres penting karena beberapa alasan:

- **Pengalaman pengguna yang lebih baik:** Pengguna melihat pembaruan saat pekerjaan berlangsung, bukan hanya di akhir.
- **Umpan balik waktu nyata:** Klien dapat menampilkan progress bar atau log, membuat aplikasi terasa responsif.
- **Debugging dan pemantauan yang lebih mudah:** Pengembang dan pengguna dapat melihat di mana proses mungkin lambat atau macet.

### Cara Mengimplementasikan Notifikasi Progres

Berikut cara Anda dapat mengimplementasikan notifikasi progres dalam MCP:

- **Di server:** Gunakan `ctx.info()` atau `ctx.log()` untuk mengirim notifikasi saat setiap item diproses. Ini mengirimkan pesan ke klien sebelum hasil utama siap.
- **Di klien:** Implementasikan handler pesan yang mendengarkan dan menampilkan notifikasi saat tiba. Handler ini membedakan antara notifikasi dan hasil akhir.

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

Berikut beberapa pertimbangan keamanan utama:

- **Validasi Header Origin**: Selalu validasi header `Origin` untuk mencegah serangan DNS rebinding.
- **Binding Localhost**: Untuk pengembangan lokal, ikat server ke `localhost` untuk menghindari eksposur ke internet publik.
- **Otentikasi**: Terapkan otentikasi (misalnya kunci API, OAuth) untuk penyebaran produksi.
- **CORS**: Konfigurasikan kebijakan Cross-Origin Resource Sharing (CORS) untuk membatasi akses.
- **HTTPS**: Gunakan HTTPS di produksi untuk mengenkripsi lalu lintas.

### Praktik Terbaik

Selain itu, berikut beberapa praktik terbaik yang harus diikuti saat mengimplementasikan keamanan di server streaming MCP Anda:

- Jangan pernah mempercayai permintaan masuk tanpa validasi.
- Catat dan pantau semua akses dan kesalahan.
- Perbarui dependensi secara rutin untuk menambal kerentanan keamanan.

### Tantangan

Anda akan menghadapi beberapa tantangan saat mengimplementasikan keamanan di server streaming MCP:

- Menyeimbangkan keamanan dengan kemudahan pengembangan
- Memastikan kompatibilitas dengan berbagai lingkungan klien


## Upgrade dari SSE ke Streamable HTTP

Untuk aplikasi yang saat ini menggunakan Server-Sent Events (SSE), migrasi ke Streamable HTTP menawarkan kemampuan yang lebih baik dan keberlanjutan jangka panjang yang lebih baik untuk implementasi MCP Anda.

### Mengapa Upgrade?

Ada dua alasan kuat untuk upgrade dari SSE ke Streamable HTTP:

- Streamable HTTP menawarkan skalabilitas, kompatibilitas, dan dukungan notifikasi yang lebih kaya dibandingkan SSE.
- Ini adalah transport yang direkomendasikan untuk aplikasi MCP baru.

### Langkah Migrasi

Berikut cara Anda dapat bermigrasi dari SSE ke Streamable HTTP dalam aplikasi MCP Anda:

- **Perbarui kode server** untuk menggunakan `transport="streamable-http"` di `mcp.run()`.
- **Perbarui kode klien** untuk menggunakan `streamablehttp_client` menggantikan klien SSE.
- **Implementasikan handler pesan** di klien untuk memproses notifikasi.
- **Uji kompatibilitas** dengan alat dan alur kerja yang sudah ada.

### Mempertahankan Kompatibilitas

Disarankan untuk mempertahankan kompatibilitas dengan klien SSE yang ada selama proses migrasi. Berikut beberapa strategi:

- Anda dapat mendukung SSE dan Streamable HTTP dengan menjalankan kedua transport pada endpoint berbeda.
- Migrasikan klien ke transport baru secara bertahap.

### Tantangan

Pastikan Anda menangani tantangan berikut selama migrasi:

- Memastikan semua klien diperbarui
- Menangani perbedaan dalam pengiriman notifikasi

### Tugas: Bangun Aplikasi MCP Streaming Anda Sendiri

**Skenario:**
Bangun server dan klien MCP di mana server memproses daftar item (misalnya, file atau dokumen) dan mengirim notifikasi untuk setiap item yang diproses. Klien harus menampilkan setiap notifikasi saat tiba.

**Langkah-langkah:**

1. Implementasikan alat server yang memproses daftar dan mengirim notifikasi untuk setiap item.
2. Implementasikan klien dengan handler pesan untuk menampilkan notifikasi secara waktu nyata.
3. Uji implementasi Anda dengan menjalankan server dan klien, dan amati notifikasi.

[Solusi](./solution/README.md)

## Bacaan Lanjutan & Selanjutnya?

Untuk melanjutkan perjalanan Anda dengan streaming MCP dan memperluas pengetahuan, bagian ini menyediakan sumber daya tambahan dan langkah berikut yang disarankan untuk membangun aplikasi yang lebih canggih.

### Bacaan Lanjutan

- [Microsoft: Pengantar Streaming HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS di ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Selanjutnya?

- Cobalah membangun alat MCP yang lebih canggih yang menggunakan streaming untuk analitik waktu nyata, obrolan, atau pengeditan kolaboratif.
- Jelajahi integrasi streaming MCP dengan framework frontend (React, Vue, dll.) untuk pembaruan UI secara langsung.
- Selanjutnya: [Menggunakan Microsoft Foundry Toolkit untuk Visual Studio Code](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->