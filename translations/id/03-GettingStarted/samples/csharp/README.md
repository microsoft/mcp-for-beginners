# Basic Calculator MCP Service

Layanan ini menyediakan operasi kalkulator dasar melalui Model Context Protocol (MCP). Dirancang sebagai contoh sederhana untuk pemula yang belajar tentang implementasi MCP.

Untuk informasi lebih lanjut, lihat [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Fitur

Layanan kalkulator ini menawarkan kemampuan berikut:

1. **Operasi Aritmatika Dasar**:
   - Penjumlahan dua angka
   - Pengurangan satu angka dari angka lain
   - Perkalian dua angka
   - Pembagian satu angka dengan angka lain (dengan pengecekan pembagian nol)

## Menggunakan Tipe `stdio`
  
## Konfigurasi

1. **Konfigurasikan MCP Servers**:
   - Buka workspace Anda di VS Code.
   - Buat file `.vscode/mcp.json` di folder workspace Anda untuk mengonfigurasi MCP servers. Contoh konfigurasi:

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

   - Anda akan diminta memasukkan root repository GitHub, yang bisa didapatkan dari perintah `git rev-parse --show-toplevel`.

## Menggunakan Layanan

Layanan ini menyediakan endpoint API berikut melalui protokol MCP:

- `add(a, b)`: Menjumlahkan dua angka
- `subtract(a, b)`: Mengurangkan angka kedua dari angka pertama
- `multiply(a, b)`: Mengalikan dua angka
- `divide(a, b)`: Membagi angka pertama dengan angka kedua (dengan pengecekan nol)
- isPrime(n): Memeriksa apakah sebuah angka adalah bilangan prima

## Uji dengan Github Copilot Chat di VS Code

1. Coba buat permintaan ke layanan menggunakan protokol MCP. Misalnya, Anda bisa bertanya:
   - "Add 5 and 3"
   - "Subtract 10 from 4"
   - "Multiply 6 and 7"
   - "Divide 8 by 2"
   - "Does 37854 prime?"
   - "What are the 3 prime numbers before after 4242?"
2. Untuk memastikan menggunakan tools, tambahkan #MyCalculator pada prompt. Contohnya:
   - "Add 5 and 3 #MyCalculator"
   - "Subtract 10 from 4 #MyCalculator"

## Versi Containerized

Solusi sebelumnya sangat baik jika Anda sudah menginstal .NET SDK dan semua dependensi sudah tersedia. Namun, jika Anda ingin membagikan solusi ini atau menjalankannya di lingkungan berbeda, Anda bisa menggunakan versi containerized.

1. Jalankan Docker dan pastikan sudah aktif.
1. Dari terminal, masuk ke folder `03-GettingStarted\samples\csharp\src`
1. Untuk membangun image Docker untuk layanan kalkulator, jalankan perintah berikut (ganti `<YOUR-DOCKER-USERNAME>` dengan username Docker Hub Anda):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Setelah image selesai dibuat, mari unggah ke Docker Hub. Jalankan perintah berikut:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Menggunakan Versi Dockerized

1. Di file `.vscode/mcp.json`, ganti konfigurasi server dengan yang berikut:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Melihat konfigurasi tersebut, Anda bisa lihat bahwa perintahnya adalah `docker` dan argumennya `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Flag `--rm` memastikan container dihapus setelah berhenti, dan flag `-i` memungkinkan Anda berinteraksi dengan input standar container. Argumen terakhir adalah nama image yang baru saja kita buat dan unggah ke Docker Hub.

## Uji Versi Dockerized

Mulai MCP Server dengan mengklik tombol Start kecil di atas `"mcp-calc": {`, dan seperti sebelumnya Anda bisa meminta layanan kalkulator untuk melakukan perhitungan.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.