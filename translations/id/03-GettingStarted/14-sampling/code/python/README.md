# Jalankan contoh

> [!WARNING]
> Contoh ini menggunakan Sampling yang sudah usang dan endpoint HTTP+SSE warisan. Ini
> dipertahankan untuk kompatibilitas MCP `2025-11-25`. Implementasi baru sebaiknya langsung memanggil
> penyedia LLM dan menggunakan HTTP Streamable untuk lalu lintas MCP jarak jauh.

## Buat lingkungan virtual

```sh
python -m venv venv
source ./venv/bin/activate
```

## Pasang ketergantungan

```sh
pip install "mcp[cli]"
```

## Jalankan server

```sh
uvicorn server:app --port 8000
```

## Uji server dengan GitHub Copilot dan VS Code

Tambahkan entri ke mcp.json seperti ini:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Pastikan Anda mengklik "start" pada server.

Di GitHub Copilot, tempelkan prompt berikut:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Kali pertama Anda akan diminta untuk menerima tindakan Sampling, kemudian Anda akan diminta menerima alat untuk menjalankan "create_blog". Anda harus melihat respons yang mirip dengan:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->