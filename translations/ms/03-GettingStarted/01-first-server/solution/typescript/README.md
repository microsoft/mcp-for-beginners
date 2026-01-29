# Menjalankan sampel ini

Anda disarankan untuk memasang `uv` tetapi ia bukan keperluan, lihat [arahan](https://docs.astral.sh/uv/#highlights)

## -1- Pasang kebergantungan

```bash
npm install
```

## -3- Jalankan sampel

```bash
npm run build
```

## -4- Uji sampel

Dengan pelayan berjalan di satu terminal, buka terminal lain dan jalankan arahan berikut:

```bash
npm run inspector
```

Ini akan memulakan pelayan web dengan antara muka visual yang membolehkan anda menguji sampel.

Setelah pelayan disambungkan:

- cuba senaraikan alat dan jalankan `add`, dengan argumen 2 dan 4, anda sepatutnya melihat 6 dalam hasilnya.
- pergi ke sumber dan templat sumber dan panggil "greeting", taipkan nama dan anda sepatutnya melihat ucapan dengan nama yang anda berikan.

### Ujian dalam mod CLI

Pemeriksa yang anda jalankan sebenarnya adalah aplikasi Node.js dan `mcp dev` adalah pembungkus di sekelilingnya.

Anda boleh melancarkannya secara langsung dalam mod CLI dengan menjalankan arahan berikut:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Ini akan menyenaraikan semua alat yang tersedia dalam pelayan. Anda sepatutnya melihat output berikut:

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

Untuk memanggil alat, taipkan:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Anda sepatutnya melihat output berikut:

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
> Biasanya lebih pantas menjalankan pemeriksa dalam mod CLI berbanding dalam pelayar.
> Baca lebih lanjut tentang pemeriksa [di sini](https://github.com/modelcontextprotocol/inspector).

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.