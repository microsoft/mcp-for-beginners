# Menjalankan contoh ini

Anda disarankan untuk memasang `uv` tetapi ia bukan wajib, lihat [arahan](https://docs.astral.sh/uv/#highlights)

## -0- Cipta persekitaran maya

```bash
python -m venv venv
```

## -1- Aktifkan persekitaran maya

```bash
venv\Scrips\activate
```

## -2- Pasang kebergantungan

```bash
pip install "mcp[cli]"
```

## -3- Jalankan contoh


```bash
python client.py
```

Anda sepatutnya melihat output yang serupa dengan:

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
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.