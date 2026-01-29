# Pelajaran: Membangun Pelayan MCP Carian Web

Bab ini menunjukkan cara membina agen AI dunia sebenar yang berintegrasi dengan API luaran, mengendalikan pelbagai jenis data, menguruskan ralat, dan mengatur pelbagai alat—semuanya dalam format sedia produksi. Anda akan melihat:

- **Integrasi dengan API luaran yang memerlukan pengesahan**
- **Mengendalikan pelbagai jenis data dari pelbagai titik akhir**
- **Strategi pengendalian ralat dan pencatatan yang kukuh**
- **Pengurusan pelbagai alat dalam satu pelayan**

Pada akhirnya, anda akan mempunyai pengalaman praktikal dengan corak dan amalan terbaik yang penting untuk aplikasi AI dan LLM yang maju.

## Pengenalan

Dalam pelajaran ini, anda akan belajar cara membina pelayan dan klien MCP lanjutan yang memperluaskan keupayaan LLM dengan data web masa nyata menggunakan SerpAPI. Ini adalah kemahiran penting untuk membangunkan agen AI dinamik yang boleh mengakses maklumat terkini dari web.

## Objektif Pembelajaran

Pada akhir pelajaran ini, anda akan dapat:

- Mengintegrasikan API luaran (seperti SerpAPI) dengan selamat ke dalam pelayan MCP
- Melaksanakan pelbagai alat untuk carian web, berita, produk, dan soal jawab
- Mengurai dan memformat data berstruktur untuk penggunaan LLM
- Mengendalikan ralat dan mengurus had kadar API dengan berkesan
- Membina dan menguji klien MCP automatik dan interaktif

## Pelayan MCP Carian Web

Bahagian ini memperkenalkan seni bina dan ciri Pelayan MCP Carian Web. Anda akan melihat bagaimana FastMCP dan SerpAPI digunakan bersama untuk memperluaskan keupayaan LLM dengan data web masa nyata.

### Gambaran Keseluruhan

Pelaksanaan ini menampilkan empat alat yang mempamerkan kebolehan MCP untuk mengendalikan tugasan berasaskan API luaran yang pelbagai dengan selamat dan cekap:

- **general_search**: Untuk keputusan web yang luas
- **news_search**: Untuk tajuk berita terkini
- **product_search**: Untuk data e-dagang
- **qna**: Untuk petikan soal jawab

### Ciri-ciri
- **Contoh Kod**: Termasuk blok kod khusus bahasa untuk Python (dan mudah diperluas ke bahasa lain) menggunakan pivot kod untuk kejelasan

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

Sebelum menjalankan klien, adalah berguna untuk memahami apa yang dilakukan oleh pelayan. Fail [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) melaksanakan pelayan MCP, mendedahkan alat untuk carian web, berita, produk, dan soal jawab dengan mengintegrasikan SerpAPI. Ia mengendalikan permintaan masuk, mengurus panggilan API, mengurai respons, dan mengembalikan hasil berstruktur kepada klien.

Anda boleh menyemak pelaksanaan penuh dalam [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Berikut adalah contoh ringkas bagaimana pelayan mentakrif dan mendaftar alat:

### Pelayan Python

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

- **Integrasi API Luaran**: Menunjukkan pengendalian kunci API dan permintaan luaran dengan selamat
- **Penguraian Data Berstruktur**: Menunjukkan cara menukar respons API ke format mesra LLM
- **Pengendalian Ralat**: Pengendalian ralat yang kukuh dengan pencatatan yang sesuai
- **Klien Interaktif**: Termasuk ujian automatik dan mod interaktif untuk pengujian
- **Pengurusan Konteks**: Memanfaatkan MCP Context untuk pencatatan dan penjejakan permintaan

## Prasyarat

Sebelum anda mula, pastikan persekitaran anda disediakan dengan betul dengan mengikuti langkah-langkah ini. Ini akan memastikan semua kebergantungan dipasang dan kunci API anda dikonfigurasikan dengan betul untuk pembangunan dan pengujian yang lancar.

- Python 3.8 atau lebih tinggi
- Kunci API SerpAPI (Daftar di [SerpAPI](https://serpapi.com/) - pelan percuma tersedia)

## Pemasangan

Untuk memulakan, ikut langkah-langkah berikut untuk menyediakan persekitaran anda:

1. Pasang kebergantungan menggunakan uv (disyorkan) atau pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Buat fail `.env` di akar projek dengan kunci SerpAPI anda:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Penggunaan

Pelayan MCP Carian Web adalah komponen teras yang mendedahkan alat untuk carian web, berita, produk, dan soal jawab dengan mengintegrasikan SerpAPI. Ia mengendalikan permintaan masuk, mengurus panggilan API, mengurai respons, dan mengembalikan hasil berstruktur kepada klien.

Anda boleh menyemak pelaksanaan penuh dalam [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Menjalankan Pelayan

Untuk memulakan pelayan MCP, gunakan arahan berikut:

```bash
python server.py
```

Pelayan akan berjalan sebagai pelayan MCP berasaskan stdio yang boleh disambungkan terus oleh klien.

### Mod Klien

Klien (`client.py`) menyokong dua mod untuk berinteraksi dengan pelayan MCP:

- **Mod Normal**: Menjalankan ujian automatik yang menguji semua alat dan mengesahkan respons mereka. Ini berguna untuk memeriksa dengan cepat bahawa pelayan dan alat berfungsi seperti yang dijangkakan.
- **Mod Interaktif**: Memulakan antara muka menu di mana anda boleh memilih dan memanggil alat secara manual, memasukkan pertanyaan tersuai, dan melihat hasil secara masa nyata. Ini sesuai untuk meneroka keupayaan pelayan dan bereksperimen dengan input yang berbeza.

Anda boleh menyemak pelaksanaan penuh dalam [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Menjalankan Klien

Untuk menjalankan ujian automatik (ini akan memulakan pelayan secara automatik):

```bash
python client.py
```

Atau jalankan dalam mod interaktif:

```bash
python client.py --interactive
```

### Menguji dengan Kaedah Berbeza

Terdapat beberapa cara untuk menguji dan berinteraksi dengan alat yang disediakan oleh pelayan, bergantung pada keperluan dan aliran kerja anda.

#### Menulis Skrip Ujian Tersuai dengan MCP Python SDK
Anda juga boleh membina skrip ujian anda sendiri menggunakan MCP Python SDK:

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

Dalam konteks ini, "skrip ujian" bermaksud program Python tersuai yang anda tulis untuk bertindak sebagai klien bagi pelayan MCP. Daripada menjadi ujian unit formal, skrip ini membolehkan anda menyambung secara programatik ke pelayan, memanggil mana-mana alat dengan parameter pilihan anda, dan memeriksa hasilnya. Pendekatan ini berguna untuk:
- Membuat prototaip dan bereksperimen dengan panggilan alat
- Mengesahkan bagaimana pelayan bertindak balas terhadap input berbeza
- Mengautomasikan panggilan alat berulang
- Membina aliran kerja atau integrasi anda sendiri di atas pelayan MCP

Anda boleh menggunakan skrip ujian untuk mencuba pertanyaan baru dengan cepat, menyahpepijat tingkah laku alat, atau sebagai titik permulaan untuk automasi yang lebih maju. Berikut adalah contoh cara menggunakan MCP Python SDK untuk membuat skrip sedemikian:

## Penerangan Alat

Anda boleh menggunakan alat berikut yang disediakan oleh pelayan untuk melakukan pelbagai jenis carian dan pertanyaan. Setiap alat diterangkan di bawah dengan parameter dan contoh penggunaannya.

Bahagian ini menyediakan butiran tentang setiap alat yang tersedia dan parameternya.

### general_search

Melakukan carian web umum dan mengembalikan hasil yang diformat.

**Cara memanggil alat ini:**

Anda boleh memanggil `general_search` dari skrip anda sendiri menggunakan MCP Python SDK, atau secara interaktif menggunakan Inspector atau mod klien interaktif. Berikut adalah contoh kod menggunakan SDK:

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

Sebagai alternatif, dalam mod interaktif, pilih `general_search` dari menu dan masukkan pertanyaan anda apabila diminta.

**Parameter:**
- `query` (string): Pertanyaan carian

**Contoh Permintaan:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Mencari artikel berita terkini berkaitan dengan pertanyaan.

**Cara memanggil alat ini:**

Anda boleh memanggil `news_search` dari skrip anda sendiri menggunakan MCP Python SDK, atau secara interaktif menggunakan Inspector atau mod klien interaktif. Berikut adalah contoh kod menggunakan SDK:

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

Sebagai alternatif, dalam mod interaktif, pilih `news_search` dari menu dan masukkan pertanyaan anda apabila diminta.

**Parameter:**
- `query` (string): Pertanyaan carian

**Contoh Permintaan:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Mencari produk yang sepadan dengan pertanyaan.

**Cara memanggil alat ini:**

Anda boleh memanggil `product_search` dari skrip anda sendiri menggunakan MCP Python SDK, atau secara interaktif menggunakan Inspector atau mod klien interaktif. Berikut adalah contoh kod menggunakan SDK:

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

Sebagai alternatif, dalam mod interaktif, pilih `product_search` dari menu dan masukkan pertanyaan anda apabila diminta.

**Parameter:**
- `query` (string): Pertanyaan carian produk

**Contoh Permintaan:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Mendapatkan jawapan langsung kepada soalan dari enjin carian.

**Cara memanggil alat ini:**

Anda boleh memanggil `qna` dari skrip anda sendiri menggunakan MCP Python SDK, atau secara interaktif menggunakan Inspector atau mod klien interaktif. Berikut adalah contoh kod menggunakan SDK:

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

Sebagai alternatif, dalam mod interaktif, pilih `qna` dari menu dan masukkan soalan anda apabila diminta.

**Parameter:**
- `question` (string): Soalan untuk mendapatkan jawapan

**Contoh Permintaan:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Butiran Kod

Bahagian ini menyediakan petikan kod dan rujukan untuk pelaksanaan pelayan dan klien.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Lihat [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) dan [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) untuk butiran pelaksanaan penuh.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Konsep Lanjutan dalam Pelajaran Ini

Sebelum anda mula membina, berikut adalah beberapa konsep lanjutan penting yang akan muncul sepanjang bab ini. Memahami ini akan membantu anda mengikuti dengan lebih mudah, walaupun anda baru mengenalinya:

- **Pengurusan Pelbagai Alat**: Ini bermaksud menjalankan beberapa alat berbeza (seperti carian web, carian berita, carian produk, dan soal jawab) dalam satu pelayan MCP. Ia membolehkan pelayan anda mengendalikan pelbagai tugasan, bukan hanya satu.
- **Pengendalian Had Kadar API**: Banyak API luaran (seperti SerpAPI) mengehadkan berapa banyak permintaan yang boleh anda buat dalam tempoh tertentu. Kod yang baik akan memeriksa had ini dan mengendalikannya dengan baik, supaya aplikasi anda tidak rosak jika anda mencapai had.
- **Penguraian Data Berstruktur**: Respons API sering kompleks dan bersarang. Konsep ini berkaitan dengan menukar respons tersebut menjadi format yang bersih dan mudah digunakan yang mesra untuk LLM atau program lain.
- **Pemulihan Ralat**: Kadang-kadang berlaku masalah—mungkin rangkaian gagal, atau API tidak mengembalikan apa yang anda jangkakan. Pemulihan ralat bermaksud kod anda boleh mengendalikan masalah ini dan masih memberikan maklum balas berguna, bukannya terhenti.
- **Pengesahan Parameter**: Ini berkaitan dengan memeriksa bahawa semua input kepada alat anda adalah betul dan selamat digunakan. Ia termasuk menetapkan nilai lalai dan memastikan jenis data betul, yang membantu mengelakkan pepijat dan kekeliruan.

Bahagian ini akan membantu anda mendiagnosis dan menyelesaikan masalah biasa yang mungkin anda hadapi semasa bekerja dengan Pelayan MCP Carian Web. Jika anda menghadapi ralat atau tingkah laku yang tidak dijangka semasa bekerja dengan Pelayan MCP Carian Web, bahagian penyelesaian masalah ini menyediakan penyelesaian untuk isu yang paling biasa. Semak petua ini sebelum mendapatkan bantuan lanjut—ia sering menyelesaikan masalah dengan cepat.

## Penyelesaian Masalah

Semasa bekerja dengan Pelayan MCP Carian Web, anda mungkin kadang-kadang menghadapi masalah—ini adalah perkara biasa apabila membangunkan dengan API luaran dan alat baru. Bahagian ini menyediakan penyelesaian praktikal untuk masalah yang paling biasa, supaya anda boleh kembali ke landasan dengan cepat. Jika anda menghadapi ralat, mulakan di sini: petua di bawah menangani isu yang paling kerap dihadapi pengguna dan sering dapat menyelesaikan masalah anda tanpa bantuan tambahan.

### Isu Biasa

Berikut adalah beberapa masalah yang paling kerap dihadapi pengguna, bersama dengan penjelasan jelas dan langkah untuk menyelesaikannya:

1. **Kunci SERPAPI_KEY hilang dalam fail .env**
   - Jika anda melihat ralat `SERPAPI_KEY environment variable not found`, ini bermakna aplikasi anda tidak dapat mencari kunci API yang diperlukan untuk mengakses SerpAPI. Untuk membetulkannya, buat fail bernama `.env` di akar projek anda (jika belum ada) dan tambah baris seperti `SERPAPI_KEY=your_serpapi_key_here`. Pastikan anda menggantikan `your_serpapi_key_here` dengan kunci sebenar anda dari laman web SerpAPI.

2. **Ralat modul tidak ditemui**
   - Ralat seperti `ModuleNotFoundError: No module named 'httpx'` menunjukkan bahawa pakej Python yang diperlukan tidak dipasang. Ini biasanya berlaku jika anda belum memasang semua kebergantungan. Untuk menyelesaikannya, jalankan `pip install -r requirements.txt` dalam terminal anda untuk memasang semua yang diperlukan oleh projek anda.

3. **Masalah sambungan**
   - Jika anda mendapat ralat seperti `Error during client execution`, ini sering bermakna klien tidak dapat menyambung ke pelayan, atau pelayan tidak berjalan seperti yang dijangkakan. Semak semula bahawa klien dan pelayan adalah versi yang serasi, dan bahawa `server.py` ada dan berjalan di direktori yang betul. Memulakan semula kedua-dua pelayan dan klien juga boleh membantu.

4. **Ralat SerpAPI**
   - Melihat `Search API returned error status: 401` bermakna kunci SerpAPI anda hilang, salah, atau telah tamat tempoh. Pergi ke papan pemuka SerpAPI anda, sahkan kunci anda, dan kemas kini fail `.env` jika perlu. Jika kunci anda betul tetapi anda masih melihat ralat ini, periksa sama ada pelan percuma anda telah habis kuota.

### Mod Debug

Secara lalai, aplikasi hanya mencatat maklumat penting. Jika anda mahu melihat lebih banyak butiran tentang apa yang sedang berlaku (contohnya, untuk mendiagnosis masalah yang rumit), anda boleh mengaktifkan mod DEBUG. Ini akan menunjukkan lebih banyak maklumat tentang setiap langkah yang diambil oleh aplikasi.

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

Perhatikan bagaimana mod DEBUG termasuk baris tambahan tentang permintaan HTTP, respons, dan butiran dalaman lain. Ini sangat membantu untuk penyelesaian masalah.
Untuk mengaktifkan mod DEBUG, tetapkan tahap logging kepada DEBUG di bahagian atas `client.py` atau `server.py` anda:

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

## Apa yang seterusnya

- [5.10 Penstriman Masa Sebenar](../mcp-realtimestreaming/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.