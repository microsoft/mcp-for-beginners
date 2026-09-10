# MCP Calculator Server (Python)



Pelaksanaan pelayan Model Context Protocol (MCP) mudah dalam Python yang menyediakan fungsi kalkulator asas.


## Pemasangan

Pasang kebergantungan yang diperlukan:

```bash
pip install -r requirements.txt
```

Atau pasang SDK Python MCP secara langsung:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Penggunaan

### Menjalankan Pelayan

Pelayan direka untuk digunakan oleh klien MCP (seperti Claude Desktop). Untuk memulakan pelayan:

```bash
python mcp_calculator_server.py
```

**Nota**: Apabila dijalankan secara langsung di terminal, anda akan melihat ralat pengesahan JSON-RPC. Ini adalah tingkah laku normal - pelayan menunggu mesej klien MCP yang diformatkan dengan betul.

### Menguji Fungsi

Untuk menguji bahawa fungsi kalkulator berfungsi dengan betul:

```bash
python test_calculator.py
```

## Menyelesaikan Masalah

### Ralat Import

Jika anda melihat `ModuleNotFoundError: Tiada modul bernama 'mcp'`, pasang SDK Python MCP:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Ralat JSON-RPC Apabila Menjalankan Secara Langsung

Ralat seperti "JSON Tidak Sah: EOF semasa mengurai nilai" apabila menjalankan pelayan secara langsung adalah dijangka. Pelayan memerlukan mesej klien MCP, bukan input terminal langsung.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->