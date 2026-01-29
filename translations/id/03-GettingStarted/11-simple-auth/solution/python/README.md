# Jalankan Contoh

## Buat lingkungan

```sh
python -m venv venv
source ./venv/bin/activate
```

## Instal dependensi

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Buat token

Anda perlu membuat token yang akan digunakan oleh klien untuk berkomunikasi dengan server.

Panggil:

```sh
python util.py
```

## Jalankan kode

Jalankan kode dengan:

```sh
python server.py
```

Di terminal terpisah, ketik:

```sh
python client.py
```

Di terminal server, Anda seharusnya melihat sesuatu seperti:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Di jendela klien, Anda seharusnya melihat teks serupa dengan:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Ini berarti semuanya berfungsi.

### Ubah informasi untuk melihat kegagalan

Temukan kode ini di *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Ubah sehingga tertulis "User.Write". Token Anda saat ini tidak memiliki tingkat izin tersebut, jadi jika Anda memulai ulang server dan mencoba menjalankan klien sekali lagi, Anda seharusnya melihat kesalahan serupa dengan berikut ini di terminal server:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Anda dapat mengembalikan kode server Anda ke semula atau membuat token baru yang memiliki cakupan tambahan ini, terserah Anda.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.