# Menerapkan Server MCP

> [!NOTE]
> Contoh konfigurasi yang menggunakan endpoint `/sse` menargetkan transport HTTP+SSE warisan.
> Server jarak jauh MCP `2026-07-28` menggunakan HTTP Streamable, biasanya pada
> endpoint yang ditentukan server seperti `/mcp`.

Menerapkan server MCP Anda memungkinkan orang lain mengakses alat dan sumber dayanya di luar lingkungan lokal Anda. Ada beberapa strategi penerapan yang perlu dipertimbangkan, tergantung pada kebutuhan Anda untuk skalabilitas, keandalan, dan kemudahan pengelolaan. Di bawah ini Anda akan menemukan panduan untuk menerapkan server MCP secara lokal, dalam kontainer, dan ke cloud.

## Ikhtisar

Pelajaran ini membahas cara menerapkan aplikasi Server MCP Anda.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Mengevaluasi berbagai pendekatan penerapan.
- Menerapkan aplikasi Anda.

## Pengembangan dan penerapan lokal

Jika server Anda dimaksudkan untuk digunakan dengan menjalankannya di mesin pengguna, Anda dapat mengikuti langkah-langkah berikut:

1. **Unduh server**. Jika Anda tidak menulis server, maka unduh dulu ke mesin Anda.
1. **Mulai proses server**: Jalankan aplikasi server MCP Anda

Untuk SSE (tidak diperlukan untuk server tipe stdio)

1. **Konfigurasi jaringan**: Pastikan server dapat diakses pada port yang diharapkan
1. **Hubungkan klien**: Gunakan URL koneksi lokal seperti `http://localhost:3000`

## Penerapan Cloud

Server MCP dapat diterapkan ke berbagai platform cloud:

- **Fungsi Serverless**: Terapkan server MCP ringan sebagai fungsi serverless
- **Layanan Kontainer**: Gunakan layanan seperti Azure Container Apps, AWS ECS, atau Google Cloud Run
- **Kubernetes**: Terapkan dan kelola server MCP dalam klaster Kubernetes untuk ketersediaan tinggi

### Contoh: Azure Container Apps

Azure Container Apps mendukung penerapan Server MCP. Ini masih dalam pengerjaan dan saat ini mendukung server SSE.

Berikut cara Anda melakukannya:

1. Kloning repositori:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Jalankan secara lokal untuk menguji:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Untuk mencoba secara lokal, buat file *mcp.json* di direktori *.vscode* dan tambahkan konten berikut:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

Setelah server SSE dijalankan, Anda dapat mengklik ikon putar di file JSON, Anda sekarang harus melihat alat di server yang diambil oleh GitHub Copilot, lihat ikon Alat.

1. Untuk menerapkan, jalankan perintah berikut:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Begitulah, terapkan secara lokal, terapkan ke Azure melalui langkah-langkah ini.

## Sumber Daya Tambahan

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Artikel Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repositori Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Selanjutnya

- Selanjutnya: [Topik Server Lanjutan](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->