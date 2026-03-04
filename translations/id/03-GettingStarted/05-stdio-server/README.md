# Server MCP dengan transport stdio

> **⚠️ Pembaruan Penting**: Mulai dari Spesifikasi MCP 2025-06-18, transport SSE (Server-Sent Events) mandiri telah **dihapus** dan digantikan oleh transport "Streamable HTTP". Spesifikasi MCP saat ini mendefinisikan dua mekanisme transport utama:
> 1. **stdio** - Input/output standar (direkomendasikan untuk server lokal)
> 2. **Streamable HTTP** - Untuk server jarak jauh yang mungkin menggunakan SSE secara internal
>
> Pelajaran ini telah diperbarui untuk memfokuskan pada **transport stdio**, yang merupakan pendekatan yang direkomendasikan untuk sebagian besar implementasi server MCP.

Transport stdio memungkinkan server MCP berkomunikasi dengan klien melalui aliran input dan output standar. Ini adalah mekanisme transport yang paling sering digunakan dan direkomendasikan dalam spesifikasi MCP saat ini, memberikan cara yang sederhana dan efisien untuk membangun server MCP yang dapat dengan mudah diintegrasikan dengan berbagai aplikasi klien.

## Ikhtisar

Pelajaran ini membahas cara membangun dan menggunakan Server MCP menggunakan transport stdio.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan bisa:

- Membangun Server MCP menggunakan transport stdio.
- Debug Server MCP menggunakan Inspector.
- Menggunakan Server MCP dengan Visual Studio Code.
- Memahami mekanisme transport MCP saat ini dan alasan stdio direkomendasikan.

## Transport stdio - Cara Kerja

Transport stdio adalah salah satu dari dua jenis transport yang didukung dalam spesifikasi MCP saat ini (2025-06-18). Cara kerjanya sebagai berikut:

- **Komunikasi Sederhana**: Server membaca pesan JSON-RPC dari input standar (`stdin`) dan mengirim pesan ke output standar (`stdout`).
- **Berbasis Proses**: Klien menjalankan server MCP sebagai proses anak.
- **Format Pesan**: Pesan adalah permintaan JSON-RPC, notifikasi, atau respons individual yang dipisahkan oleh baris baru.
- **Logging**: Server DAPAT menulis string UTF-8 ke error standar (`stderr`) untuk keperluan logging.

### Persyaratan Utama:
- Pesan HARUS dipisahkan oleh baris baru dan TIDAK BOLEH berisi baris baru tertanam
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
```

Dalam kode sebelumnya:

- Kami mengimpor kelas `Server` dan `StdioServerTransport` dari MCP SDK
- Kami membuat instance server dengan konfigurasi dan kapabilitas dasar

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
- Mendefinisikan alat menggunakan dekorator
- Menggunakan pengelola konteks stdio_server untuk menangani transport

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

Perbedaan utama dari SSE adalah server stdio:

- Tidak membutuhkan pengaturan server web atau endpoint HTTP
- Dijalankan sebagai proses anak oleh klien
- Berkomunikasi lewat aliran stdin/stdout
- Lebih sederhana untuk diimplementasikan dan debugging

## Latihan: Membuat server stdio

Untuk membuat server kita, kita perlu mengingat dua hal:

- Kita perlu menggunakan server web untuk mengekspos endpoint koneksi dan pesan.

## Lab: Membuat server MCP stdio sederhana

Dalam lab ini, kita akan membuat server MCP sederhana menggunakan transport stdio yang direkomendasikan. Server ini akan mengekspos alat yang dapat dipanggil oleh klien menggunakan Protokol Model Context standar.

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

# Konfigurasikan logging
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

## Perbedaan utama dari pendekatan SSE yang sudah dihentikan

**Transport Stdio (Standar Saat Ini):**
- Model subprocess sederhana - klien menjalankan server sebagai proses anak
- Komunikasi melalui stdin/stdout menggunakan pesan JSON-RPC
- Tidak diperlukan setup server HTTP
- Performa dan keamanan yang lebih baik
- Debugging dan pengembangan lebih mudah

**Transport SSE (Dihentikan sejak MCP 2025-06-18):**
- Memerlukan server HTTP dengan endpoint SSE
- Setup lebih kompleks dengan infrastruktur server web
- Pertimbangan keamanan tambahan untuk endpoint HTTP
- Kini digantikan oleh Streamable HTTP untuk skenario berbasis web

### Membuat server dengan transport stdio

Untuk membuat server stdio kita, kita perlu:

1. **Impor pustaka yang diperlukan** - Kita perlu komponen server MCP dan transport stdio
2. **Buat instance server** - Definisikan server dengan kapabilitasnya
3. **Definisikan alat** - Tambahkan fungsi yang ingin diekspos
4. **Siapkan transport** - Konfigurasi komunikasi stdio
5. **Jalankan server** - Mulai server dan tangani pesan

Mari bangun ini langkah demi langkah:

### Langkah 1: Membuat server stdio dasar

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

### Langkah 2: Tambahkan lebih banyak alat

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

Server akan mulai dan menunggu input dari stdin. Komunikasi menggunakan pesan JSON-RPC melalui transport stdio.

### Langkah 4: Pengujian dengan Inspector

Anda dapat menguji server Anda menggunakan MCP Inspector:

1. Install Inspector: `npx @modelcontextprotocol/inspector`
2. Jalankan Inspector dan arahkan ke server Anda
3. Uji alat yang telah Anda buat

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debugging server stdio Anda

### Menggunakan MCP Inspector

MCP Inspector adalah alat yang sangat berguna untuk debugging dan pengujian server MCP. Berikut cara menggunakannya dengan server stdio Anda:

1. **Install Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Jalankan Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Uji server Anda**: Inspector menyediakan antarmuka web di mana Anda dapat:
   - Melihat kapabilitas server
   - Menguji alat dengan parameter berbeda
   - Memantau pesan JSON-RPC
   - Debug masalah koneksi

### Menggunakan VS Code

Anda juga bisa melakukan debugging server MCP langsung di VS Code:

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

- Gunakan `stderr` untuk logging - jangan pernah menulis ke `stdout` karena diperuntukkan untuk pesan MCP
- Pastikan semua pesan JSON-RPC dipisahkan dengan baris baru
- Uji dengan alat sederhana terlebih dahulu sebelum menambah fungsi kompleks
- Gunakan Inspector untuk memverifikasi format pesan

## Mengonsumsi server stdio Anda di VS Code

Setelah membangun server MCP stdio, Anda bisa mengintegrasikannya dengan VS Code untuk menggunakannya bersama Claude atau klien kompatibel MCP lainnya.

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
   - "Apa info servernya?"

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

Dalam pelajaran yang diperbarui ini, Anda belajar bagaimana:

- Membangun server MCP menggunakan **transport stdio** saat ini (pendekatan yang direkomendasikan)
- Memahami mengapa transport SSE dihentikan dan diganti dengan stdio dan Streamable HTTP
- Membuat alat yang dapat dipanggil oleh klien MCP
- Debug server menggunakan MCP Inspector
- Mengintegrasikan server stdio Anda dengan VS Code dan Claude

Transport stdio memberikan cara yang lebih sederhana, aman, dan berkinerja lebih baik untuk membangun server MCP dibanding pendekatan SSE yang dihapus. Ini adalah transport yang direkomendasikan untuk sebagian besar implementasi server MCP sejak spesifikasi 2025-06-18.


### .NET

1. Mari buat beberapa alat terlebih dahulu, untuk ini kita akan membuat file *Tools.cs* dengan isi berikut:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Latihan: Menguji server stdio Anda

Sekarang setelah Anda membangun server stdio, mari uji untuk memastikan berfungsi dengan benar.

### Prasyarat

1. Pastikan Anda telah menginstal MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Kode server Anda sudah disimpan (misalnya, `server.py`)

### Pengujian dengan Inspector

1. **Mulai Inspector dengan server Anda**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Buka antarmuka web**: Inspector akan membuka jendela browser yang menampilkan kapabilitas server Anda.

3. **Uji alat**: 
   - Coba alat `get_greeting` dengan nama berbeda
   - Uji alat `calculate_sum` dengan beberapa angka
   - Panggil alat `get_server_info` untuk melihat metadata server

4. **Pantau komunikasi**: Inspector menampilkan pesan JSON-RPC yang dipertukarkan antara klien dan server.

### Apa yang harus Anda lihat

Saat server berjalan dengan benar, Anda harus melihat:
- Kapabilitas server tercantum di Inspector
- Alat tersedia untuk pengujian
- Pertukaran pesan JSON-RPC berhasil
- Respon alat ditampilkan di antarmuka

### Masalah umum dan solusi

**Server tidak mulai:**
- Periksa semua dependensi sudah terpasang: `pip install mcp`
- Verifikasi sintaks Python dan indentasi
- Cari pesan kesalahan di konsol

**Alat tidak muncul:**
- Pastikan dekorator `@server.tool()` ada
- Periksa fungsi alat didefinisikan sebelum `main()`
- Pastikan server dikonfigurasi dengan benar

**Masalah koneksi:**
- Pastikan server menggunakan transport stdio dengan benar
- Periksa tidak ada proses lain yang mengganggu
- Verifikasi sintaks perintah Inspector

## Tugas

Cobalah kembangkan server Anda dengan lebih banyak kapabilitas. Lihat [halaman ini](https://api.chucknorris.io/) untuk, misalnya, menambahkan alat yang memanggil API. Anda putuskan seperti apa servernya. Selamat bersenang-senang :)

## Solusi

[Solusi](./solution/README.md) Berikut adalah kemungkinan solusi dengan kode yang berfungsi.

## Poin Penting

Poin penting dari bab ini adalah:

- Transport stdio adalah mekanisme yang direkomendasikan untuk server MCP lokal.
- Transport stdio memungkinkan komunikasi lancar antara server MCP dan klien menggunakan aliran input dan output standar.
- Anda dapat menggunakan Inspector dan Visual Studio Code untuk mengonsumsi server stdio secara langsung, membuat debugging dan integrasi lebih mudah.

## Contoh 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Sumber Tambahan

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Apa Selanjutnya

## Langkah Berikutnya

Setelah Anda belajar cara membangun server MCP dengan transport stdio, Anda bisa mengeksplorasi topik lanjutan:

- **Selanjutnya**: [HTTP Streaming dengan MCP (Streamable HTTP)](../06-http-streaming/README.md) - Pelajari mekanisme transport lain yang didukung untuk server jarak jauh
- **Lanjutan**: [Praktik Terbaik Keamanan MCP](../../02-Security/README.md) - Terapkan keamanan di server MCP Anda
- **Produksi**: [Strategi Deploy](../09-deployment/README.md) - Deploy server Anda untuk penggunaan produksi

## Sumber Tambahan

- [Spesifikasi MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Spesifikasi resmi
- [Dokumentasi MCP SDK](https://github.com/modelcontextprotocol/sdk) - Referensi SDK untuk semua bahasa
- [Contoh Komunitas](../../06-CommunityContributions/README.md) - Contoh server lainnya dari komunitas

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan terjemahan yang akurat, mohon diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan jasa penerjemah profesional manusia. Kami tidak bertanggung jawab atas miskomunikasi atau kesalahpahaman yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->