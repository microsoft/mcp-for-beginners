# Server Kalkulator MCP (Python)

Implementasi server Model Context Protocol (MCP) sederhana dalam Python yang menyediakan fungsi kalkulator dasar.

## Instalasi

Pasang dependensi yang diperlukan:

```bash
pip install -r requirements.txt
```

Atau pasang MCP Python SDK secara langsung:

```bash
pip install mcp>=1.18.0
```

## Penggunaan

### Menjalankan Server

Server ini dirancang untuk digunakan oleh klien MCP (seperti Claude Desktop). Untuk memulai server:

```bash
python mcp_calculator_server.py
```

**Catatan**: Saat dijalankan langsung di terminal, Anda akan melihat kesalahan validasi JSON-RPC. Ini adalah perilaku normal - server sedang menunggu pesan klien MCP yang diformat dengan benar.

### Menguji Fungsi

Untuk menguji bahwa fungsi kalkulator bekerja dengan benar:

```bash
python test_calculator.py
```

## Pemecahan Masalah

### Kesalahan Impor

Jika Anda melihat `ModuleNotFoundError: No module named 'mcp'`, pasang MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### Kesalahan JSON-RPC Saat Menjalankan Langsung

Kesalahan seperti "Invalid JSON: EOF while parsing a value" saat menjalankan server secara langsung adalah hal yang diharapkan. Server membutuhkan pesan dari klien MCP, bukan input langsung dari terminal.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang salah yang timbul dari penggunaan terjemahan ini.