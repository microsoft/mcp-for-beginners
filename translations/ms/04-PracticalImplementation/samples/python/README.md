# Model Context Protocol (MCP) Pelaksanaan Python

Repositori ini mengandungi pelaksanaan Python bagi Model Context Protocol (MCP), yang menunjukkan cara untuk mencipta aplikasi server dan klien yang berkomunikasi menggunakan piawaian MCP.

## Gambaran Keseluruhan

Pelaksanaan MCP terdiri daripada dua komponen utama:

1. **MCP Server (`server.py`)** - Server yang menyediakan:
   - **Tools**: Fungsi yang boleh dipanggil dari jauh
   - **Resources**: Data yang boleh diambil
   - **Prompts**: Templat untuk menghasilkan arahan bagi model bahasa

2. **MCP Client (`client.py`)** - Aplikasi klien yang menyambung ke server dan menggunakan ciri-cirinya

## Ciri-ciri

Pelaksanaan ini menunjukkan beberapa ciri utama MCP:

### Tools
- `completion` - Menjana teks lengkap dari model AI (disimulasikan)
- `add` - Kalkulator ringkas yang menambah dua nombor

### Resources
- `models://` - Mengembalikan maklumat tentang model AI yang tersedia
- `greeting://{name}` - Mengembalikan ucapan peribadi untuk nama yang diberikan

### Prompts
- `review_code` - Menjana arahan untuk menyemak kod

## Pemasangan

Untuk menggunakan pelaksanaan MCP ini, pasang pakej yang diperlukan:

```powershell
pip install mcp-server mcp-client
```

## Menjalankan Server dan Klien

### Memulakan Server

Jalankan server dalam satu tetingkap terminal:

```powershell
python server.py
```

Server juga boleh dijalankan dalam mod pembangunan menggunakan MCP CLI:

```powershell
mcp dev server.py
```

Atau dipasang dalam Claude Desktop (jika tersedia):

```powershell
mcp install server.py
```

### Menjalankan Klien

Jalankan klien dalam tetingkap terminal yang lain:

```powershell
python client.py
```

Ini akan menyambung ke server dan menunjukkan semua ciri yang tersedia.

### Penggunaan Klien

Klien (`client.py`) menunjukkan semua keupayaan MCP:

```powershell
python client.py
```

Ini akan menyambung ke server dan menggunakan semua ciri termasuk tools, resources, dan prompts. Output akan menunjukkan:

1. Keputusan alat kalkulator (5 + 7 = 12)
2. Respons alat completion untuk "What is the meaning of life?"
3. Senarai model AI yang tersedia
4. Ucapan peribadi untuk "MCP Explorer"
5. Templat arahan semakan kod

## Butiran Pelaksanaan

Server dilaksanakan menggunakan API `FastMCP`, yang menyediakan abstraksi tahap tinggi untuk mentakrifkan perkhidmatan MCP. Berikut adalah contoh ringkas bagaimana tools ditakrifkan:

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

Klien menggunakan perpustakaan klien MCP untuk menyambung dan memanggil server:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Ketahui Lebih Lanjut

Untuk maklumat lanjut tentang MCP, lawati: https://modelcontextprotocol.io/

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.