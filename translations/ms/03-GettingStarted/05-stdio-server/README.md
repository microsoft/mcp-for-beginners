# Pelayan MCP dengan Pengangkutan stdio

> **⚠️ Kemas Kini Penting**: Sehingga Spesifikasi MCP 2025-06-18, pengangkutan SSE (Server-Sent Events) yang berdiri sendiri telah **dihentikan** dan digantikan oleh pengangkutan "Streamable HTTP". Spesifikasi MCP semasa mentakrifkan dua mekanisme pengangkutan utama:
> 1. **stdio** - Input/output standard (disyorkan untuk pelayan tempatan)
> 2. **Streamable HTTP** - Untuk pelayan jauh yang mungkin menggunakan SSE secara dalaman
>
> Pelajaran ini telah dikemas kini untuk memberi tumpuan kepada **pengangkutan stdio**, yang merupakan pendekatan yang disyorkan untuk kebanyakan pelaksanaan pelayan MCP.

Pengangkutan stdio membolehkan pelayan MCP berkomunikasi dengan pelanggan melalui aliran input dan output standard. Ini adalah mekanisme pengangkutan yang paling biasa digunakan dan disyorkan dalam spesifikasi MCP semasa, menyediakan cara yang mudah dan cekap untuk membina pelayan MCP yang boleh diintegrasikan dengan mudah dengan pelbagai aplikasi pelanggan.

## Gambaran Keseluruhan

Pelajaran ini merangkumi cara membina dan menggunakan Pelayan MCP menggunakan pengangkutan stdio.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Membina Pelayan MCP menggunakan pengangkutan stdio.
- Menyahpepijat Pelayan MCP menggunakan Inspector.
- Menggunakan Pelayan MCP dengan Visual Studio Code.
- Memahami mekanisme pengangkutan MCP semasa dan mengapa stdio disyorkan.


## Pengangkutan stdio - Cara Kerjanya

Pengangkutan stdio adalah salah satu daripada dua pengangkutan standard dalam Spesifikasi MCP
`2026-07-28`. Berikut cara ia berfungsi:

- **Komunikasi Mudah**: Pelayan membaca mesej JSON-RPC dari input standard (`stdin`) dan menghantar mesej ke output standard (`stdout`).
- **Berasaskan Proses**: Pelanggan melancarkan pelayan MCP sebagai subproses.
- **Format Mesej**: Mesej adalah permintaan JSON-RPC, pemberitahuan, atau jawapan yang berasingan, dipisahkan oleh baris baru.
- **Penjejakan**: Pelayan BOLEH menulis rentetan UTF-8 ke ralat standard (`stderr`) untuk tujuan penjejakan.

### Keperluan Utama:
- Mesej MESTI dipisahkan oleh baris baru dan TIDAK BOLEH mengandungi baris baru tersemat
- Pelayan TIDAK BOLEH menulis apa-apa ke `stdout` yang bukan mesej MCP yang sah
- Pelanggan TIDAK BOLEH menulis apa-apa ke `stdin` pelayan yang bukan mesej MCP yang sah

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

Dalam kod sebelum ini:

- Kami mengimport kelas `Server` dan `StdioServerTransport` dari MCP SDK
- Kami membuat contoh pelayan dengan konfigurasi asas dan keupayaan
- Kami membuat contoh `StdioServerTransport` dan menyambungkan pelayan kepadanya, membolehkan komunikasi melalui stdin/stdout

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

Dalam kod sebelum ini kami:

- Membuat contoh pelayan menggunakan MCP SDK
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

- Tidak memerlukan tetapan pelayan web atau titik akhir HTTP
- Dilancarkan sebagai subproses oleh pelanggan
- Berkomunikasi melalui aliran stdin/stdout
- Lebih mudah dilaksanakan dan dibaiki

## Latihan: Mencipta Pelayan stdio

Untuk mencipta pelayan kita, kita perlu ingat dua perkara:

- Kita perlu menggunakan pelayan web untuk mendedahkan titik akhir bagi sambungan dan mesej.
## Makmal: Mencipta pelayan MCP stdio mudah

Dalam makmal ini, kita akan mencipta pelayan MCP mudah menggunakan pengangkutan stdio yang disyorkan. Pelayan ini akan mendedahkan alat yang boleh dipanggil oleh pelanggan menggunakan Protokol Konteks Model standard.

### Prasyarat

- Python 3.8 atau lebih baru
- MCP Python SDK: `pip install mcp`
- Pemahaman asas mengenai pengaturcaraan async

Mari kita mula dengan mencipta pelayan MCP stdio pertama kita:

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

## Perbezaan utama daripada pendekatan SSE yang dihentikan

**Pengangkutan Stdio (Standard Semasa):**
- Model subproses mudah - pelanggan melancarkan pelayan sebagai proses anak
- Komunikasi melalui stdin/stdout menggunakan mesej JSON-RPC
- Tiada tetapan pelayan HTTP diperlukan
- Prestasi dan keselamatan lebih baik
- Penyahpepijatan dan pembangunan lebih mudah

**Pengangkutan SSE (Dihentikan sejak MCP 2025-06-18):**
- Memerlukan pelayan HTTP dengan titik akhir SSE
- Tetapan lebih kompleks dengan infrastruktur pelayan web
- Pertimbangan keselamatan tambahan untuk titik akhir HTTP
- Kini digantikan oleh Streamable HTTP untuk senario berasaskan web

### Mencipta pelayan dengan pengangkutan stdio

Untuk mencipta pelayan stdio kita, kita perlu:

1. **Import perpustakaan yang diperlukan** - Kita perlukan komponen pelayan MCP dan pengangkutan stdio
2. **Cipta contoh pelayan** - Definisikan pelayan dengan keupayaannya
3. **Definisikan alat** - Tambah fungsi yang kita mahu dedahkan
4. **Tetapkan pengangkutan** - Konfigurasikan komunikasi stdio
5. **Jalankan pelayan** - Mulakan pelayan dan kendalikan mesej

Mari bina langkah demi langkah:

### Langkah 1: Cipta pelayan stdio asas

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
3. Uji alat yang anda cipta

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Menyahpepijat pelayan stdio anda

### Menggunakan MCP Inspector

MCP Inspector adalah alat berharga untuk menyahpepijat dan menguji pelayan MCP. Berikut cara menggunakannya dengan pelayan stdio anda:

1. **Pasang Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Jalankan Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Uji pelayan anda**: Inspector menyediakan antara muka web di mana anda boleh:
   - Melihat keupayaan pelayan
   - Uji alat dengan parameter berbeza
   - Memantau mesej JSON-RPC
   - Nyahpepijat isu sambungan

### Menggunakan VS Code

Anda juga boleh menyahpepijat pelayan MCP anda terus dalam VS Code:

1. Cipta konfigurasi pelancaran dalam `.vscode/launch.json`:
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

- Gunakan `stderr` untuk penjejakan - jangan sekali-kali menulis ke `stdout` kerana ia dikhaskan untuk mesej MCP
- Pastikan semua mesej JSON-RPC dipisahkan oleh baris baru
- Uji dengan alat mudah terlebih dahulu sebelum menambah fungsi kompleks
- Gunakan Inspector untuk mengesahkan format mesej

## Menggunakan pelayan stdio anda dalam VS Code

Setelah anda membina pelayan MCP stdio anda, anda boleh mengintegrasikannya dengan VS Code untuk menggunakannya dengan Claude atau pelanggan lain yang serasi MCP.

### Konfigurasi

1. **Cipta fail konfigurasi MCP** di `%APPDATA%\Claude\claude_desktop_config.json` (Windows) atau `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Mulakan semula Claude**: Tutup dan buka semula Claude untuk memuatkan konfigurasi pelayan baru.

3. **Uji sambungan**: Mulakan perbualan dengan Claude dan cuba gunakan alat pelayan anda:
   - "Bolehkah kamu menyapa saya menggunakan alat salam?"
   - "Kira jumlah 15 dan 27"
   - "Apa info pelayan?"

### Contoh pelayan stdio TypeScript

Berikut contoh lengkap TypeScript untuk rujukan:

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

Dalam pelajaran yang dikemas kini ini, anda telah belajar cara untuk:

- Membina pelayan MCP menggunakan **pengangkutan stdio** semasa (pendekatan yang disyorkan)
- Memahami mengapa pengangkutan SSE dihentikan demi stdio dan Streamable HTTP
- Cipta alat yang boleh dipanggil oleh pelanggan MCP
- Nyahpepijat pelayan anda menggunakan MCP Inspector
- Integrasikan pelayan stdio anda dengan VS Code dan Claude

Pengangkutan stdio menyediakan cara yang lebih mudah, lebih selamat, dan lebih berprestasi untuk membina pelayan MCP berbanding pendekatan SSE yang dihentikan. Ia adalah pengangkutan yang disyorkan untuk kebanyakan pelaksanaan pelayan MCP sejak spesifikasi 2025-06-18.


### .NET

1. Mari kita cipta beberapa alat dahulu, untuk ini kita akan cipta fail *Tools.cs* dengan kandungan berikut:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Latihan: Menguji pelayan stdio anda

Sekarang anda telah membina pelayan stdio anda, mari uji ia untuk memastikan ia berfungsi dengan betul.

### Prasyarat

1. Pastikan anda telah memasang MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Kod pelayan anda harus disimpan (contohnya, sebagai `server.py`)

### Menguji dengan Inspector

1. **Mulakan Inspector dengan pelayan anda**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Buka antara muka web**: Inspector akan membuka tetingkap pelayar menunjukkan keupayaan pelayan anda.

3. **Uji alat**: 
   - Cuba alat `get_greeting` dengan nama berbeza
   - Uji alat `calculate_sum` dengan nombor berlainan
   - Panggil alat `get_server_info` untuk melihat metadata pelayan

4. **Pantau komunikasi**: Inspector menunjukkan mesej JSON-RPC yang dipertukarkan antara pelanggan dan pelayan.

### Apa yang patut anda lihat

Bila pelayan anda bermula dengan betul, anda harus melihat:
- Keupayaan pelayan disenaraikan dalam Inspector
- Alat tersedia untuk ujian
- Pertukaran mesej JSON-RPC yang berjaya
- Respons alat dipaparkan dalam antara muka

### Isu biasa dan penyelesaian

**Pelayan tidak bermula:**
- Semak semua kebergantungan dipasang: `pip install mcp`
- Periksa sintaks dan indentasi Python
- Cari mesej ralat dalam konsol

**Alat tidak muncul:**
- Pastikan dekorator `@server.tool()` ada
- Periksa bahawa fungsi alat didefinisikan sebelum `main()`
- Sahkan pelayan dikonfigurasi dengan betul

**Isu sambungan:**
- Pastikan pelayan menggunakan pengangkutan stdio dengan betul
- Semak tidak ada proses lain mengganggu
- Sahkan sintaks arahan Inspector

## Tugasan

Cuba bina pelayan anda dengan lebih banyak keupayaan. Lihat [halaman ini](https://api.chucknorris.io/) untuk, sebagai contoh, menambah alat yang memanggil API. Anda tentukan bagaimana rupa pelayan tersebut. Selamat mencuba :)
## Penyelesaian

[Penyelesaian](./solution/README.md) Berikut adalah penyelesaian yang mungkin dengan kod yang berfungsi.

## Pengajaran Utama

Pengajaran utama dari bab ini adalah:

- Pengangkutan stdio adalah mekanisme yang disyorkan untuk pelayan MCP tempatan.
- Pengangkutan stdio membenarkan komunikasi lancar antara pelayan MCP dan pelanggan menggunakan aliran input dan output standard.
- Anda boleh guna kedua-dua Inspector dan Visual Studio Code untuk menggunakan pelayan stdio terus, memudahkan penyahpepijatan dan integrasi.

## Contoh

- [Penghitung Java](../samples/java/calculator/README.md)
- [Penghitung .NET](../../../../03-GettingStarted/samples/csharp)
- [Penghitung JavaScript](../samples/javascript/README.md)
- [Penghitung TypeScript](../samples/typescript/README.md)
- [Penghitung Python](../../../../03-GettingStarted/samples/python)

## Sumber Tambahan

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Apa Seterusnya

## Langkah Seterusnya

Sekarang anda telah belajar bagaimana membina pelayan MCP dengan pengangkutan stdio, anda boleh meneroka topik yang lebih maju:

- **Seterusnya**: [HTTP Streaming dengan MCP (Streamable HTTP)](../06-http-streaming/README.md) - Pelajari mengenai mekanisme pengangkutan lain yang disokong untuk pelayan jauh
- **Lanjutan**: [Amalan Terbaik Keselamatan MCP](../../02-Security/README.md) - Laksanakan keselamatan dalam pelayan MCP anda
- **Pengeluaran**: [Strategi Penyebaran](../09-deployment/README.md) - Sebarkan pelayan anda untuk kegunaan pengeluaran

## Sumber Tambahan

- [Spesifikasi MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Spesifikasi semasa
- [Dokumentasi SDK MCP](https://github.com/modelcontextprotocol/sdk) - Rujukan SDK untuk semua bahasa
- [Contoh Komuniti](../../06-CommunityContributions/README.md) - Lebih banyak contoh pelayan dari komuniti

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->