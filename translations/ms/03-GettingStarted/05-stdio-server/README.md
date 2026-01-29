# Pelayan MCP dengan Pengangkutan stdio

> **⚠️ Kemas Kini Penting**: Mulai Spesifikasi MCP 2025-06-18, pengangkutan SSE (Server-Sent Events) yang berdiri sendiri telah **dihentikan** dan digantikan dengan pengangkutan "Streamable HTTP". Spesifikasi MCP semasa mendefinisikan dua mekanisme pengangkutan utama:
> 1. **stdio** - Input/output standard (disarankan untuk pelayan tempatan)
> 2. **Streamable HTTP** - Untuk pelayan jauh yang mungkin menggunakan SSE secara dalaman
>
> Pelajaran ini telah dikemas kini untuk memberi fokus kepada **pengangkutan stdio**, yang merupakan pendekatan yang disarankan untuk kebanyakan implementasi pelayan MCP.

Pengangkutan stdio membolehkan pelayan MCP berkomunikasi dengan klien melalui aliran input dan output standard. Ini adalah mekanisme pengangkutan yang paling biasa digunakan dan disarankan dalam spesifikasi MCP semasa, menyediakan cara yang mudah dan efisien untuk membina pelayan MCP yang boleh diintegrasikan dengan pelbagai aplikasi klien.

## Gambaran Keseluruhan

Pelajaran ini merangkumi cara membina dan menggunakan Pelayan MCP menggunakan pengangkutan stdio.

## Objektif Pembelajaran

Pada akhir pelajaran ini, anda akan dapat:

- Membina Pelayan MCP menggunakan pengangkutan stdio.
- Menyahpepijat Pelayan MCP menggunakan Inspector.
- Menggunakan Pelayan MCP dengan Visual Studio Code.
- Memahami mekanisme pengangkutan MCP semasa dan mengapa stdio disarankan.

## Pengangkutan stdio - Cara Ia Berfungsi

Pengangkutan stdio adalah salah satu daripada dua jenis pengangkutan yang disokong dalam spesifikasi MCP semasa (2025-06-18). Berikut adalah cara ia berfungsi:

- **Komunikasi Mudah**: Pelayan membaca mesej JSON-RPC dari input standard (`stdin`) dan menghantar mesej ke output standard (`stdout`).
- **Berasaskan Proses**: Klien melancarkan pelayan MCP sebagai subprocess.
- **Format Mesej**: Mesej adalah permintaan, pemberitahuan, atau respons JSON-RPC individu, dipisahkan oleh baris baru.
- **Log**: Pelayan BOLEH menulis string UTF-8 ke ralat standard (`stderr`) untuk tujuan log.

### Keperluan Utama:
- Mesej MESTI dipisahkan oleh baris baru dan MESTI TIDAK mengandungi baris baru yang tertanam.
- Pelayan MESTI TIDAK menulis apa-apa ke `stdout` yang bukan mesej MCP yang sah.
- Klien MESTI TIDAK menulis apa-apa ke `stdin` pelayan yang bukan mesej MCP yang sah.

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

Dalam kod di atas:

- Kami mengimport kelas `Server` dan `StdioServerTransport` dari MCP SDK.
- Kami mencipta instance pelayan dengan konfigurasi dan keupayaan asas.

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

Dalam kod di atas, kami:

- Mencipta instance pelayan menggunakan MCP SDK.
- Mendefinisikan alat menggunakan dekorator.
- Menggunakan pengurus konteks stdio_server untuk mengendalikan pengangkutan.

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

Perbezaan utama dari SSE adalah bahawa pelayan stdio:

- Tidak memerlukan persediaan pelayan web atau endpoint HTTP.
- Dilancarkan sebagai subprocess oleh klien.
- Berkomunikasi melalui aliran stdin/stdout.
- Lebih mudah untuk dilaksanakan dan disahpepijat.

## Latihan: Membuat Pelayan stdio

Untuk membuat pelayan kami, kami perlu mengingat dua perkara:

- Kami perlu menggunakan pelayan web untuk mendedahkan endpoint untuk sambungan dan mesej.

## Makmal: Membuat pelayan MCP stdio yang ringkas

Dalam makmal ini, kami akan membuat pelayan MCP yang ringkas menggunakan pengangkutan stdio yang disarankan. Pelayan ini akan mendedahkan alat yang boleh dipanggil oleh klien menggunakan Protokol Model Context standard.

### Prasyarat

- Python 3.8 atau lebih baru.
- MCP Python SDK: `pip install mcp`.
- Pemahaman asas tentang pengaturcaraan async.

Mari kita mulakan dengan membuat pelayan MCP stdio pertama kita:

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

## Perbezaan utama dari pendekatan SSE yang dihentikan

**Pengangkutan Stdio (Standard Semasa):**
- Model subprocess yang mudah - klien melancarkan pelayan sebagai proses anak.
- Komunikasi melalui stdin/stdout menggunakan mesej JSON-RPC.
- Tidak memerlukan persediaan pelayan HTTP.
- Prestasi dan keselamatan yang lebih baik.
- Penyahpepijatan dan pembangunan yang lebih mudah.

**Pengangkutan SSE (Dihentikan mulai MCP 2025-06-18):**
- Memerlukan pelayan HTTP dengan endpoint SSE.
- Persediaan yang lebih kompleks dengan infrastruktur pelayan web.
- Pertimbangan keselamatan tambahan untuk endpoint HTTP.
- Kini digantikan oleh Streamable HTTP untuk senario berasaskan web.

### Membuat pelayan dengan pengangkutan stdio

Untuk membuat pelayan stdio kami, kami perlu:

1. **Mengimport pustaka yang diperlukan** - Kami memerlukan komponen pelayan MCP dan pengangkutan stdio.
2. **Mencipta instance pelayan** - Mendefinisikan pelayan dengan keupayaannya.
3. **Mendefinisikan alat** - Menambah fungsi yang ingin kami dedahkan.
4. **Menyiapkan pengangkutan** - Mengkonfigurasi komunikasi stdio.
5. **Menjalankan pelayan** - Memulakan pelayan dan mengendalikan mesej.

Mari kita bina langkah demi langkah:

### Langkah 1: Membuat pelayan stdio asas

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

### Langkah 2: Menambah lebih banyak alat

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

Pelayan akan bermula dan menunggu input dari stdin. Ia berkomunikasi menggunakan mesej JSON-RPC melalui pengangkutan stdio.

### Langkah 4: Ujian dengan Inspector

Anda boleh menguji pelayan anda menggunakan MCP Inspector:

1. Pasang Inspector: `npx @modelcontextprotocol/inspector`.
2. Jalankan Inspector dan arahkan ke pelayan anda.
3. Uji alat yang telah anda buat.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Menyahpepijat pelayan stdio anda

### Menggunakan MCP Inspector

MCP Inspector adalah alat yang berguna untuk menyahpepijat dan menguji pelayan MCP. Berikut adalah cara menggunakannya dengan pelayan stdio anda:

1. **Pasang Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Jalankan Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Uji pelayan anda**: Inspector menyediakan antara muka web di mana anda boleh:
   - Melihat keupayaan pelayan.
   - Menguji alat dengan parameter yang berbeza.
   - Memantau mesej JSON-RPC.
   - Menyahpepijat isu sambungan.

### Menggunakan VS Code

Anda juga boleh menyahpepijat pelayan MCP anda secara langsung dalam VS Code:

1. Buat konfigurasi pelancaran dalam `.vscode/launch.json`:
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

2. Tetapkan breakpoint dalam kod pelayan anda.
3. Jalankan debugger dan uji dengan Inspector.

### Petua penyahpepijatan biasa

- Gunakan `stderr` untuk log - jangan menulis ke `stdout` kerana ia dikhaskan untuk mesej MCP.
- Pastikan semua mesej JSON-RPC dipisahkan oleh baris baru.
- Uji dengan alat yang mudah terlebih dahulu sebelum menambah fungsi yang kompleks.
- Gunakan Inspector untuk mengesahkan format mesej.

## Menggunakan pelayan stdio anda dalam VS Code

Setelah anda membina pelayan MCP stdio anda, anda boleh mengintegrasikannya dengan VS Code untuk menggunakannya dengan Claude atau klien lain yang serasi dengan MCP.

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

2. **Mulakan semula Claude**: Tutup dan buka semula Claude untuk memuatkan konfigurasi pelayan baru.

3. **Uji sambungan**: Mulakan perbualan dengan Claude dan cuba gunakan alat pelayan anda:
   - "Bolehkan anda menyapa saya menggunakan alat sapaan?"
   - "Kira jumlah 15 dan 27."
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

Dalam pelajaran yang dikemas kini ini, anda telah belajar cara:

- Membina pelayan MCP menggunakan **pengangkutan stdio** semasa (pendekatan yang disarankan).
- Memahami mengapa pengangkutan SSE dihentikan memihak kepada stdio dan Streamable HTTP.
- Membuat alat yang boleh dipanggil oleh klien MCP.
- Menyahpepijat pelayan anda menggunakan MCP Inspector.
- Mengintegrasikan pelayan stdio anda dengan VS Code dan Claude.

Pengangkutan stdio menyediakan cara yang lebih mudah, lebih selamat, dan lebih berprestasi untuk membina pelayan MCP berbanding pendekatan SSE yang dihentikan. Ia adalah pengangkutan yang disarankan untuk kebanyakan implementasi pelayan MCP mulai spesifikasi 2025-06-18.

### .NET

1. Mari kita buat beberapa alat terlebih dahulu, untuk ini kita akan membuat fail *Tools.cs* dengan kandungan berikut:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Latihan: Menguji pelayan stdio anda

Sekarang setelah anda membina pelayan stdio anda, mari kita uji untuk memastikan ia berfungsi dengan betul.

### Prasyarat

1. Pastikan anda telah memasang MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Kod pelayan anda harus disimpan (contohnya, sebagai `server.py`).

### Ujian dengan Inspector

1. **Mulakan Inspector dengan pelayan anda**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Buka antara muka web**: Inspector akan membuka tetingkap pelayar yang menunjukkan keupayaan pelayan anda.

3. **Uji alat**: 
   - Cuba alat `get_greeting` dengan nama yang berbeza.
   - Uji alat `calculate_sum` dengan nombor yang berbeza.
   - Panggil alat `get_server_info` untuk melihat metadata pelayan.

4. **Pantau komunikasi**: Inspector menunjukkan mesej JSON-RPC yang dipertukarkan antara klien dan pelayan.

### Apa yang anda harus lihat

Apabila pelayan anda bermula dengan betul, anda seharusnya melihat:
- Keupayaan pelayan disenaraikan dalam Inspector.
- Alat tersedia untuk diuji.
- Pertukaran mesej JSON-RPC yang berjaya.
- Respons alat dipaparkan dalam antara muka.

### Isu biasa dan penyelesaian

**Pelayan tidak bermula:**
- Periksa bahawa semua kebergantungan telah dipasang: `pip install mcp`.
- Sahkan sintaks Python dan indentasi.
- Cari mesej ralat dalam konsol.

**Alat tidak muncul:**
- Pastikan dekorator `@server.tool()` hadir.
- Periksa bahawa fungsi alat ditakrifkan sebelum `main()`.
- Sahkan pelayan dikonfigurasi dengan betul.

**Isu sambungan:**
- Pastikan pelayan menggunakan pengangkutan stdio dengan betul.
- Periksa bahawa tiada proses lain yang mengganggu.
- Sahkan sintaks arahan Inspector.

## Tugasan

Cuba bina pelayan anda dengan lebih banyak keupayaan. Lihat [halaman ini](https://api.chucknorris.io/) untuk, sebagai contoh, menambah alat yang memanggil API. Anda tentukan bagaimana pelayan itu seharusnya kelihatan. Selamat mencuba :)

## Penyelesaian

[Penyelesaian](./solution/README.md) Berikut adalah penyelesaian yang mungkin dengan kod yang berfungsi.

## Poin Penting

Poin penting dari bab ini adalah seperti berikut:

- Pengangkutan stdio adalah mekanisme yang disarankan untuk pelayan MCP tempatan.
- Pengangkutan stdio membolehkan komunikasi lancar antara pelayan MCP dan klien menggunakan aliran input dan output standard.
- Anda boleh menggunakan kedua-dua Inspector dan Visual Studio Code untuk menggunakan pelayan stdio secara langsung, menjadikan penyahpepijatan dan integrasi lebih mudah.

## Contoh 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Sumber Tambahan

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Apa Seterusnya

## Langkah Seterusnya

Sekarang setelah anda belajar cara membina pelayan MCP dengan pengangkutan stdio, anda boleh meneroka topik yang lebih maju:

- **Seterusnya**: [HTTP Streaming dengan MCP (Streamable HTTP)](../06-http-streaming/README.md) - Pelajari tentang mekanisme pengangkutan lain yang disokong untuk pelayan jauh.
- **Lanjutan**: [Amalan Terbaik Keselamatan MCP](../../02-Security/README.md) - Laksanakan keselamatan dalam pelayan MCP anda.
- **Pengeluaran**: [Strategi Penerapan](../09-deployment/README.md) - Terapkan pelayan anda untuk penggunaan pengeluaran.

## Sumber Tambahan

- [Spesifikasi MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Spesifikasi rasmi.
- [Dokumentasi MCP SDK](https://github.com/modelcontextprotocol/sdk) - Rujukan SDK untuk semua bahasa.
- [Contoh Komuniti](../../06-CommunityContributions/README.md) - Lebih banyak contoh pelayan dari komuniti.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.