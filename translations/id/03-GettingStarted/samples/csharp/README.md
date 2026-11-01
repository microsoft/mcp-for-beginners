# Layanan Kalkulator Dasar MCP

Layanan ini menyediakan operasi kalkulator dasar melalui Model Context Protocol (MCP). Dirancang sebagai contoh sederhana bagi pemula yang mempelajari implementasi MCP.

Untuk informasi lebih lanjut, lihat [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Fitur

Layanan kalkulator ini menawarkan kemampuan berikut:

1. **Operasi Aritmatika Dasar**:
   - Penjumlahan dua angka
   - Pengurangan satu angka dari angka lain
   - Perkalian dua angka
   - Pembagian satu angka dengan angka lain (dengan pemeriksaan pembagian nol)

## Menggunakan Tipe `stdio`
  
## Konfigurasi

1. **Konfigurasikan Server MCP**:
   - Buka ruang kerja Anda di VS Code.
   - Buat file `.vscode/mcp.json` di folder ruang kerja Anda untuk mengkonfigurasi server MCP. Contoh konfigurasi:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - Anda akan diminta memasukkan root repositori GitHub, yang bisa diperoleh dari perintah, `git rev-parse --show-toplevel`.

## Menggunakan Layanan

Layanan menyediakan endpoint API berikut melalui protokol MCP:

- `add(a, b)`: Menambahkan dua angka
- `subtract(a, b)`: Mengurangi angka kedua dari angka pertama
- `multiply(a, b)`: Mengalikan dua angka
- `divide(a, b)`: Membagi angka pertama dengan angka kedua (dengan pemeriksaan nol)
- isPrime(n): Mengecek apakah sebuah angka adalah prima

## Uji dengan Github Copilot Chat di VS Code

1. Cobalah membuat permintaan ke layanan menggunakan protokol MCP. Misalnya, Anda bisa bertanya:
   - "Tambahkan 5 dan 3"
   - "Kurangi 10 dari 4"
   - "Kalikan 6 dan 7"
   - "Bagikan 8 dengan 2"
   - "Apakah 37854 prima?"
   - "Apa 3 angka prima sebelum dan sesudah 4242?"
2. Untuk memastikan sedang menggunakan alat, tambahkan #MyCalculator pada prompt. Contohnya:
   - "Tambahkan 5 dan 3 #MyCalculator"
   - "Kurangi 10 dari 4 #MyCalculator


## Versi dalam Kontainer

Solusi sebelumnya sangat bagus ketika Anda sudah menginstal .NET SDK dan semua dependensi sudah tersedia. Namun, jika Anda ingin membagikan solusi atau menjalankannya di lingkungan berbeda, Anda dapat menggunakan versi dalam kontainer.

1. Mulai Docker dan pastikan berjalan.
1. Dari terminal, navigasikan ke folder `03-GettingStarted\samples\csharp\src` 
1. Untuk membangun image Docker untuk layanan kalkulator, jalankan perintah berikut (ganti `<YOUR-DOCKER-USERNAME>` dengan username Docker Hub Anda):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Setelah image dibangun, mari unggah ke Docker Hub. Jalankan perintah berikut:
   ```bash
   docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
   ```

## Gunakan Versi Dockerized

1. Di file `.vscode/mcp.json`, ganti konfigurasi server dengan berikut:
   ```json
    "mcp-calculator": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calculator"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Melihat konfigurasi, Anda dapat melihat bahwa perintah adalah `docker` dan argumennya adalah `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calculator`. Flag `--rm` memastikan kontainer dihapus setelah berhenti, dan flag `-i` memungkinkan Anda berinteraksi dengan input standar kontainer. Argumen terakhir adalah nama image yang baru saja kita bangun dan dorong ke Docker Hub.

## Uji Versi Dockerized

Mulai Server MCP dengan mengklik tombol Start kecil di atas `"mcp-calculator": {`, dan seperti sebelumnya Anda dapat meminta layanan kalkulator melakukan perhitungan untuk Anda.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->