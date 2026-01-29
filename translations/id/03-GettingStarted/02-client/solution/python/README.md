# Menjalankan contoh ini

Disarankan untuk menginstal `uv` tapi tidak wajib, lihat [instruksi](https://docs.astral.sh/uv/#highlights)

## -0- Buat lingkungan virtual

```bash
python -m venv venv
```

## -1- Aktifkan lingkungan virtual

```bash
venv\Scrips\activate
```

## -2- Instal dependensi

```bash
pip install "mcp[cli]"
```

## -3- Jalankan contoh


```bash
python client.py
```

Anda seharusnya melihat output yang mirip dengan:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
                    INFO     Processing request of type ReadResourceRequest                                                                            server.py:534
CALL TOOL
                    INFO     Processing request of type CallToolRequest                                                                                server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.