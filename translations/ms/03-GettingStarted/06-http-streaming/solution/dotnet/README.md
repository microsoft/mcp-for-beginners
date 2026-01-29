# Menjalankan sampel ini

## -1- Pasang kebergantungan

```bash
dotnet restore
```

## -2- Jalankan sampel

```bash
dotnet run
```

## -3- Uji sampel

Buka terminal berasingan sebelum menjalankan arahan di bawah (pastikan pelayan masih berjalan).

Dengan pelayan berjalan di satu terminal, buka terminal lain dan jalankan arahan berikut:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Ini akan memulakan pelayan web dengan antara muka visual yang membolehkan anda menguji sampel.

> Pastikan **Streamable HTTP** dipilih sebagai jenis pengangkutan, dan URL adalah `http://localhost:3001/mcp`.

Setelah pelayan disambungkan:

- cuba senaraikan alat dan jalankan `add`, dengan argumen 2 dan 4, anda sepatutnya melihat 6 dalam hasilnya.
- pergi ke sumber dan templat sumber dan panggil "greeting", taipkan nama dan anda sepatutnya melihat ucapan dengan nama yang anda berikan.

### Ujian dalam mod CLI

Anda boleh melancarkannya secara langsung dalam mod CLI dengan menjalankan arahan berikut:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Ini akan menyenaraikan semua alat yang tersedia di pelayan. Anda sepatutnya melihat output berikut:

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

Untuk memanggil alat, taipkan:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
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
> Biasanya lebih pantas menjalankan inspector dalam mod CLI berbanding di pelayar.
> Baca lebih lanjut tentang inspector [di sini](https://github.com/modelcontextprotocol/inspector).

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.