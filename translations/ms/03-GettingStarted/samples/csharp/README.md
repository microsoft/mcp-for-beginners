# Perkhidmatan Pengira Asas MCP  

Perkhidmatan ini menyediakan operasi pengiraan asas melalui Model Context Protocol (MCP). Ia direka sebagai contoh mudah untuk pemula yang belajar tentang pelaksanaan MCP.  

Untuk maklumat lanjut, lihat [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)  

## Ciri-ciri  

Perkhidmatan kalkulator ini menawarkan kemampuan berikut:  

1. **Operasi Aritmetik Asas**:  
   - Penambahan dua nombor  
   - Penolakan satu nombor daripada nombor lain  
   - Perkalian dua nombor  
   - Pembahagian satu nombor dengan nombor lain (dengan pemeriksaan pembahagian dengan sifar)  

## Menggunakan Jenis `stdio`  
  
## Konfigurasi  

1. **Konfigurasikan Pelayan MCP**:  
   - Buka ruang kerja anda dalam VS Code.  
   - Cipta fail `.vscode/mcp.json` dalam folder ruang kerja anda untuk mengkonfigurasi pelayan MCP. Contoh konfigurasi:  

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
  
   - Anda akan diminta untuk memasukkan repositori GitHub root, yang boleh diperoleh daripada arahan, `git rev-parse --show-toplevel`.  

## Menggunakan Perkhidmatan  

Perkhidmatan ini mendedahkan API endpoints berikut melalui protokol MCP:  

- `add(a, b)`: Tambah dua nombor bersama  
- `subtract(a, b)`: Tolak nombor kedua daripada yang pertama  
- `multiply(a, b)`: Darab dua nombor  
- `divide(a, b)`: Bahagikan nombor pertama dengan yang kedua (dengan pemeriksaan sifar)  
- isPrime(n): Periksa jika nombor adalah nombor perdana  

## Uji dengan Github Copilot Chat dalam VS Code  

1. Cuba buat permintaan kepada perkhidmatan menggunakan protokol MCP. Contohnya, anda boleh bertanya:  
   - "Tambahkan 5 dan 3"  
   - "Tolak 10 daripada 4"  
   - "Darab 6 dan 7"  
   - "Bahagikan 8 dengan 2"  
   - "Adakah 37854 nombor perdana?"  
   - "Apakah 3 nombor perdana sebelum selepas 4242?"  
2. Untuk memastikan ia menggunakan alat, tambah #MyCalculator ke prompt. Contohnya:  
   - "Tambahkan 5 dan 3 #MyCalculator"  
   - "Tolak 10 daripada 4 #MyCalculator  


## Versi Berkontena  

Penyelesaian sebelumnya sesuai apabila anda telah memasang .NET SDK, dan semua kebergantungan tersedia. Namun, jika anda ingin berkongsi penyelesaian atau menjalankannya dalam persekitaran berbeza, anda boleh menggunakan versi berkontena ini.  

1. Mulakan Docker dan pastikan ia berjalan.  
1. Dari terminal, navigasi ke dalam folder `03-GettingStarted\samples\csharp\src`   
1. Untuk membina imej Docker untuk perkhidmatan kalkulator, jalankan arahan berikut (ganti `<YOUR-DOCKER-USERNAME>` dengan nama pengguna Docker Hub anda):  
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Selepas imej dibina, mari muat naik ke Docker Hub. Jalankan arahan berikut:  
   ```bash
   docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
   ```
  
## Gunakan Versi Dockerized  

1. Dalam fail `.vscode/mcp.json`, gantikan konfigurasi pelayan dengan yang berikut:  
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
   Melihat konfigurasi, anda dapat lihat bahawa arahan adalah `docker` dan argumen adalah `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calculator`. Flag `--rm` memastikan kontena dihapus selepas ia berhenti, dan flag `-i` membolehkan anda berinteraksi dengan input standard kontena. Argumen terakhir ialah nama imej yang baru kita bina dan muat naik ke Docker Hub.  

## Uji Versi Dockerized  

Mulakan Server MCP dengan mengklik butang Mula kecil di atas `"mcp-calculator": {`, dan seperti sebelumnya anda boleh meminta perkhidmatan kalkulator melakukan beberapa pengiraan untuk anda.  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->