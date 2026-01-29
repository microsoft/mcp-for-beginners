# Menjalankan Contoh Ini

Berikut adalah cara menjalankan server dan klien streaming HTTP klasik, serta server dan klien streaming MCP menggunakan Python.

### Gambaran Umum

- Anda akan mengatur server MCP yang mengirimkan notifikasi kemajuan ke klien saat memproses item.
- Klien akan menampilkan setiap notifikasi secara real-time.
- Panduan ini mencakup prasyarat, pengaturan, menjalankan, dan pemecahan masalah.

### Prasyarat

- Python 3.9 atau lebih baru
- Paket Python `mcp` (instal dengan `pip install mcp`)

### Instalasi & Pengaturan

1. Clone repositori atau unduh file solusi.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Buat dan aktifkan lingkungan virtual (disarankan):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Instal dependensi yang diperlukan:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### File

- **Server:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Klien:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Menjalankan Server Streaming HTTP Klasik

1. Masuk ke direktori solusi:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Jalankan server streaming HTTP klasik:

   ```pwsh
   python server.py
   ```

3. Server akan mulai dan menampilkan:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Menjalankan Klien Streaming HTTP Klasik

1. Buka terminal baru (aktifkan lingkungan virtual dan direktori yang sama):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Anda akan melihat pesan yang di-streaming dicetak secara berurutan:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### Menjalankan Server Streaming MCP

1. Masuk ke direktori solusi:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Jalankan server MCP dengan transport streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Server akan mulai dan menampilkan:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Menjalankan Klien Streaming MCP

1. Buka terminal baru (aktifkan lingkungan virtual dan direktori yang sama):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Anda akan melihat notifikasi dicetak secara real-time saat server memproses setiap item:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### Langkah-Langkah Implementasi Utama

1. **Buat server MCP menggunakan FastMCP.**
2. **Definisikan alat yang memproses daftar dan mengirimkan notifikasi menggunakan `ctx.info()` atau `ctx.log()`.**
3. **Jalankan server dengan `transport="streamable-http"`.**
4. **Implementasikan klien dengan handler pesan untuk menampilkan notifikasi saat diterima.**

### Penjelasan Kode
- Server menggunakan fungsi async dan konteks MCP untuk mengirimkan pembaruan kemajuan.
- Klien mengimplementasikan handler pesan async untuk mencetak notifikasi dan hasil akhir.

### Tips & Pemecahan Masalah

- Gunakan `async/await` untuk operasi non-blocking.
- Selalu tangani pengecualian di server dan klien untuk meningkatkan ketahanan.
- Uji dengan beberapa klien untuk mengamati pembaruan real-time.
- Jika Anda mengalami kesalahan, periksa versi Python Anda dan pastikan semua dependensi telah diinstal.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.