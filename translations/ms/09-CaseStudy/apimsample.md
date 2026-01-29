# Kajian Kes: Dedahkan REST API dalam API Management sebagai pelayan MCP

Azure API Management adalah perkhidmatan yang menyediakan Gateway di atas Endpoint API anda. Cara ia berfungsi adalah Azure API Management bertindak seperti proksi di hadapan API anda dan boleh menentukan apa yang perlu dilakukan dengan permintaan masuk.

Dengan menggunakannya, anda menambah pelbagai ciri seperti:

- **Keselamatan**, anda boleh menggunakan segala-galanya daripada kunci API, JWT hingga identiti terurus.
- **Had kadar**, ciri hebat ialah keupayaan untuk menentukan berapa banyak panggilan yang dibenarkan dalam tempoh masa tertentu. Ini membantu memastikan semua pengguna mendapat pengalaman yang baik dan juga perkhidmatan anda tidak dibebani dengan permintaan.
- **Penskalaan & Pengimbangan Beban**. Anda boleh menyediakan beberapa endpoint untuk mengimbangi beban dan juga menentukan cara untuk "mengimbangi beban".
- **Ciri AI seperti caching semantik**, had token, pemantauan token dan banyak lagi. Ini adalah ciri hebat yang meningkatkan responsif serta membantu anda memantau penggunaan token anda. [Baca lebih lanjut di sini](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Mengapa MCP + Azure API Management?

Model Context Protocol (MCP) dengan cepat menjadi standard untuk aplikasi AI agen dan cara untuk mendedahkan alat dan data secara konsisten. Azure API Management adalah pilihan semula jadi apabila anda perlu "menguruskan" API. Pelayan MCP sering berintegrasi dengan API lain untuk menyelesaikan permintaan kepada alat, sebagai contoh. Oleh itu, menggabungkan Azure API Management dan MCP sangat masuk akal.

## Gambaran Keseluruhan

Dalam kes penggunaan ini, kita akan belajar untuk mendedahkan endpoint API sebagai Pelayan MCP. Dengan melakukan ini, kita boleh dengan mudah menjadikan endpoint ini sebahagian daripada aplikasi agen sambil memanfaatkan ciri-ciri daripada Azure API Management.

## Ciri Utama

- Anda memilih kaedah endpoint yang ingin didedahkan sebagai alat.
- Ciri tambahan yang anda dapat bergantung pada apa yang anda konfigurasikan dalam bahagian polisi untuk API anda. Tetapi di sini kami akan menunjukkan cara anda boleh menambah had kadar.

## Langkah Awal: Import API

Jika anda sudah mempunyai API dalam Azure API Management, bagus, anda boleh melangkau langkah ini. Jika tidak, lihat pautan ini, [mengimport API ke Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Dedahkan API sebagai Pelayan MCP

Untuk mendedahkan endpoint API, ikuti langkah-langkah berikut:

1. Navigasi ke Azure Portal dan alamat berikut <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   Navigasi ke instans API Management anda.

1. Dalam menu kiri, pilih **APIs > MCP Servers > + Create new MCP Server**.

1. Dalam API, pilih REST API untuk didedahkan sebagai pelayan MCP.

1. Pilih satu atau lebih Operasi API untuk didedahkan sebagai alat. Anda boleh memilih semua operasi atau hanya operasi tertentu.

    ![Pilih kaedah untuk didedahkan](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Pilih **Create**.

1. Navigasi ke pilihan menu **APIs** dan **MCP Servers**, anda seharusnya melihat yang berikut:

    ![Lihat Pelayan MCP dalam panel utama](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Pelayan MCP telah dicipta dan operasi API didedahkan sebagai alat. Pelayan MCP disenaraikan dalam panel MCP Servers. Lajur URL menunjukkan endpoint pelayan MCP yang boleh anda panggil untuk ujian atau dalam aplikasi klien.

## Pilihan: Konfigurasikan Polisi

Azure API Management mempunyai konsep teras polisi di mana anda menetapkan peraturan yang berbeza untuk endpoint anda seperti had kadar atau caching semantik. Polisi ini ditulis dalam format XML.

Berikut adalah cara anda boleh menetapkan polisi untuk menghadkan kadar pelayan MCP anda:

1. Dalam portal, di bawah **APIs**, pilih **MCP Servers**.

1. Pilih pelayan MCP yang anda cipta.

1. Dalam menu kiri, di bawah MCP, pilih **Policies**.

1. Dalam editor polisi, tambah atau edit polisi yang anda ingin terapkan pada alat pelayan MCP. Polisi ditakrifkan dalam format XML. Sebagai contoh, anda boleh menambah polisi untuk menghadkan panggilan kepada alat pelayan MCP (contohnya, 5 panggilan setiap 30 saat bagi setiap alamat IP klien). Berikut adalah XML yang akan menyebabkan had kadar:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Berikut adalah imej editor polisi:

    ![Editor polisi](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Cuba Ia

Mari pastikan Pelayan MCP kita berfungsi seperti yang diinginkan.

Untuk ini, kita akan menggunakan Visual Studio Code dan GitHub Copilot dalam mod Agennya. Kita akan menambah pelayan MCP ke dalam fail *mcp.json*. Dengan cara ini, Visual Studio Code akan bertindak sebagai klien dengan keupayaan agen dan pengguna akhir boleh menaip arahan dan berinteraksi dengan pelayan tersebut.

Berikut adalah cara untuk menambah pelayan MCP dalam Visual Studio Code:

1. Gunakan arahan MCP: **Add Server dari Command Palette**.

1. Apabila diminta, pilih jenis pelayan: **HTTP (HTTP atau Server Sent Events)**.

1. Masukkan URL pelayan MCP dalam API Management. Contoh: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (untuk endpoint SSE) atau **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (untuk endpoint MCP), perhatikan perbezaan antara pengangkutan ialah `/sse` atau `/mcp`.

1. Masukkan ID pelayan pilihan anda. Ini bukan nilai penting tetapi ia akan membantu anda mengingati apa instans pelayan ini.

1. Pilih sama ada untuk menyimpan konfigurasi ke tetapan ruang kerja anda atau tetapan pengguna.

  - **Tetapan ruang kerja** - Konfigurasi pelayan disimpan ke fail .vscode/mcp.json yang hanya tersedia dalam ruang kerja semasa.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    atau jika anda memilih HTTP streaming sebagai pengangkutan, ia akan sedikit berbeza:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Tetapan pengguna** - Konfigurasi pelayan ditambah ke fail *settings.json* global anda dan tersedia dalam semua ruang kerja. Konfigurasi kelihatan seperti berikut:

    ![Tetapan pengguna](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Anda juga perlu menambah konfigurasi, iaitu header untuk memastikan ia mengesahkan dengan betul terhadap Azure API Management. Ia menggunakan header yang dipanggil **Ocp-Apim-Subscription-Key**.

    - Berikut adalah cara anda boleh menambahnya ke tetapan:

    ![Menambah header untuk pengesahan](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ini akan menyebabkan arahan dipaparkan untuk meminta nilai kunci API yang boleh anda temui di Azure Portal untuk instans Azure API Management anda.

   - Untuk menambahnya ke *mcp.json* sebaliknya, anda boleh menambahnya seperti berikut:

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

### Gunakan Mod Agen

Sekarang kita sudah bersedia sama ada dalam tetapan atau dalam *.vscode/mcp.json*. Mari cuba.

Seharusnya ada ikon Alat seperti berikut, di mana alat yang didedahkan dari pelayan anda disenaraikan:

![Alat dari pelayan](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik ikon alat dan anda seharusnya melihat senarai alat seperti berikut:

    ![Alat](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Masukkan arahan dalam chat untuk memanggil alat. Sebagai contoh, jika anda memilih alat untuk mendapatkan maklumat tentang pesanan, anda boleh bertanya kepada agen tentang pesanan. Berikut adalah contoh arahan:

    ```text
    get information from order 2
    ```

    Anda kini akan dipaparkan dengan ikon alat yang meminta anda untuk meneruskan memanggil alat. Pilih untuk terus menjalankan alat, anda seharusnya melihat output seperti berikut:

    ![Hasil dari arahan](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **apa yang anda lihat di atas bergantung pada alat yang anda tetapkan, tetapi idenya adalah anda mendapat respons teks seperti di atas**

## Rujukan

Berikut adalah cara anda boleh belajar lebih lanjut:

- [Tutorial tentang Azure API Management dan MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Contoh Python: Amankan pelayan MCP jauh menggunakan Azure API Management (eksperimen)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Makmal kebenaran klien MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Gunakan sambungan Azure API Management untuk VS Code untuk mengimport dan menguruskan API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Daftar dan temui pelayan MCP jauh dalam Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Repositori hebat yang menunjukkan banyak keupayaan AI dengan Azure API Management
- [Bengkel AI Gateway](https://azure-samples.github.io/AI-Gateway/) Mengandungi bengkel menggunakan Azure Portal, yang merupakan cara yang baik untuk mula menilai keupayaan AI.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.