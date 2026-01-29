# MCP stdio Server - Penyelesaian Python

> **⚠️ Penting**: Penyelesaian ini telah dikemas kini untuk menggunakan **pengangkutan stdio** seperti yang disarankan oleh Spesifikasi MCP 2025-06-18. Pengangkutan SSE asal telah dihentikan.

## Gambaran Keseluruhan

Penyelesaian Python ini menunjukkan cara membina pelayan MCP menggunakan pengangkutan stdio terkini. Pengangkutan stdio lebih mudah, lebih selamat, dan memberikan prestasi yang lebih baik berbanding pendekatan SSE yang telah dihentikan.

## Prasyarat

- Python 3.8 atau lebih terkini
- Disarankan untuk memasang `uv` untuk pengurusan pakej, lihat [arahan](https://docs.astral.sh/uv/#highlights)

## Arahan Persediaan

### Langkah 1: Buat persekitaran maya

```bash
python -m venv venv
```

### Langkah 2: Aktifkan persekitaran maya

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Langkah 3: Pasang kebergantungan

```bash
pip install mcp
```

## Menjalankan Pelayan

Pelayan stdio berfungsi secara berbeza daripada pelayan SSE lama. Sebaliknya daripada memulakan pelayan web, ia berkomunikasi melalui stdin/stdout:

```bash
python server.py
```

**Penting**: Pelayan akan kelihatan seperti tergantung - ini adalah normal! Ia sedang menunggu mesej JSON-RPC daripada stdin.

## Menguji Pelayan

### Kaedah 1: Menggunakan MCP Inspector (Disarankan)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Ini akan:
1. Melancarkan pelayan anda sebagai subprocess
2. Membuka antara muka web untuk ujian
3. Membolehkan anda menguji semua alat pelayan secara interaktif

### Kaedah 2: Ujian JSON-RPC secara langsung

Anda juga boleh menguji dengan menghantar mesej JSON-RPC secara langsung:

1. Mulakan pelayan: `python server.py`
2. Hantar mesej JSON-RPC (contoh):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Pelayan akan memberikan respons dengan alat yang tersedia

### Alat yang Tersedia

Pelayan menyediakan alat berikut:

- **add(a, b)**: Menjumlahkan dua nombor
- **multiply(a, b)**: Mendarabkan dua nombor  
- **get_greeting(name)**: Menjana ucapan peribadi
- **get_server_info()**: Mendapatkan maklumat tentang pelayan

### Ujian dengan Claude Desktop

Untuk menggunakan pelayan ini dengan Claude Desktop, tambahkan konfigurasi ini ke dalam `claude_desktop_config.json`:

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

## Perbezaan Utama dari SSE

**Pengangkutan stdio (Terkini):**
- ✅ Persediaan lebih mudah - tidak memerlukan pelayan web
- ✅ Keselamatan lebih baik - tiada endpoint HTTP
- ✅ Komunikasi berasaskan subprocess
- ✅ JSON-RPC melalui stdin/stdout
- ✅ Prestasi lebih baik

**Pengangkutan SSE (Dihentikan):**
- ❌ Memerlukan persediaan pelayan HTTP
- ❌ Memerlukan rangka kerja web (Starlette/FastAPI)
- ❌ Pengurusan routing dan sesi lebih kompleks
- ❌ Pertimbangan keselamatan tambahan
- ❌ Kini dihentikan dalam MCP 2025-06-18

## Petua Penyahpepijatan

- Gunakan `stderr` untuk log (jangan gunakan `stdout`)
- Uji dengan Inspector untuk penyahpepijatan visual
- Pastikan semua mesej JSON dipisahkan dengan baris baru
- Periksa bahawa pelayan bermula tanpa ralat

Penyelesaian ini mengikuti spesifikasi MCP terkini dan menunjukkan amalan terbaik untuk pelaksanaan pengangkutan stdio.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.