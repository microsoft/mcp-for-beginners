# Menjalankan contoh ini

## -1- Instal dependensi

```bash
dotnet restore
```

## -3- Jalankan contoh

```bash
dotnet run
```

## -4- Uji contoh

Dengan server berjalan di satu terminal, buka terminal lain dan jalankan perintah berikut:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Ini akan memulai server web dengan antarmuka visual yang memungkinkan Anda untuk menguji contoh ini.

Setelah server terhubung:

- coba daftar alat dan jalankan `add`, dengan argumen 2 dan 4, Anda akan melihat hasilnya adalah 6.
- pergi ke sumber daya dan template sumber daya, lalu panggil "greeting", masukkan nama, dan Anda akan melihat sapaan dengan nama yang Anda berikan.

### Pengujian dalam mode CLI

Anda dapat meluncurkannya langsung dalam mode CLI dengan menjalankan perintah berikut:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Ini akan menampilkan semua alat yang tersedia di server. Anda akan melihat output berikut:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
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
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Anda akan melihat output berikut:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
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
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.