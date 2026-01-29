# MCP stdio Server - Solusi .NET

> **⚠️ Penting**: Solusi ini telah diperbarui untuk menggunakan **transport stdio** sesuai rekomendasi Spesifikasi MCP 2025-06-18. Transport SSE yang lama telah dihentikan.

## Gambaran Umum

Solusi .NET ini menunjukkan cara membangun server MCP menggunakan transport stdio terkini. Transport stdio lebih sederhana, lebih aman, dan memberikan kinerja yang lebih baik dibandingkan pendekatan SSE yang sudah dihentikan.

## Prasyarat

- .NET 9.0 SDK atau yang lebih baru
- Pemahaman dasar tentang dependency injection di .NET

## Instruksi Pengaturan

### Langkah 1: Pulihkan dependensi

```bash
dotnet restore
```

### Langkah 2: Bangun proyek

```bash
dotnet build
```

## Menjalankan Server

Server stdio berjalan dengan cara yang berbeda dibandingkan server berbasis HTTP yang lama. Alih-alih memulai server web, server ini berkomunikasi melalui stdin/stdout:

```bash
dotnet run
```

**Penting**: Server akan tampak seperti berhenti - ini normal! Server sedang menunggu pesan JSON-RPC dari stdin.

## Menguji Server

### Metode 1: Menggunakan MCP Inspector (Direkomendasikan)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Langkah ini akan:
1. Meluncurkan server Anda sebagai subprocess
2. Membuka antarmuka web untuk pengujian
3. Memungkinkan Anda menguji semua alat server secara interaktif

### Metode 2: Pengujian langsung melalui command line

Anda juga dapat menguji dengan langsung meluncurkan Inspector:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Alat yang Tersedia

Server menyediakan alat-alat berikut:

- **AddNumbers(a, b)**: Menjumlahkan dua angka
- **MultiplyNumbers(a, b)**: Mengalikan dua angka  
- **GetGreeting(name)**: Membuat salam yang dipersonalisasi
- **GetServerInfo()**: Mendapatkan informasi tentang server

### Pengujian dengan Claude Desktop

Untuk menggunakan server ini dengan Claude Desktop, tambahkan konfigurasi berikut ke `claude_desktop_config.json` Anda:

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

## Struktur Proyek

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Perbedaan Utama dari HTTP/SSE

**Transport stdio (Saat Ini):**
- ✅ Pengaturan lebih sederhana - tidak memerlukan server web
- ✅ Keamanan lebih baik - tidak ada endpoint HTTP
- ✅ Menggunakan `Host.CreateApplicationBuilder()` alih-alih `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` alih-alih `WithHttpTransport()`
- ✅ Aplikasi konsol alih-alih aplikasi web
- ✅ Kinerja lebih baik

**Transport HTTP/SSE (Dihentikan):**
- ❌ Membutuhkan server web ASP.NET Core
- ❌ Memerlukan pengaturan routing `app.MapMcp()`
- ❌ Konfigurasi dan dependensi lebih kompleks
- ❌ Pertimbangan keamanan tambahan
- ❌ Sekarang dihentikan dalam MCP 2025-06-18

## Fitur Pengembangan

- **Dependency Injection**: Dukungan penuh DI untuk layanan dan logging
- **Structured Logging**: Logging yang terstruktur ke stderr menggunakan `ILogger<T>`
- **Tool Attributes**: Definisi alat yang bersih menggunakan atribut `[McpServerTool]`
- **Dukungan Async**: Semua alat mendukung operasi async
- **Penanganan Kesalahan**: Penanganan kesalahan yang baik dan logging

## Tips Pengembangan

- Gunakan `ILogger` untuk logging (jangan pernah menulis langsung ke stdout)
- Bangun dengan `dotnet build` sebelum pengujian
- Uji dengan Inspector untuk debugging visual
- Semua logging secara otomatis diarahkan ke stderr
- Server menangani sinyal shutdown dengan baik

Solusi ini mengikuti spesifikasi MCP terkini dan menunjukkan praktik terbaik untuk implementasi transport stdio menggunakan .NET.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.