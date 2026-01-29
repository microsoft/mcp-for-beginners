# 📘 Solusi Tugas: Memperluas Server MCP Kalkulator Anda dengan Alat Akar Kuadrat

## Ikhtisar
Dalam tugas ini, Anda menambahkan alat baru pada server MCP kalkulator Anda yang dapat menghitung akar kuadrat dari sebuah angka. Penambahan ini memungkinkan agen AI Anda untuk menangani pertanyaan matematika yang lebih kompleks, seperti "Berapa akar kuadrat dari 16?" atau "Hitung √49," menggunakan perintah dalam bahasa alami.

## 🛠️ Mengimplementasikan Alat Akar Kuadrat
Untuk menambahkan fungsi ini, Anda mendefinisikan sebuah fungsi alat baru di file server.py Anda. Berikut implementasinya:

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

## 🔍 Cara Kerjanya

- **Mengimpor modul `math`**: Untuk melakukan operasi matematika yang lebih dari sekadar aritmatika dasar, Python menyediakan modul bawaan `math`. Modul ini berisi berbagai fungsi dan konstanta matematika. Dengan mengimpornya menggunakan `import math`, Anda dapat menggunakan fungsi seperti `math.sqrt()`, yang menghitung akar kuadrat dari sebuah angka.
- **Definisi Fungsi**: Dekorator `@server.tool()` mendaftarkan fungsi `sqrt` sebagai alat yang dapat diakses oleh agen AI Anda.
- **Parameter Input**: Fungsi ini menerima satu argumen `a` bertipe `float`.
- **Penanganan Error**: Jika `a` bernilai negatif, fungsi akan memunculkan `ValueError` untuk mencegah perhitungan akar kuadrat dari angka negatif, yang tidak didukung oleh fungsi `math.sqrt()`.
- **Nilai Kembali**: Untuk input yang tidak negatif, fungsi mengembalikan akar kuadrat dari `a` menggunakan metode bawaan Python `math.sqrt()`.

## 🔄 Memulai Ulang Server
Setelah menambahkan alat `sqrt` baru, penting untuk memulai ulang server MCP Anda agar agen dapat mengenali dan menggunakan fungsi yang baru ditambahkan.

## 💬 Contoh Perintah untuk Menguji Alat Baru
Berikut beberapa perintah dalam bahasa alami yang bisa Anda gunakan untuk menguji fungsi akar kuadrat:

- "Berapa akar kuadrat dari 25?"
- "Hitung akar kuadrat dari 81."
- "Cari akar kuadrat dari 0."
- "Berapa akar kuadrat dari 2.25?"

Perintah-perintah ini akan memicu agen untuk memanggil alat `sqrt` dan mengembalikan hasil yang benar.

## ✅ Ringkasan
Dengan menyelesaikan tugas ini, Anda telah:

- Memperluas server MCP kalkulator Anda dengan alat `sqrt` baru.
- Memungkinkan agen AI Anda untuk melakukan perhitungan akar kuadrat melalui perintah bahasa alami.
- Berlatih menambahkan alat baru dan memulai ulang server untuk mengintegrasikan fungsi tambahan.

Jangan ragu untuk bereksperimen lebih jauh dengan menambahkan alat matematika lain, seperti perpangkatan atau fungsi logaritma, untuk terus meningkatkan kemampuan agen Anda!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.