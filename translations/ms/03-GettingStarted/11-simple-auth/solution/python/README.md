# Jalankan Sampel

## Cipta persekitaran

```sh
python -m venv venv
source ./venv/bin/activate
```

## Pasang kebergantungan

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Jana token

Anda perlu menjana token yang akan digunakan oleh klien untuk berkomunikasi dengan pelayan.

Panggil:

```sh
python util.py
```

## Jalankan kod

Jalankan kod dengan:

```sh
python server.py
```

Dalam terminal yang berasingan, taip:

```sh
python client.py
```

Dalam terminal pelayan, anda sepatutnya melihat sesuatu seperti:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Dalam tetingkap klien, anda sepatutnya melihat teks yang serupa dengan:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Ini bermakna semuanya berfungsi.

### Tukar maklumat untuk melihat ia gagal

Cari kod ini dalam *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Tukar supaya ia mengatakan "User.Write". Token semasa anda tidak mempunyai tahap kebenaran tersebut, jadi jika anda mulakan semula pelayan dan cuba jalankan klien sekali lagi, anda sepatutnya melihat ralat yang serupa dengan berikut dalam terminal pelayan:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Anda boleh sama ada menukar semula kod pelayan anda atau menjana token baharu yang mengandungi skop tambahan ini, terpulang kepada anda.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.