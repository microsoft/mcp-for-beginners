# Menggunakan Pelayan MCP

Menggunakan pelayan MCP anda membolehkan orang lain mengakses alat dan sumbernya di luar persekitaran tempatan anda. Terdapat beberapa strategi penggunaan yang boleh dipertimbangkan, bergantung pada keperluan anda untuk kebolehsuaian, kebolehpercayaan, dan kemudahan pengurusan. Di bawah ini anda akan menemui panduan untuk menggunakan pelayan MCP secara tempatan, dalam kontena, dan ke awan.

## Gambaran Keseluruhan

Pelajaran ini menerangkan cara menggunakan aplikasi Pelayan MCP anda.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Menilai pelbagai pendekatan penggunaan.
- Menggunakan aplikasi anda.

## Pembangunan dan penggunaan tempatan

Jika pelayan anda bertujuan untuk digunakan dengan menjalankannya pada mesin pengguna, anda boleh mengikuti langkah-langkah berikut:

1. **Muat turun pelayan**. Jika anda tidak menulis pelayan tersebut, muat turun dahulu ke mesin anda.  
1. **Mulakan proses pelayan**: Jalankan aplikasi pelayan MCP anda

Untuk SSE (tidak diperlukan untuk pelayan jenis stdio)

1. **Konfigurasikan rangkaian**: Pastikan pelayan boleh diakses pada port yang dijangka  
1. **Sambungkan klien**: Gunakan URL sambungan tempatan seperti `http://localhost:3000`

## Penggunaan Awan

Pelayan MCP boleh digunakan pada pelbagai platform awan:

- **Fungsi Tanpa Pelayan**: Gunakan pelayan MCP ringan sebagai fungsi tanpa pelayan  
- **Perkhidmatan Kontena**: Gunakan perkhidmatan seperti Azure Container Apps, AWS ECS, atau Google Cloud Run  
- **Kubernetes**: Gunakan dan urus pelayan MCP dalam kluster Kubernetes untuk ketersediaan tinggi

### Contoh: Azure Container Apps

Azure Container Apps menyokong penggunaan Pelayan MCP. Ia masih dalam pembangunan dan kini menyokong pelayan SSE.

Berikut adalah cara anda boleh melakukannya:

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

1. Untuk mencuba secara tempatan, buat fail *mcp.json* dalam direktori *.vscode* dan tambah kandungan berikut:

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

  Setelah pelayan SSE dimulakan, anda boleh klik ikon main dalam fail JSON, anda sepatutnya dapat melihat alat pada pelayan diambil oleh GitHub Copilot, lihat ikon Alat.

1. Untuk menggunakan, jalankan arahan berikut:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Itulah dia, gunakan secara tempatan, gunakan ke Azure melalui langkah-langkah ini.

## Sumber Tambahan

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Artikel Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repositori Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Apa Seterusnya

- Seterusnya: [Pelaksanaan Praktikal](../../04-PracticalImplementation/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.