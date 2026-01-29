# Pelayan MCP Calculator (Python)

Pelaksanaan pelayan Model Context Protocol (MCP) yang ringkas dalam Python yang menyediakan fungsi kalkulator asas.

## Pemasangan

Pasang keperluan yang diperlukan:

```bash
pip install -r requirements.txt
```

Atau pasang MCP Python SDK secara langsung:

```bash
pip install mcp>=1.18.0
```

## Penggunaan

### Menjalankan Pelayan

Pelayan ini direka untuk digunakan oleh klien MCP (seperti Claude Desktop). Untuk memulakan pelayan:

```bash
python mcp_calculator_server.py
```

**Nota**: Apabila dijalankan terus di terminal, anda akan melihat ralat pengesahan JSON-RPC. Ini adalah tingkah laku biasa - pelayan sedang menunggu mesej klien MCP yang diformat dengan betul.

### Menguji Fungsi

Untuk menguji bahawa fungsi kalkulator berfungsi dengan betul:

```bash
python test_calculator.py
```

## Penyelesaian Masalah

### Ralat Import

Jika anda melihat `ModuleNotFoundError: No module named 'mcp'`, pasang MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### Ralat JSON-RPC Apabila Dijalankan Secara Langsung

Ralat seperti "Invalid JSON: EOF while parsing a value" apabila menjalankan pelayan secara langsung adalah dijangka. Pelayan memerlukan mesej klien MCP, bukan input terminal secara langsung.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.