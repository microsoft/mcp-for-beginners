# Menjalankan contoh ini

Disarankan untuk menginstal `uv` tetapi tidak wajib, lihat [instruksi](https://docs.astral.sh/uv/#highlights)

## -0- Buat lingkungan virtual

```bash
python -m venv venv
```

## -1- Aktifkan lingkungan virtual

```bash
venv\Scripts\activate
```

## -2- Instal dependensi

```bash
pip install "mcp[cli]"
```

## -3- Jalankan contoh

```bash
mcp run server.py
```

## -4- Uji contoh

Dengan server berjalan di satu terminal, buka terminal lain dan jalankan perintah berikut:

```bash
mcp dev server.py
```

Ini akan memulai server web dengan antarmuka visual yang memungkinkan Anda untuk menguji contoh.

Setelah server terhubung:

- coba daftar alat dan jalankan `add`, dengan argumen 2 dan 4, Anda akan melihat hasilnya adalah 6.

- pergi ke sumber daya dan template sumber daya lalu panggil get_greeting, masukkan nama, dan Anda akan melihat salam dengan nama yang Anda berikan.

### Pengujian dalam mode CLI

Inspector yang Anda jalankan sebenarnya adalah aplikasi Node.js dan `mcp dev` adalah pembungkus di sekitarnya.

Anda dapat meluncurkannya langsung dalam mode CLI dengan menjalankan perintah berikut:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

Ini akan menampilkan semua alat yang tersedia di server. Anda akan melihat output berikut:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

Untuk memanggil alat, ketik:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Anda akan melihat output berikut:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Biasanya jauh lebih cepat menjalankan inspector dalam mode CLI daripada di browser.
> Baca lebih lanjut tentang inspector [di sini](https://github.com/modelcontextprotocol/inspector).

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.