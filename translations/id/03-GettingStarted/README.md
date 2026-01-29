## Memulai  

[![Bangun Server MCP Pertama Anda](../../../translated_images/id/04.0ea920069efd979a0b2dad51e72c1df7ead9c57b3305796068a6cee1f0dd6674.png)](https://youtu.be/sNDZO9N4m9Y)

_(Klik gambar di atas untuk menonton video pelajaran ini)_

Bagian ini terdiri dari beberapa pelajaran:

- **1 Server pertama Anda**, dalam pelajaran pertama ini, Anda akan belajar cara membuat server pertama Anda dan memeriksanya dengan alat inspeksi, cara yang berguna untuk menguji dan memperbaiki server Anda, [ke pelajaran](01-first-server/README.md)

- **2 Klien**, dalam pelajaran ini, Anda akan belajar cara menulis klien yang dapat terhubung ke server Anda, [ke pelajaran](02-client/README.md)

- **3 Klien dengan LLM**, cara yang lebih baik untuk menulis klien adalah dengan menambahkan LLM sehingga dapat "bernegosiasi" dengan server Anda tentang apa yang harus dilakukan, [ke pelajaran](03-llm-client/README.md)

- **4 Menggunakan mode GitHub Copilot Agent di Visual Studio Code**. Di sini, kita akan melihat cara menjalankan Server MCP dari dalam Visual Studio Code, [ke pelajaran](04-vscode/README.md)

- **5 Server Transport stdio** stdio transport adalah standar yang direkomendasikan untuk komunikasi server-ke-klien MCP dalam spesifikasi saat ini, menyediakan komunikasi berbasis subprocess yang aman [ke pelajaran](05-stdio-server/README.md)

- **6 HTTP Streaming dengan MCP (Streamable HTTP)**. Pelajari tentang HTTP streaming modern, notifikasi progres, dan cara mengimplementasikan server dan klien MCP yang skalabel dan real-time menggunakan Streamable HTTP. [ke pelajaran](06-http-streaming/README.md)

- **7 Memanfaatkan AI Toolkit untuk VSCode** untuk menggunakan dan menguji Klien dan Server MCP Anda [ke pelajaran](07-aitk/README.md)

- **8 Pengujian**. Di sini kita akan fokus terutama pada cara menguji server dan klien kita dengan berbagai cara, [ke pelajaran](08-testing/README.md)

- **9 Deployment**. Bab ini akan membahas berbagai cara untuk menerapkan solusi MCP Anda, [ke pelajaran](09-deployment/README.md)

- **10 Penggunaan server tingkat lanjut**. Bab ini mencakup penggunaan server tingkat lanjut, [ke pelajaran](./10-advanced/README.md)

- **11 Auth**. Bab ini membahas cara menambahkan autentikasi sederhana, mulai dari Basic Auth hingga menggunakan JWT dan RBAC. Anda disarankan untuk memulai di sini dan kemudian melihat Topik Lanjutan di Bab 5 serta melakukan penguatan keamanan tambahan melalui rekomendasi di Bab 2, [ke pelajaran](./11-simple-auth/README.md)

Model Context Protocol (MCP) adalah protokol terbuka yang menstandarkan cara aplikasi menyediakan konteks untuk LLM. Pikirkan MCP seperti port USB-C untuk aplikasi AI - ini menyediakan cara standar untuk menghubungkan model AI ke berbagai sumber data dan alat.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Menyiapkan lingkungan pengembangan untuk MCP dalam C#, Java, Python, TypeScript, dan JavaScript
- Membangun dan menerapkan server MCP dasar dengan fitur khusus (resources, prompts, dan tools)
- Membuat aplikasi host yang terhubung ke server MCP
- Menguji dan memperbaiki implementasi MCP
- Memahami tantangan umum dalam pengaturan dan solusinya
- Menghubungkan implementasi MCP Anda ke layanan LLM populer

## Menyiapkan Lingkungan MCP Anda

Sebelum mulai bekerja dengan MCP, penting untuk mempersiapkan lingkungan pengembangan Anda dan memahami alur kerja dasar. Bagian ini akan memandu Anda melalui langkah-langkah awal untuk memastikan awal yang lancar dengan MCP.

### Prasyarat

Sebelum memulai pengembangan MCP, pastikan Anda memiliki:

- **Lingkungan Pengembangan**: Untuk bahasa pilihan Anda (C#, Java, Python, TypeScript, atau JavaScript)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, atau editor kode modern lainnya
- **Package Managers**: NuGet, Maven/Gradle, pip, atau npm/yarn
- **API Keys**: Untuk layanan AI apa pun yang Anda rencanakan untuk digunakan dalam aplikasi host Anda

### SDK Resmi

Dalam bab-bab berikutnya, Anda akan melihat solusi yang dibangun menggunakan Python, TypeScript, Java, dan .NET. Berikut adalah semua SDK resmi yang didukung.

MCP menyediakan SDK resmi untuk berbagai bahasa:
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Dikelola bekerja sama dengan Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Dikelola bekerja sama dengan Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Implementasi resmi TypeScript
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Implementasi resmi Python
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Implementasi resmi Kotlin
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Dikelola bekerja sama dengan Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Implementasi resmi Rust

## Poin Penting

- Menyiapkan lingkungan pengembangan MCP mudah dilakukan dengan SDK khusus bahasa
- Membangun server MCP melibatkan pembuatan dan pendaftaran alat dengan skema yang jelas
- Klien MCP terhubung ke server dan model untuk memanfaatkan kemampuan yang diperluas
- Pengujian dan debugging sangat penting untuk implementasi MCP yang andal
- Opsi penerapan berkisar dari pengembangan lokal hingga solusi berbasis cloud

## Latihan

Kami memiliki serangkaian contoh yang melengkapi latihan yang akan Anda lihat di semua bab dalam bagian ini. Selain itu, setiap bab juga memiliki latihan dan tugasnya sendiri.

- [Java Calculator](./samples/java/calculator/README.md)
- [.Net Calculator](../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](./samples/javascript/README.md)
- [TypeScript Calculator](./samples/typescript/README.md)
- [Python Calculator](../../../03-GettingStarted/samples/python)

## Sumber Daya Tambahan

- [Bangun Agen menggunakan Model Context Protocol di Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Remote MCP dengan Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Selanjutnya

Berikutnya: [Membuat Server MCP Pertama Anda](01-first-server/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.