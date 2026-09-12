# Kajian Kes: Dedahkan REST API dalam Pengurusan API sebagai pelayan MCP

Azure API Management, ialah perkhidmatan yang menyediakan Gateway di atas Titik Akhir API anda. Cara ia berfungsi ialah Azure API Management bertindak seperti proksi di hadapan API anda dan boleh memutuskan apa yang perlu dilakukan dengan permintaan yang masuk.

Dengan menggunakannya, anda menambah pelbagai ciri seperti:

- **Keselamatan**, anda boleh menggunakan segala-galanya dari kunci API, JWT kepada identiti terurus.
- **Had kadar**, ciri hebat ialah dapat memutuskan berapa banyak panggilan yang dibenarkan setiap unit masa tertentu. Ini membantu memastikan semua pengguna mendapat pengalaman yang hebat dan juga bahawa perkhidmatan anda tidak terbeban dengan permintaan.
- **Penskalalaan & Pengimbangan beban**. Anda boleh menetapkan sejumlah titik akhir untuk mengimbangkan beban dan anda juga boleh memutuskan bagaimana untuk "mengimbangkan beban".
- **Ciri AI seperti caching semantik**, had token dan pemantauan token dan banyak lagi. Ini adalah ciri hebat yang meningkatkan tindak balas serta membantu anda mengawasi perbelanjaan token anda. [Baca lebih lanjut di sini](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Kenapa MCP + Azure API Management?

Model Context Protocol dengan cepat menjadi standard untuk aplikasi AI agenik dan cara untuk mendedahkan alat dan data secara konsisten. Azure API Management adalah pilihan semula jadi apabila anda perlu "mengurus" API. Pelayan MCP sering mengintegrasi dengan API lain untuk menyelesaikan permintaan kepada alat misalnya. Oleh itu menggabungkan Azure API Management dan MCP adalah sangat masuk akal.

## Gambaran Keseluruhan

Dalam kes penggunaan khusus ini kita akan belajar untuk mendedahkan titik akhir API sebagai Pelayan MCP. Dengan berbuat demikian, kita boleh dengan mudah menjadikan titik akhir ini sebahagian daripada aplikasi agenik sambil memanfaatkan ciri dari Azure API Management.

## Ciri Utama

- Anda memilih kaedah titik akhir yang anda ingin dedahkan sebagai alat.
- Ciri tambahan yang anda dapat bergantung pada apa yang anda konfigurasi dalam bahagian polisi untuk API anda. Tetapi di sini kami akan tunjukkan cara untuk menambah had kadar.

## Langkah Pra: Import API

Jika anda sudah mempunyai API dalam Azure API Management itu bagus, maka anda boleh langkau langkah ini. Jika tidak, lihat pautan ini, [mengimport API ke Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Dedahkan API sebagai Pelayan MCP

Untuk mendedahkan titik akhir API, mari ikuti langkah berikut:

1. Navigasi ke Azure Portal dan alamat berikut <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Navigasi ke instance Pengurusan API anda.

1. Dalam menu kiri, pilih APIs > MCP Servers > + Buat Pelayan MCP baru.

1. Dalam API, pilih REST API untuk didedahkan sebagai pelayan MCP.

1. Pilih satu atau lebih Operasi API untuk didedahkan sebagai alat. Anda boleh memilih semua operasi atau hanya operasi tertentu.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Pilih **Create**.

1. Navigasi ke pilihan menu **APIs** dan **MCP Servers**, anda sepatutnya melihat seperti berikut:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Pelayan MCP telah dicipta dan operasi API didedahkan sebagai alat. Pelayan MCP disenaraikan dalam pane Pelayan MCP. Lajur URL menunjukkan titik akhir pelayan MCP yang boleh anda panggil untuk ujian atau dalam aplikasi klien.

## Pilihan: Konfigurasi polisi

Azure API Management mempunyai konsep teras polisi di mana anda menetapkan peraturan berbeza untuk titik akhir anda seperti contohnya had kadar atau caching semantik. Polisi ini ditulis dalam XML.

Ini cara untuk menetapkan polisi had kadar untuk Pelayan MCP anda:

1. Dalam portal, di bawah APIs, pilih **MCP Servers**.

1. Pilih pelayan MCP yang anda cipta.

1. Dalam menu kiri, di bawah MCP, pilih **Policies**.

1. Dalam editor polisi, tambah atau sunting polisi yang anda ingin gunakan pada alat pelayan MCP. Polisi ditakrifkan dalam format XML. Contohnya, anda boleh tambah polisi untuk mengehadkan panggilan kepada alat pelayan MCP (dalam contoh ini, 5 panggilan setiap 30 saat setiap alamat IP klien). Ini XML yang akan menyebabkan had kadar:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Ini gambar editor polisi:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Cuba ia

Mari pastikan Pelayan MCP kita berfungsi seperti yang dimaksudkan.

> [!NOTE]
> Azure API Management kini mendedahkan pelayan ini melalui Streamable
> HTTP `/mcp` endpoint. Pengangkutan HTTP+SSE `/sse` yang lama telah tidak disokong dan
> hanya harus digunakan dengan klien warisan.

Untuk ini, kita akan menggunakan Visual Studio Code dan GitHub Copilot serta mod Agennya. Kita akan menambah pelayan MCP ke *mcp.json*. Dengan berbuat demikian, Visual Studio Code akan bertindak sebagai klien dengan keupayaan agenik dan pengguna akhir akan dapat menaip arahan dan berinteraksi dengan pelayan tersebut.

Mari kita lihat bagaimana, untuk menambah pelayan MCP dalam Visual Studio Code:

1. Gunakan arahan MCP: **Add Server dari Command Palette**.

1. Apabila diminta, pilih jenis pelayan: **HTTP (HTTP atau Server Sent Events)**.

1. Masukkan URL HTTP Streamable yang ditunjukkan untuk pelayan MCP dalam Pengurusan API.
    Contohnya:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Masukkan ID pelayan pilihan anda. Ini bukan nilai penting tetapi ia akan membantu anda ingat apa contoh pelayan ini.

1. Pilih sama ada untuk menyimpan konfigurasi dalam tetapan ruang kerja atau tetapan pengguna.

  - **Tetapan ruang kerja** - Konfigurasi pelayan disimpan ke fail .vscode/mcp.json hanya tersedia dalam ruang kerja semasa.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Tetapan pengguna** - Konfigurasi pelayan ditambah ke fail global *settings.json* anda dan tersedia dalam semua ruang kerja. Konfigurasi kelihatan seperti berikut:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Anda juga perlu menambah konfigurasi, satu header untuk memastikan ia mengesahkan dengan betul ke Azure API Management. Ia menggunakan header yang dipanggil **Ocp-Apim-Subscription-Key*. 

    - Ini cara anda boleh menambahkannya ke tetapan:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ini akan menyebabkan satu arahan paparan yang meminta nilai kunci API yang boleh anda temui dalam Azure Portal untuk instance Azure API Management anda.

   - Untuk menambahkannya ke *mcp.json* sebaliknya, anda boleh menambahkannya seperti berikut:

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

### Gunakan mod Agen

Sekarang kita sudah bersedia sama ada dalam tetapan atau dalam *.vscode/mcp.json*. Mari cuba.

Sepatutnya ada ikon Alat seperti berikut, di mana alat yang didedahkan dari pelayan anda disenaraikan:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik ikon alat dan anda akan lihat senarai alat seperti berikut:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Masukkan arahan dalam chat untuk memanggil alat. Contohnya, jika anda memilih alat untuk mendapatkan maklumat mengenai pesanan, anda boleh bertanya agen tentang pesanan. Ini adalah contoh arahan:

    ```text
    get information from order 2
    ```

    Anda kini akan dipaparkan ikon alat yang meminta anda untuk terus memanggil alat. Pilih untuk meneruskan menjalankan alat, anda kini sepatutnya melihat output seperti berikut:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **apa yang anda lihat di atas bergantung pada alat yang anda telah tetapkan, tapi idenya adalah anda mendapat jawapan berbentuk teks seperti di atas**


## Rujukan

Ini cara anda boleh belajar lebih lanjut:

- [Tutorial mengenai Azure API Management dan MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Contoh Python: Lindungi pelayan MCP jauh menggunakan Azure API Management (eksperimen)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Makmal pengesahan klien MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Gunakan sambungan Azure API Management untuk VS Code untuk mengimport dan mengurus API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Daftar dan temui pelayan MCP jauh dalam Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [Pintu Gerbang AI](https://github.com/Azure-Samples/AI-Gateway) Repositori hebat yang menunjukkan banyak keupayaan AI dengan Azure API Management
- [Bengkel Pintu Gerbang AI](https://azure-samples.github.io/AI-Gateway/) Mengandungi bengkel menggunakan Azure Portal, yang merupakan cara terbaik untuk mula menilai keupayaan AI.

## Apa Seterusnya

- Kembali ke: [Gambaran Keseluruhan Kajian Kes](./README.md)
- Seterusnya: [Ejen Perjalanan Azure AI](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->