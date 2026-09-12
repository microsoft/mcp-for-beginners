# Server MCP dengan Transportasi stdio

> **⚠️ Pembaruan Penting**: Mulai dari Spesifikasi MCP 2025-06-18, transportasi SSE (Server-Sent Events) mandiri telah **dihentikan** dan digantikan oleh transportasi "Streamable HTTP". Spesifikasi MCP saat ini mendefinisikan dua mekanisme transportasi utama:
> 1. **stdio** - Input/output standar (direkomendasikan untuk server lokal)
> 2. **Streamable HTTP** - Untuk server jarak jauh yang mungkin menggunakan SSE secara internal
>
> Pelajaran ini telah diperbarui untuk fokus pada **transportasi stdio**, yang merupakan pendekatan yang direkomendasikan untuk sebagian besar implementasi server MCP.

Transportasi stdio memungkinkan server MCP berkomunikasi dengan klien melalui aliran input dan output standar. Ini adalah mekanisme transportasi yang paling umum digunakan dan direkomendasikan dalam spesifikasi MCP saat ini, menyediakan cara yang sederhana dan efisien untuk membangun server MCP yang dapat dengan mudah diintegrasikan dengan berbagai aplikasi klien.

## Ikhtisar

Pelajaran ini membahas cara membangun dan menggunakan Server MCP menggunakan transportasi stdio.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Membangun Server MCP menggunakan transportasi stdio.
- Debug Server MCP menggunakan Inspector.
- Menggunakan Server MCP melalui Visual Studio Code.
- Memahami mekanisme transportasi MCP saat ini dan mengapa stdio direkomendasikan.


## Transportasi stdio - Cara Kerjanya

Transportasi stdio adalah salah satu dari dua transportasi standar dalam Spesifikasi MCP
`2026-07-28`. Berikut cara kerjanya:

- **Komunikasi Sederhana**: Server membaca pesan JSON-RPC dari input standar (`stdin`) dan mengirim pesan ke output standar (`stdout`).
- **Berbasis Proses**: Klien menjalankan server MCP sebagai subprocess.
- **Format Pesan**: Pesan adalah permintaan JSON-RPC individual, notifikasi, atau respons, yang dipisahkan oleh baris baru.
- **Pencatatan**: Server BOLEH menulis string UTF-8 ke error standar (`stderr`) untuk keperluan logging.

### Persyaratan Utama:
- Pesan HARUS dipisahkan oleh baris baru dan TIDAK BOLEH mengandung baris baru yang tertanam
- Server TIDAK BOLEH menulis apa pun ke `stdout` yang bukan pesan MCP yang valid
- Klien TIDAK BOLEH menulis apa pun ke `stdin` server yang bukan pesan MCP yang valid

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
- Menggunakan context manager stdio_server untuk menangani transportasi

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

- Tidak memerlukan pengaturan server web atau endpoint HTTP
- Dijalankan sebagai subprocess oleh klien
- Berkomunikasi melalui aliran stdin/stdout
- Lebih sederhana untuk diimplementasikan dan debug

## Latihan: Membuat Server stdio

Untuk membuat server kita, kita perlu mengingat dua hal:

- Kita perlu menggunakan server web untuk mengekspos endpoint untuk koneksi dan pesan.
## Lab: Membuat server MCP stdio sederhana

Dalam lab ini, kita akan membuat server MCP sederhana menggunakan transportasi stdio yang direkomendasikan. Server ini akan mengekspos tools yang dapat dipanggil klien menggunakan Protokol Konteks Model standar.

### Prasyarat

- Python 3.8 atau lebih baru
- MCP Python SDK: `pip install mcp`
- Pemahaman dasar tentang pemrograman asinkron

Mari mulai dengan membuat server MCP stdio pertama kita:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Konfigurasikan pencatatan
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
    # Gunakan transport stdio
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

**Transportasi stdio (Standar Saat Ini):**
- Model subprocess sederhana - klien menjalankan server sebagai proses anak
- Komunikasi melalui stdin/stdout menggunakan pesan JSON-RPC
- Tidak memerlukan pengaturan server HTTP
- Performa dan keamanan lebih baik
- Debugging dan pengembangan lebih mudah

**Transportasi SSE (Dihentikan sejak MCP 2025-06-18):**
- Memerlukan server HTTP dengan endpoint SSE
- Pengaturan lebih kompleks dengan infrastruktur server web
- Pertimbangan keamanan tambahan untuk endpoint HTTP
- Kini digantikan oleh Streamable HTTP untuk skenario berbasis web

### Membuat server dengan transportasi stdio

Untuk membuat server stdio kita, kita perlu:

1. **Impor pustaka yang diperlukan** - Kita membutuhkan komponen server MCP dan transportasi stdio
2. **Buat instance server** - Definisikan server dengan kapabilitasnya
3. **Definisikan tools** - Tambahkan fungsi yang ingin diekspos
4. **Atur transportasi** - Konfigurasikan komunikasi stdio
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

### Langkah 2: Tambah lebih banyak tools

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

Server akan mulai dan menunggu input dari stdin. Ia berkomunikasi menggunakan pesan JSON-RPC melalui transportasi stdio.

### Langkah 4: Menguji dengan Inspector

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

MCP Inspector adalah alat yang berharga untuk debugging dan pengujian server MCP. Berikut cara menggunakannya dengan server stdio Anda:

1. **Instal Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Jalankan Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Uji server Anda**: Inspector menyediakan antarmuka web dimana Anda bisa:
   - Melihat kapabilitas server
   - Menguji tools dengan berbagai parameter
   - Memantau pesan JSON-RPC
   - Debug masalah koneksi

### Menggunakan VS Code

Anda juga dapat debugging server MCP langsung di VS Code:

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

2. Tetapkan breakpoint di kode server Anda
3. Jalankan debugger dan uji dengan Inspector

### Tips debugging umum

- Gunakan `stderr` untuk logging - jangan pernah menulis ke `stdout` karena itu dikhususkan untuk pesan MCP
- Pastikan semua pesan JSON-RPC dipisahkan oleh baris baru
- Uji dengan tools sederhana terlebih dahulu sebelum menambah fungsi yang kompleks
- Gunakan Inspector untuk memverifikasi format pesan

## Menggunakan server stdio Anda di VS Code

Setelah Anda membangun server MCP stdio Anda, Anda dapat mengintegrasikannya dengan VS Code untuk digunakan dengan Claude atau klien MCP kompatibel lainnya.

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

3. **Uji koneksi**: Mulai percakapan dengan Claude dan coba gunakan tools server Anda:
   - "Bisakah kamu menyapa saya menggunakan alat sapaan?"
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

// Tambahkan alat-alat
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

- Membangun server MCP menggunakan **transportasi stdio** saat ini (pendekatan yang direkomendasikan)
- Memahami mengapa transportasi SSE dihentikan digantikan oleh stdio dan Streamable HTTP
- Membuat tools yang dapat dipanggil oleh klien MCP
- Debug server Anda menggunakan MCP Inspector
- Mengintegrasikan server stdio Anda dengan VS Code dan Claude

Transportasi stdio menyediakan cara yang lebih sederhana, lebih aman, dan lebih berkinerja untuk membangun server MCP dibandingkan pendekatan SSE yang dihentikan. Ini adalah transportasi yang direkomendasikan untuk sebagian besar implementasi server MCP sejak spesifikasi 2025-06-18.


### .NET

1. Mari kita buat beberapa tools terlebih dahulu, untuk ini kita akan membuat file *Tools.cs* dengan isi berikut:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Latihan: Menguji server stdio Anda

Sekarang setelah Anda membangun server stdio Anda, mari kita uji untuk memastikan ia berfungsi dengan benar.

### Prasyarat

1. Pastikan Anda telah memasang MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Kode server Anda harus tersimpan (misalnya, sebagai `server.py`)

### Pengujian dengan Inspector

1. **Mulai Inspector dengan server Anda**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Buka antarmuka web**: Inspector akan membuka jendela browser yang menampilkan kapabilitas server Anda.

3. **Uji tools**: 
   - Coba tool `get_greeting` dengan nama yang berbeda
   - Uji tool `calculate_sum` dengan berbagai angka
   - Panggil tool `get_server_info` untuk melihat metadata server

4. **Pantau komunikasi**: Inspector menampilkan pesan JSON-RPC yang dipertukarkan antara klien dan server.

### Apa yang harus Anda lihat

Ketika server Anda berjalan dengan benar, Anda harus melihat:
- Kapabilitas server tercantum di Inspector
- Tools tersedia untuk pengujian
- Pertukaran pesan JSON-RPC yang berhasil
- Respon tool ditampilkan di antarmuka

### Masalah umum dan solusi

**Server tidak mau start:**
- Periksa bahwa semua dependensi terpasang: `pip install mcp`
- Periksa sintaks dan indentasi Python
- Cari pesan error di konsol

**Tools tidak muncul:**
- Pastikan dekorator `@server.tool()` ada
- Periksa fungsi tool sudah didefinisikan sebelum `main()`
- Pastikan server dikonfigurasi dengan benar

**Masalah koneksi:**
- Pastikan server menggunakan transportasi stdio dengan benar
- Periksa tidak ada proses lain yang mengganggu
- Verifikasi sintaks perintah Inspector

## Tugas

Cobalah membangun server Anda dengan kapabilitas lebih banyak. Lihat [halaman ini](https://api.chucknorris.io/) untuk, misalnya, menambahkan tool yang memanggil API. Anda tentukan bagaimana servernya harus terlihat. Selamat bersenang-senang :)
## Solusi

[Solusi](./solution/README.md) Berikut adalah solusi yang mungkin dengan kode kerja.

## Poin Penting

Poin-poin penting dari bab ini adalah sebagai berikut:

- Transportasi stdio adalah mekanisme yang direkomendasikan untuk server MCP lokal.
- Transportasi stdio memungkinkan komunikasi mulus antara server dan klien MCP menggunakan aliran input dan output standar.
- Anda dapat menggunakan baik Inspector maupun Visual Studio Code untuk langsung menggunakan server stdio, membuat debugging dan integrasi menjadi mudah.

## Contoh 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Sumber Daya Tambahan

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Apa Selanjutnya

## Langkah Berikutnya

Sekarang setelah Anda belajar cara membangun server MCP dengan transportasi stdio, Anda dapat mengeksplorasi topik yang lebih lanjut:

- **Selanjutnya**: [HTTP Streaming dengan MCP (Streamable HTTP)](../06-http-streaming/README.md) - Pelajari mekanisme transportasi lainnya yang didukung untuk server jarak jauh
- **Lanjutan**: [Praktik Terbaik Keamanan MCP](../../02-Security/README.md) - Terapkan keamanan pada server MCP Anda
- **Produksi**: [Strategi Deployment](../09-deployment/README.md) - Deploy server Anda untuk penggunaan produksi

## Sumber Daya Tambahan

- [Spesifikasi MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Spesifikasi terkini
- [Dokumentasi MCP SDK](https://github.com/modelcontextprotocol/sdk) - Referensi SDK untuk semua bahasa
- [Contoh Komunitas](../../06-CommunityContributions/README.md) - Lebih banyak contoh server dari komunitas

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->