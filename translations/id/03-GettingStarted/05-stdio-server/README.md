# Server MCP dengan Transport stdio

> **⚠️ Pembaruan Penting**: Mulai MCP Spesifikasi 2025-06-18, transport SSE (Server-Sent Events) mandiri telah **dihapus** dan digantikan dengan transport "Streamable HTTP". Spesifikasi MCP saat ini mendefinisikan dua mekanisme transport utama:
> 1. **stdio** - Input/output standar (direkomendasikan untuk server lokal)
> 2. **Streamable HTTP** - Untuk server jarak jauh yang mungkin menggunakan SSE secara internal
>
> Pelajaran ini telah diperbarui untuk fokus pada **transport stdio**, yang merupakan pendekatan yang direkomendasikan untuk sebagian besar implementasi server MCP.

Transport stdio memungkinkan server MCP berkomunikasi dengan klien melalui aliran input dan output standar. Ini adalah mekanisme transport yang paling umum digunakan dan direkomendasikan dalam spesifikasi MCP saat ini, menyediakan cara yang sederhana dan efisien untuk membangun server MCP yang dapat dengan mudah terintegrasi dengan berbagai aplikasi klien.

## Ikhtisar

Pelajaran ini membahas cara membangun dan menggunakan Server MCP dengan transport stdio.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Membangun Server MCP menggunakan transport stdio.
- Debug Server MCP menggunakan Inspector.
- Menggunakan Server MCP menggunakan Visual Studio Code.
- Memahami mekanisme transport MCP saat ini dan mengapa stdio direkomendasikan.


## Transport stdio - Cara Kerjanya

Transport stdio adalah salah satu dari dua transport standar dalam Spesifikasi MCP
`2026-07-28`. Berikut cara kerjanya:

- **Komunikasi Sederhana**: Server membaca pesan JSON-RPC dari input standar (`stdin`) dan mengirim pesan ke output standar (`stdout`).
- **Berbasis Proses**: Klien meluncurkan server MCP sebagai proses anak.
- **Format Pesan**: Pesan berupa permintaan, notifikasi, atau respons JSON-RPC individual, dipisahkan oleh baris baru.
- **Logging**: Server BOLEH menulis string UTF-8 ke error standar (`stderr`) untuk keperluan logging.

### Persyaratan Kunci:
- Pesan HARUS dipisahkan oleh baris baru dan TIDAK BOLEH mengandung baris baru tertanam
- Server TIDAK BOLEH menulis apa pun ke `stdout` yang bukan pesan MCP valid
- Klien TIDAK BOLEH menulis apa pun ke `stdin` server yang bukan pesan MCP valid

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

Dalam kode sebelumnya:

- Kami mengimpor kelas `Server` dan `StdioServerTransport` dari MCP SDK
- Kami membuat instance server dengan konfigurasi dan kemampuan dasar
- Kami membuat instance `StdioServerTransport` dan menghubungkan server ke sana, memungkinkan komunikasi melalui stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

Dalam kode sebelumnya kami:

- Membuat instance server menggunakan MCP SDK
- Mendefinisikan alat menggunakan dekorator
- Menggunakan manajer konteks stdio_server untuk menangani transport

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Perbedaan utama dari SSE adalah bahwa server stdio:

- Tidak memerlukan pengaturan server web atau endpoint HTTP
- Diluncurkan sebagai proses anak oleh klien
- Berkomunikasi melalui aliran stdin/stdout
- Lebih sederhana untuk diimplementasikan dan debug

## Latihan: Membuat Server stdio

Untuk membuat server kita, kita perlu mengingat dua hal:

- Kita perlu menggunakan server web untuk mengekspos endpoint untuk koneksi dan pesan.
## Lab: Membuat server MCP stdio sederhana

Dalam lab ini, kita akan membuat server MCP sederhana menggunakan transport stdio yang direkomendasikan. Server ini akan mengekspos alat yang dapat dipanggil klien menggunakan Model Context Protocol standar.

### Prasyarat

- Python 3.8 atau lebih baru
- MCP Python SDK: `pip install mcp`
- Pemahaman dasar tentang pemrograman async

Mari mulai dengan membuat server MCP stdio pertama kita:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Perbedaan kunci dari pendekatan SSE yang sudah tidak digunakan

**Transport Stdio (Standar Saat Ini):**
- Model subprocess sederhana - klien meluncurkan server sebagai proses anak
- Komunikasi melalui stdin/stdout menggunakan pesan JSON-RPC
- Tidak perlu pengaturan server HTTP
- Kinerja dan keamanan lebih baik
- Lebih mudah dalam debugging dan pengembangan

**Transport SSE (Tidak Digunakan Mulai MCP 2025-06-18):**
- Memerlukan server HTTP dengan endpoint SSE
- Pengaturan lebih kompleks dengan infrastruktur server web
- Pertimbangan keamanan tambahan untuk endpoint HTTP
- Kini digantikan oleh Streamable HTTP untuk skenario berbasis web

### Membuat server dengan transport stdio

Untuk membuat server stdio kita, kita perlu:

1. **Impor pustaka yang dibutuhkan** - Kita membutuhkan komponen server MCP dan transport stdio
2. **Buat instance server** - Mendefinisikan server dengan kemampuannya
3. **Definisikan alat** - Tambahkan fungsi yang ingin kita ekspos
4. **Atur transport** - Konfigurasikan komunikasi stdio
5. **Jalankan server** - Mulai server dan tangani pesan

Mari kita bangun langkah demi langkah:

### Langkah 1: Membuat server stdio dasar

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Langkah 2: Menambahkan lebih banyak alat

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### Langkah 3: Menjalankan server

Simpan kode sebagai `server.py` dan jalankan dari baris perintah:

```bash
python server.py
```

Server akan mulai dan menunggu input dari stdin. Server berkomunikasi menggunakan pesan JSON-RPC melalui transport stdio.

### Langkah 4: Pengujian dengan Inspector

Anda dapat menguji server Anda menggunakan MCP Inspector:

1. Instal Inspector: `npx @modelcontextprotocol/inspector`
2. Jalankan Inspector dan arahkan ke server Anda
3. Uji alat yang telah Anda buat

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debug server stdio Anda

### Menggunakan MCP Inspector

MCP Inspector adalah alat berharga untuk debugging dan pengujian server MCP. Berikut cara menggunakannya dengan server stdio Anda:

1. **Instal Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Jalankan Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Uji server Anda**: Inspector menyediakan antarmuka web dimana Anda dapat:
   - Melihat kemampuan server
   - Menguji alat dengan parameter berbeda
   - Memantau pesan JSON-RPC
   - Debug masalah koneksi

### Menggunakan VS Code

Anda juga dapat debug server MCP Anda langsung di VS Code:

1. Buat konfigurasi peluncuran di `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Atur breakpoint di kode server Anda
3. Jalankan debugger dan uji dengan Inspector

### Tips debugging umum

- Gunakan `stderr` untuk logging - jangan pernah menulis ke `stdout` karena itu tercadangkan untuk pesan MCP
- Pastikan semua pesan JSON-RPC dipisahkan oleh baris baru
- Uji dengan alat sederhana dulu sebelum menambahkan fungsi kompleks
- Gunakan Inspector untuk memverifikasi format pesan

## Menggunakan server stdio Anda di VS Code

Setelah Anda membangun server MCP stdio Anda, Anda dapat mengintegrasikannya dengan VS Code untuk digunakan dengan Claude atau klien kompatibel MCP lainnya.

### Konfigurasi

1. **Buat file konfigurasi MCP** di `%APPDATA%\Claude\claude_desktop_config.json` (Windows) atau `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Restart Claude**: Tutup dan buka kembali Claude untuk memuat konfigurasi server baru.

3. **Uji koneksi**: Mulai percakapan dengan Claude dan coba gunakan alat server Anda:
   - "Bisakah kamu menyapaku menggunakan alat sapaan?"
   - "Hitung jumlah 15 dan 27"
   - "Apa info server?"

### Contoh server stdio TypeScript

Berikut contoh lengkap TypeScript untuk referensi:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Add tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### Contoh server stdio .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Ringkasan

Dalam pelajaran yang diperbarui ini, Anda telah belajar bagaimana:

- Membangun server MCP menggunakan **transport stdio** saat ini (pendekatan yang direkomendasikan)
- Memahami alasan penghapusan transport SSE dan mengapa stdio dan Streamable HTTP yang dipilih
- Membuat alat yang dapat dipanggil oleh klien MCP
- Debug server Anda menggunakan MCP Inspector
- Mengintegrasikan server stdio Anda dengan VS Code dan Claude

Transport stdio menawarkan cara yang lebih sederhana, lebih aman, dan lebih berkinerja untuk membangun server MCP dibandingkan pendekatan SSE yang sudah tidak digunakan. Ini adalah transport yang direkomendasikan untuk sebagian besar implementasi server MCP sesuai spesifikasi 2025-06-18.


### .NET

1. Mari kita buat beberapa alat terlebih dahulu, untuk ini kita akan membuat file *Tools.cs* dengan isi berikut:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Latihan: Menguji server stdio Anda

Sekarang setelah Anda membangun server stdio, mari uji agar memastikan server berjalan dengan benar.

### Prasyarat

1. Pastikan Anda sudah menginstal MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Kode server Anda sudah tersimpan (misalnya sebagai `server.py`)

### Pengujian dengan Inspector

1. **Mulai Inspector dengan server Anda**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Buka antarmuka web**: Inspector akan membuka jendela browser yang menampilkan kemampuan server Anda.

3. **Uji alat**: 
   - Coba alat `get_greeting` dengan nama berbeda
   - Uji alat `calculate_sum` dengan berbagai angka
   - Panggil alat `get_server_info` untuk melihat metadata server

4. **Pantau komunikasi**: Inspector menampilkan pesan JSON-RPC yang dipertukarkan antara klien dan server.

### Yang harus Anda lihat

Ketika server Anda mulai dengan benar, Anda harus melihat:
- Kemampuan server tercantum di Inspector
- Alat tersedia untuk pengujian
- Pertukaran pesan JSON-RPC berhasil
- Respons alat ditampilkan di antarmuka

### Masalah umum dan solusi

**Server tidak mulai:**
- Periksa apakah semua dependensi sudah terinstal: `pip install mcp`
- Verifikasi sintaks dan indentasi Python
- Cari pesan error di konsol

**Alat tidak muncul:**
- Pastikan dekorator `@server.tool()` ada
- Periksa fungsi alat sudah didefinisikan sebelum `main()`
- Verifikasi server sudah dikonfigurasi dengan benar

**Masalah koneksi:**
- Pastikan server menggunakan transport stdio dengan benar
- Periksa bahwa tidak ada proses lain yang mengganggu
- Verifikasi sintaks perintah Inspector

## Tugas

Cobalah membangun server Anda dengan kemampuan lebih banyak. Lihat [halaman ini](https://api.chucknorris.io/) misalnya untuk menambahkan alat yang memanggil API. Anda tentukan bagaimana seharusnya server tampil. Selamat bersenang-senang :)
## Solusi

[Solusi](./solution/README.md) Berikut solusi yang mungkin dengan kode yang berfungsi.

## Poin Penting

Poin penting dari bab ini adalah:

- Transport stdio adalah mekanisme yang direkomendasikan untuk server MCP lokal.
- Transport stdio memungkinkan komunikasi lancar antara server MCP dan klien menggunakan aliran input dan output standar.
- Anda dapat menggunakan Inspector dan Visual Studio Code untuk menggunakan server stdio secara langsung, memudahkan debugging dan integrasi.

## Contoh 

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Sumber Daya Tambahan

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Apa Selanjutnya

## Langkah Berikutnya

Sekarang Anda telah belajar cara membangun server MCP dengan transport stdio, Anda dapat menjelajahi topik yang lebih lanjut:

- **Berikutnya**: [HTTP Streaming dengan MCP (Streamable HTTP)](../06-http-streaming/README.md) - Pelajari mekanisme transport lain yang didukung untuk server jarak jauh
- **Lanjutan**: [Praktik Terbaik Keamanan MCP](../../02-Security/README.md) - Terapkan keamanan di server MCP Anda
- **Produksi**: [Strategi Penyebaran](../09-deployment/README.md) - Menyebarkan server Anda untuk penggunaan produksi

## Sumber Daya Tambahan

- [Spesifikasi MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Spesifikasi saat ini
- [Dokumentasi MCP SDK](https://github.com/modelcontextprotocol/sdk) - Referensi SDK untuk semua bahasa
- [Contoh Komunitas](../../06-CommunityContributions/README.md) - Contoh server lebih banyak dari komunitas

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->