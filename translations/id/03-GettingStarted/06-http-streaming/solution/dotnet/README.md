# Menjalankan contoh ini

## -1- Instal dependensi

```bash
dotnet restore
```

## -2- Jalankan contoh

```bash
dotnet run
```

## -3- Uji contoh

Buka terminal terpisah sebelum menjalankan perintah di bawah ini (pastikan server masih berjalan).

Dengan server berjalan di satu terminal, buka terminal lain dan jalankan perintah berikut:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Ini akan memulai server web dengan antarmuka visual yang memungkinkan Anda menguji contoh ini.

> Pastikan bahwa **Streamable HTTP** dipilih sebagai jenis transportasi, dan URL adalah `http://localhost:3001/mcp`.

Setelah server terhubung:

- coba daftar alat dan jalankan `add`, dengan argumen 2 dan 4, Anda akan melihat hasilnya adalah 6.
- pergi ke sumber daya dan template sumber daya lalu panggil "greeting", masukkan nama, dan Anda akan melihat sapaan dengan nama yang Anda berikan.

### Pengujian dalam mode CLI

Anda dapat meluncurkannya langsung dalam mode CLI dengan menjalankan perintah berikut:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Ini akan menampilkan semua alat yang tersedia di server. Anda akan melihat output berikut:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

Untuk memanggil alat, ketik:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
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