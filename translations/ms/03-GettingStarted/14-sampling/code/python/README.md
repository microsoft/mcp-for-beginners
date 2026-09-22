# Jalankan contoh

> [!WARNING]
> Contoh ini menggunakan Sampling yang sudah lapuk dan titik akhir HTTP+SSE lama. Ia
> dikekalkan untuk keserasian MCP `2025-11-25`. Pelaksanaan baru harus memanggil
> pembekal LLM secara langsung dan menggunakan Streamable HTTP untuk trafik MCP jauh.

## Buat persekitaran maya

```sh
python -m venv venv
source ./venv/bin/activate
```

## Pasang kebergantungan

```sh
pip install "mcp[cli]"
```

## Jalankan pelayan

```sh
uvicorn server:app --port 8000
```

## Uji pelayan menggunakan GitHub Copilot dan VS Code

Tambahkan entri ke dalam mcp.json seperti berikut:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Pastikan anda klik "start" pada pelayan.

Dalam GitHub Copilot tampal arahan berikut:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Kali pertama anda akan ditanya sama ada untuk menerima tindakan Sampling, kemudian anda akan diminta menerima alat untuk menjalankan "create_blog". Anda harus melihat respons yang serupa dengan:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->