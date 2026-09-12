# Studi Kasus: Mengekspos REST API di Manajemen API sebagai server MCP

Azure API Management, adalah layanan yang menyediakan Gateway di atas Endpoint API Anda. Cara kerjanya adalah Azure API Management bertindak seperti proxy di depan API Anda dan dapat memutuskan apa yang harus dilakukan dengan permintaan yang masuk.

Dengan menggunakannya, Anda menambahkan serangkaian fitur seperti:

- **Keamanan**, Anda dapat menggunakan segala sesuatu mulai dari kunci API, JWT hingga managed identity.
- **Pembatasan laju (Rate limiting)**, fitur hebat adalah kemampuan untuk memutuskan berapa banyak panggilan yang diterima per satuan waktu tertentu. Ini membantu memastikan semua pengguna memiliki pengalaman yang baik dan juga bahwa layanan Anda tidak kewalahan dengan permintaan.
- **Skalabilitas & Penyeimbangan beban (Load balancing)**. Anda dapat mengatur beberapa endpoint untuk menyeimbangkan beban dan juga dapat memutuskan bagaimana cara "load balance".
- **Fitur AI seperti caching semantik**, batas token dan pemantauan token, dan lainnya. Ini adalah fitur hebat yang meningkatkan responsivitas serta membantu Anda mengendalikan pengeluaran token. [Baca lebih lanjut di sini](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Mengapa MCP + Azure API Management?

Model Context Protocol dengan cepat menjadi standar untuk aplikasi AI agentik dan cara mengekspos alat serta data secara konsisten. Azure API Management adalah pilihan alami ketika Anda perlu "mengelola" API. Server MCP sering terintegrasi dengan API lain untuk menyelesaikan permintaan ke alat misalnya. Oleh karena itu, menggabungkan Azure API Management dengan MCP sangat masuk akal.

## Ikhtisar

Dalam kasus penggunaan ini, kita akan belajar cara mengekspos endpoint API sebagai Server MCP. Dengan melakukan ini, kita bisa dengan mudah membuat endpoint ini bagian dari aplikasi agentik sambil juga memanfaatkan fitur dari Azure API Management.

## Fitur Kunci

- Anda memilih metode endpoint yang ingin diekspos sebagai alat.
- Fitur tambahan yang Anda dapatkan tergantung pada apa yang Anda konfigurasikan di bagian kebijakan untuk API Anda. Namun di sini kami akan menunjukkan cara menambahkan pembatasan laju.

## Langkah Awal: impor sebuah API

Jika Anda sudah memiliki API di Azure API Management, bagus, maka Anda bisa melewati langkah ini. Jika belum, lihat tautan ini, [mengimpor API ke Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Mengekspos API sebagai Server MCP

Untuk mengekspos endpoint API, mari ikuti langkah-langkah ini:

1. Navigasi ke Azure Portal dan alamat berikut <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Navigasi ke instance API Management Anda.

1. Di menu sebelah kiri, pilih APIs > MCP Servers > + Buat server MCP baru.

1. Pada API, pilih REST API yang ingin diekspos sebagai server MCP.

1. Pilih satu atau lebih Operasi API untuk diekspos sebagai alat. Anda bisa memilih semua operasi atau hanya operasi tertentu.

    ![Pilih metode yang akan diekspos](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Pilih **Buat**.

1. Navigasi ke opsi menu **APIs** dan **MCP Servers**, Anda akan melihat hal berikut:

    ![Lihat server MCP di panel utama](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Server MCP telah dibuat dan operasi API diekspos sebagai alat. Server MCP terdaftar di panel MCP Servers. Kolom URL menunjukkan endpoint server MCP yang bisa Anda panggil untuk pengujian atau di dalam aplikasi klien.

## Opsional: Konfigurasi kebijakan

Azure API Management memiliki konsep inti kebijakan di mana Anda menetapkan aturan berbeda untuk endpoint Anda seperti misalnya pembatasan laju atau caching semantik. Kebijakan ini dibuat dalam format XML.

Berikut cara Anda dapat mengatur kebijakan untuk membatasi laju server MCP Anda:

1. Di portal, di bawah APIs, pilih **MCP Servers**.

1. Pilih server MCP yang Anda buat.

1. Di menu sebelah kiri, di bawah MCP, pilih **Policies**.

1. Di editor kebijakan, tambahkan atau edit kebijakan yang ingin Anda terapkan ke alat server MCP. Kebijakan didefinisikan dalam format XML. Misalnya, Anda bisa menambahkan kebijakan untuk membatasi panggilan ke alat server MCP (dalam contoh ini, 5 panggilan per 30 detik per alamat IP klien). Berikut XML yang akan menyebabkan pembatasan laju:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Berikut adalah gambar editor kebijakan:

    ![Editor kebijakan](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Coba

Mari kita pastikan Server MCP kita berfungsi sebagaimana mestinya.

> [!NOTE]
> Azure API Management saat ini mengekspos server ini melalui Streamable
> HTTP endpoint `/mcp`. Transport HTTP+SSE `/sse` yang lama sudah usang dan
> sebaiknya hanya digunakan untuk klien lawas.

Untuk ini, kita akan menggunakan Visual Studio Code dan GitHub Copilot serta mode Agentnya. Kita akan menambahkan server MCP ke *mcp.json* sambil. Dengan melakukan itu, Visual Studio Code akan bertindak sebagai klien dengan kemampuan agentik dan pengguna akhir bisa mengetik permintaan dan berinteraksi dengan server tersebut.

Mari kita lihat bagaimana caranya, menambahkan server MCP di Visual Studio Code:

1. Gunakan perintah MCP: **Add Server dari Command Palette**.

1. Saat diminta, pilih tipe server: **HTTP (HTTP atau Server Sent Events)**.

1. Masukkan URL Streamable HTTP yang ditampilkan untuk server MCP di API Management.
    Misalnya:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Masukkan ID server sesuai pilihan Anda. Ini bukan nilai penting tapi ini membantu Anda mengingat instance server ini.

1. Pilih apakah akan menyimpan konfigurasi ke pengaturan workspace atau pengaturan pengguna.

  - **Pengaturan workspace** - Konfigurasi server disimpan ke file .vscode/mcp.json yang hanya tersedia di workspace saat ini.

    *mcp.json*

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

1. Anda juga perlu menambahkan konfigurasi, sebuah header untuk memastikan autentikasi yang benar ke Azure API Management. Ini menggunakan header bernama **Ocp-Apim-Subscription-Key*.

    - Berikut cara menambahkannya ke pengaturan:

    ![Menambahkan header untuk autentikasi](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ini akan menampilkan prompt untuk meminta nilai kunci API yang bisa Anda temukan di Azure Portal untuk instance Azure API Management Anda.

   - Untuk menambahkannya ke *mcp.json*, Anda bisa menambahkannya seperti ini:

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

### Gunakan mode Agent

Sekarang semua sudah siap di pengaturan atau di *.vscode/mcp.json*. Mari kita coba.

Akan ada ikon Tools seperti ini, di mana alat yang diekspos dari server Anda terdaftar:

![Alat dari server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik ikon alat dan Anda akan melihat daftar alat seperti ini:

    ![Alat](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Masukkan prompt di chat untuk memanggil alat tersebut. Misalnya, jika Anda memilih alat untuk mendapatkan informasi tentang pesanan, Anda bisa menanyakan agen tentang pesanan. Berikut contoh prompt:

    ```text
    get information from order 2
    ```

    Anda sekarang akan melihat ikon alat yang meminta Anda untuk melanjutkan memanggil alat. Pilih untuk melanjutkan menjalankan alat, Anda sekarang harus melihat output seperti ini:

    ![Hasil dari prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **apa yang Anda lihat di atas tergantung pada alat yang telah Anda siapkan, tetapi idenya adalah Anda mendapatkan respons tekstual seperti di atas**


## Referensi

Berikut cara Anda bisa belajar lebih banyak:

- [Tutorial tentang Azure API Management dan MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Contoh Python: Amankan server MCP jarak jauh menggunakan Azure API Management (eksperimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Lab otorisasi klien MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Gunakan ekstensi Azure API Management untuk VS Code untuk mengimpor dan mengelola API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Daftar dan temukan server MCP jarak jauh di Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Repositori hebat yang menunjukkan banyak kemampuan AI dengan Azure API Management
- [Workshop AI Gateway](https://azure-samples.github.io/AI-Gateway/) Berisi workshop menggunakan Azure Portal, ini adalah cara yang bagus untuk mulai mengevaluasi kemampuan AI.

## Selanjutnya

- Kembali ke: [Ikhtisar Studi Kasus](./README.md)
- Berikutnya: [Agen Perjalanan Azure AI](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->