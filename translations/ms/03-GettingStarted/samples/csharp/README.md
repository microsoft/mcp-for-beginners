# Perkhidmatan Kalkulator Asas MCP

Perkhidmatan ini menyediakan operasi kalkulator asas melalui Model Context Protocol (MCP). Ia direka sebagai contoh mudah untuk pemula yang ingin mempelajari tentang pelaksanaan MCP.

Untuk maklumat lanjut, lihat [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Ciri-ciri

Perkhidmatan kalkulator ini menawarkan keupayaan berikut:

1. **Operasi Aritmetik Asas**:
   - Penambahan dua nombor
   - Penolakan satu nombor daripada nombor lain
   - Pendaraban dua nombor
   - Pembahagian satu nombor dengan nombor lain (dengan pemeriksaan pembahagian dengan sifar)

## Menggunakan Jenis `stdio`
  
## Konfigurasi

1. **Konfigurasikan Pelayan MCP**:
   - Buka ruang kerja anda di VS Code.
   - Buat fail `.vscode/mcp.json` dalam folder ruang kerja anda untuk mengkonfigurasi pelayan MCP. Contoh konfigurasi:

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

   - Anda akan diminta untuk memasukkan akar repositori GitHub, yang boleh diperoleh dari arahan `git rev-parse --show-toplevel`.

## Menggunakan Perkhidmatan

Perkhidmatan ini mendedahkan API berikut melalui protokol MCP:

- `add(a, b)`: Menambah dua nombor bersama
- `subtract(a, b)`: Menolak nombor kedua daripada nombor pertama
- `multiply(a, b)`: Mendarab dua nombor
- `divide(a, b)`: Membahagikan nombor pertama dengan nombor kedua (dengan pemeriksaan sifar)
- isPrime(n): Semak sama ada nombor itu nombor perdana

## Uji dengan Github Copilot Chat di VS Code

1. Cuba buat permintaan kepada perkhidmatan menggunakan protokol MCP. Contohnya, anda boleh bertanya:
   - "Tambah 5 dan 3"
   - "Tolak 10 daripada 4"
   - "Darab 6 dan 7"
   - "Bahagi 8 dengan 2"
   - "Adakah 37854 nombor perdana?"
   - "Apakah 3 nombor perdana sebelum dan selepas 4242?"
2. Untuk memastikan ia menggunakan alat tersebut, tambah #MyCalculator pada arahan. Contohnya:
   - "Tambah 5 dan 3 #MyCalculator"
   - "Tolak 10 daripada 4 #MyCalculator"

## Versi Berkontena

Penyelesaian sebelum ini sangat sesuai apabila anda telah memasang .NET SDK dan semua kebergantungan telah tersedia. Namun, jika anda ingin berkongsi penyelesaian atau menjalankannya dalam persekitaran berbeza, anda boleh menggunakan versi berkontena.

1. Mulakan Docker dan pastikan ia berjalan.
1. Dari terminal, navigasi ke folder `03-GettingStarted\samples\csharp\src`
1. Untuk membina imej Docker bagi perkhidmatan kalkulator, jalankan arahan berikut (gantikan `<YOUR-DOCKER-USERNAME>` dengan nama pengguna Docker Hub anda):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. Setelah imej dibina, mari muat naik ke Docker Hub. Jalankan arahan berikut:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Gunakan Versi Dockerized

1. Dalam fail `.vscode/mcp.json`, gantikan konfigurasi pelayan dengan yang berikut:
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
   Melihat konfigurasi tersebut, anda boleh lihat arahan adalah `docker` dan argumennya adalah `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Flag `--rm` memastikan kontena dipadam selepas ia berhenti, dan flag `-i` membolehkan anda berinteraksi dengan input standard kontena. Argumen terakhir adalah nama imej yang baru sahaja kita bina dan muat naik ke Docker Hub.

## Uji Versi Dockerized

Mulakan Pelayan MCP dengan mengklik butang Mula kecil di atas `"mcp-calc": {`, dan seperti sebelum ini anda boleh meminta perkhidmatan kalkulator melakukan pengiraan untuk anda.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.