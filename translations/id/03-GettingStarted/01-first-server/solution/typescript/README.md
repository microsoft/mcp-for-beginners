# Menjalankan Contoh Ini

Disarankan untuk menginstal `uv`, meskipun tidak wajib, lihat [petunjuk](https://docs.astral.sh/uv/#highlights)

## -1- Instal dependensi

```bash
npm install
```

## -3- Jalankan contoh

```bash
npm run build
```

## -4- Uji contoh

Dengan server berjalan di satu terminal, buka terminal lain dan jalankan perintah berikut:

```bash
npm run inspector
```

Ini akan memulai server web dengan antarmuka visual yang memungkinkan Anda menguji contoh ini.

Setelah server terhubung:

- coba daftar alat dan jalankan `add`, dengan argumen 2 dan 4, Anda seharusnya melihat hasil 6.
- buka sumber daya dan template sumber daya lalu panggil "greeting", masukkan nama, dan Anda akan melihat sapaan dengan nama yang Anda masukkan.

### Pengujian dalam Mode CLI

Inspector yang Anda jalankan sebenarnya adalah aplikasi Node.js, dan `mcp dev` adalah pembungkus di sekitarnya.

Anda dapat meluncurkannya langsung dalam mode CLI dengan menjalankan perintah berikut:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Ini akan menampilkan daftar semua alat yang tersedia di server. Anda seharusnya melihat output berikut:

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
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Anda seharusnya melihat output berikut:

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
> Biasanya jauh lebih cepat menjalankan inspector dalam mode CLI dibandingkan di browser.
> Baca lebih lanjut tentang inspector [di sini](https://github.com/modelcontextprotocol/inspector).

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.