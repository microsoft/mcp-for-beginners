# Jalankan contoh

## Siapkan lingkungan virtual

```sh
python -m venv venv
source ./venv/bin/activate
```

## Instal dependensi

```sh
pip install "mcp[cli]"
```

## Jalankan kode

```sh
python client.py
```

Anda seharusnya melihat teks:

```text
Available tools: ['add']
Result of add tool: meta=None content=[TextContent(type='text', text='8.0', annotations=None, meta=None)] structuredContent=None isError=False
```

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.