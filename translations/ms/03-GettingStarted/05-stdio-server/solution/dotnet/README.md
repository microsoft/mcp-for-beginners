# MCP stdio Server - Penyelesaian .NET

> **⚠️ Penting**: Penyelesaian ini telah dikemas kini untuk menggunakan **pengangkutan stdio** seperti yang disarankan oleh Spesifikasi MCP 2025-06-18. Pengangkutan SSE asal telah dihentikan.

## Gambaran Keseluruhan

Penyelesaian .NET ini menunjukkan cara membina pelayan MCP menggunakan pengangkutan stdio terkini. Pengangkutan stdio lebih mudah, lebih selamat, dan memberikan prestasi yang lebih baik berbanding pendekatan SSE yang telah dihentikan.

## Prasyarat

- SDK .NET 9.0 atau lebih baru
- Pemahaman asas tentang suntikan kebergantungan .NET

## Arahan Persediaan

### Langkah 1: Pulihkan kebergantungan

```bash
dotnet restore
```

### Langkah 2: Bina projek

```bash
dotnet build
```

## Menjalankan Pelayan

Pelayan stdio berfungsi secara berbeza daripada pelayan berasaskan HTTP yang lama. Sebaliknya, ia berkomunikasi melalui stdin/stdout:

```bash
dotnet run
```

**Penting**: Pelayan akan kelihatan seperti tergantung - ini adalah normal! Ia sedang menunggu mesej JSON-RPC daripada stdin.

## Ujian Pelayan

### Kaedah 1: Menggunakan MCP Inspector (Disarankan)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Ini akan:
1. Melancarkan pelayan anda sebagai subprocess
2. Membuka antara muka web untuk ujian
3. Membolehkan anda menguji semua alat pelayan secara interaktif

### Kaedah 2: Ujian terus melalui baris arahan

Anda juga boleh menguji dengan melancarkan Inspector secara langsung:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Alat yang Tersedia

Pelayan menyediakan alat berikut:

- **AddNumbers(a, b)**: Menambah dua nombor
- **MultiplyNumbers(a, b)**: Mendarab dua nombor  
- **GetGreeting(name)**: Menjana ucapan peribadi
- **GetServerInfo()**: Mendapatkan maklumat tentang pelayan

### Ujian dengan Claude Desktop

Untuk menggunakan pelayan ini dengan Claude Desktop, tambahkan konfigurasi ini ke `claude_desktop_config.json` anda:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Struktur Projek

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Perbezaan Utama dari HTTP/SSE

**Pengangkutan stdio (Terkini):**
- ✅ Persediaan lebih mudah - tidak memerlukan pelayan web
- ✅ Keselamatan lebih baik - tiada endpoint HTTP
- ✅ Menggunakan `Host.CreateApplicationBuilder()` dan bukannya `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` dan bukannya `WithHttpTransport()`
- ✅ Aplikasi konsol dan bukannya aplikasi web
- ✅ Prestasi lebih baik

**Pengangkutan HTTP/SSE (Dihentikan):**
- ❌ Memerlukan pelayan web ASP.NET Core
- ❌ Memerlukan persediaan routing `app.MapMcp()`
- ❌ Konfigurasi dan kebergantungan lebih kompleks
- ❌ Pertimbangan keselamatan tambahan
- ❌ Kini dihentikan dalam MCP 2025-06-18

## Ciri Pembangunan

- **Suntikan Kebergantungan**: Sokongan penuh DI untuk perkhidmatan dan log
- **Log Berstruktur**: Log yang betul ke stderr menggunakan `ILogger<T>`
- **Atribut Alat**: Definisi alat yang bersih menggunakan atribut `[McpServerTool]`
- **Sokongan Async**: Semua alat menyokong operasi async
- **Pengendalian Ralat**: Pengendalian ralat dan log yang baik

## Petua Pembangunan

- Gunakan `ILogger` untuk log (jangan tulis terus ke stdout)
- Bina dengan `dotnet build` sebelum ujian
- Uji dengan Inspector untuk debugging visual
- Semua log secara automatik pergi ke stderr
- Pelayan mengendalikan isyarat penutupan dengan baik

Penyelesaian ini mengikuti spesifikasi MCP terkini dan menunjukkan amalan terbaik untuk pelaksanaan pengangkutan stdio menggunakan .NET.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.