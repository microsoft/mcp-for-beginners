# Studi Kasus: Mengekspos REST API di API Management sebagai Server MCP

Azure API Management adalah layanan yang menyediakan Gateway di atas Endpoint API Anda. Cara kerjanya adalah Azure API Management bertindak seperti proxy di depan API Anda dan dapat memutuskan apa yang harus dilakukan dengan permintaan yang masuk.

Dengan menggunakannya, Anda dapat menambahkan berbagai fitur seperti:

- **Keamanan**, Anda dapat menggunakan segala sesuatu mulai dari kunci API, JWT hingga identitas terkelola.
- **Pembatasan tingkat**, fitur hebat yang memungkinkan Anda memutuskan berapa banyak panggilan yang dapat diterima dalam satuan waktu tertentu. Ini membantu memastikan semua pengguna mendapatkan pengalaman yang baik dan juga layanan Anda tidak kewalahan dengan permintaan.
- **Skalabilitas & Load balancing**. Anda dapat mengatur sejumlah endpoint untuk menyeimbangkan beban dan juga memutuskan bagaimana "load balancing" dilakukan.
- **Fitur AI seperti caching semantik**, batas token, pemantauan token, dan lainnya. Fitur-fitur ini sangat baik untuk meningkatkan responsivitas serta membantu Anda memantau penggunaan token. [Baca lebih lanjut di sini](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Mengapa MCP + Azure API Management?

Model Context Protocol (MCP) dengan cepat menjadi standar untuk aplikasi AI agentik dan cara mengekspos alat serta data secara konsisten. Azure API Management adalah pilihan alami ketika Anda perlu "mengelola" API. Server MCP sering kali terintegrasi dengan API lain untuk menyelesaikan permintaan ke alat tertentu. Oleh karena itu, menggabungkan Azure API Management dan MCP sangat masuk akal.

## Gambaran Umum

Dalam kasus penggunaan ini, kita akan belajar mengekspos endpoint API sebagai Server MCP. Dengan melakukan ini, kita dapat dengan mudah menjadikan endpoint ini bagian dari aplikasi agentik sambil memanfaatkan fitur-fitur dari Azure API Management.

## Fitur Utama

- Anda dapat memilih metode endpoint yang ingin diekspos sebagai alat.
- Fitur tambahan yang Anda dapatkan bergantung pada apa yang Anda konfigurasikan di bagian kebijakan untuk API Anda. Namun, di sini kami akan menunjukkan cara menambahkan pembatasan tingkat.

## Langkah Awal: Mengimpor API

Jika Anda sudah memiliki API di Azure API Management, Anda dapat melewati langkah ini. Jika belum, lihat tautan ini, [mengimpor API ke Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Mengekspos API sebagai Server MCP

Untuk mengekspos endpoint API, ikuti langkah-langkah berikut:

1. Buka Azure Portal di alamat berikut <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. 
   Arahkan ke instance API Management Anda.

1. Di menu sebelah kiri, pilih **APIs > MCP Servers > + Create new MCP Server**.

1. Pada API, pilih REST API yang akan diekspos sebagai server MCP.

1. Pilih satu atau lebih Operasi API untuk diekspos sebagai alat. Anda dapat memilih semua operasi atau hanya operasi tertentu.

    ![Pilih metode untuk diekspos](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Pilih **Create**.

1. Arahkan ke opsi menu **APIs** dan **MCP Servers**, Anda akan melihat tampilan berikut:

    ![Lihat Server MCP di panel utama](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Server MCP telah dibuat dan operasi API telah diekspos sebagai alat. Server MCP terdaftar di panel MCP Servers. Kolom URL menunjukkan endpoint server MCP yang dapat Anda panggil untuk pengujian atau dalam aplikasi klien.

## Opsional: Mengonfigurasi Kebijakan

Azure API Management memiliki konsep inti kebijakan di mana Anda dapat mengatur berbagai aturan untuk endpoint Anda, seperti pembatasan tingkat atau caching semantik. Kebijakan ini ditulis dalam format XML.

Berikut cara mengatur kebijakan untuk membatasi tingkat panggilan ke Server MCP Anda:

1. Di portal, di bawah **APIs**, pilih **MCP Servers**.

1. Pilih server MCP yang telah Anda buat.

1. Di menu sebelah kiri, di bawah MCP, pilih **Policies**.

1. Di editor kebijakan, tambahkan atau edit kebijakan yang ingin Anda terapkan pada alat server MCP. Kebijakan didefinisikan dalam format XML. Sebagai contoh, Anda dapat menambahkan kebijakan untuk membatasi panggilan ke alat server MCP (dalam contoh ini, 5 panggilan per 30 detik per alamat IP klien). Berikut XML yang akan menyebabkan pembatasan tingkat:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Berikut adalah gambar editor kebijakan:

    ![Editor kebijakan](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Mencoba Server MCP

Mari kita pastikan Server MCP kita berfungsi sebagaimana mestinya.

Untuk ini, kita akan menggunakan Visual Studio Code dan GitHub Copilot dalam mode Agen. Kita akan menambahkan server MCP ke file *mcp.json*. Dengan melakukan ini, Visual Studio Code akan bertindak sebagai klien dengan kemampuan agentik, dan pengguna akhir dapat mengetikkan prompt dan berinteraksi dengan server tersebut.

Berikut cara menambahkan server MCP di Visual Studio Code:

1. Gunakan perintah **MCP: Add Server** dari Command Palette.

1. Saat diminta, pilih jenis server: **HTTP (HTTP atau Server Sent Events)**.

1. Masukkan URL server MCP di API Management. Contoh: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (untuk endpoint SSE) atau **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (untuk endpoint MCP), perhatikan perbedaan transportasi adalah `/sse` atau `/mcp`.

1. Masukkan ID server pilihan Anda. Nilai ini tidak terlalu penting tetapi akan membantu Anda mengingat instance server ini.

1. Pilih apakah akan menyimpan konfigurasi ke pengaturan workspace atau pengaturan pengguna.

  - **Pengaturan workspace** - Konfigurasi server disimpan ke file .vscode/mcp.json yang hanya tersedia di workspace saat ini.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    atau jika Anda memilih HTTP streaming sebagai transportasi, akan sedikit berbeda:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Pengaturan pengguna** - Konfigurasi server ditambahkan ke file *settings.json* global Anda dan tersedia di semua workspace. Konfigurasinya terlihat seperti berikut:

    ![Pengaturan pengguna](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Anda juga perlu menambahkan konfigurasi header untuk memastikan autentikasi ke Azure API Management. Header ini disebut **Ocp-Apim-Subscription-Key**.

    - Berikut cara menambahkannya ke pengaturan:

    ![Menambahkan header untuk autentikasi](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ini akan memunculkan prompt untuk meminta nilai kunci API yang dapat Anda temukan di Azure Portal untuk instance Azure API Management Anda.

   - Untuk menambahkannya ke *mcp.json*, Anda dapat menambahkannya seperti ini:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Menggunakan Mode Agen

Sekarang kita sudah siap di pengaturan atau di *.vscode/mcp.json*. Mari kita coba.

Harus ada ikon Tools seperti ini, di mana alat yang diekspos dari server Anda terdaftar:

![Alat dari server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik ikon alat dan Anda akan melihat daftar alat seperti ini:

    ![Alat](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Masukkan prompt di chat untuk memanggil alat. Sebagai contoh, jika Anda memilih alat untuk mendapatkan informasi tentang pesanan, Anda dapat meminta agen tentang pesanan. Berikut contoh prompt:

    ```text
    get information from order 2
    ```

    Anda sekarang akan melihat ikon alat yang meminta Anda untuk melanjutkan memanggil alat. Pilih untuk melanjutkan menjalankan alat, Anda sekarang akan melihat output seperti ini:

    ![Hasil dari prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Apa yang Anda lihat di atas tergantung pada alat yang telah Anda atur, tetapi idenya adalah Anda mendapatkan respons tekstual seperti di atas.**

## Referensi

Berikut cara Anda dapat mempelajari lebih lanjut:

- [Tutorial tentang Azure API Management dan MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Contoh Python: Mengamankan server MCP jarak jauh menggunakan Azure API Management (eksperimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Lab otorisasi klien MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Menggunakan ekstensi Azure API Management untuk VS Code untuk mengimpor dan mengelola API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Mendaftarkan dan menemukan server MCP jarak jauh di Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Repositori hebat yang menunjukkan banyak kemampuan AI dengan Azure API Management
- [Workshop AI Gateway](https://azure-samples.github.io/AI-Gateway/) Berisi workshop menggunakan Azure Portal, yang merupakan cara hebat untuk mulai mengevaluasi kemampuan AI.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.