# Jalankan Contoh

Contoh ini memulai MCP Server dengan middleware yang memeriksa header Authorization yang valid.

## Instalasi dependensi

```bash
pip install "mcp[cli]" 
```

## Mulai server

```bash
python server.py
```

jalankan klien di terminal lain

```bash
python client.py
```

Anda seharusnya melihat hasil yang mirip dengan:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

ini berarti kredensial yang dikirimkan telah diizinkan.

Coba ubah kredensial di `client.py` menjadi "secret-token2", lalu Anda seharusnya melihat teks ini sebagai bagian dari respons:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

ini berarti Anda telah diautentikasi (Anda memiliki kredensial), tetapi kredensial tersebut tidak valid.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.