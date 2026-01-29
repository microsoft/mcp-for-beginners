# Menjalankan Sampel Ini

Berikut adalah cara menjalankan pelayan dan klien penstriman HTTP klasik, serta pelayan dan klien penstriman MCP menggunakan Python.

### Gambaran Umum

- Anda akan menyediakan pelayan MCP yang menstrimkan notifikasi kemajuan kepada klien semasa ia memproses item.
- Klien akan memaparkan setiap notifikasi secara masa nyata.
- Panduan ini merangkumi prasyarat, penyediaan, cara menjalankan, dan penyelesaian masalah.

### Prasyarat

- Python 3.9 atau lebih baru
- Pakej Python `mcp` (pasang dengan `pip install mcp`)

### Pemasangan & Penyediaan

1. Klon repositori atau muat turun fail penyelesaian.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Buat dan aktifkan persekitaran maya (disarankan):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Pasang kebergantungan yang diperlukan:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Fail

- **Pelayan:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Klien:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Menjalankan Pelayan Penstriman HTTP Klasik

1. Pergi ke direktori penyelesaian:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Mulakan pelayan penstriman HTTP klasik:

   ```pwsh
   python server.py
   ```

3. Pelayan akan bermula dan memaparkan:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Menjalankan Klien Penstriman HTTP Klasik

1. Buka terminal baru (aktifkan persekitaran maya dan direktori yang sama):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Anda akan melihat mesej yang distrim dicetak secara berurutan:

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

### Menjalankan Pelayan Penstriman MCP

1. Pergi ke direktori penyelesaian:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Mulakan pelayan MCP dengan pengangkutan streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Pelayan akan bermula dan memaparkan:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Menjalankan Klien Penstriman MCP

1. Buka terminal baru (aktifkan persekitaran maya dan direktori yang sama):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Anda akan melihat notifikasi dicetak secara masa nyata semasa pelayan memproses setiap item:
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

### Langkah-Langkah Utama Pelaksanaan

1. **Buat pelayan MCP menggunakan FastMCP.**
2. **Tentukan alat yang memproses senarai dan menghantar notifikasi menggunakan `ctx.info()` atau `ctx.log()`.**
3. **Jalankan pelayan dengan `transport="streamable-http"`.**
4. **Laksanakan klien dengan pengendali mesej untuk memaparkan notifikasi semasa ia tiba.**

### Penjelasan Kod
- Pelayan menggunakan fungsi async dan konteks MCP untuk menghantar kemas kini kemajuan.
- Klien melaksanakan pengendali mesej async untuk mencetak notifikasi dan hasil akhir.

### Petua & Penyelesaian Masalah

- Gunakan `async/await` untuk operasi yang tidak menyekat.
- Sentiasa tangani pengecualian di kedua-dua pelayan dan klien untuk ketahanan.
- Uji dengan pelbagai klien untuk melihat kemas kini masa nyata.
- Jika anda menghadapi ralat, periksa versi Python anda dan pastikan semua kebergantungan telah dipasang.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.