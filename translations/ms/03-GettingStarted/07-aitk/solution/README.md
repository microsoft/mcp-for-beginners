# 📘 Penyelesaian Tugasan: Memperluaskan Server MCP Kalkulator Anda dengan Alat Punca Kuasa Dua

## Gambaran Keseluruhan
Dalam tugasan ini, anda telah menambah baik server MCP kalkulator anda dengan menambah alat baru yang mengira punca kuasa dua sesuatu nombor. Penambahan ini membolehkan ejen AI anda mengendalikan soalan matematik yang lebih kompleks, seperti "Apakah punca kuasa dua bagi 16?" atau "Kira √49," menggunakan arahan dalam bahasa semula jadi.

## 🛠️ Melaksanakan Alat Punca Kuasa Dua
Untuk menambah fungsi ini, anda telah mentakrifkan fungsi alat baru dalam fail server.py anda. Berikut adalah pelaksanaannya:

```python
"""
Sample MCP Calculator Server implementation in Python.

This module demonstrates how to create a simple MCP server with calculator tools
that can perform basic arithmetic operations (add, subtract, multiply, divide).
"""

from mcp.server.fastmcp import FastMCP
import math

server = FastMCP("calculator")

@server.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together and return the result."""
    return a + b

@server.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the result."""
    return a - b

@server.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together and return the result."""
    return a * b

@server.tool()
def divide(a: float, b: float) -> float:
    """
    Divide a by b and return the result.
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@server.tool()
def sqrt(a: float) -> float:
    """
    Return the square root of a.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(a)
```

## 🔍 Cara Ia Berfungsi

- **Import modul `math`**: Untuk melakukan operasi matematik yang lebih daripada aritmetik asas, Python menyediakan modul terbina dalam `math`. Modul ini mengandungi pelbagai fungsi dan pemalar matematik. Dengan mengimportnya menggunakan `import math`, anda boleh menggunakan fungsi seperti `math.sqrt()`, yang mengira punca kuasa dua sesuatu nombor.
- **Definisi Fungsi**: Dekorator `@server.tool()` mendaftarkan fungsi `sqrt` sebagai alat yang boleh diakses oleh ejen AI anda.
- **Parameter Input**: Fungsi ini menerima satu argumen `a` bertipe `float`.
- **Pengendalian Ralat**: Jika `a` adalah negatif, fungsi akan membangkitkan `ValueError` untuk mengelakkan pengiraan punca kuasa dua nombor negatif, yang tidak disokong oleh fungsi `math.sqrt()`.
- **Nilai Pulangan**: Untuk input bukan negatif, fungsi akan memulangkan punca kuasa dua `a` menggunakan kaedah terbina dalam Python `math.sqrt()`.

## 🔄 Memulakan Semula Server
Selepas menambah alat `sqrt` yang baru, adalah penting untuk memulakan semula server MCP anda supaya ejen dapat mengenal pasti dan menggunakan fungsi baru yang telah ditambah.

## 💬 Contoh Arahan untuk Menguji Alat Baru
Berikut adalah beberapa arahan dalam bahasa semula jadi yang boleh anda gunakan untuk menguji fungsi punca kuasa dua:

- "Apakah punca kuasa dua bagi 25?"
- "Kira punca kuasa dua bagi 81."
- "Cari punca kuasa dua bagi 0."
- "Apakah punca kuasa dua bagi 2.25?"

Arahan-arahan ini sepatutnya mengaktifkan ejen untuk menggunakan alat `sqrt` dan memulangkan keputusan yang betul.

## ✅ Ringkasan
Dengan menyelesaikan tugasan ini, anda telah:

- Memperluaskan server MCP kalkulator anda dengan alat `sqrt` yang baru.
- Membolehkan ejen AI anda mengendalikan pengiraan punca kuasa dua melalui arahan dalam bahasa semula jadi.
- Berlatih menambah alat baru dan memulakan semula server untuk mengintegrasikan fungsi tambahan.

Jangan ragu untuk terus mencuba dengan menambah lebih banyak alat matematik, seperti fungsi pendaraban kuasa atau logaritma, untuk terus meningkatkan keupayaan ejen anda!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.