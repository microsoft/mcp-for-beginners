# Implementasi Praktis

[![Cara Membangun, Menguji, dan Menerapkan Aplikasi MCP dengan Alat dan Alur Kerja Nyata](../../../translated_images/id/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Klik gambar di atas untuk menonton video pelajaran ini)_

Implementasi praktis adalah saat kekuatan Model Context Protocol (MCP) menjadi nyata. Meskipun memahami teori dan arsitektur di balik MCP itu penting, nilai sejati muncul ketika Anda menerapkan konsep-konsep ini untuk membangun, menguji, dan menerapkan solusi yang menyelesaikan masalah dunia nyata. Bab ini menjembatani kesenjangan antara pengetahuan konseptual dan pengembangan langsung, membimbing Anda melalui proses membawa aplikasi berbasis MCP menjadi nyata.

Apakah Anda sedang mengembangkan asisten cerdas, mengintegrasikan AI ke dalam alur kerja bisnis, atau membangun alat khusus untuk pemrosesan data, MCP menyediakan dasar yang fleksibel. Desainnya yang tidak tergantung bahasa dan SDK resmi untuk bahasa pemrograman populer membuatnya dapat diakses oleh beragam pengembang. Dengan memanfaatkan SDK ini, Anda dapat dengan cepat membuat prototipe, iterasi, dan memperluas solusi Anda di berbagai platform dan lingkungan.

Di bagian-bagian berikut, Anda akan menemukan contoh praktis, kode sampel, dan strategi penerapan yang menunjukkan cara mengimplementasikan MCP dalam C#, Java dengan Spring, TypeScript, JavaScript, dan Python. Anda juga akan mempelajari cara melakukan debug dan menguji server MCP Anda, mengelola API, dan menerapkan solusi ke cloud menggunakan Azure. Sumber daya langsung ini dirancang untuk mempercepat pembelajaran Anda dan membantu Anda dengan percaya diri membangun aplikasi MCP yang kuat dan siap produksi.

## Ikhtisar

Pelajaran ini berfokus pada aspek praktis dari implementasi MCP di berbagai bahasa pemrograman. Kita akan menjelajahi cara menggunakan SDK MCP di C#, Java dengan Spring, TypeScript, JavaScript, dan Python untuk membangun aplikasi tangguh, melakukan debug dan pengujian server MCP, serta membuat sumber daya, prompt, dan alat yang dapat digunakan kembali.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Mengimplementasikan solusi MCP menggunakan SDK resmi dalam berbagai bahasa pemrograman
- Melakukan debug dan pengujian server MCP secara sistematis
- Membuat dan menggunakan fitur server (Resources, Prompts, dan Tools)
- Merancang alur kerja MCP yang efektif untuk tugas kompleks
- Mengoptimalkan implementasi MCP untuk kinerja dan keandalan

## Sumber Daya SDK Resmi

Model Context Protocol menawarkan SDK resmi untuk berbagai bahasa (sesuai dengan [Spesifikasi MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [SDK C#](https://github.com/modelcontextprotocol/csharp-sdk)
- [SDK Java dengan Spring](https://github.com/modelcontextprotocol/java-sdk) **Catatan:** memerlukan dependensi pada [Project Reactor](https://projectreactor.io). (Lihat [diskusi issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [SDK TypeScript](https://github.com/modelcontextprotocol/typescript-sdk)
- [SDK Python](https://github.com/modelcontextprotocol/python-sdk)
- [SDK Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk)
- [SDK Go](https://github.com/modelcontextprotocol/go-sdk)

## Bekerja dengan SDK MCP

Bagian ini menyediakan contoh praktis mengimplementasikan MCP di berbagai bahasa pemrograman. Anda dapat menemukan kode sampel di direktori `samples` yang disusun menurut bahasa.

### Sampel yang Tersedia

Repositori berisi [implementasi sampel](../../../04-PracticalImplementation/samples) dalam bahasa berikut:

- [C#](./samples/csharp/README.md)
- [Java dengan Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Setiap sampel menunjukkan konsep dan pola implementasi MCP utama untuk bahasa dan ekosistem tersebut.

### Panduan Praktis

Panduan tambahan untuk implementasi MCP praktis:

- [Pagination dan Set Hasil Besar](./pagination/README.md) - Menangani pagination berbasis kursor untuk tools, resources, dan dataset besar

## Fitur Inti Server

Server MCP dapat mengimplementasikan kombinasi fitur ini:

### Resources

Resources menyediakan konteks dan data untuk digunakan pengguna atau model AI:

- Repositori dokumen
- Basis pengetahuan
- Sumber data terstruktur
- Sistem berkas

### Prompts

Prompts adalah pesan dan alur kerja bertemplate untuk pengguna:

- Template percakapan yang sudah ditentukan
- Pola interaksi terpandu
- Struktur dialog khusus

### Tools

Tools adalah fungsi yang dieksekusi oleh model AI:

- Utilitas pemrosesan data
- Integrasi API eksternal
- Kemampuan komputasi
- Fungsi pencarian

## Contoh Implementasi: Implementasi C#

Repositori resmi SDK C# berisi beberapa implementasi contoh yang menunjukkan berbagai aspek MCP:

- **Klien MCP Dasar**: Contoh sederhana yang menunjukkan cara membuat klien MCP dan memanggil tools
- **Server MCP Dasar**: Implementasi server minimal dengan pendaftaran tools dasar
- **Server MCP Lanjutan**: Server lengkap dengan pendaftaran tools, otentikasi, dan penanganan error
- **Integrasi ASP.NET**: Contoh yang menunjukkan integrasi dengan ASP.NET Core
- **Pola Implementasi Tools**: Berbagai pola untuk mengimplementasikan tools dengan tingkat kompleksitas berbeda

SDK MCP C# sedang dalam tahap pratinjau dan API mungkin berubah. Kami akan terus memperbarui blog ini seiring evolusi SDK.

### Fitur Utama

- [ModelContextProtocol MCP C# di Nuget](https://www.nuget.org/packages/ModelContextProtocol)
- Membangun [Server MCP pertama Anda](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Untuk contoh implementasi lengkap C#, kunjungi [repositori sampel SDK C# resmi](https://github.com/modelcontextprotocol/csharp-sdk)

## Contoh Implementasi: Implementasi Java dengan Spring

SDK Java dengan Spring menawarkan opsi implementasi MCP yang kuat dengan fitur kelas enterprise.

### Fitur Utama

- Integrasi Spring Framework
- Keamanan tipe yang kuat
- Dukungan pemrograman reaktif
- Penanganan error komprehensif

Untuk contoh implementasi lengkap Java dengan Spring, lihat [sampel Java dengan Spring](samples/java/containerapp/README.md) di direktori sampel.

## Contoh Implementasi: Implementasi JavaScript

SDK JavaScript menyediakan pendekatan ringan dan fleksibel untuk implementasi MCP.

### Fitur Utama

- Dukungan Node.js dan browser
- API berbasis Promise
- Integrasi mudah dengan Express dan framework lain
- Dukungan WebSocket untuk streaming

Untuk contoh implementasi lengkap JavaScript, lihat [sampel JavaScript](samples/javascript/README.md) di direktori sampel.

## Contoh Implementasi: Implementasi Python

SDK Python menawarkan pendekatan Pythonik untuk implementasi MCP dengan integrasi framework ML yang sangat baik.

### Fitur Utama

- Dukungan async/await dengan asyncio
- Integrasi FastAPI
- Pendaftaran tool yang sederhana
- Integrasi native dengan pustaka ML populer

Untuk contoh implementasi lengkap Python, lihat [sampel Python](samples/python/README.md) di direktori sampel.

## Manajemen API

Azure API Management adalah solusi ideal untuk mengamankan Server MCP. Idemya adalah menempatkan instance Azure API Management di depan Server MCP Anda dan membiarkannya menangani fitur yang kemungkinan Anda perlukan seperti:

- pembatasan laju (rate limiting)
- manajemen token
- pemantauan
- penyeimbangan beban
- keamanan

### Sampel Azure

Berikut adalah Sampel Azure yang melakukan hal tersebut, yaitu [membuat Server MCP dan mengamankannya dengan Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Lihat bagaimana alur otorisasi terjadi pada gambar berikut:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Pada gambar di atas, terjadi hal-hal berikut:

- Otentikasi/Otorisasi dilakukan menggunakan Microsoft Entra.
- Azure API Management bertindak sebagai gateway dan menggunakan kebijakan untuk mengarahkan dan mengelola lalu lintas.
- Azure Monitor mencatat semua permintaan untuk analisis lebih lanjut.

#### Alur Otorisasi

Mari kita lihat alur otorisasi lebih detail:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Spesifikasi otorisasi MCP

Pelajari lebih lanjut tentang [spesifikasi Otorisasi MCP](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Menerapkan Remote MCP Server ke Azure

Mari kita lihat apakah kita dapat menerapkan sampel yang disebutkan sebelumnya:

1. Clone repositori

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Daftarkan penyedia sumber daya `Microsoft.App`.

   - Jika Anda menggunakan Azure CLI, jalankan `az provider register --namespace Microsoft.App --wait`.
   - Jika Anda menggunakan Azure PowerShell, jalankan `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Kemudian jalankan `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` setelah beberapa saat untuk memeriksa apakah pendaftaran sudah selesai.

1. Jalankan perintah [azd](https://aka.ms/azd) ini untuk menyediakan layanan api management, function app (dengan kode), dan semua sumber daya Azure lain yang dibutuhkan

    ```shell
    azd up
    ```

    Perintah ini harus menerapkan semua sumber daya cloud di Azure

### Menguji server Anda dengan MCP Inspector

1. Di **jendela terminal baru**, instal dan jalankan MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Anda akan melihat antarmuka seperti:

    ![Connect to Node inspector](../../../translated_images/id/connect.141db0b2bd05f096.webp)

1. Klik CTRL untuk membuka aplikasi web MCP Inspector dari URL yang ditampilkan oleh aplikasi (misal [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Setel jenis transport ke `SSE`
1. Setel URL ke endpoint API Management SSE Anda yang berjalan yang ditampilkan setelah `azd up` dan **Sambungkan**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Daftar Tools**. Klik pada sebuah tool dan **Jalankan Tool**.

Jika semua langkah berhasil, Anda sekarang harus terhubung ke server MCP dan berhasil memanggil sebuah tools.

## Server MCP untuk Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Sekumpulan repositori ini adalah template cepat untuk membangun dan menerapkan server MCP (Model Context Protocol) jarak jauh khusus menggunakan Azure Functions dengan Python, C# .NET, atau Node/TypeScript.

Sampel ini menyediakan solusi lengkap yang memungkinkan pengembang untuk:

- Membangun dan menjalankan lokal: Mengembangkan dan debug server MCP di mesin lokal
- Menerapkan ke Azure: Dengan mudah menerapkan ke cloud dengan perintah azd up yang sederhana
- Terhubung dari klien: Terhubung ke server MCP dari berbagai klien termasuk mode agen Copilot VS Code dan alat MCP Inspector

### Fitur Utama

- Keamanan dari desain: Server MCP diamankan menggunakan kunci dan HTTPS
- Opsi otentikasi: Mendukung OAuth menggunakan otentikasi bawaan dan/atau API Management
- Isolasi jaringan: Memungkinkan isolasi jaringan menggunakan Azure Virtual Networks (VNET)
- Arsitektur tanpa server: Memanfaatkan Azure Functions untuk eksekusi yang skalabel dan berbasis event
- Pengembangan lokal: Dukungan pengembangan dan debug lokal yang komprehensif
- Penyebaran sederhana: Proses penyebaran yang mudah ke Azure

Repositori ini mencakup semua file konfigurasi, kode sumber, dan definisi infrastruktur yang Anda perlukan untuk segera memulai implementasi server MCP siap produksi.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Implementasi contoh MCP menggunakan Azure Functions dengan Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Implementasi contoh MCP menggunakan Azure Functions dengan C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Implementasi contoh MCP menggunakan Azure Functions dengan Node/TypeScript.

## Intisari Utama

- SDK MCP menyediakan alat khusus bahasa untuk mengimplementasikan solusi MCP yang tangguh
- Proses debugging dan pengujian sangat penting untuk aplikasi MCP yang andal
- Template prompt yang dapat digunakan ulang memungkinkan interaksi AI yang konsisten
- Alur kerja yang dirancang dengan baik dapat mengorkestrasi tugas kompleks menggunakan berbagai tools
- Mengimplementasikan solusi MCP memerlukan pertimbangan keamanan, kinerja, dan penanganan kesalahan

## Latihan

Rancang alur kerja MCP praktis yang menangani masalah dunia nyata di bidang Anda:

1. Identifikasi 3-4 tools yang akan berguna untuk menyelesaikan masalah ini
2. Buat diagram alur kerja yang menunjukkan bagaimana tools ini berinteraksi
3. Implementasikan versi dasar dari salah satu tools menggunakan bahasa pilihan Anda
4. Buat template prompt yang dapat membantu model menggunakan tool Anda secara efektif

## Sumber Daya Tambahan

---

## Apa Berikutnya

Selanjutnya: [Topik Lanjutan](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah dan otoritatif. Untuk informasi penting, disarankan menggunakan jasa terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->