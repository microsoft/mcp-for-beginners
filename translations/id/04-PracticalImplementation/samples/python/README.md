# Implementasi Python Model Context Protocol (MCP)

Repositori ini berisi implementasi Python dari Model Context Protocol (MCP), yang menunjukkan cara membuat aplikasi server dan klien yang berkomunikasi menggunakan standar MCP.

## Ikhtisar

Implementasi MCP terdiri dari dua komponen utama:

1. **MCP Server (`server.py`)** - Server yang menyediakan:
   - **Tools**: Fungsi yang dapat dipanggil secara remote
   - **Resources**: Data yang dapat diambil
   - **Prompts**: Template untuk membuat prompt bagi model bahasa

2. **MCP Client (`client.py`)** - Aplikasi klien yang terhubung ke server dan menggunakan fiturnya

## Fitur

Implementasi ini menunjukkan beberapa fitur utama MCP:

### Tools
- `completion` - Menghasilkan teks penyelesaian dari model AI (disimulasikan)
- `add` - Kalkulator sederhana yang menjumlahkan dua angka

### Resources
- `models://` - Mengembalikan informasi tentang model AI yang tersedia
- `greeting://{name}` - Mengembalikan sapaan personal untuk nama yang diberikan

### Prompts
- `review_code` - Membuat prompt untuk mereview kode

## Instalasi

Untuk menggunakan implementasi MCP ini, pasang paket yang dibutuhkan:

```powershell
pip install mcp-server mcp-client
```

## Menjalankan Server dan Klien

### Memulai Server

Jalankan server di satu jendela terminal:

```powershell
python server.py
```

Server juga dapat dijalankan dalam mode pengembangan menggunakan MCP CLI:

```powershell
mcp dev server.py
```

Atau diinstal di Claude Desktop (jika tersedia):

```powershell
mcp install server.py
```

### Menjalankan Klien

Jalankan klien di jendela terminal lain:

```powershell
python client.py
```

Ini akan terhubung ke server dan mendemonstrasikan semua fitur yang tersedia.

### Penggunaan Klien

Klien (`client.py`) menunjukkan semua kemampuan MCP:

```powershell
python client.py
```

Ini akan terhubung ke server dan menjalankan semua fitur termasuk tools, resources, dan prompts. Output akan menampilkan:

1. Hasil tool kalkulator (5 + 7 = 12)
2. Respon tool completion untuk "What is the meaning of life?"
3. Daftar model AI yang tersedia
4. Sapaan personal untuk "MCP Explorer"
5. Template prompt review kode

## Detail Implementasi

Server diimplementasikan menggunakan API `FastMCP`, yang menyediakan abstraksi tingkat tinggi untuk mendefinisikan layanan MCP. Berikut contoh sederhana bagaimana tools didefinisikan:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

Klien menggunakan library MCP client untuk terhubung dan memanggil server:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Pelajari Lebih Lanjut

Untuk informasi lebih lanjut tentang MCP, kunjungi: https://modelcontextprotocol.io/

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.