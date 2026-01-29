# Jalankan sampel

Sampel ini memulakan MCP Server dengan middleware yang memeriksa header Authorization yang sah.

## Pasang kebergantungan

```bash
pip install "mcp[cli]" 
```

## Mulakan pelayan

```bash
python server.py
```

mulakan klien di terminal lain

```bash
python client.py
```

Anda sepatutnya melihat hasil yang serupa dengan:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

ini bermaksud kelayakan yang dihantar telah dibenarkan.

Cuba ubah kelayakan dalam `client.py` kepada "secret-token2", kemudian anda sepatutnya melihat teks ini sebagai sebahagian daripada respons:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

ini bermaksud anda telah diautentikasi (anda mempunyai kelayakan), tetapi ia tidak sah.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.