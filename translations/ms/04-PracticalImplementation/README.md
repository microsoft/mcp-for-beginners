# Pelaksanaan Praktikal

[![Cara Membina, Menguji, dan Melancarkan Apl MCP dengan Alat dan Aliran Kerja Sebenar](../../../translated_images/ms/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Klik imej di atas untuk menonton video pelajaran ini)_

Pelaksanaan praktikal adalah di mana kuasa Model Context Protocol (MCP) menjadi nyata. Walaupun memahami teori dan seni bina di belakang MCP adalah penting, nilai sebenar muncul apabila anda menerapkan konsep-konsep ini untuk membina, menguji, dan melancarkan penyelesaian yang menyelesaikan masalah dunia sebenar. Bab ini menghubungkan jurang antara pengetahuan konsep dan pembangunan praktikal, membimbing anda melalui proses membawa aplikasi berasaskan MCP ke kehidupan.

Sama ada anda sedang membangunkan pembantu pintar, mengintegrasikan AI ke dalam aliran kerja perniagaan, atau membina alat khusus untuk pemprosesan data, MCP menyediakan asas yang fleksibel. Reka bentuk yang tidak bergantung bahasa dan SDK rasmi untuk bahasa pengaturcaraan popular menjadikannya boleh diakses oleh pelbagai pembangun. Dengan menggunakan SDK ini, anda boleh dengan cepat membuat prototaip, iterasi, dan skala penyelesaian anda merentas platform dan persekitaran yang berbeza.

Dalam bahagian berikut, anda akan menemui contoh praktikal, kod sampel, dan strategi pelancaran yang menunjukkan cara melaksanakan MCP dalam C#, Java dengan Spring, TypeScript, JavaScript, dan Python. Anda juga akan belajar cara untuk mengesan ralat dan menguji pelayan MCP anda, mengurus API, dan melancarkan penyelesaian ke awan menggunakan Azure. Sumber praktikal ini direka untuk mempercepatkan pembelajaran anda dan membantu anda membina aplikasi MCP yang kukuh dan sedia untuk pengeluaran dengan yakin.

## Gambaran Keseluruhan

Pelajaran ini menumpukan pada aspek praktikal pelaksanaan MCP merentas pelbagai bahasa pengaturcaraan. Kami akan meneroka cara menggunakan SDK MCP dalam C#, Java dengan Spring, TypeScript, JavaScript, dan Python untuk membina aplikasi kukuh, mengesan ralat dan menguji pelayan MCP, serta mencipta sumber, arahan, dan alat yang boleh digunakan semula.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Melaksanakan penyelesaian MCP menggunakan SDK rasmi dalam pelbagai bahasa pengaturcaraan
- Mengesan ralat dan menguji pelayan MCP secara sistematik
- Mencipta dan menggunakan ciri pelayan (Sumber, Arahan, dan Alat)
- Mereka bentuk aliran kerja MCP yang berkesan untuk tugasan kompleks
- Mengoptimumkan pelaksanaan MCP untuk prestasi dan kebolehpercayaan

## Sumber SDK Rasmi

Model Context Protocol menawarkan SDK rasmi untuk pelbagai bahasa (selaras dengan [Spesifikasi MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java dengan Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Nota:** memerlukan kebergantungan pada [Project Reactor](https://projectreactor.io). (Lihat [isu perbincangan 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Bekerja dengan SDK MCP

Bahagian ini menyediakan contoh praktikal pelaksanaan MCP merentas pelbagai bahasa pengaturcaraan. Anda boleh menemui kod sampel dalam direktori `samples` yang disusun mengikut bahasa.

### Sampel Tersedia

Repositori ini termasuk [pelaksanaan sampel](../../../04-PracticalImplementation/samples) dalam bahasa berikut:

- [C#](./samples/csharp/README.md)
- [Java dengan Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Setiap sampel menunjukkan konsep utama MCP dan corak pelaksanaan untuk bahasa dan ekosistem khusus tersebut.

### Panduan Praktikal

Panduan tambahan untuk pelaksanaan MCP praktikal:

- [Penomboran dan Set Keputusan Besar](./pagination/README.md) - Mengendalikan penomboran berasaskan penuding bagi alat, sumber, dan set data besar

## Ciri Teras Pelayan

Pelayan MCP boleh melaksanakan mana-mana gabungan ciri ini:

### Sumber

Sumber menyediakan konteks dan data untuk digunakan oleh pengguna atau model AI:

- Repositori dokumen
- Pangkalan pengetahuan
- Sumber data berstruktur
- Sistem fail

### Arahan

Arahan adalah mesej dan aliran kerja yang berasaskan templat untuk pengguna:

- Templat perbualan yang telah ditetapkan
- Corak interaksi berpandu
- Struktur dialog khusus

### Alat

Alat adalah fungsi untuk model AI laksanakan:

- Utiliti pemprosesan data
- Integrasi API luaran
- Keupayaan pengiraan
- Fungsi carian

## Pelaksanaan Sampel: Pelaksanaan C#

Repositori SDK C# rasmi mengandungi beberapa pelaksanaan sampel yang menunjukkan aspek berbeza MCP:

- **Klien MCP Asas**: Contoh mudah menunjukkan cara mencipta klien MCP dan memanggil alat
- **Pelayan MCP Asas**: Pelaksanaan pelayan minimum dengan pendaftaran alat asas
- **Pelayan MCP Lanjutan**: Pelayan penuh ciri dengan pendaftaran alat, pengesahan, dan pengendalian ralat
- **Integrasi ASP.NET**: Contoh menunjukkan integrasi dengan ASP.NET Core
- **Corak Pelaksanaan Alat**: Pelbagai corak untuk melaksanakan alat dengan pelbagai tahap kerumitan

SDK MCP C# masih dalam pratinjau dan API mungkin berubah. Kami akan terus mengemas kini blog ini seiring evolusi SDK.

### Ciri Utama

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Membina [Pelayan MCP pertama anda](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Untuk sampel pelaksanaan C# lengkap, lawati [repositori sampel SDK C# rasmi](https://github.com/modelcontextprotocol/csharp-sdk)

## Pelaksanaan sampel: Pelaksanaan Java dengan Spring

SDK Java dengan Spring menawarkan pilihan pelaksanaan MCP yang kukuh dengan ciri tahap perusahaan.

### Ciri Utama

- Integrasi Spring Framework
- Keselamatan jenis yang kukuh
- Sokongan pengaturcaraan reaktif
- Pengendalian ralat menyeluruh

Untuk sampel pelaksanaan Java dengan Spring lengkap, lihat [sampel Java dengan Spring](samples/java/containerapp/README.md) dalam direktori sampel.

## Pelaksanaan sampel: Pelaksanaan JavaScript

SDK JavaScript menyediakan pendekatan ringan dan fleksibel untuk pelaksanaan MCP.

### Ciri Utama

- Sokongan Node.js dan pelayar
- API berasaskan janji
- Integrasi mudah dengan Express dan rangka kerja lain
- Sokongan WebSocket untuk penstriman

Untuk sampel pelaksanaan JavaScript lengkap, lihat [sampel JavaScript](samples/javascript/README.md) dalam direktori sampel.

## Pelaksanaan sampel: Pelaksanaan Python

SDK Python menawarkan pendekatan Pythonik untuk pelaksanaan MCP dengan integrasi rangka kerja ML yang sangat baik.

### Ciri Utama

- Sokongan async/await dengan asyncio
- Integrasi FastAPI
- Pendaftaran alat mudah
- Integrasi asli dengan perpustakaan ML popular

Untuk sampel pelaksanaan Python lengkap, lihat [sampel Python](samples/python/README.md) dalam direktori sampel.

## Pengurusan API

Azure API Management adalah jawapan hebat bagi bagaimana kita dapat mengamankan Pelayan MCP. Idea adalah untuk meletakkan instans Azure API Management di hadapan Pelayan MCP anda dan membiarkannya mengendalikan ciri-ciri yang mungkin anda mahu seperti:

- had kadar
- pengurusan token
- pemantauan
- pengimbangan beban
- keselamatan

### Sampel Azure

Berikut adalah Sampel Azure yang melakukan perkara tersebut, iaitu [mencipta Pelayan MCP dan mengamankannya dengan Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Lihat bagaimana aliran kebenaran berlaku dalam imej di bawah:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Dalam imej sebelum ini, perkara berikut berlaku:

- Pengesahan/Kebenaran berlaku menggunakan Microsoft Entra.
- Azure API Management bertindak sebagai pintu masuk dan menggunakan dasar untuk mengarahkan dan mengurus trafik.
- Azure Monitor merekod semua permintaan untuk analisis lanjut.

#### Aliran kebenaran

Mari lihat aliran kebenaran dengan lebih terperinci:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Spesifikasi kebenaran MCP

Ketahui lebih lanjut tentang [Spesifikasi Kebenaran MCP](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Melancarkan Pelayan MCP Jauh ke Azure

Mari lihat jika kita boleh melancarkan sampel yang disebut sebelum ini:

1. Klon repositori

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Daftarkan penyedia sumber `Microsoft.App`.

   - Jika anda menggunakan Azure CLI, jalankan `az provider register --namespace Microsoft.App --wait`.
   - Jika anda menggunakan Azure PowerShell, jalankan `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Kemudian jalankan `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` selepas beberapa ketika untuk memeriksa jika pendaftaran selesai.

1. Jalankan perintah [azd](https://aka.ms/azd) ini untuk menyediakan perkhidmatan pengurusan api, aplikasi fungsi (dengan kod) dan semua sumber Azure lain yang diperlukan

    ```shell
    azd up
    ```

    Perintah ini harus melancarkan semua sumber awan di Azure

### Menguji pelayan anda dengan MCP Inspector

1. Dalam **tetingkap terminal baru**, pasang dan jalankan MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Anda sepatutnya melihat antara muka seperti:

    ![Connect to Node inspector](../../../translated_images/ms/connect.141db0b2bd05f096.webp)

1. CTRL klik untuk memuatkan aplikasi web MCP Inspector dari URL yang dipaparkan oleh aplikasi (contoh: [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Tetapkan jenis pengangkutan kepada `SSE`
1. Tetapkan URL ke titik akhir SSE Pengurusan API anda yang sedang berjalan yang dipaparkan selepas `azd up` dan **Sambungkan**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Senaraikan Alat**. Klik pada alat dan **Jalankan Alat**.

Jika semua langkah berjaya, anda kini berhubung dengan pelayan MCP dan anda telah dapat memanggil alat.

## Pelayan MCP untuk Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Set repositori ini adalah templat permulaan pantas untuk membina dan melancarkan pelayan MCP (Model Context Protocol) jauh tersuai menggunakan Azure Functions dengan Python, C# .NET atau Node/TypeScript.

Sampel ini menyediakan penyelesaian lengkap yang membolehkan pembangun untuk:

- Membina dan jalankan secara lokal: Membangun dan mengesan ralat pelayan MCP di mesin lokal
- Lancarkan ke Azure: Lancarkan ke awan dengan mudah menggunakan arahan azd up yang ringkas
- Sambungkan dari klien: Sambungkan ke pelayan MCP dari pelbagai klien termasuk mod agen Copilot VS Code dan alat MCP Inspector

### Ciri Utama

- Keselamatan secara reka bentuk: Pelayan MCP diamankan menggunakan kunci dan HTTPS
- Pilihan pengesahan: Menyokong OAuth menggunakan pengesahan terbina dalam dan/atau Pengurusan API
- Pengasingan rangkaian: Membenarkan pengasingan rangkaian menggunakan Rangkaian Maya Azure (VNET)
- Seni bina tanpa pelayan: Menggunakan Azure Functions untuk pelaksanaan berasaskan acara yang boleh diskalakan
- Pembangunan tempatan: Sokongan pembangunan dan pengesanan ralat tempatan yang menyeluruh
- Pelancaran mudah: Proses pelancaran yang dipermudahkan ke Azure

Repositori termasuk semua fail konfigurasi yang diperlukan, kod sumber, dan definisi infrastruktur untuk memulakan dengan cepat pelaksanaan pelayan MCP yang sedia untuk pengeluaran.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Pelaksanaan sampel MCP menggunakan Azure Functions dengan Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Pelaksanaan sampel MCP menggunakan Azure Functions dengan C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Pelaksanaan sampel MCP menggunakan Azure Functions dengan Node/TypeScript.

## Penemuan Utama

- SDK MCP menyediakan alat khusus bahasa untuk melaksanakan penyelesaian MCP yang kukuh
- Proses mengesan ralat dan menguji adalah penting untuk aplikasi MCP yang boleh dipercayai
- Templat arahan boleh digunakan semula membolehkan interaksi AI yang konsisten
- Aliran kerja yang direka dengan baik boleh mengatur tugasan kompleks menggunakan pelbagai alat
- Melaksanakan penyelesaian MCP memerlukan pertimbangan keselamatan, prestasi, dan pengendalian ralat

## Latihan

Reka aliran kerja MCP praktikal yang menangani masalah dunia sebenar dalam domain anda:

1. Kenal pasti 3-4 alat yang berguna untuk menyelesaikan masalah ini
2. Cipta diagram aliran kerja yang menunjukkan bagaimana alat-alat ini berinteraksi
3. Laksanakan versi asas salah satu alat menggunakan bahasa pilihan anda
4. Cipta templat arahan yang akan membantu model menggunakan alat anda dengan berkesan

## Sumber Tambahan

---

## Apakah Seterusnya

Seterusnya: [Topik Lanjutan](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sah dan utama. Untuk maklumat yang kritikal, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau tafsiran yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->