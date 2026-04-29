# Server MCP dengan Transport stdio

> **⚠️ Pembaruan Penting**: Mulai MCP Specification 2025-06-18, transport SSE (Server-Sent Events) mandiri telah **dihapus** dan digantikan oleh transport "Streamable HTTP". Spesifikasi MCP saat ini mendefinisikan dua mekanisme transport utama:
> 1. **stdio** - Input/output standar (direkomendasikan untuk server lokal)
> 2. **Streamable HTTP** - Untuk server jarak jauh yang mungkin menggunakan SSE secara internal
>
> Pelajaran ini telah diperbarui untuk fokus pada **transport stdio**, yang merupakan pendekatan yang direkomendasikan untuk sebagian besar implementasi server MCP.

Transport stdio memungkinkan server MCP berkomunikasi dengan klien melalui stream input dan output standar. Ini adalah mekanisme transport paling umum digunakan dan direkomendasikan dalam spesifikasi MCP saat ini, menyediakan cara yang sederhana dan efisien untuk membangun server MCP yang mudah diintegrasikan dengan berbagai aplikasi klien.

## Ikhtisar

Pelajaran ini membahas cara membangun dan menggunakan Server MCP menggunakan transport stdio.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Membangun Server MCP menggunakan transport stdio.
- Men-debug Server MCP menggunakan Inspector.
- Mengonsumsi Server MCP menggunakan Visual Studio Code.
- Memahami mekanisme transport MCP saat ini dan mengapa stdio direkomendasikan.


## Transport stdio - Cara Kerjanya

Transport stdio adalah salah satu dari dua tipe transport yang didukung dalam spesifikasi MCP saat ini (2025-06-18). Berikut cara kerjanya:

- **Komunikasi Sederhana**: Server membaca pesan JSON-RPC dari input standar (`stdin`) dan mengirim pesan ke output standar (`stdout`).
- **Berbasis proses**: Klien meluncurkan server MCP sebagai subproses.
- **Format Pesan**: Pesan merupakan permintaan, notifikasi, atau respons JSON-RPC individual, dipisahkan oleh baris baru.
- **Logging**: Server BOLEH menulis string UTF-8 ke error standar (`stderr`) untuk tujuan pencatatan.

### Persyaratan Utama:
- Pesan HARUS dipisahkan oleh baris baru dan TIDAK BOLEH mengandung baris baru yang tertanam
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
- Kami membuat instance `StdioServerTransport` dan menghubungkan server ke transport tersebut, memungkinkan komunikasi melalui stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Buat instance server
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
- Mendefinisikan tools menggunakan dekorator
- Menggunakan context manager stdio_server untuk menangani transport

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

Perbedaan utama dengan SSE adalah server stdio:

- Tidak memerlukan pengaturan web server atau endpoint HTTP
- Diluncurkan sebagai subproses oleh klien
- Berkomunikasi melalui stream stdin/stdout
- Lebih sederhana untuk diimplementasikan dan di-debug

## Latihan: Membuat Server stdio

Untuk membuat server kita, kita perlu mengingat dua hal:

- Kita perlu menggunakan web server untuk mengekspos endpoint untuk koneksi dan pesan.
## Lab: Membuat server MCP stdio sederhana

Dalam lab ini, kita akan membuat server MCP sederhana menggunakan transport stdio yang direkomendasikan. Server ini akan mengekspos tools yang dapat dipanggil klien menggunakan Model Context Protocol standar.

### Prasyarat

- Python 3.8 atau lebih baru
- MCP Python SDK: `pip install mcp`
- Pemahaman dasar pemrograman async

Mari mulai dengan membuat server MCP stdio pertama kita:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Konfigurasi pencatatan
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Buat server
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
    # Gunakan transportasi stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Perbedaan utama dari pendekatan SSE yang sudah usang

**Transport Stdio (Standar Saat Ini):**
- Model subproses sederhana - klien meluncurkan server sebagai proses anak
- Komunikasi melalui stdin/stdout menggunakan pesan JSON-RPC
- Tidak perlu pengaturan server HTTP
- Performa dan keamanan lebih baik
- Debugging dan pengembangan lebih mudah

**Transport SSE (Usang sejak MCP 2025-06-18):**
- Membutuhkan server HTTP dengan endpoint SSE
- Pengaturan lebih kompleks dengan infrastruktur web server
- Pertimbangan keamanan tambahan untuk endpoint HTTP
- Sekarang digantikan oleh Streamable HTTP untuk skenario berbasis web

### Membuat server dengan transport stdio

Untuk membuat server stdio kita, kita perlu:

1. **Impor library yang diperlukan** - Kita perlu komponen server MCP dan transport stdio
2. **Buat instance server** - Mendefinisikan server dengan kemampuannya
3. **Definisikan tools** - Menambahkan fungsi yang ingin diekspos
4. **Setel transport** - Konfigurasikan komunikasi stdio
5. **Jalankan server** - Mulai server dan tangani pesan

Mari bangun ini langkah demi langkah:

### Langkah 1: Buat server stdio dasar

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfigurasikan pencatatan
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Buat server
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

### Langkah 2: Tambahkan lebih banyak tools

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

Simpan kode sebagai `server.py` dan jalankan dari command line:

```bash
python server.py
```

Server akan mulai dan menunggu input dari stdin. Ia berkomunikasi menggunakan pesan JSON-RPC melalui transport stdio.

### Langkah 4: Pengujian dengan Inspector

Anda dapat menguji server Anda menggunakan MCP Inspector:

1. Instal Inspector: `npx @modelcontextprotocol/inspector`
2. Jalankan Inspector dan arahkan ke server Anda
3. Uji tools yang telah Anda buat

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debugging server stdio Anda

### Menggunakan MCP Inspector

MCP Inspector adalah alat yang sangat berguna untuk debugging dan pengujian server MCP. Berikut cara menggunakannya dengan server stdio Anda:

1. **Instal Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Jalankan Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Uji server Anda**: Inspector menyediakan antarmuka web di mana Anda bisa:
   - Melihat kemampuan server
   - Menguji tools dengan berbagai parameter
   - Memantau pesan JSON-RPC
   - Debug masalah koneksi

### Menggunakan VS Code

Anda juga bisa men-debug server MCP langsung di VS Code:

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

2. Set breakpoint di kode server Anda
3. Jalankan debugger dan uji dengan Inspector

### Tips debugging umum

- Gunakan `stderr` untuk logging - jangan pernah menulis ke `stdout` karena itu dikhususkan untuk pesan MCP
- Pastikan semua pesan JSON-RPC dipisahkan oleh baris baru
- Uji dengan tools sederhana terlebih dahulu sebelum menambah fungsionalitas kompleks
- Gunakan Inspector untuk memverifikasi format pesan

## Mengonsumsi server stdio Anda di VS Code

Setelah Anda membangun server MCP stdio, Anda dapat mengintegrasikannya dengan VS Code untuk digunakan dengan Claude atau klien MCP lainnya.

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

2. **Restart Claude**: Tutup dan buka kembali Claude untuk memuat konfigurasi server yang baru.

3. **Uji koneksi**: Mulai percakapan dengan Claude dan coba gunakan tools server Anda:
   - "Bisakah kamu menyapaku menggunakan tool greeting?"
   - "Hitung jumlah dari 15 dan 27"
   - "Apa info server?"

### Contoh server stdio TypeScript

Berikut contoh lengkap TypeScript sebagai referensi:

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

// Tambahkan alat
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

Dalam pelajaran yang diperbarui ini, Anda telah belajar cara:

- Membangun server MCP menggunakan **transport stdio** saat ini (pendekatan yang direkomendasikan)
- Memahami mengapa transport SSE dihapus digantikan dengan stdio dan Streamable HTTP
- Membuat tools yang dapat dipanggil oleh klien MCP
- Men-debug server Anda menggunakan MCP Inspector
- Mengintegrasikan server stdio dengan VS Code dan Claude

Transport stdio menyediakan cara yang lebih sederhana, lebih aman, dan lebih cepat untuk membangun server MCP dibandingkan pendekatan SSE yang usang. Ini adalah transport yang direkomendasikan untuk sebagian besar implementasi server MCP sejak spesifikasi 2025-06-18.


### .NET

1. Mari buat beberapa tools terlebih dahulu, untuk ini kita akan membuat file *Tools.cs* dengan isi sebagai berikut:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Latihan: Menguji server stdio Anda

Sekarang setelah Anda membangun server stdio, mari kita uji agar memastikan ia bekerja dengan benar.

### Prasyarat

1. Pastikan Anda sudah menginstal MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Kode server Anda harus sudah disimpan (misal sebagai `server.py`)

### Pengujian dengan Inspector

1. **Mulai Inspector dengan server Anda**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Buka antarmuka web**: Inspector akan membuka jendela browser yang menampilkan kemampuan server Anda.

3. **Uji tools**: 
   - Coba tool `get_greeting` dengan berbagai nama
   - Uji tool `calculate_sum` dengan angka yang berbeda
   - Panggil tool `get_server_info` untuk melihat metadata server

4. **Pantau komunikasi**: Inspector memperlihatkan pesan JSON-RPC yang dipertukarkan antara klien dan server.

### Apa yang harus Anda lihat

Saat server Anda berjalan dengan benar, Anda akan melihat:
- Kemampuan server tercantum di Inspector
- Tools yang tersedia untuk diuji
- Pertukaran pesan JSON-RPC berhasil
- Respon tool ditampilkan di antarmuka

### Masalah umum dan solusinya

**Server tidak mau mulai:**
- Periksa semua dependensi sudah terpasang: `pip install mcp`
- Periksa syntax dan indentasi Python
- Cari pesan kesalahan di konsol

**Tools tidak muncul:**
- Pastikan dekorator `@server.tool()` ada
- Periksa fungsi tools sudah didefinisikan sebelum `main()`
- Pastikan server dikonfigurasi dengan benar

**Masalah koneksi:**
- Pastikan server menggunakan transport stdio dengan benar
- Periksa tidak ada proses lain yang mengganggu
- Verifikasi sintaks perintah Inspector

## Tugas

Cobalah membangun server Anda dengan kemampuan lebih banyak. Lihat [halaman ini](https://api.chucknorris.io/) untuk, misalnya, menambahkan tool yang memanggil API. Anda bebas menentukan seperti apa server itu. Selamat bersenang-senang :)
## Solusi

[Solusi](./solution/README.md) Berikut solusi yang mungkin dengan kode yang berfungsi.

## Poin Penting

Poin penting dari bab ini adalah sebagai berikut:

- Transport stdio merupakan mekanisme yang direkomendasikan untuk server MCP lokal.
- Transport stdio memungkinkan komunikasi lancar antara server dan klien MCP menggunakan stream input dan output standar.
- Anda dapat menggunakan baik Inspector maupun Visual Studio Code untuk mengonsumsi server stdio secara langsung, membuat debugging dan integrasi menjadi mudah.

## Contoh 

- [Java Calculator](../samples/java/calculator/README.md)
- [Calculator .Net](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Sumber Tambahan

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Selanjutnya

## Langkah Berikutnya

Sekarang Anda telah belajar cara membangun server MCP dengan transport stdio, Anda dapat menjelajahi topik yang lebih maju:

- **Selanjutnya**: [HTTP Streaming dengan MCP (Streamable HTTP)](../06-http-streaming/README.md) - Pelajari mekanisme transport lain yang didukung untuk server jarak jauh
- **Lanjutan**: [Praktik Terbaik Keamanan MCP](../../02-Security/README.md) - Terapkan keamanan dalam server MCP Anda
- **Produksi**: [Strategi Deployment](../09-deployment/README.md) - Implementasikan server untuk penggunaan produksi

## Sumber Tambahan

- [Spesifikasi MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Spesifikasi resmi
- [Dokumentasi MCP SDK](https://github.com/modelcontextprotocol/sdk) - Referensi SDK untuk semua bahasa
- [Contoh Komunitas](../../06-CommunityContributions/README.md) - Lebih banyak contoh server dari komunitas

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai ketepatan, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi yang penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->