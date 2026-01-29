# Server MCP dengan Transport stdio

> **⚠️ Pembaruan Penting**: Mulai Spesifikasi MCP 2025-06-18, transport SSE (Server-Sent Events) yang berdiri sendiri telah **dihentikan** dan digantikan oleh transport "Streamable HTTP". Spesifikasi MCP saat ini mendefinisikan dua mekanisme transport utama:
> 1. **stdio** - Input/output standar (direkomendasikan untuk server lokal)
> 2. **Streamable HTTP** - Untuk server jarak jauh yang mungkin menggunakan SSE secara internal
>
> Pelajaran ini telah diperbarui untuk berfokus pada **transport stdio**, yang merupakan pendekatan yang direkomendasikan untuk sebagian besar implementasi server MCP.

Transport stdio memungkinkan server MCP berkomunikasi dengan klien melalui aliran input dan output standar. Ini adalah mekanisme transport yang paling umum digunakan dan direkomendasikan dalam spesifikasi MCP saat ini, menyediakan cara yang sederhana dan efisien untuk membangun server MCP yang dapat dengan mudah diintegrasikan dengan berbagai aplikasi klien.

## Gambaran Umum

Pelajaran ini mencakup cara membangun dan menggunakan server MCP menggunakan transport stdio.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Membangun server MCP menggunakan transport stdio.
- Melakukan debug server MCP menggunakan Inspector.
- Menggunakan server MCP dengan Visual Studio Code.
- Memahami mekanisme transport MCP saat ini dan mengapa stdio direkomendasikan.

## Transport stdio - Cara Kerjanya

Transport stdio adalah salah satu dari dua jenis transport yang didukung dalam spesifikasi MCP saat ini (2025-06-18). Berikut cara kerjanya:

- **Komunikasi Sederhana**: Server membaca pesan JSON-RPC dari input standar (`stdin`) dan mengirim pesan ke output standar (`stdout`).
- **Berbasis Proses**: Klien meluncurkan server MCP sebagai subproses.
- **Format Pesan**: Pesan adalah permintaan, notifikasi, atau respons JSON-RPC individual yang dipisahkan oleh baris baru.
- **Logging**: Server DAPAT menulis string UTF-8 ke kesalahan standar (`stderr`) untuk tujuan logging.

### Persyaratan Utama:
- Pesan HARUS dipisahkan oleh baris baru dan TIDAK BOLEH mengandung baris baru yang tertanam.
- Server TIDAK BOLEH menulis apa pun ke `stdout` yang bukan pesan MCP yang valid.
- Klien TIDAK BOLEH menulis apa pun ke `stdin` server yang bukan pesan MCP yang valid.

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
```

Dalam kode di atas:

- Kami mengimpor kelas `Server` dan `StdioServerTransport` dari MCP SDK.
- Kami membuat instance server dengan konfigurasi dan kapabilitas dasar.

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

Dalam kode di atas, kami:

- Membuat instance server menggunakan MCP SDK.
- Mendefinisikan alat menggunakan dekorator.
- Menggunakan manajer konteks stdio_server untuk menangani transport.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Perbedaan utama dari SSE adalah bahwa server stdio:

- Tidak memerlukan pengaturan server web atau endpoint HTTP.
- Diluncurkan sebagai subproses oleh klien.
- Berkomunikasi melalui aliran stdin/stdout.
- Lebih sederhana untuk diimplementasikan dan di-debug.

## Latihan: Membuat Server stdio

Untuk membuat server kita, kita perlu mengingat dua hal:

- Kita perlu menggunakan server web untuk mengekspos endpoint untuk koneksi dan pesan.

## Lab: Membuat server MCP stdio sederhana

Dalam lab ini, kita akan membuat server MCP sederhana menggunakan transport stdio yang direkomendasikan. Server ini akan mengekspos alat yang dapat dipanggil klien menggunakan Model Context Protocol standar.

### Prasyarat

- Python 3.8 atau lebih baru
- MCP Python SDK: `pip install mcp`
- Pemahaman dasar tentang pemrograman async

Mari kita mulai dengan membuat server MCP stdio pertama kita:

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

## Perbedaan utama dari pendekatan SSE yang dihentikan

**Transport Stdio (Standar Saat Ini):**
- Model subproses sederhana - klien meluncurkan server sebagai proses anak.
- Komunikasi melalui stdin/stdout menggunakan pesan JSON-RPC.
- Tidak memerlukan pengaturan server HTTP.
- Performa dan keamanan lebih baik.
- Debugging dan pengembangan lebih mudah.

**Transport SSE (Dihentikan mulai MCP 2025-06-18):**
- Memerlukan server HTTP dengan endpoint SSE.
- Pengaturan lebih kompleks dengan infrastruktur server web.
- Pertimbangan keamanan tambahan untuk endpoint HTTP.
- Sekarang digantikan oleh Streamable HTTP untuk skenario berbasis web.

### Membuat server dengan transport stdio

Untuk membuat server stdio kita, kita perlu:

1. **Mengimpor pustaka yang diperlukan** - Kita memerlukan komponen server MCP dan transport stdio.
2. **Membuat instance server** - Mendefinisikan server dengan kapabilitasnya.
3. **Mendefinisikan alat** - Menambahkan fungsionalitas yang ingin kita ekspos.
4. **Mengatur transport** - Mengonfigurasi komunikasi stdio.
5. **Menjalankan server** - Memulai server dan menangani pesan.

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

Simpan kode sebagai `server.py` dan jalankan dari command line:

```bash
python server.py
```

Server akan mulai dan menunggu input dari stdin. Komunikasi dilakukan menggunakan pesan JSON-RPC melalui transport stdio.

### Langkah 4: Menguji dengan Inspector

Anda dapat menguji server Anda menggunakan MCP Inspector:

1. Instal Inspector: `npx @modelcontextprotocol/inspector`
2. Jalankan Inspector dan arahkan ke server Anda.
3. Uji alat yang telah Anda buat.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Debugging server stdio Anda

### Menggunakan MCP Inspector

MCP Inspector adalah alat yang berharga untuk debugging dan pengujian server MCP. Berikut cara menggunakannya dengan server stdio Anda:

1. **Instal Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Jalankan Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Uji server Anda**: Inspector menyediakan antarmuka web di mana Anda dapat:
   - Melihat kapabilitas server.
   - Menguji alat dengan parameter berbeda.
   - Memantau pesan JSON-RPC.
   - Debug masalah koneksi.

### Menggunakan VS Code

Anda juga dapat melakukan debug server MCP Anda langsung di VS Code:

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

2. Tetapkan breakpoint di kode server Anda.
3. Jalankan debugger dan uji dengan Inspector.

### Tips debugging umum

- Gunakan `stderr` untuk logging - jangan pernah menulis ke `stdout` karena itu disediakan untuk pesan MCP.
- Pastikan semua pesan JSON-RPC dipisahkan oleh baris baru.
- Uji dengan alat sederhana terlebih dahulu sebelum menambahkan fungsionalitas kompleks.
- Gunakan Inspector untuk memverifikasi format pesan.

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
   - "Bisakah kamu menyapa saya menggunakan alat greeting?"
   - "Hitung jumlah 15 dan 27."
   - "Apa info servernya?"

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
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Ringkasan

Dalam pelajaran yang diperbarui ini, Anda telah mempelajari cara:

- Membangun server MCP menggunakan **transport stdio** (pendekatan yang direkomendasikan).
- Memahami mengapa transport SSE dihentikan demi stdio dan Streamable HTTP.
- Membuat alat yang dapat dipanggil oleh klien MCP.
- Melakukan debug server Anda menggunakan MCP Inspector.
- Mengintegrasikan server stdio Anda dengan VS Code dan Claude.

Transport stdio menyediakan cara yang lebih sederhana, lebih aman, dan lebih cepat untuk membangun server MCP dibandingkan pendekatan SSE yang dihentikan. Ini adalah transport yang direkomendasikan untuk sebagian besar implementasi server MCP sesuai spesifikasi 2025-06-18.

## Sampel

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Sumber Daya Tambahan

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Apa Selanjutnya

## Langkah Berikutnya

Sekarang setelah Anda mempelajari cara membangun server MCP dengan transport stdio, Anda dapat menjelajahi topik yang lebih lanjut:

- **Berikutnya**: [HTTP Streaming dengan MCP (Streamable HTTP)](../06-http-streaming/README.md) - Pelajari mekanisme transport lain yang didukung untuk server jarak jauh.
- **Lanjutan**: [Praktik Terbaik Keamanan MCP](../../02-Security/README.md) - Terapkan keamanan di server MCP Anda.
- **Produksi**: [Strategi Deployment](../09-deployment/README.md) - Deploy server Anda untuk penggunaan produksi.

## Sumber Daya Tambahan

- [Spesifikasi MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Spesifikasi resmi.
- [Dokumentasi MCP SDK](https://github.com/modelcontextprotocol/sdk) - Referensi SDK untuk semua bahasa.
- [Contoh Komunitas](../../06-CommunityContributions/README.md) - Contoh server lainnya dari komunitas.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.