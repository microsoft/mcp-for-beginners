# Studi Kasus: Mengekspos REST API di Manajemen API sebagai server MCP

Azure API Management, adalah layanan yang menyediakan Gateway di atas API Endpoints Anda. Cara kerjanya adalah Azure API Management bertindak seperti proxy di depan API Anda dan dapat memutuskan apa yang harus dilakukan dengan permintaan yang masuk.

Dengan menggunakannya, Anda menambahkan serangkaian fitur seperti:

- **Keamanan**, Anda dapat menggunakan segala sesuatu mulai dari kunci API, JWT hingga identitas terkelola.
- **Pembatasan laju**, fitur hebat adalah kemampuan untuk menentukan berapa banyak panggilan yang diperbolehkan per satuan waktu tertentu. Ini membantu memastikan semua pengguna memiliki pengalaman yang baik dan juga agar layanan Anda tidak kewalahan dengan permintaan.
- **Skalabilitas & Penyeimbangan beban**. Anda dapat mengatur sejumlah endpoint untuk menyeimbangkan beban dan Anda juga dapat memutuskan bagaimana cara "menyeimbangkan beban".
- **Fitur AI seperti caching semantik**, batas token dan pemantauan token dan lainnya. Ini adalah fitur hebat yang meningkatkan responsivitas serta membantu Anda mengendalikan pengeluaran token Anda. [Baca lebih lanjut di sini](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Mengapa MCP + Azure API Management?

Model Context Protocol dengan cepat menjadi standar untuk aplikasi AI agen dan cara mengekspos alat serta data secara konsisten. Azure API Management adalah pilihan alami ketika Anda perlu "mengelola" API. Server MCP sering kali terintegrasi dengan API lain untuk menyelesaikan permintaan ke alat misalnya. Oleh karena itu menggabungkan Azure API Management dan MCP sangat masuk akal.

## Ikhtisar

Dalam kasus penggunaan khusus ini kita akan belajar bagaimana mengekspos endpoint API sebagai Server MCP. Dengan melakukan ini, kita dapat dengan mudah membuat endpoint ini menjadi bagian dari aplikasi agen sambil memanfaatkan fitur dari Azure API Management.

## Fitur Utama

- Anda memilih metode endpoint yang ingin diekspos sebagai alat.
- Fitur tambahan yang Anda dapatkan tergantung pada apa yang Anda konfigurasikan di bagian kebijakan untuk API Anda. Namun di sini kami akan menunjukkan cara menambahkan pembatasan laju.

## Langkah awal: Impor API

Jika Anda sudah memiliki API di Azure API Management, bagus, maka Anda bisa melewati langkah ini. Jika tidak, lihat tautan ini, [mengimpor API ke Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Mengekspos API sebagai Server MCP

Untuk mengekspos endpoint API, ikuti langkah-langkah ini:

1. Akses Azure Portal dan alamat berikut <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Arahkan ke instance Manajemen API Anda.

1. Pada menu kiri, pilih APIs > MCP Servers > + Buat server MCP baru.

1. Pada API, pilih API REST yang akan diekspos sebagai server MCP.

1. Pilih satu atau beberapa Operasi API yang akan diekspos sebagai alat. Anda dapat memilih semua operasi atau operasi tertentu saja.

    ![Pilih metode untuk diekspos](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Pilih **Buat**.

1. Arahkan ke opsi menu **APIs** dan **MCP Servers**, Anda akan melihat seperti berikut:

    ![Lihat MCP Server di panel utama](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Server MCP telah dibuat dan operasi API diekspos sebagai alat. Server MCP tercantum di panel MCP Servers. Kolom URL menampilkan endpoint server MCP yang dapat Anda panggil untuk pengujian atau dalam aplikasi klien.

## Opsional: Konfigurasi kebijakan

Azure API Management memiliki konsep inti berupa kebijakan di mana Anda menetapkan aturan berbeda untuk endpoint Anda seperti contoh pembatasan laju atau caching semantik. Kebijakan ini ditulis dalam XML.

Berikut cara Anda dapat mengatur kebijakan untuk membatasi laju Server MCP Anda:

1. Di portal, di bawah APIs, pilih **MCP Servers**.

1. Pilih server MCP yang Anda buat.

1. Pada menu kiri, di bawah MCP, pilih **Policies**.

1. Di editor kebijakan, tambahkan atau edit kebijakan yang ingin Anda terapkan pada alat server MCP. Kebijakan didefinisikan dalam format XML. Misalnya, Anda bisa menambahkan kebijakan untuk membatasi panggilan ke alat server MCP (dalam contoh ini, 5 panggilan per 30 detik per alamat IP klien). Berikut XML yang menyebabkan pembatasan laju:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Berikut adalah gambar editor kebijakan:

    ![Editor kebijakan](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Coba langsung

Mari kita pastikan Server MCP kita bekerja sesuai harapan.

> [!NOTE]
> Azure API Management saat ini mengekspos server ini melalui endpoint Streamable
> HTTP `/mcp` . Transport HTTP+SSE `/sse` yang lama sudah tidak digunakan dan
> hanya boleh dipakai dengan klien warisan.

Untuk ini, kita akan menggunakan Visual Studio Code dan GitHub Copilot serta mode Agent-nya. Kita akan menambahkan server MCP ke sebuah berkas *mcp.json*. Dengan melakukan ini, Visual Studio Code akan bertindak sebagai klien dengan kemampuan agensik dan pengguna akhir dapat mengetik prompt serta berinteraksi dengan server tersebut.

Mari kita lihat cara menambahkan server MCP di Visual Studio Code:

1. Gunakan perintah MCP: **Add Server dari Command Palette**.

1. Ketika diminta, pilih tipe server: **HTTP (HTTP atau Server Sent Events)**.

1. Masukkan URL HTTP Streamable yang ditampilkan untuk server MCP di API Management.
    Misalnya:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Masukkan ID server sesuai pilihan Anda. Nilai ini tidak penting tapi akan membantu Anda mengingat instance server ini.

1. Pilih apakah konfigurasi disimpan ke pengaturan workspace atau pengaturan pengguna.

    - **Pengaturan workspace** - Konfigurasi server disimpan ke sebuah berkas `.vscode/mcp.json` yang hanya tersedia di workspace saat ini.

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - **Pengaturan pengguna** - Konfigurasi server ditambahkan ke berkas *settings.json* global Anda dan tersedia di semua workspace. Konfigurasi tampak seperti berikut:

      ![Pengaturan pengguna](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Anda juga perlu menambahkan header konfigurasi untuk memastikan autentikasi dengan benar ke Azure API Management. Ini menggunakan header bernama **Ocp-Apim-Subscription-Key**.

    - Berikut cara menambahkannya ke pengaturan:


    ![Menambahkan header untuk autentikasi](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ini akan memunculkan prompt untuk meminta nilai kunci API yang dapat Anda temukan di Azure Portal untuk instance Azure API Management Anda.

   - Untuk menambahkannya ke *mcp.json*, Anda bisa menambahkannya seperti berikut:

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

Harus ada ikon Tools seperti ini, di mana alat yang diekspos dari server Anda terdaftar:

![Alat dari server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik ikon tools dan Anda akan melihat daftar alat seperti ini:

    ![Alat](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Masukkan sebuah prompt di chat untuk memanggil alat tersebut. Misalnya, jika Anda memilih alat untuk mendapatkan informasi mengenai sebuah pesanan, Anda bisa menanyakan agen tentang pesanan itu. Berikut contoh prompt:

    ```text
    get information from order 2
    ```

    Anda akan melihat ikon tools yang meminta Anda untuk melanjutkan pemanggilan alat. Pilih untuk mulai menjalankan alat, Anda sekarang akan melihat output seperti ini:

    ![Hasil dari prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **apa yang Anda lihat di atas tergantung pada alat yang telah Anda atur, tapi idenya adalah Anda mendapatkan respons tekstual seperti di atas**


## Referensi

Berikut bagaimana Anda bisa belajar lebih lanjut:

- [Tutorial tentang Azure API Management dan MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Contoh Python: Amankan server MCP jarak jauh menggunakan Azure API Management (eksperimen)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Lab otorisasi klien MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Gunakan ekstensi Azure API Management untuk VS Code untuk mengimpor dan mengelola API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Daftar dan temukan server MCP jarak jauh di Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Repo hebat yang menunjukkan banyak kemampuan AI dengan Azure API Management
- [Workshop AI Gateway](https://azure-samples.github.io/AI-Gateway/) Berisi workshop menggunakan Azure Portal, yang merupakan cara yang bagus untuk mulai mengevaluasi kemampuan AI.

## Selanjutnya

- Kembali ke: [Ikhtisar Studi Kasus](./README.md)
- Selanjutnya: [Agen Perjalanan Azure AI](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->