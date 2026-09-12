# Mengatur Klien Host MCP Populer

> [!NOTE]
> Konfigurasi host yang mengarah ke `/sse` adalah contoh legasi HTTP+SSE untuk
> MCP `2025-11-25`. Untuk MCP `2026-07-28`, pilih Streamable HTTP di host yang
> mendukungnya dan gunakan endpoint yang dikonfigurasi oleh server.

Panduan ini membahas cara mengonfigurasi dan menggunakan server MCP dengan aplikasi host AI populer. Setiap host memiliki pendekatan konfigurasi sendiri, tetapi setelah disiapkan, semuanya berkomunikasi dengan server MCP menggunakan protokol standar.

## Apa itu Host MCP?

**Host MCP** adalah aplikasi AI yang dapat terhubung ke server MCP untuk memperluas kemampuannya. Anggaplah sebagai "front end" yang berinteraksi dengan pengguna, sementara server MCP menyediakan alat dan data "back end".

```mermaid
flowchart LR
    User[👤 Pengguna] --> Host[🖥️ Host MCP]
    Host --> S1[Server MCP A]
    Host --> S2[Server MCP B]
    Host --> S3[Server MCP C]
    
    subgraph "Host Populer"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Prasyarat

- Server MCP untuk dihubungkan (lihat [Modul 3.1 - Server Pertama](../01-first-server/README.md))
- Aplikasi host terpasang di sistem Anda
- Familiaritas dasar dengan file konfigurasi JSON

---

## 1. Claude Desktop

**Claude Desktop** adalah aplikasi desktop resmi Anthropic yang mendukung MCP secara native.

### Instalasi

1. Unduh Claude Desktop dari [claude.ai/download](https://claude.ai/download)
2. Instal dan masuk menggunakan akun Anthropic Anda

### Konfigurasi

Claude Desktop menggunakan file konfigurasi JSON untuk mendefinisikan server MCP.

**Lokasi file konfigurasi:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Contoh konfigurasi:**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### Opsi Konfigurasi

| Kolom | Deskripsi | Contoh |
|-------|-------------|---------|
| `command` | Executable yang akan dijalankan | `"python"`, `"node"`, `"npx"` |
| `args` | Argumen baris perintah | `["-m", "my_server"]` |
| `env` | Variabel lingkungan | `{"API_KEY": "xxx"}` |
| `cwd` | Direktori kerja | `"/path/to/server"` |

### Menguji Pengaturan Anda

1. Simpan file konfigurasi
2. Mulai ulang Claude Desktop sepenuhnya (keluar lalu buka lagi)
3. Buka percakapan baru
4. Cari ikon 🔌 yang menandakan server tersambung
5. Coba minta Claude menggunakan salah satu alat Anda

### Memecahkan Masalah Claude Desktop

**Server tidak muncul:**
- Periksa sintaks file konfigurasi dengan validator JSON
- Pastikan jalur perintah benar
- Periksa log Claude Desktop: Bantuan → Tampilkan Log

**Server crash saat startup:**
- Uji server secara manual di terminal terlebih dahulu
- Pastikan variabel lingkungan diatur dengan benar
- Pastikan semua dependensi terpasang

---

## 2. VS Code dengan GitHub Copilot

VS Code mendukung MCP melalui ekstensi GitHub Copilot Chat.

### Prasyarat

1. VS Code 1.99+ terpasang
2. Ekstensi GitHub Copilot terpasang
3. Ekstensi GitHub Copilot Chat terpasang

### Konfigurasi

VS Code menggunakan `.vscode/mcp.json` di workspace atau pengaturan pengguna Anda.

**Konfigurasi workspace** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

**Pengaturan pengguna** (`settings.json`):

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### Menggunakan MCP di VS Code

1. Buka panel Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Ketik `@` untuk melihat alat MCP yang tersedia
3. Gunakan bahasa alami untuk memanggil alat: "Hitung 25 * 48 menggunakan kalkulator"

### Memecahkan Masalah VS Code

**Server MCP tidak dimuat:**
- Periksa panel Output → "MCP" untuk log kesalahan
- Muat ulang jendela: Ctrl+Shift+P → "Developer: Reload Window"
- Pastikan server berjalan secara mandiri terlebih dahulu

---

## 3. Cursor

**Cursor** adalah editor kode berbasis AI pertama dengan dukungan MCP bawaan.

### Instalasi

1. Unduh Cursor dari [cursor.sh](https://cursor.sh)
2. Instal dan masuk

### Konfigurasi

Cursor menggunakan format konfigurasi serupa dengan Claude Desktop.

**Lokasi file konfigurasi:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Contoh konfigurasi:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### Menggunakan MCP di Cursor

1. Buka chat AI Cursor (Ctrl+L / Cmd+L)
2. Alat MCP muncul otomatis dalam saran
3. Minta AI melakukan tugas menggunakan server terhubung

---

## 4. Cline (Berbasis Terminal)

**Cline** adalah klien MCP berbasis terminal, ideal untuk alur kerja command-line.

### Instalasi

```bash
npm install -g @anthropic/cline
```

### Konfigurasi

Cline menggunakan variabel lingkungan dan argumen baris perintah.

**Menggunakan variabel lingkungan:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Menggunakan argumen baris perintah:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**File konfigurasi** (`~/.clinerc`):

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### Menggunakan Cline

```bash
# Mulai sesi interaktif
cline

# Kuery tunggal dengan MCP
cline "Calculate the square root of 144 using the calculator"

# Daftar alat yang tersedia
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** adalah editor kode bertenaga AI lain dengan dukungan MCP.

### Instalasi

1. Unduh Windsurf dari [codeium.com/windsurf](https://codeium.com/windsurf)
2. Instal dan buat akun

### Konfigurasi

Konfigurasi Windsurf diatur melalui UI pengaturan:

1. Buka Pengaturan (Ctrl+, / Cmd+,)
2. Cari "MCP"
3. Klik "Edit di settings.json"

**Contoh konfigurasi:**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## Perbandingan Jenis Transportasi

Host yang berbeda mendukung mekanisme transportasi yang berbeda:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (input/output standar): Terbaik untuk server lokal yang dimulai oleh host
**SSE/HTTP**: Terbaik untuk server jarak jauh atau server yang dibagikan antara beberapa klien

---

## Pemecahan Masalah Umum

### Server tidak mau mulai

1. **Uji server secara manual terlebih dahulu:**
   ```bash
   # Untuk Python
   python -m your_server_module
   
   # Untuk Node.js
   node /path/to/server/index.js
   ```

2. **Periksa jalur perintah:**
   - Gunakan jalur absolut jika memungkinkan
   - Pastikan executable ada di PATH Anda

3. **Verifikasi dependensi:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Server terhubung tapi alat tidak berfungsi

1. **Periksa log server** - Sebagian besar host memiliki opsi logging
2. **Verifikasi pendaftaran alat** - Gunakan MCP Inspector untuk menguji
3. **Periksa izin** - Beberapa alat memerlukan akses file/jaringan

### Variabel lingkungan tidak diteruskan

- Beberapa host memfilter variabel lingkungan
- Gunakan bidang `env` dalam konfigurasi secara eksplisit
- Hindari data sensitif dalam file konfigurasi (gunakan pengelolaan rahasia)

---

## Praktik Keamanan Terbaik

1. **Jangan pernah commit API key** ke file konfigurasi
2. **Gunakan variabel lingkungan** untuk data sensitif
3. **Batasi izin server** hanya pada kebutuhan yang diperlukan
4. **Tinjau kode server** sebelum memberikan akses ke sistem Anda
5. **Gunakan daftar izinkan** untuk akses sistem file dan jaringan

---

## Apa Selanjutnya

- [3.13 - Debugging dengan MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Buat server MCP pertama Anda](../01-first-server/README.md)
- [Modul 5 - Topik Lanjutan](../../05-AdvancedTopics/README.md)

---

## Sumber Daya Tambahan

- [Dokumentasi Claude Desktop MCP](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [Ekstensi VS Code MCP](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [Spesifikasi MCP - Transportasi](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Registri Server MCP Resmi](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->