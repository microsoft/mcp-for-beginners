# Menjalankan contoh ini

Contoh ini melibatkan penggunaan LLM pada klien. LLM memerlukan anda sama ada menjalankan ini dalam Codespaces atau menyediakan token akses peribadi di GitHub untuk berfungsi.

## -1- Pasang kebergantungan

```bash
npm install
```

## -3- Jalankan pelayan

```bash
npm run build
```

## -4- Jalankan klien

```sh
npm run client
```

Anda sepatutnya melihat keputusan yang serupa dengan:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.