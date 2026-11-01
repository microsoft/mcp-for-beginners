# Kajian Kes: Dedahkan REST API dalam Pengurusan API sebagai pelayan MCP

Azure API Management, adalah perkhidmatan yang menyediakan Gateway di atas Titik Akhir API anda. Cara ia berfungsi ialah Azure API Management bertindak seperti proksi di hadapan API anda dan boleh memutuskan apa yang perlu dilakukan dengan permintaan masuk.

Dengan menggunakannya, anda menambah satu set ciri seperti:

- **Keselamatan**, anda boleh menggunakan segala-galanya dari kekunci API, JWT hingga identiti terurus.
- **Had kadar**, ciri hebat adalah dapat memutuskan berapa panggilan yang dibenarkan dalam setiap unit masa tertentu. Ini membantu memastikan semua pengguna mempunyai pengalaman yang baik dan juga agar perkhidmatan anda tidak dibanjiri dengan permintaan.
- **Penyesuaian & Pengimbangan beban**. Anda boleh menyediakan beberapa titik akhir untuk mengimbangi beban dan juga boleh memutuskan bagaimana untuk "mengimbangi beban".
- **Ciri AI seperti penjejakan semantik**, had token dan pemantauan token dan banyak lagi. Ini adalah ciri hebat yang meningkatkan daya tindakbalas serta membantu anda memantau perbelanjaan token anda. [Baca lebih lanjut di sini](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Kenapa MCP + Azure API Management?

Model Context Protocol dengan pantas menjadi piawai untuk aplikasi AI beragen dan cara untuk mendedahkan alat dan data secara konsisten. Azure API Management adalah pilihan semula jadi apabila anda perlu "mengurus" API. Pelayan MCP sering berintegrasi dengan API lain untuk menyelesaikan permintaan ke alat contohnya. Oleh itu, menggabungkan Azure API Management dan MCP sangat masuk akal.

## Gambaran Keseluruhan

Dalam kes penggunaan khusus ini kita akan belajar mendedahkan titik akhir API sebagai Pelayan MCP. Dengan cara ini, kita boleh dengan mudah menjadikan titik akhir ini sebahagian daripada aplikasi beragen sambil memanfaatkan ciri-ciri dari Azure API Management.

## Ciri-ciri Utama

- Anda memilih kaedah titik akhir yang anda mahu dedahkan sebagai alat.
- Ciri tambahan yang anda dapat bergantung pada apa yang anda konfigurasikan dalam bahagian polisi untuk API anda. Tetapi di sini kami akan tunjukkan bagaimana anda boleh menambah had kadar.

## Langkah Pra: import API

Jika anda sudah mempunyai API dalam Azure API Management, bagus, maka anda boleh langkau langkah ini. Jika tidak, lihat pautan ini, [mengimport API ke Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Dedahkan API sebagai Pelayan MCP

Untuk mendedahkan titik akhir API, ikut langkah-langkah berikut:

1. Navigasi ke Azure Portal dan alamat berikut <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Navigasi ke contoh Pengurusan API anda.

1. Dalam menu kiri, pilih APIs > MCP Servers > + Create new MCP Server.

1. Dalam API, pilih REST API yang hendak didedahkan sebagai pelayan MCP.

1. Pilih satu atau lebih Operasi API untuk didedahkan sebagai alat. Anda boleh pilih semua operasi atau hanya operasi tertentu.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Pilih **Create**.

1. Navigasi ke pilihan menu **APIs** dan **MCP Servers**, anda akan melihat berikut:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Pelayan MCP telah dibuat dan operasi API didedahkan sebagai alat. Pelayan MCP disenaraikan dalam panel MCP Servers. Lajur URL menunjukkan titik akhir pelayan MCP yang boleh anda panggil untuk ujian atau dalam aplikasi klien.

## Pilihan: Konfigurasikan polisi

Azure API Management mempunyai konsep teras polisi di mana anda menetapkan peraturan berbeza untuk titik akhir anda seperti contohnya had kadar atau penjejakan semantik. Polisi-polisi ini disusun dalam XML.

Berikut adalah cara anda boleh tetapkan polisi untuk had kadar pelayan MCP anda:

1. Dalam portal, di bawah APIs, pilih **MCP Servers**.

1. Pilih pelayan MCP yang anda buat.

1. Dalam menu kiri, di bawah MCP, pilih **Policies**.

1. Dalam editor polisi, tambahkan atau edit polisi yang ingin anda pakai pada alat pelayan MCP tersebut. Polisi ditentukan dalam format XML. Contohnya, anda boleh tambah polisi untuk hadkan panggilan ke alat pelayan MCP (dalam contoh ini, 5 panggilan per 30 saat per alamat IP klien). Berikut XML yang akan menyebabkan had kadar:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Berikut gambar editor polisi:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Cuba ia

Mari pastikan Pelayan MCP kita berfungsi seperti yang dimaksudkan.

> [!NOTE]
> Azure API Management kini mendedahkan pelayan ini melalui Streamable
> HTTP `/mcp` endpoint. Pengangkutan HTTP+SSE lama `/sse` sudah tidak digalakkan dan
> hanya perlu digunakan dengan klien warisan.

Untuk ini, kami akan menggunakan Visual Studio Code dan GitHub Copilot serta mod Ejen-nya. Kami akan menambah pelayan MCP ke fail *mcp.json*. Dengan ini, Visual Studio Code akan bertindak sebagai klien dengan keupayaan beragen dan pengguna akhirnya dapat menaip arahan dan berinteraksi dengan pelayan tersebut.

Mari lihat bagaimana, untuk tambah pelayan MCP dalam Visual Studio Code:

1. Gunakan arahan MCP: **Add Server dari Command Palette**.

1. Apabila diminta, pilih jenis pelayan: **HTTP (HTTP atau Server Sent Events)**.

1. Masukkan URL HTTP Streamable yang dipaparkan untuk pelayan MCP dalam Pengurusan API.
    Contohnya:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Masukkan ID pelayan pilihan anda. Ini bukan nilai penting tetapi ia membantu anda ingat apa contoh pelayan ini.

1. Pilih sama ada untuk simpan konfigurasi ke tetapan ruang kerja atau tetapan pengguna.

    - **Tetapan ruang kerja** - Konfigurasi pelayan disimpan ke fail `.vscode/mcp.json`, yang hanya tersedia dalam ruang kerja semasa.

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - **Tetapan pengguna** - Konfigurasi pelayan ditambah ke fail *settings.json* global dan boleh digunakan di semua ruang kerja. Konfigurasinya kelihatan seperti berikut:

      ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Anda juga perlu menambah pengepala konfigurasi untuk memastikan ia mengesahkan dengan betul ke arah Azure API Management. Ia menggunakan pengepala yang dipanggil **Ocp-Apim-Subscription-Key**.

    - Berikut cara anda boleh tambahkannya ke tetapan:


    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ini akan menyebabkan satu arahan dipaparkan untuk meminta nilai kekunci API yang boleh anda temui dalam Azure Portal untuk contoh Azure API Management anda.

   - Untuk menambahkannya ke *mcp.json* sebaliknya, anda boleh tambah seperti berikut:

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

### Gunakan mod Ejen

Sekarang kita sudah sedia sama ada dalam tetapan atau dalam *.vscode/mcp.json*. Mari cuba.

Harus ada ikon Alat seperti ini, di mana alat yang didedahkan dari pelayan anda disenaraikan:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik ikon alat dan anda akan melihat senarai alat seperti ini:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Taip arahan dalam sembang untuk memanggil alat tersebut. Contohnya, jika anda memilih alat untuk mendapatkan maklumat mengenai pesanan, anda boleh tanya ejen tentang pesanan. Berikut contoh arahan:

    ```text
    get information from order 2
    ```

    Kini anda akan dipaparkan ikon alat yang meminta anda untuk teruskan memanggil alat. Pilih untuk teruskan menjalankan alat, anda akan lihat output seperti ini:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **apa yang anda lihat di atas bergantung pada alat yang anda sediakan, tetapi idenya ialah anda mendapat respons teks seperti di atas**


## Rujukan

Berikut cara anda boleh belajar lebih lanjut:

- [Tutorial mengenai Azure API Management dan MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Contoh Python: Amankan pelayan MCP jauh menggunakan Azure API Management (eksperimen)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Makmal kebenaran klien MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Gunakan pelanjutan Azure API Management untuk VS Code untuk import dan urus API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Daftar dan temui pelayan MCP jauh dalam Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Repo hebat yang menunjukkan banyak keupayaan AI dengan Azure API Management
- [Bengkel AI Gateway](https://azure-samples.github.io/AI-Gateway/) Mengandungi bengkel menggunakan Azure Portal, yang merupakan cara terbaik untuk mula menilai keupayaan AI.

## Apa Seterusnya

- Kembali ke: [Gambaran Keseluruhan Kajian Kes](./README.md)
- Seterusnya: [Ejen Perjalanan Azure AI](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->