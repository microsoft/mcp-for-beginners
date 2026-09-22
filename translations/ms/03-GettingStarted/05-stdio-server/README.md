# Server MCP dengan Pengangkutan stdio

> **⚠️ Kemas Kini Penting**: Mulai Spesifikasi MCP 2025-06-18, pengangkutan SSE (Server-Sent Events) berdiri sendiri telah **dihentikan** dan digantikan dengan pengangkutan "Streamable HTTP". Spesifikasi MCP semasa menetapkan dua mekanisme pengangkutan utama:
> 1. **stdio** - Input/output standard (disyorkan untuk pelayan tempatan)
> 2. **Streamable HTTP** - Untuk pelayan jauh yang mungkin menggunakan SSE secara dalaman
>
> Pelajaran ini telah dikemas kini untuk memberi tumpuan kepada **pengangkutan stdio**, yang merupakan pendekatan yang disyorkan untuk kebanyakan pelaksanaan pelayan MCP.

Pengangkutan stdio membolehkan pelayan MCP berkomunikasi dengan pelanggan melalui aliran input dan output standard. Ini adalah mekanisme pengangkutan yang paling biasa digunakan dan disyorkan dalam spesifikasi MCP semasa, menyediakan cara yang mudah dan cekap untuk membina pelayan MCP yang boleh disepadukan dengan pelbagai aplikasi pelanggan.

## Gambaran Keseluruhan

Pelajaran ini menerangkan cara membina dan menggunakan Pelayan MCP menggunakan pengangkutan stdio.

## Objektif Pembelajaran

Pada akhir pelajaran ini, anda akan dapat:

- Membina Pelayan MCP menggunakan pengangkutan stdio.
- Menyahpepijat Pelayan MCP menggunakan Inspector.
- Menggunakan Pelayan MCP dalam Visual Studio Code.
- Memahami mekanisme pengangkutan MCP semasa dan sebab pengangkutan stdio disyorkan.


## Pengangkutan stdio - Cara Kerjanya

Pengangkutan stdio adalah salah satu daripada dua pengangkutan standard dalam Spesifikasi MCP
`2026-07-28`. Berikut adalah cara kerjanya:

- **Komunikasi Mudah**: Pelayan membaca mesej JSON-RPC dari input standard (`stdin`) dan menghantar mesej ke output standard (`stdout`).
- **Berasaskan Proses**: Pelanggan melancarkan pelayan MCP sebagai subprocess.
- **Format Mesej**: Mesej adalah permintaan JSON-RPC, notifikasi, atau tindak balas individu, yang dipisahkan oleh baris baru.
- **Log**: Pelayan BOLEH menulis string UTF-8 ke ralat standard (`stderr`) untuk tujuan logging.

### Keperluan Utama:
- Mesej MESTI dipisahkan oleh baris baru dan TIDAK MESTI mengandungi baris baru tertanam
- Pelayan TIDAK MESTI menulis apa-apa ke `stdout` yang bukan mesej MCP yang sah
- Pelanggan TIDAK MESTI menulis apa-apa ke `stdin` pelayan yang bukan mesej MCP yang sah

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

Dalam kod di atas:

- Kami mengimport kelas `Server` dan `StdioServerTransport` dari SDK MCP
- Kami membuat satu instans pelayan dengan konfigurasi dan kebolehan asas
- Kami membuat instans `StdioServerTransport` dan menghubungkan pelayan kepadanya, membolehkan komunikasi melalui stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Cipta instans pelayan
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

Dalam kod di atas kami:

- Membuat instans pelayan menggunakan SDK MCP
- Mendefinisikan alat menggunakan dekorator
- Menggunakan pengurus konteks stdio_server untuk mengendalikan pengangkutan

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

Perbezaan utama daripada SSE ialah pelayan stdio:

- Tidak memerlukan setup pelayan web atau endpoint HTTP
- Dilancarkan sebagai subprocess oleh pelanggan
- Berkomunikasi melalui aliran stdin/stdout
- Lebih mudah untuk diimplementasi dan debug

## Latihan: Membuat Pelayan stdio

Untuk membuat pelayan kita, kita perlu ingat dua perkara:

- Kita perlu menggunakan pelayan web untuk mendedahkan endpoint untuk sambungan dan mesej.
## Makmal: Membuat pelayan MCP stdio mudah

Dalam makmal ini, kita akan membuat pelayan MCP mudah menggunakan pengangkutan stdio yang disyorkan. Pelayan ini akan mendedahkan alat yang boleh dipanggil oleh pelanggan menggunakan Protokol Konteks Model standard.

### Prasyarat

- Python 3.8 atau lebih baru
- SDK MCP Python: `pip install mcp`
- Pemahaman asas tentang pengaturcaraan async

Mari kita mulakan dengan membuat pelayan MCP stdio pertama kita:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Konfigurasikan log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cipta pelayan
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
    # Gunakan pengangkutan stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Perbezaan utama daripada pendekatan SSE yang dihentikan

**Pengangkutan Stdio (Standard Semasa):**
- Model subprocess mudah - pelanggan melancarkan pelayan sebagai proses anak
- Komunikasi melalui stdin/stdout menggunakan mesej JSON-RPC
- Tiada setup pelayan HTTP diperlukan
- Prestasi dan keselamatan lebih baik
- Mudah untuk debug dan pembangunan

**Pengangkutan SSE (Dihentikan mulai MCP 2025-06-18):**
- Memerlukan pelayan HTTP dengan endpoint SSE
- Setup lebih kompleks dengan infrastruktur pelayan web
- Pertimbangan keselamatan tambahan untuk endpoint HTTP
- Kini digantikan oleh Streamable HTTP untuk senario berasaskan web

### Membuat pelayan dengan pengangkutan stdio

Untuk membuat pelayan stdio kita, kita perlu:

1. **Import perpustakaan yang diperlukan** - Kita perlukan komponen pelayan MCP dan pengangkutan stdio
2. **Buat instans pelayan** - Definisikan pelayan dengan kebolehannya
3. **Definisikan alat** - Tambah fungsi yang mahu didedahkan
4. **Atur pengangkutan** - Konfigurasi komunikasi stdio
5. **Jalankan pelayan** - Mulakan pelayan dan kendalikan mesej

Mari bina ini langkah demi langkah:

### Langkah 1: Buat pelayan stdio asas

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfigurasikan pencatatan
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cipta pelayan
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

### Langkah 2: Tambah lebih banyak alat

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

### Langkah 3: Menjalankan pelayan

Simpan kod sebagai `server.py` dan jalankan dari baris arahan:

```bash
python server.py
```

Pelayan akan bermula dan menunggu input dari stdin. Ia berkomunikasi menggunakan mesej JSON-RPC melalui pengangkutan stdio.

### Langkah 4: Menguji dengan Inspector

Anda boleh menguji pelayan anda menggunakan MCP Inspector:

1. Pasang Inspector: `npx @modelcontextprotocol/inspector`
2. Jalankan Inspector dan arahkan ke pelayan anda
3. Uji alat yang telah anda cipta

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Menyahpepijat pelayan stdio anda

### Menggunakan MCP Inspector

MCP Inspector adalah alat berharga untuk menyahpepijat dan menguji pelayan MCP. Berikut adalah cara menggunakannya dengan pelayan stdio anda:

1. **Pasang Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Jalankan Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Uji pelayan anda**: Inspector menyediakan antara muka web di mana anda boleh:
   - Melihat kebolehan pelayan
   - Menguji alat dengan parameter berbeza
   - Memantau mesej JSON-RPC
   - Menyahpepijat masalah sambungan

### Menggunakan VS Code

Anda juga boleh menyahpepijat pelayan MCP anda terus dalam VS Code:

1. Buat konfigurasi pelancaran di `.vscode/launch.json`:
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

2. Tetapkan titik henti dalam kod pelayan anda
3. Jalankan debugger dan uji dengan Inspector

### Petua penyahpepijatan biasa

- Gunakan `stderr` untuk logging - jangan tulis ke `stdout` kerana ia dikhaskan untuk mesej MCP
- Pastikan semua mesej JSON-RPC dipisahkan dengan baris baru
- Uji dengan alat mudah terlebih dahulu sebelum menambah fungsi kompleks
- Gunakan Inspector untuk mengesahkan format mesej

## Menggunakan pelayan stdio anda dalam VS Code

Setelah anda membina pelayan MCP stdio anda, anda boleh menyepadukannya dengan VS Code untuk menggunakannya dengan Claude atau pelanggan MCP lain.

### Konfigurasi

1. **Buat fail konfigurasi MCP** di `%APPDATA%\Claude\claude_desktop_config.json` (Windows) atau `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Mulakan semula Claude**: Tutup dan buka semula Claude untuk memuat konfigurasi pelayan baru.

3. **Uji sambungan**: Mulakan perbualan dengan Claude dan cuba gunakan alat pelayan anda:
   - "Bolehkah anda menyapa saya menggunakan alat sapaan?"
   - "Kira jumlah 15 dan 27"
   - "Apa maklumat pelayan?"

### Contoh pelayan stdio TypeScript

Berikut adalah contoh lengkap TypeScript untuk rujukan:

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

// Tambah alat
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

### Contoh pelayan stdio .NET

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

Dalam pelajaran yang dikemas kini ini, anda belajar bagaimana untuk:

- Membina pelayan MCP menggunakan **pengangkutan stdio** semasa (pendekatan yang disyorkan)
- Memahami sebab pengangkutan SSE dihentikan dan digantikan oleh pengangkutan stdio dan Streamable HTTP
- Membina alat yang boleh dipanggil oleh pelanggan MCP
- Menyahpepijat pelayan anda menggunakan MCP Inspector
- Menyepadukan pelayan stdio anda dengan VS Code dan Claude

Pengangkutan stdio menyediakan cara yang lebih mudah, selamat, dan berprestasi untuk membina pelayan MCP berbanding pendekatan SSE yang dihentikan. Ia adalah pengangkutan yang disyorkan untuk kebanyakan pelaksanaan pelayan MCP mulai spesifikasi 2025-06-18.


### .NET

1. Mari kita cipta beberapa alat terlebih dahulu, untuk ini kita akan membuat fail *Tools.cs* dengan kandungan berikut:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Latihan: Menguji pelayan stdio anda

Sekarang anda telah membina pelayan stdio anda, mari uji untuk memastikan ia berfungsi dengan betul.

### Prasyarat

1. Pastikan anda telah memasang MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Kod pelayan anda harus disimpan (contoh, sebagai `server.py`)

### Menguji dengan Inspector

1. **Mulakan Inspector dengan pelayan anda**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Buka antara muka web**: Inspector akan membuka tetingkap pelayar yang memaparkan kebolehan pelayan anda.

3. **Uji alat**:
   - Cuba alat `get_greeting` dengan nama yang berbeza
   - Uji alat `calculate_sum` dengan pelbagai nombor
   - Panggil alat `get_server_info` untuk melihat metadata pelayan

4. **Pantau komunikasi**: Inspector memaparkan mesej JSON-RPC yang dipertukarkan antara pelanggan dan pelayan.

### Apa yang anda harus lihat

Apabila pelayan anda bermula dengan betul, anda harus melihat:
- Kebolehan pelayan disenaraikan dalam Inspector
- Alat tersedia untuk ujian
- Pertukaran mesej JSON-RPC berjaya
- Respons alat dipaparkan dalam antara muka

### Isu biasa dan penyelesaian

**Pelayan tidak bermula:**
- Semak semua kebergantungan telah dipasang: `pip install mcp`
- Semak sintaks dan indentasi Python
- Cari mesej ralat dalam konsol

**Alat tidak muncul:**
- Pastikan dekorator `@server.tool()` ada
- Semak fungsi alat telah didefinisikan sebelum `main()`
- Pastikan pelayan dikonfigurasikan dengan betul

**Masalah sambungan:**
- Pastikan pelayan menggunakan pengangkutan stdio dengan betul
- Semak tiada proses lain mengganggu
- Semak sintaks arahan Inspector

## Tugasan

Cuba bina pelayan anda dengan lebih kebolehan. Lihat [halaman ini](https://api.chucknorris.io/) untuk, sebagai contoh, menambah alat yang memanggil API. Anda tentukan bagaimana pelayan harus kelihatan. Selamat berseronok :)
## Penyelesaian

[Penyelesaian](./solution/README.md) Berikut adalah penyelesaian yang mungkin dengan kod yang berfungsi.

## Pengajaran Utama

Pengajaran utama dari bab ini adalah:

- Pengangkutan stdio adalah mekanisme yang disyorkan untuk pelayan MCP tempatan.
- Pengangkutan stdio membolehkan komunikasi lancar antara pelayan MCP dan pelanggan menggunakan aliran input dan output standard.
- Anda boleh menggunakan kedua-dua Inspector dan Visual Studio Code untuk menggunakan pelayan stdio secara langsung, menjadikan penyahpepijatan dan penyepaduan mudah.

## Contoh

- [Kalkulator Java](../samples/java/calculator/README.md)
- [Kalkulator .Net](../../../../03-GettingStarted/samples/csharp)
- [Kalkulator JavaScript](../samples/javascript/README.md)
- [Kalkulator TypeScript](../samples/typescript/README.md)
- [Kalkulator Python](../../../../03-GettingStarted/samples/python) 

## Sumber Tambahan

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Apa Seterusnya

## Langkah Seterusnya

Kini anda telah belajar cara membina pelayan MCP dengan pengangkutan stdio, anda boleh meneroka topik lebih maju:

- **Seterusnya**: [Penstriman HTTP dengan MCP (Streamable HTTP)](../06-http-streaming/README.md) - Pelajari mekanisme pengangkutan lain untuk pelayan jauh
- **Lanjutan**: [Amalan Terbaik Keselamatan MCP](../../02-Security/README.md) - Laksanakan keselamatan dalam pelayan MCP anda
- **Produksi**: [Strategi Penggubahan](../09-deployment/README.md) - Gunakan pelayan anda untuk penggunaan produksi

## Sumber Tambahan

- [Spesifikasi MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Spesifikasi semasa
- [Dokumentasi SDK MCP](https://github.com/modelcontextprotocol/sdk) - Rujukan SDK untuk semua bahasa
- [Contoh Komuniti](../../06-CommunityContributions/README.md) - Lebih banyak contoh pelayan dari komuniti

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->