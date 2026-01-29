# MCP stdio Server - Solusi Python

> **⚠️ Penting**: Solusi ini telah diperbarui untuk menggunakan **transport stdio** sesuai rekomendasi Spesifikasi MCP 2025-06-18. Transport SSE yang lama telah dihentikan.

## Ikhtisar

Solusi Python ini menunjukkan cara membangun server MCP menggunakan transport stdio terkini. Transport stdio lebih sederhana, lebih aman, dan memberikan kinerja yang lebih baik dibandingkan pendekatan SSE yang sudah dihentikan.

## Prasyarat

- Python 3.8 atau lebih baru
- Disarankan untuk menginstal `uv` untuk manajemen paket, lihat [instruksi](https://docs.astral.sh/uv/#highlights)

## Instruksi Pengaturan

### Langkah 1: Buat lingkungan virtual

```bash
python -m venv venv
```

### Langkah 2: Aktifkan lingkungan virtual

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Langkah 3: Instal dependensi

```bash
pip install mcp
```

## Menjalankan Server

Server stdio berjalan berbeda dari server SSE yang lama. Alih-alih memulai server web, server ini berkomunikasi melalui stdin/stdout:

```bash
python server.py
```

**Penting**: Server akan tampak seperti berhenti - ini normal! Server sedang menunggu pesan JSON-RPC dari stdin.

## Menguji Server

### Metode 1: Menggunakan MCP Inspector (Direkomendasikan)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Ini akan:
1. Meluncurkan server Anda sebagai subprocess
2. Membuka antarmuka web untuk pengujian
3. Memungkinkan Anda menguji semua alat server secara interaktif

### Metode 2: Pengujian JSON-RPC langsung

Anda juga dapat menguji dengan mengirimkan pesan JSON-RPC secara langsung:

1. Mulai server: `python server.py`
2. Kirim pesan JSON-RPC (contoh):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Server akan merespons dengan alat yang tersedia

### Alat yang Tersedia

Server menyediakan alat berikut:

- **add(a, b)**: Menambahkan dua angka
- **multiply(a, b)**: Mengalikan dua angka  
- **get_greeting(name)**: Membuat salam yang dipersonalisasi
- **get_server_info()**: Mendapatkan informasi tentang server

### Pengujian dengan Claude Desktop

Untuk menggunakan server ini dengan Claude Desktop, tambahkan konfigurasi ini ke `claude_desktop_config.json` Anda:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Perbedaan Utama dari SSE

**Transport stdio (Saat Ini):**
- ✅ Pengaturan lebih sederhana - tidak perlu server web
- ✅ Keamanan lebih baik - tidak ada endpoint HTTP
- ✅ Komunikasi berbasis subprocess
- ✅ JSON-RPC melalui stdin/stdout
- ✅ Kinerja lebih baik

**Transport SSE (Dihentikan):**
- ❌ Memerlukan pengaturan server HTTP
- ❌ Membutuhkan kerangka kerja web (Starlette/FastAPI)
- ❌ Manajemen routing dan sesi lebih kompleks
- ❌ Pertimbangan keamanan tambahan
- ❌ Sekarang dihentikan dalam MCP 2025-06-18

## Tips Debugging

- Gunakan `stderr` untuk logging (jangan pernah `stdout`)
- Uji dengan Inspector untuk debugging visual
- Pastikan semua pesan JSON memiliki pemisah baris
- Periksa apakah server dimulai tanpa kesalahan

Solusi ini mengikuti spesifikasi MCP terkini dan menunjukkan praktik terbaik untuk implementasi transport stdio.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.