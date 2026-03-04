# Pelayan MCP dengan Pengangkutan stdio

> **⚠️ Kemas Kini Penting**: Bermula dari Spesifikasi MCP 2025-06-18, pengangkutan SSE (Server-Sent Events) berdiri sendiri telah **dihentikan** dan digantikan dengan pengangkutan "HTTP Boleh Alir" (Streamable HTTP). Spesifikasi MCP semasa mentakrifkan dua mekanisme pengangkutan utama:
> 1. **stdio** - Input/output standard (disyorkan untuk pelayan tempatan)
> 2. **Streamable HTTP** - Untuk pelayan jauh yang mungkin menggunakan SSE secara dalaman
>
> Pelajaran ini telah dikemas kini untuk memberi tumpuan kepada **pengangkutan stdio**, yang merupakan pendekatan yang disyorkan untuk kebanyakan pelaksanaan pelayan MCP.

Pengangkutan stdio membolehkan pelayan MCP berkomunikasi dengan klien melalui aliran input dan output standard. Ini adalah mekanisme pengangkutan yang paling biasa digunakan dan disyorkan dalam spesifikasi MCP semasa, menyediakan cara yang mudah dan cekap untuk membina pelayan MCP yang boleh disepadukan dengan pelbagai aplikasi klien.

## Gambaran Keseluruhan

Pelajaran ini merangkumi cara membina dan menggunakan Pelayan MCP menggunakan pengangkutan stdio.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Membina Pelayan MCP menggunakan pengangkutan stdio.
- Membuat debug Pelayan MCP menggunakan Inspector.
- Menggunakan Pelayan MCP menggunakan Visual Studio Code.
- Memahami mekanisme pengangkutan MCP semasa dan mengapa stdio disyorkan.

## Pengangkutan stdio - Bagaimana Ia Berfungsi

Pengangkutan stdio adalah salah satu daripada dua jenis pengangkutan yang disokong dalam spesifikasi MCP semasa (2025-06-18). Berikut adalah cara kerjanya:

- **Komunikasi Mudah**: Pelayan membaca mesej JSON-RPC dari input standard (`stdin`) dan menghantar mesej ke output standard (`stdout`).
- **Berasaskan Proses**: Klien melancarkan pelayan MCP sebagai subprocess.
- **Format Mesej**: Mesej adalah permintaan JSON-RPC individu, pemberitahuan, atau tindak balas, dipisahkan oleh baris baru.
- **Pelog**: Pelayan BOLEH menulis rentetan UTF-8 ke ralat standard (`stderr`) untuk tujuan pelog.

### Keperluan Utama:
- Mesej MESTI dipisahkan oleh baris baru dan TIDAK MESTI mengandungi baris baru terbenam
- Pelayan TIDAK MESTI menulis apa-apa ke `stdout` yang bukan mesej MCP yang sah
- Klien TIDAK MESTI menulis apa-apa ke `stdin` pelayan yang bukan mesej MCP yang sah

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
  
Dalam kod sebelum ini:

- Kami mengimport kelas `Server` dan `StdioServerTransport` dari MCP SDK
- Kami mencipta contoh pelayan dengan konfigurasi asas dan keupayaan

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
  
Dalam kod sebelum ini kami:

- Mencipta contoh pelayan menggunakan MCP SDK
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
  
Perbezaan utama dari SSE ialah pelayan stdio:

- Tidak memerlukan persediaan pelayan web atau titik akhir HTTP
- Dilancarkan sebagai subprocess oleh klien
- Berkomunikasi melalui aliran stdin/stdout
- Lebih mudah untuk dilaksanakan dan debug

## Latihan: Mencipta Pelayan stdio

Untuk mencipta pelayan kita, kita perlu ingat dua perkara:

- Kita perlu menggunakan pelayan web untuk mendedahkan titik akhir untuk sambungan dan mesej.

## Makmal: Mencipta pelayan MCP stdio yang mudah

Dalam makmal ini, kita akan mencipta pelayan MCP mudah menggunakan pengangkutan stdio yang disyorkan. Pelayan ini akan mendedahkan alat yang boleh dipanggil oleh klien menggunakan Protokol Konteks Model standard.

### Prasyarat

- Python 3.8 atau lebih baru
- MCP Python SDK: `pip install mcp`
- Pemahaman asas mengenai pengaturcaraan async

Mari mulakan dengan mencipta pelayan MCP stdio pertama kita:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Konfigurasikan pencatatan
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Buat pelayan
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
  
## Perbezaan utama dari pendekatan SSE yang telah dihentikan

**Pengangkutan stdio (Standard Semasa):**
- Model subprocess mudah - klien melancarkan pelayan sebagai proses anak
- Komunikasi melalui stdin/stdout menggunakan mesej JSON-RPC
- Tiada persediaan pelayan HTTP diperlukan
- Prestasi dan keselamatan yang lebih baik
- Debug dan pembangunan lebih mudah

**Pengangkutan SSE (Dihentikan sejak MCP 2025-06-18):**
- Memerlukan pelayan HTTP dengan titik akhir SSE
- Persediaan lebih kompleks dengan infrastruktur pelayan web
- Pertimbangan keselamatan tambahan untuk titik akhir HTTP
- Kini digantikan oleh Streamable HTTP untuk senario berasaskan web

### Mencipta pelayan dengan pengangkutan stdio

Untuk mencipta pelayan stdio kita, kita perlu:

1. **Import perpustakaan yang diperlukan** - Kita perlu komponen pelayan MCP dan pengangkutan stdio
2. **Cipta contoh pelayan** - Takrif pelayan dengan keupayaannya
3. **Tentukan alat** - Tambah fungsi yang ingin didedahkan
4. **Sediakan pengangkutan** - Konfigurasi komunikasi stdio
5. **Jalankan pelayan** - Mulakan pelayan dan kendalikan mesej

Mari bina ini langkah demi langkah:

### Langkah 1: Cipta pelayan stdio asas

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfigurasikan logging
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

Simpan kod sebagai `server.py` dan jalankan dari baris perintah:

```bash
python server.py
```
  
Pelayan akan mula beroperasi dan menunggu input dari stdin. Ia berkomunikasi menggunakan mesej JSON-RPC melalui pengangkutan stdio.

### Langkah 4: Ujian dengan Inspector

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
  
## Debug pelayan stdio anda

### Menggunakan MCP Inspector

MCP Inspector adalah alat yang berguna untuk debug dan menguji pelayan MCP. Berikut cara menggunakannya dengan pelayan stdio anda:

1. **Pasang Inspector**:  
   ```bash
   npx @modelcontextprotocol/inspector
   ```
  
2. **Jalankan Inspector**:  
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
3. **Uji pelayan anda**: Inspector menyediakan antaramuka web di mana anda boleh:  
   - Melihat keupayaan pelayan  
   - Menguji alat dengan parameter berbeza  
   - Memantau mesej JSON-RPC  
   - Debug masalah sambungan  

### Menggunakan VS Code

Anda juga boleh debug pelayan MCP anda terus dalam VS Code:

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
  
2. Tetapkan breakpoint dalam kod pelayan anda  
3. Jalankan debugger dan uji dengan Inspector  

### Petua debug biasa

- Gunakan `stderr` untuk pelog - jangan tulis ke `stdout` kerana ia dikhaskan untuk mesej MCP  
- Pastikan semua mesej JSON-RPC dipisahkan oleh baris baru  
- Uji dengan alat mudah dahulu sebelum menambah fungsi kompleks  
- Gunakan Inspector untuk mengesahkan format mesej  

## Menggunakan pelayan stdio anda dalam VS Code

Setelah anda membina pelayan MCP stdio, anda boleh menyepadukannya dengan VS Code untuk menggunakannya dengan Claude atau klien yang menyokong MCP lainnya.

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
  
2. **Mulakan semula Claude**: Tutup dan buka semula Claude untuk memuat konfigurasi pelayan baru.

3. **Uji sambungan**: Mulakan perbualan dengan Claude dan cuba alat pelayan anda:  
   - "Boleh tolong sapakan saya menggunakan alat sapaan?"  
   - "Kira jumlah 15 dan 27"  
   - "Apa info pelayan?"  

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

Dalam pelajaran yang dikemas kini ini, anda telah belajar untuk:

- Membina pelayan MCP menggunakan **pengangkutan stdio** semasa (pendekatan disyorkan)  
- Memahami mengapa pengangkutan SSE dihentikan dan digantikan dengan stdio dan Streamable HTTP  
- Mencipta alat yang boleh dipanggil oleh klien MCP  
- Debug pelayan anda menggunakan MCP Inspector  
- Menyepadukan pelayan stdio anda dengan VS Code dan Claude  

Pengangkutan stdio menyediakan cara yang lebih mudah, lebih selamat, dan lebih berprestasi untuk membina pelayan MCP berbanding pendekatan SSE yang dihentikan. Ia adalah pengangkutan yang disyorkan untuk kebanyakan pelaksanaan pelayan MCP bermula dari spesifikasi 2025-06-18.

### .NET

1. Mari kita cipta beberapa alat terlebih dahulu, untuk ini kita akan cipta fail *Tools.cs* dengan kandungan berikut:  

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```
  
## Latihan: Menguji pelayan stdio anda

Kini setelah anda membina pelayan stdio, mari kita uji untuk memastikan ia berfungsi dengan betul.

### Prasyarat

1. Pastikan anda telah memasang MCP Inspector:  
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```
  
2. Kod pelayan anda harus disimpan (contohnya sebagai `server.py`)

### Ujian dengan Inspector

1. **Mulakan Inspector dengan pelayan anda**:  
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
2. **Buka antaramuka web**: Inspector akan membuka tetingkap pelayar yang menunjukkan keupayaan pelayan anda.

3. **Uji alat**:  
   - Cuba alat `get_greeting` dengan nama yang berbeza  
   - Uji alat `calculate_sum` dengan pelbagai nombor  
   - Panggil alat `get_server_info` untuk melihat metadata pelayan  

4. **Pantau komunikasi**: Inspector menunjukkan mesej JSON-RPC yang dipertukarkan antara klien dan pelayan.

### Apa yang harus anda lihat

Apabila pelayan anda bermula dengan betul, anda harus melihat:  
- Keupayaan pelayan disenaraikan dalam Inspector  
- Alat tersedia untuk ujian  
- Pertukaran mesej JSON-RPC berjaya  
- Respons alat dipaparkan dalam antaramuka  

### Isu biasa dan penyelesaian

**Pelayan tidak mula:**  
- Periksa bahawa semua kebergantungan dipasang: `pip install mcp`  
- Semak sintaks dan penjajaran Python  
- Cari mesej ralat dalam konsol  

**Alat tidak muncul:**  
- Pastikan dekorator `@server.tool()` ada  
- Semak bahawa fungsi alat telah didefinisikan sebelum `main()`  
- Periksa pelayan dikonfigurasikan dengan betul  

**Masalah sambungan:**  
- Pastikan pelayan menggunakan pengangkutan stdio dengan betul  
- Periksa tiada proses lain mengganggu  
- Semak sintaks arahan Inspector  

## Tugasan

Cuba bina pelayan anda dengan lebih banyak keupayaan. Lihat [laman ini](https://api.chucknorris.io/) untuk contohnya, tambahkan alat yang memanggil API. Anda tentukan bagaimana pelayan itu akan kelihatan. Selamat mencuba :)  
## Penyelesaian

[Penyelesaian](./solution/README.md) Berikut adalah kemungkinan penyelesaian dengan kod yang berfungsi.

## Pengajaran Utama

Pengajaran utama dari bab ini adalah seperti berikut:

- Pengangkutan stdio adalah mekanisme yang disyorkan untuk pelayan MCP tempatan.  
- Pengangkutan stdio membolehkan komunikasi lancar antara pelayan MCP dan klien menggunakan aliran input dan output standard.  
- Anda boleh menggunakan kedua-dua Inspector dan Visual Studio Code untuk menggunakan pelayan stdio secara langsung, menjadikan debug dan penyepaduan mudah.

## Sampel

- [Kalkulator Java](../samples/java/calculator/README.md)  
- [Kalkulator .Net](../../../../03-GettingStarted/samples/csharp)  
- [Kalkulator JavaScript](../samples/javascript/README.md)  
- [Kalkulator TypeScript](../samples/typescript/README.md)  
- [Kalkulator Python](../../../../03-GettingStarted/samples/python)  

## Sumber Tambahan

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Apa Seterusnya

## Langkah Seterusnya

Kini setelah anda belajar cara membina pelayan MCP dengan pengangkutan stdio, anda boleh menerokai topik yang lebih maju:

- **Seterusnya**: [Penstriman HTTP dengan MCP (Streamable HTTP)](../06-http-streaming/README.md) - Ketahui mengenai mekanisme pengangkutan lain yang disokong untuk pelayan jauh  
- **Lanjutan**: [Amalan Terbaik Keselamatan MCP](../../02-Security/README.md) - Laksanakan keselamatan dalam pelayan MCP anda  
- **Pengeluaran**: [Strategi Pengeluaran](../09-deployment/README.md) - Mengedarkan pelayan anda untuk penggunaan pengeluaran

## Sumber Tambahan

- [Spesifikasi MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Spesifikasi rasmi  
- [Dokumentasi MCP SDK](https://github.com/modelcontextprotocol/sdk) - Rujukan SDK untuk semua bahasa  
- [Contoh Komuniti](../../06-CommunityContributions/README.md) - Lebih banyak contoh pelayan dari komuniti

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi ralat atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->