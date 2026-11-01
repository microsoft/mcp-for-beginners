# Menyebarkan Pelayan MCP

> [!NOTE]
> Contoh konfigurasi yang menggunakan `/sse` titik akhir mensasarkan pengangkutan HTTP+SSE warisan.
> Pelayan jauh MCP `2026-07-28` menggunakan HTTP Boleh-Alir, biasanya pada
> titik akhir yang ditetapkan oleh pelayan seperti `/mcp`.

Menyebarkan pelayan MCP anda membolehkan orang lain mengakses alat dan sumbernya di luar persekitaran tempatan anda. Terdapat beberapa strategi penyebaran yang boleh dipertimbangkan, bergantung pada keperluan anda untuk skalabiliti, kebolehpercayaan, dan kemudahan pengurusan. Di bawah, anda akan menemui panduan untuk menyebarkan pelayan MCP secara tempatan, dalam bekas, dan ke awan.

## Gambaran Keseluruhan

Pelajaran ini merangkumi cara untuk menyebarkan aplikasi Pelayan MCP anda.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Menilai pendekatan penyebaran yang berbeza.
- Menyebarkan aplikasi anda.

## Pembangunan dan Penyebaran Tempatan

Jika pelayan anda direka untuk digunakan dengan menjalankannya pada mesin pengguna, anda boleh mengikuti langkah-langkah berikut:

1. **Muat turun pelayan**. Jika anda tidak menulis pelayan itu, muat turun dahulu ke mesin anda.
1. **Mulakan proses pelayan**: Jalankan aplikasi pelayan MCP anda

Untuk SSE (tidak diperlukan untuk pelayan jenis stdio)

1. **Konfigurasikan rangkaian**: Pastikan pelayan boleh diakses pada port yang dijangkakan
1. **Sambungkan klien**: Gunakan URL sambungan tempatan seperti `http://localhost:3000`

## Penyebaran Awan

Pelayan MCP boleh disebarkan ke pelbagai platform awan:

- **Fungsi Tanpa Pelayan**: Sebarkan pelayan MCP ringan sebagai fungsi tanpa pelayan
- **Perkhidmatan Bekas**: Gunakan perkhidmatan seperti Azure Container Apps, AWS ECS, atau Google Cloud Run
- **Kubernetes**: Sebarkan dan urus pelayan MCP dalam kelompok Kubernetes untuk ketersediaan tinggi

### Contoh: Azure Container Apps

Azure Container Apps menyokong penyebaran Pelayan MCP. Ia masih dalam proses pembangunan dan kini menyokong pelayan SSE.

Berikut cara anda boleh melakukannya:

1. Klon repositori:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Jalankan secara tempatan untuk menguji:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Untuk mencubanya secara tempatan, buatkan fail *mcp.json* dalam direktori *.vscode* dan tambah kandungan berikut:

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

  Setelah pelayan SSE dimulakan, anda boleh klik ikon main dalam fail JSON itu, anda kini sepatutnya melihat alat pada pelayan yang diambil oleh GitHub Copilot, lihat ikon Alat.

1. Untuk menyebarkan, jalankan arahan berikut:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Itu dia, sebarkan secara tempatan, sebarkan ke Azure melalui langkah-langkah ini.

## Sumber Tambahan

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Artikel Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repositori MCP Azure Container Apps](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Apa Seterusnya

- Seterusnya: [Topik Pelayan Lanjutan](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->