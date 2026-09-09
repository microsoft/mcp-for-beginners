# MCP Calculator Server (Python)



Implementasi server Model Context Protocol (MCP) sederhana dalam Python yang menyediakan fungsi kalkulator dasar.


## Instalasi

Pasang dependensi yang diperlukan:

```bash
pip install -r requirements.txt
```

Atau pasang SDK MCP Python langsung:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Penggunaan

### Menjalankan Server

Server ini dirancang untuk digunakan oleh klien MCP (seperti Claude Desktop). Untuk memulai server:

```bash
python mcp_calculator_server.py
```

**Catatan**: Saat dijalankan langsung di terminal, Anda akan melihat kesalahan validasi JSON-RPC. Ini adalah perilaku normal - server menunggu pesan klien MCP yang diformat dengan benar.

### Menguji Fungsi

Untuk menguji bahwa fungsi kalkulator bekerja dengan benar:

```bash
python test_calculator.py
```

## Pemecahan Masalah

### Kesalahan Impor

Jika Anda melihat `ModuleNotFoundError: No module named 'mcp'`, pasang SDK MCP Python:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Kesalahan JSON-RPC Saat Menjalankan Langsung

Kesalahan seperti "Invalid JSON: EOF while parsing a value" saat menjalankan server langsung adalah hal yang diharapkan. Server membutuhkan pesan klien MCP, bukan input langsung dari terminal.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->