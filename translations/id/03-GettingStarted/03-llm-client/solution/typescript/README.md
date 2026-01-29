# Menjalankan contoh ini

Contoh ini melibatkan penggunaan LLM di sisi klien. LLM membutuhkan Anda untuk menjalankan ini di Codespaces atau mengatur personal access token di GitHub agar dapat bekerja.

## -1- Instal dependensi

```bash
npm install
```

## -3- Jalankan server

```bash
npm run build
```

## -4- Jalankan klien

```sh
npm run client
```

Anda akan melihat hasil yang mirip dengan:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.