# Pelajaran: Membangun Server MCP Pencarian Web

Bab ini menunjukkan cara membangun agen AI dunia nyata yang terintegrasi dengan API eksternal, menangani berbagai jenis data, mengelola kesalahan, dan mengorkestrasi beberapa alat—semua dalam format siap produksi. Anda akan melihat:

- **Integrasi dengan API eksternal yang memerlukan autentikasi**
- **Menangani berbagai jenis data dari beberapa endpoint**
- **Strategi penanganan kesalahan dan pencatatan yang kuat**
- **Orkestrasi multi-alat dalam satu server**

Di akhir pelajaran, Anda akan memiliki pengalaman praktis dengan pola dan praktik terbaik yang penting untuk aplikasi AI dan LLM tingkat lanjut.

## Pendahuluan

Dalam pelajaran ini, Anda akan belajar cara membangun server dan klien MCP canggih yang memperluas kemampuan LLM dengan data web waktu nyata menggunakan SerpAPI. Ini adalah keterampilan penting untuk mengembangkan agen AI dinamis yang dapat mengakses informasi terkini dari web.

## Tujuan Pembelajaran

Di akhir pelajaran ini, Anda akan mampu:

- Mengintegrasikan API eksternal (seperti SerpAPI) secara aman ke dalam server MCP
- Menerapkan beberapa alat untuk pencarian web, berita, produk, dan tanya jawab
- Mengurai dan memformat data terstruktur untuk konsumsi LLM
- Menangani kesalahan dan mengelola batasan rate API secara efektif
- Membangun dan menguji klien MCP otomatis dan interaktif

## Server MCP Pencarian Web

Bagian ini memperkenalkan arsitektur dan fitur Server MCP Pencarian Web. Anda akan melihat bagaimana FastMCP dan SerpAPI digunakan bersama untuk memperluas kemampuan LLM dengan data web waktu nyata.

### Gambaran Umum

Implementasi ini menampilkan empat alat yang menunjukkan kemampuan MCP untuk menangani tugas yang beragam dan didorong oleh API eksternal secara aman dan efisien:

- **general_search**: Untuk hasil web umum
- **news_search**: Untuk berita terkini
- **product_search**: Untuk data e-commerce
- **qna**: Untuk potongan tanya jawab

### Fitur
- **Contoh Kode**: Menyertakan blok kode spesifik bahasa untuk Python (dan mudah diperluas ke bahasa lain) menggunakan pivot kode untuk kejelasan

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

Sebelum menjalankan klien, ada baiknya memahami apa yang dilakukan server. File [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) mengimplementasikan server MCP, yang menyediakan alat untuk pencarian web, berita, produk, dan tanya jawab dengan mengintegrasikan SerpAPI. Server ini menangani permintaan masuk, mengelola panggilan API, mengurai respons, dan mengembalikan hasil terstruktur ke klien.

Anda dapat meninjau implementasi lengkap di [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Berikut contoh singkat bagaimana server mendefinisikan dan mendaftarkan sebuah alat:

### Server Python

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **Integrasi API Eksternal**: Menunjukkan penanganan kunci API dan permintaan eksternal secara aman
- **Penguraian Data Terstruktur**: Menampilkan cara mengubah respons API menjadi format yang ramah LLM
- **Penanganan Kesalahan**: Penanganan kesalahan yang kuat dengan pencatatan yang sesuai
- **Klien Interaktif**: Menyertakan pengujian otomatis dan mode interaktif untuk pengujian
- **Manajemen Konteks**: Memanfaatkan MCP Context untuk pencatatan dan pelacakan permintaan

## Prasyarat

Sebelum memulai, pastikan lingkungan Anda sudah disiapkan dengan benar dengan mengikuti langkah-langkah berikut. Ini akan memastikan semua dependensi terpasang dan kunci API Anda dikonfigurasi dengan benar untuk pengembangan dan pengujian yang lancar.

- Python 3.8 atau lebih tinggi
- Kunci API SerpAPI (Daftar di [SerpAPI](https://serpapi.com/) - tersedia tier gratis)

## Instalasi

Untuk memulai, ikuti langkah-langkah berikut untuk menyiapkan lingkungan Anda:

1. Pasang dependensi menggunakan uv (direkomendasikan) atau pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Buat file `.env` di root proyek dengan kunci SerpAPI Anda:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Penggunaan

Server MCP Pencarian Web adalah komponen inti yang menyediakan alat untuk pencarian web, berita, produk, dan tanya jawab dengan mengintegrasikan SerpAPI. Server ini menangani permintaan masuk, mengelola panggilan API, mengurai respons, dan mengembalikan hasil terstruktur ke klien.

Anda dapat meninjau implementasi lengkap di [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Menjalankan Server

Untuk memulai server MCP, gunakan perintah berikut:

```bash
python server.py
```

Server akan berjalan sebagai server MCP berbasis stdio yang dapat langsung dihubungkan oleh klien.

### Mode Klien

Klien (`client.py`) mendukung dua mode untuk berinteraksi dengan server MCP:

- **Mode Normal**: Menjalankan pengujian otomatis yang menggunakan semua alat dan memverifikasi responsnya. Ini berguna untuk memeriksa dengan cepat bahwa server dan alat berfungsi seperti yang diharapkan.
- **Mode Interaktif**: Memulai antarmuka berbasis menu di mana Anda dapat memilih dan memanggil alat secara manual, memasukkan kueri khusus, dan melihat hasil secara real time. Ini ideal untuk mengeksplorasi kemampuan server dan bereksperimen dengan input yang berbeda.

Anda dapat meninjau implementasi lengkap di [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Menjalankan Klien

Untuk menjalankan pengujian otomatis (ini akan otomatis memulai server):

```bash
python client.py
```

Atau jalankan dalam mode interaktif:

```bash
python client.py --interactive
```

### Pengujian dengan Metode Berbeda

Ada beberapa cara untuk menguji dan berinteraksi dengan alat yang disediakan oleh server, tergantung kebutuhan dan alur kerja Anda.

#### Menulis Skrip Uji Kustom dengan MCP Python SDK
Anda juga dapat membuat skrip uji Anda sendiri menggunakan MCP Python SDK:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

Dalam konteks ini, "skrip uji" berarti program Python kustom yang Anda tulis untuk bertindak sebagai klien bagi server MCP. Alih-alih menjadi unit test formal, skrip ini memungkinkan Anda terhubung secara programatik ke server, memanggil alat apa pun dengan parameter yang Anda pilih, dan memeriksa hasilnya. Pendekatan ini berguna untuk:
- Membuat prototipe dan bereksperimen dengan panggilan alat
- Memvalidasi bagaimana server merespons input yang berbeda
- Mengotomatisasi pemanggilan alat berulang
- Membangun alur kerja atau integrasi Anda sendiri di atas server MCP

Anda dapat menggunakan skrip uji untuk mencoba kueri baru dengan cepat, men-debug perilaku alat, atau bahkan sebagai titik awal untuk otomatisasi yang lebih maju. Berikut contoh cara menggunakan MCP Python SDK untuk membuat skrip seperti itu:

## Deskripsi Alat

Anda dapat menggunakan alat-alat berikut yang disediakan oleh server untuk melakukan berbagai jenis pencarian dan kueri. Setiap alat dijelaskan di bawah dengan parameter dan contoh penggunaannya.

Bagian ini memberikan detail tentang setiap alat yang tersedia dan parameternya.

### general_search

Melakukan pencarian web umum dan mengembalikan hasil yang diformat.

**Cara memanggil alat ini:**

Anda dapat memanggil `general_search` dari skrip Anda sendiri menggunakan MCP Python SDK, atau secara interaktif menggunakan Inspector atau mode klien interaktif. Berikut contoh kode menggunakan SDK:

# [Contoh Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

Sebagai alternatif, dalam mode interaktif, pilih `general_search` dari menu dan masukkan kueri Anda saat diminta.

**Parameter:**
- `query` (string): Kueri pencarian

**Contoh Permintaan:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Mencari artikel berita terbaru terkait kueri.

**Cara memanggil alat ini:**

Anda dapat memanggil `news_search` dari skrip Anda sendiri menggunakan MCP Python SDK, atau secara interaktif menggunakan Inspector atau mode klien interaktif. Berikut contoh kode menggunakan SDK:

# [Contoh Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

Sebagai alternatif, dalam mode interaktif, pilih `news_search` dari menu dan masukkan kueri Anda saat diminta.

**Parameter:**
- `query` (string): Kueri pencarian

**Contoh Permintaan:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Mencari produk yang sesuai dengan kueri.

**Cara memanggil alat ini:**

Anda dapat memanggil `product_search` dari skrip Anda sendiri menggunakan MCP Python SDK, atau secara interaktif menggunakan Inspector atau mode klien interaktif. Berikut contoh kode menggunakan SDK:

# [Contoh Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

Sebagai alternatif, dalam mode interaktif, pilih `product_search` dari menu dan masukkan kueri Anda saat diminta.

**Parameter:**
- `query` (string): Kueri pencarian produk

**Contoh Permintaan:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Mendapatkan jawaban langsung untuk pertanyaan dari mesin pencari.

**Cara memanggil alat ini:**

Anda dapat memanggil `qna` dari skrip Anda sendiri menggunakan MCP Python SDK, atau secara interaktif menggunakan Inspector atau mode klien interaktif. Berikut contoh kode menggunakan SDK:

# [Contoh Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

Sebagai alternatif, dalam mode interaktif, pilih `qna` dari menu dan masukkan pertanyaan Anda saat diminta.

**Parameter:**
- `question` (string): Pertanyaan yang ingin dicari jawabannya

**Contoh Permintaan:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Detail Kode

Bagian ini menyediakan potongan kode dan referensi untuk implementasi server dan klien.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Lihat [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) dan [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) untuk detail implementasi lengkap.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Konsep Lanjutan dalam Pelajaran Ini

Sebelum mulai membangun, berikut beberapa konsep lanjutan penting yang akan muncul sepanjang bab ini. Memahami ini akan membantu Anda mengikuti materi, bahkan jika Anda baru mengenalnya:

- **Orkestrasi Multi-alat**: Ini berarti menjalankan beberapa alat berbeda (seperti pencarian web, pencarian berita, pencarian produk, dan tanya jawab) dalam satu server MCP. Ini memungkinkan server Anda menangani berbagai tugas, bukan hanya satu.
- **Penanganan Batas Rate API**: Banyak API eksternal (seperti SerpAPI) membatasi berapa banyak permintaan yang bisa Anda buat dalam waktu tertentu. Kode yang baik memeriksa batas ini dan menanganinya dengan baik, sehingga aplikasi Anda tidak rusak jika batas tercapai.
- **Penguraian Data Terstruktur**: Respons API seringkali kompleks dan bersarang. Konsep ini tentang mengubah respons tersebut menjadi format yang bersih dan mudah digunakan yang ramah untuk LLM atau program lain.
- **Pemulihan Kesalahan**: Kadang-kadang terjadi masalah—mungkin jaringan gagal, atau API tidak mengembalikan apa yang Anda harapkan. Pemulihan kesalahan berarti kode Anda dapat menangani masalah ini dan tetap memberikan umpan balik yang berguna, bukan crash.
- **Validasi Parameter**: Ini tentang memeriksa bahwa semua input ke alat Anda benar dan aman digunakan. Ini termasuk menetapkan nilai default dan memastikan tipe data benar, yang membantu mencegah bug dan kebingungan.

Bagian ini akan membantu Anda mendiagnosis dan menyelesaikan masalah umum yang mungkin Anda temui saat bekerja dengan Server MCP Pencarian Web. Jika Anda mengalami kesalahan atau perilaku tak terduga saat menggunakan Server MCP Pencarian Web, bagian pemecahan masalah ini menyediakan solusi untuk masalah yang paling umum. Tinjau tips ini sebelum mencari bantuan lebih lanjut—seringkali ini dapat menyelesaikan masalah dengan cepat.

## Pemecahan Masalah

Saat bekerja dengan Server MCP Pencarian Web, Anda mungkin sesekali mengalami masalah—ini normal saat mengembangkan dengan API eksternal dan alat baru. Bagian ini memberikan solusi praktis untuk masalah yang paling umum, sehingga Anda dapat kembali bekerja dengan cepat. Jika Anda menemukan kesalahan, mulailah di sini: tips di bawah ini membahas masalah yang paling sering dihadapi pengguna dan seringkali dapat menyelesaikan masalah Anda tanpa bantuan tambahan.

### Masalah Umum

Berikut beberapa masalah yang paling sering dialami pengguna, beserta penjelasan jelas dan langkah penyelesaiannya:

1. **SERPAPI_KEY tidak ada di file .env**
   - Jika Anda melihat kesalahan `SERPAPI_KEY environment variable not found`, itu berarti aplikasi Anda tidak dapat menemukan kunci API yang diperlukan untuk mengakses SerpAPI. Untuk memperbaikinya, buat file bernama `.env` di root proyek Anda (jika belum ada) dan tambahkan baris seperti `SERPAPI_KEY=your_serpapi_key_here`. Pastikan mengganti `your_serpapi_key_here` dengan kunci asli Anda dari situs SerpAPI.

2. **Kesalahan modul tidak ditemukan**
   - Kesalahan seperti `ModuleNotFoundError: No module named 'httpx'` menunjukkan bahwa paket Python yang dibutuhkan belum terpasang. Ini biasanya terjadi jika Anda belum menginstal semua dependensi. Untuk mengatasinya, jalankan `pip install -r requirements.txt` di terminal Anda untuk memasang semua yang dibutuhkan proyek.

3. **Masalah koneksi**
   - Jika Anda mendapatkan kesalahan seperti `Error during client execution`, ini sering berarti klien tidak dapat terhubung ke server, atau server tidak berjalan seperti yang diharapkan. Periksa kembali bahwa klien dan server menggunakan versi yang kompatibel, dan bahwa `server.py` ada dan berjalan di direktori yang benar. Memulai ulang server dan klien juga bisa membantu.

4. **Kesalahan SerpAPI**
   - Melihat `Search API returned error status: 401` berarti kunci SerpAPI Anda hilang, salah, atau kadaluarsa. Buka dashboard SerpAPI Anda, verifikasi kunci, dan perbarui file `.env` jika perlu. Jika kunci sudah benar tapi masih muncul kesalahan ini, periksa apakah kuota tier gratis Anda sudah habis.

### Mode Debug

Secara default, aplikasi hanya mencatat informasi penting. Jika Anda ingin melihat lebih banyak detail tentang apa yang terjadi (misalnya, untuk mendiagnosis masalah rumit), Anda dapat mengaktifkan mode DEBUG. Ini akan menampilkan lebih banyak informasi tentang setiap langkah yang diambil aplikasi.

**Contoh: Output Normal**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Contoh: Output DEBUG**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Perhatikan bagaimana mode DEBUG menyertakan baris tambahan tentang permintaan HTTP, respons, dan detail internal lainnya. Ini sangat membantu untuk pemecahan masalah.
Untuk mengaktifkan mode DEBUG, atur level logging ke DEBUG di bagian atas `client.py` atau `server.py` Anda:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## Selanjutnya

- [5.10 Real Time Streaming](../mcp-realtimestreaming/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.