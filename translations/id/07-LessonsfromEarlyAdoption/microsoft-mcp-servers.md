# 🚀 10 Server Microsoft MCP yang Mengubah Produktivitas Pengembang

## 🎯 Apa yang Akan Anda Pelajari dalam Panduan Ini

Panduan praktis ini menampilkan sepuluh server Microsoft MCP yang secara aktif mengubah cara pengembang bekerja dengan asisten AI. Alih-alih hanya menjelaskan apa yang *bisa* dilakukan server MCP, kami akan menunjukkan server yang sudah memberikan dampak nyata dalam alur kerja pengembangan sehari-hari di Microsoft dan sekitarnya.

Setiap server dalam panduan ini dipilih berdasarkan penggunaan nyata dan umpan balik dari pengembang. Anda akan menemukan bukan hanya apa yang dilakukan setiap server, tetapi juga mengapa hal itu penting dan bagaimana memanfaatkannya secara maksimal dalam proyek Anda sendiri. Baik Anda benar-benar baru dengan MCP atau ingin memperluas pengaturan yang sudah ada, server-server ini mewakili beberapa alat paling praktis dan berdampak dalam ekosistem Microsoft.

> **💡 Tips Memulai Cepat**  
> Baru dengan MCP? Tenang saja! Panduan ini dirancang ramah untuk pemula. Kami akan menjelaskan konsep-konsep saat berjalan, dan Anda selalu bisa merujuk kembali ke modul [Introduction to MCP](../00-Introduction/README.md) dan [Core Concepts](../01-CoreConcepts/README.md) untuk pemahaman yang lebih mendalam.

## Ikhtisar

Panduan komprehensif ini mengeksplorasi sepuluh server Microsoft MCP yang merevolusi cara pengembang berinteraksi dengan asisten AI dan alat eksternal. Mulai dari pengelolaan sumber daya Azure hingga pemrosesan dokumen, server-server ini menunjukkan kekuatan Model Context Protocol dalam menciptakan alur kerja pengembangan yang mulus dan produktif.

## Tujuan Pembelajaran

Di akhir panduan ini, Anda akan:  
- Memahami bagaimana server MCP meningkatkan produktivitas pengembang  
- Mempelajari implementasi server MCP Microsoft yang paling berdampak  
- Menemukan kasus penggunaan praktis untuk setiap server  
- Mengetahui cara mengatur dan mengonfigurasi server ini di VS Code dan Visual Studio  
- Menjelajahi ekosistem MCP yang lebih luas dan arah masa depan

## 🔧 Memahami Server MCP: Panduan untuk Pemula

### Apa Itu Server MCP?

Sebagai pemula dalam Model Context Protocol (MCP), Anda mungkin bertanya: "Apa sebenarnya server MCP itu, dan kenapa saya harus peduli?" Mari mulai dengan analogi sederhana.

Bayangkan server MCP sebagai asisten khusus yang membantu pendamping AI coding Anda (seperti GitHub Copilot) terhubung ke alat dan layanan eksternal. Sama seperti Anda menggunakan berbagai aplikasi di ponsel untuk tugas berbeda—satu untuk cuaca, satu untuk navigasi, satu untuk perbankan—server MCP memberi asisten AI Anda kemampuan untuk berinteraksi dengan berbagai alat dan layanan pengembangan.

### Masalah yang Diselesaikan Server MCP

Sebelum ada server MCP, jika Anda ingin:  
- Memeriksa sumber daya Azure Anda  
- Membuat isu GitHub  
- Menjalankan query database  
- Mencari dokumentasi  

Anda harus berhenti coding, membuka browser, mengunjungi situs yang sesuai, dan melakukan tugas tersebut secara manual. Pergantian konteks yang terus-menerus ini memecah fokus dan menurunkan produktivitas.

### Bagaimana Server MCP Mengubah Pengalaman Pengembangan Anda

Dengan server MCP, Anda bisa tetap berada di lingkungan pengembangan (VS Code, Visual Studio, dll.) dan cukup meminta asisten AI Anda untuk menangani tugas-tugas tersebut. Contohnya:

**Daripada alur kerja tradisional ini:**  
1. Berhenti coding  
2. Buka browser  
3. Masuk ke portal Azure  
4. Cari detail akun penyimpanan  
5. Kembali ke VS Code  
6. Lanjutkan coding  

**Sekarang Anda bisa melakukan ini:**  
1. Tanyakan ke AI: "Bagaimana status akun penyimpanan Azure saya?"  
2. Lanjutkan coding dengan informasi yang diberikan

### Manfaat Utama untuk Pemula

#### 1. 🔄 **Tetap dalam Alur Fokus Anda**  
- Tidak perlu lagi bolak-balik antar aplikasi  
- Fokus tetap pada kode yang sedang Anda tulis  
- Mengurangi beban mental mengelola berbagai alat

#### 2. 🤖 **Gunakan Bahasa Alami, Bukan Perintah Rumit**  
- Daripada menghafal sintaks SQL, cukup jelaskan data yang Anda butuhkan  
- Daripada mengingat perintah Azure CLI, jelaskan apa yang ingin Anda capai  
- Biarkan AI menangani detail teknis sementara Anda fokus pada logika

#### 3. 🔗 **Hubungkan Berbagai Alat Bersama**  
- Buat alur kerja yang kuat dengan menggabungkan berbagai layanan  
- Contoh: "Ambil semua isu GitHub terbaru dan buat item kerja Azure DevOps yang sesuai"  
- Bangun otomatisasi tanpa menulis skrip rumit

#### 4. 🌐 **Akses Ekosistem yang Terus Berkembang**  
- Manfaatkan server yang dibuat oleh Microsoft, GitHub, dan perusahaan lain  
- Gabungkan alat dari vendor berbeda dengan mulus  
- Bergabung dengan ekosistem standar yang bekerja di berbagai asisten AI

#### 5. 🛠️ **Belajar dengan Praktik Langsung**  
- Mulai dengan server yang sudah jadi untuk memahami konsep  
- Secara bertahap buat server Anda sendiri saat semakin nyaman  
- Gunakan SDK dan dokumentasi yang tersedia sebagai panduan belajar

### Contoh Dunia Nyata untuk Pemula

Misalnya Anda baru dalam pengembangan web dan sedang mengerjakan proyek pertama. Berikut bagaimana server MCP bisa membantu:

**Pendekatan tradisional:**  
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**Dengan server MCP:**  
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### Keunggulan Standar Perusahaan

MCP menjadi standar industri yang berarti:  
- **Konsistensi**: Pengalaman serupa di berbagai alat dan perusahaan  
- **Interoperabilitas**: Server dari vendor berbeda bisa bekerja sama  
- **Masa depan terjamin**: Keterampilan dan pengaturan bisa dipindahkan antar asisten AI  
- **Komunitas**: Ekosistem besar dengan pengetahuan dan sumber daya bersama

### Memulai: Apa yang Akan Anda Pelajari

Dalam panduan ini, kita akan menjelajahi 10 server Microsoft MCP yang sangat berguna untuk pengembang di semua tingkat. Setiap server dirancang untuk:  
- Menyelesaikan tantangan pengembangan umum  
- Mengurangi tugas berulang  
- Meningkatkan kualitas kode  
- Memperluas peluang belajar

> **💡 Tips Belajar**  
> Jika Anda benar-benar baru dengan MCP, mulailah dengan modul [Introduction to MCP](../00-Introduction/README.md) dan [Core Concepts](../01-CoreConcepts/README.md). Setelah itu, kembali ke sini untuk melihat konsep-konsep tersebut diterapkan dengan alat Microsoft nyata.  
>  
> Untuk konteks tambahan tentang pentingnya MCP, baca posting Maria Naggaga: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## Memulai dengan MCP di VS Code dan Visual Studio 🚀

Mengatur server MCP ini cukup mudah jika Anda menggunakan Visual Studio Code atau Visual Studio 2022 dengan GitHub Copilot.

### Pengaturan VS Code

Berikut proses dasar untuk VS Code:

1. **Aktifkan Mode Agent**: Di VS Code, beralih ke mode Agent di jendela Copilot Chat  
2. **Konfigurasikan Server MCP**: Tambahkan konfigurasi server ke file settings.json VS Code Anda  
3. **Mulai Server**: Klik tombol "Start" untuk setiap server yang ingin Anda gunakan  
4. **Pilih Alat**: Tentukan server MCP mana yang diaktifkan untuk sesi saat ini

Untuk instruksi pengaturan lengkap, lihat dokumentasi [VS Code MCP](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Tips Pro: Kelola Server MCP seperti Profesional!**  
>  
> Tampilan Extensions di VS Code kini menyertakan [UI baru yang praktis untuk mengelola Server MCP yang terpasang](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Anda bisa dengan cepat memulai, menghentikan, dan mengelola server MCP melalui antarmuka yang jelas dan sederhana. Coba sekarang!

### Pengaturan Visual Studio 2022

Untuk Visual Studio 2022 (versi 17.14 ke atas):

1. **Aktifkan Mode Agent**: Klik dropdown "Ask" di jendela GitHub Copilot Chat dan pilih "Agent"  
2. **Buat File Konfigurasi**: Buat file `.mcp.json` di direktori solusi Anda (lokasi yang disarankan: `<SOLUTIONDIR>\.mcp.json`)  
3. **Konfigurasikan Server**: Tambahkan konfigurasi server MCP menggunakan format MCP standar  
4. **Persetujuan Alat**: Saat diminta, setujui alat yang ingin Anda gunakan dengan izin cakupan yang sesuai

Untuk instruksi pengaturan Visual Studio lengkap, lihat dokumentasi [Visual Studio MCP](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Setiap server MCP memiliki kebutuhan konfigurasi sendiri (string koneksi, autentikasi, dll.), tapi pola pengaturannya konsisten di kedua IDE.

## Pelajaran dari Server Microsoft MCP 🛠️

### 1. 📚 Microsoft Learn Docs MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Fungsi**: Microsoft Learn Docs MCP Server adalah layanan berbasis cloud yang menyediakan akses real-time bagi asisten AI ke dokumentasi resmi Microsoft melalui Model Context Protocol. Server ini terhubung ke `https://learn.microsoft.com/api/mcp` dan memungkinkan pencarian semantik di Microsoft Learn, dokumentasi Azure, dokumentasi Microsoft 365, dan sumber resmi Microsoft lainnya.

**Mengapa berguna**: Meskipun terlihat seperti "hanya dokumentasi," server ini sangat penting bagi setiap pengembang yang menggunakan teknologi Microsoft. Salah satu keluhan terbesar dari pengembang .NET tentang asisten coding AI adalah mereka tidak selalu mengikuti rilis terbaru .NET dan C#. Microsoft Learn Docs MCP Server mengatasi masalah ini dengan menyediakan akses real-time ke dokumentasi terbaru, referensi API, dan praktik terbaik. Baik Anda bekerja dengan SDK Azure terbaru, menjelajahi fitur baru C# 13, atau menerapkan pola .NET Aspire terkini, server ini memastikan asisten AI Anda memiliki akses ke informasi otoritatif dan mutakhir untuk menghasilkan kode yang akurat dan modern.

**Penggunaan nyata**: "Apa perintah az cli untuk membuat aplikasi container Azure sesuai dokumentasi resmi Microsoft Learn?" atau "Bagaimana cara mengonfigurasi Entity Framework dengan dependency injection di ASP.NET Core?" Atau "Tinjau kode ini untuk memastikan sesuai dengan rekomendasi performa di Dokumentasi Microsoft Learn." Server ini menyediakan cakupan lengkap di Microsoft Learn, dokumentasi Azure, dan Microsoft 365 dengan pencarian semantik canggih untuk menemukan informasi yang paling relevan secara kontekstual. Server mengembalikan hingga 10 potongan konten berkualitas tinggi dengan judul artikel dan URL, selalu mengakses dokumentasi Microsoft terbaru saat diterbitkan.

**Contoh unggulan**: Server ini menyediakan alat `microsoft_docs_search` yang melakukan pencarian semantik terhadap dokumentasi teknis resmi Microsoft. Setelah dikonfigurasi, Anda bisa mengajukan pertanyaan seperti "Bagaimana cara mengimplementasikan autentikasi JWT di ASP.NET Core?" dan mendapatkan jawaban resmi yang rinci beserta tautan sumber. Kualitas pencarian sangat baik karena memahami konteks – misalnya, bertanya tentang "containers" dalam konteks Azure akan mengembalikan dokumentasi Azure Container Instances, sementara dalam konteks .NET akan mengembalikan informasi koleksi C# yang relevan.

Ini sangat berguna untuk pustaka dan kasus penggunaan yang cepat berubah atau baru diperbarui. Misalnya, dalam beberapa proyek coding terbaru saya ingin memanfaatkan fitur di rilis terbaru .NET Aspire dan Microsoft.Extensions.AI. Dengan menyertakan Microsoft Learn Docs MCP server, saya bisa memanfaatkan tidak hanya dokumentasi API, tapi juga panduan dan tutorial yang baru saja diterbitkan.
> **💡 Pro Tip**
> 
> Bahkan model yang ramah alat pun perlu dorongan untuk menggunakan alat MCP! Pertimbangkan untuk menambahkan prompt sistem atau [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) seperti: "Anda memiliki akses ke `microsoft.docs.mcp` – gunakan alat ini untuk mencari dokumentasi resmi terbaru dari Microsoft saat menangani pertanyaan tentang teknologi Microsoft seperti C#, Azure, ASP.NET Core, atau Entity Framework."
>
> Untuk contoh yang bagus dari penerapan ini, lihat [mode chat C# .NET Janitor](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) dari repositori Awesome GitHub Copilot. Mode ini secara khusus memanfaatkan server Microsoft Learn Docs MCP untuk membantu membersihkan dan memodernisasi kode C# menggunakan pola dan praktik terbaik terbaru.
### 2. ☁️ Azure MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Apa fungsinya**: Azure MCP Server adalah rangkaian lengkap yang terdiri dari lebih dari 15 konektor layanan Azure khusus yang membawa seluruh ekosistem Azure ke dalam alur kerja AI Anda. Ini bukan hanya satu server – melainkan kumpulan kuat yang mencakup manajemen sumber daya, konektivitas database (PostgreSQL, SQL Server), analisis log Azure Monitor dengan KQL, integrasi Cosmos DB, dan masih banyak lagi.

**Mengapa ini berguna**: Selain hanya mengelola sumber daya Azure, server ini secara signifikan meningkatkan kualitas kode saat bekerja dengan Azure SDK. Saat Anda menggunakan Azure MCP dalam mode Agent, server ini tidak hanya membantu Anda menulis kode – tapi membantu Anda menulis kode Azure yang *lebih baik* yang mengikuti pola autentikasi terkini, praktik terbaik penanganan error, dan memanfaatkan fitur SDK terbaru. Alih-alih mendapatkan kode generik yang mungkin berfungsi, Anda mendapatkan kode yang mengikuti pola yang direkomendasikan Azure untuk beban kerja produksi.

**Modul utama meliputi**:
- **🗄️ Database Connectors**: Akses bahasa alami langsung ke Azure Database untuk PostgreSQL dan SQL Server
- **📊 Azure Monitor**: Analisis log bertenaga KQL dan wawasan operasional
- **🌐 Resource Management**: Manajemen siklus hidup sumber daya Azure secara penuh
- **🔐 Authentication**: Pola DefaultAzureCredential dan managed identity
- **📦 Storage Services**: Operasi Blob Storage, Queue Storage, dan Table Storage
- **🚀 Container Services**: Manajemen Azure Container Apps, Container Instances, dan AKS
- **Dan banyak konektor khusus lainnya**

**Penggunaan nyata**: "Daftar akun penyimpanan Azure saya", "Query workspace Log Analytics saya untuk error dalam satu jam terakhir", atau "Bantu saya membangun aplikasi Azure menggunakan Node.js dengan autentikasi yang tepat"

**Skenario demo lengkap**: Berikut adalah panduan lengkap yang menunjukkan kekuatan menggabungkan Azure MCP dengan ekstensi GitHub Copilot untuk Azure di VS Code. Ketika Anda sudah menginstal keduanya dan memberikan perintah:

> "Buat skrip Python yang mengunggah file ke Azure Blob Storage menggunakan autentikasi DefaultAzureCredential. Skrip harus terhubung ke akun penyimpanan Azure saya bernama 'mycompanystorage', mengunggah ke container bernama 'documents', membuat file uji dengan timestamp saat ini untuk diunggah, menangani error dengan baik dan memberikan output informatif, mengikuti praktik terbaik Azure untuk autentikasi dan penanganan error, menyertakan komentar yang menjelaskan cara kerja autentikasi DefaultAzureCredential, dan membuat skrip terstruktur dengan fungsi dan dokumentasi yang tepat."

Azure MCP Server akan menghasilkan skrip Python lengkap siap produksi yang:
- Menggunakan SDK Azure Blob Storage terbaru dengan pola async yang benar
- Menerapkan DefaultAzureCredential dengan penjelasan rantai fallback yang komprehensif
- Menyertakan penanganan error yang kuat dengan tipe exception Azure spesifik
- Mengikuti praktik terbaik Azure SDK untuk manajemen sumber daya dan koneksi
- Memberikan logging detail dan output konsol yang informatif
- Membuat skrip terstruktur dengan fungsi, dokumentasi, dan tipe hint

Yang membuat ini luar biasa adalah tanpa Azure MCP, Anda mungkin hanya mendapatkan kode blob storage generik yang berfungsi tapi tidak mengikuti pola Azure terkini. Dengan Azure MCP, Anda mendapatkan kode yang memanfaatkan metode autentikasi terbaru, menangani skenario error khusus Azure, dan mengikuti praktik yang direkomendasikan Microsoft untuk aplikasi produksi.

**Contoh unggulan**: Saya sering kesulitan mengingat perintah spesifik untuk CLI `az` dan `azd` untuk penggunaan ad-hoc. Biasanya saya harus mencari sintaks dulu, baru menjalankan perintahnya. Saya sering masuk ke portal dan klik sana-sini untuk menyelesaikan pekerjaan karena saya tidak ingin mengakui saya lupa sintaks CLI. Bisa hanya mendeskripsikan apa yang saya inginkan itu luar biasa, apalagi bisa dilakukan tanpa meninggalkan IDE saya!

Ada daftar kasus penggunaan yang bagus di [repository Azure MCP](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) untuk memulai. Untuk panduan setup lengkap dan opsi konfigurasi lanjutan, lihat [dokumentasi resmi Azure MCP](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Apa fungsinya**: GitHub MCP Server resmi menyediakan integrasi mulus dengan seluruh ekosistem GitHub, menawarkan akses remote yang di-host dan opsi deployment lokal menggunakan Docker. Ini bukan hanya operasi repositori dasar – tapi toolkit lengkap yang mencakup manajemen GitHub Actions, alur kerja pull request, pelacakan isu, pemindaian keamanan, notifikasi, dan kemampuan otomasi tingkat lanjut.

**Mengapa ini berguna**: Server ini mengubah cara Anda berinteraksi dengan GitHub dengan membawa pengalaman platform penuh langsung ke lingkungan pengembangan Anda. Alih-alih terus-menerus berpindah antara VS Code dan GitHub.com untuk manajemen proyek, review kode, dan pemantauan CI/CD, Anda bisa mengelola semuanya lewat perintah bahasa alami sambil tetap fokus pada kode Anda.

> **ℹ️ Catatan: Jenis 'Agent' yang Berbeda**
> 
> Jangan bingung antara GitHub MCP Server ini dengan GitHub Coding Agent (agen AI yang bisa Anda tugaskan untuk tugas coding otomatis pada isu). GitHub MCP Server bekerja dalam mode Agent VS Code untuk menyediakan integrasi API GitHub, sementara GitHub Coding Agent adalah fitur terpisah yang membuat pull request saat ditugaskan ke isu GitHub.

**Kemampuan utama meliputi**:
- **⚙️ GitHub Actions**: Manajemen pipeline CI/CD lengkap, pemantauan workflow, dan pengelolaan artifact
- **🔀 Pull Requests**: Membuat, meninjau, menggabungkan, dan mengelola PR dengan pelacakan status menyeluruh
- **🐛 Issues**: Manajemen siklus hidup isu lengkap, komentar, pelabelan, dan penugasan
- **🔒 Security**: Peringatan pemindaian kode, deteksi rahasia, dan integrasi Dependabot
- **🔔 Notifications**: Manajemen notifikasi pintar dan kontrol langganan repositori
- **📁 Repository Management**: Operasi file, manajemen cabang, dan administrasi repositori
- **👥 Collaboration**: Pencarian pengguna dan organisasi, manajemen tim, dan kontrol akses

**Penggunaan nyata**: "Buat pull request dari branch fitur saya", "Tunjukkan semua run CI yang gagal minggu ini", "Daftar peringatan keamanan terbuka untuk repositori saya", atau "Cari semua isu yang ditugaskan ke saya di seluruh organisasi saya"

**Skenario demo lengkap**: Berikut alur kerja kuat yang menunjukkan kemampuan GitHub MCP Server:

> "Saya perlu mempersiapkan review sprint kami. Tunjukkan semua pull request yang saya buat minggu ini, periksa status pipeline CI/CD kami, buat ringkasan peringatan keamanan yang perlu kami tangani, dan bantu saya menyusun catatan rilis berdasarkan PR yang sudah digabung dengan label 'feature'."

GitHub MCP Server akan:
- Mengquery pull request terbaru Anda dengan informasi status detail
- Menganalisis run workflow dan menyoroti kegagalan atau masalah performa
- Mengompilasi hasil pemindaian keamanan dan memprioritaskan peringatan kritis
- Menghasilkan catatan rilis komprehensif dengan mengekstrak informasi dari PR yang digabung
- Memberikan langkah selanjutnya yang dapat diambil untuk perencanaan sprint dan persiapan rilis

**Contoh unggulan**: Saya suka menggunakan ini untuk alur kerja review kode. Daripada bolak-balik antara VS Code, notifikasi GitHub, dan halaman pull request, saya bisa bilang "Tunjukkan semua PR yang menunggu review saya" lalu "Tambahkan komentar di PR #123 menanyakan tentang penanganan error di metode autentikasi." Server menangani panggilan API GitHub, menjaga konteks diskusi, dan bahkan membantu saya membuat komentar review yang lebih konstruktif.

**Opsi autentikasi**: Server mendukung OAuth (seamless di VS Code) dan Personal Access Tokens, dengan toolset yang bisa dikonfigurasi untuk mengaktifkan hanya fungsi GitHub yang Anda butuhkan. Anda bisa menjalankannya sebagai layanan remote hosted untuk setup instan atau lokal via Docker untuk kontrol penuh.

> **💡 Tips Pro**
> 
> Aktifkan hanya toolset yang Anda perlukan dengan mengonfigurasi parameter `--toolsets` di pengaturan MCP server Anda untuk mengurangi ukuran konteks dan meningkatkan pemilihan alat AI. Misalnya, tambahkan `"--toolsets", "repos,issues,pull_requests,actions"` ke argumen konfigurasi MCP untuk alur kerja pengembangan inti, atau gunakan `"--toolsets", "notifications, security"` jika Anda terutama ingin kemampuan pemantauan GitHub.

### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Apa fungsinya**: Terhubung ke layanan Azure DevOps untuk manajemen proyek menyeluruh, pelacakan work item, manajemen pipeline build, dan operasi repositori.

**Mengapa ini berguna**: Untuk tim yang menggunakan Azure DevOps sebagai platform DevOps utama, MCP server ini menghilangkan kebutuhan untuk bolak-balik antara lingkungan pengembangan dan antarmuka web Azure DevOps. Anda bisa mengelola work item, memeriksa status build, mengquery repositori, dan menangani tugas manajemen proyek langsung dari asisten AI Anda.

**Penggunaan nyata**: "Tunjukkan semua work item aktif di sprint saat ini untuk proyek WebApp", "Buat laporan bug untuk masalah login yang baru saya temukan", atau "Periksa status pipeline build kami dan tunjukkan kegagalan terbaru"

**Contoh unggulan**: Anda bisa dengan mudah memeriksa status sprint tim Anda saat ini dengan query sederhana seperti "Tunjukkan semua work item aktif di sprint saat ini untuk proyek WebApp" atau "Buat laporan bug untuk masalah login yang baru saya temukan" tanpa meninggalkan lingkungan pengembangan Anda.

### 5. 📝 MarkItDown MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Apa yang dilakukan**: MarkItDown adalah server konversi dokumen lengkap yang mengubah berbagai format file menjadi Markdown berkualitas tinggi, dioptimalkan untuk konsumsi LLM dan alur kerja analisis teks.

**Mengapa ini berguna**: Penting untuk alur kerja dokumentasi modern! MarkItDown menangani berbagai format file dengan sangat baik sambil mempertahankan struktur dokumen penting seperti judul, daftar, tabel, dan tautan. Berbeda dengan alat ekstraksi teks sederhana, ia fokus pada menjaga makna semantik dan format yang berharga untuk pemrosesan AI maupun keterbacaan manusia.

**Format file yang didukung**:
- **Dokumen Office**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **File Media**: Gambar (dengan metadata EXIF dan OCR), Audio (dengan metadata EXIF dan transkripsi suara)
- **Konten Web**: HTML, feed RSS, URL YouTube, halaman Wikipedia
- **Format Data**: CSV, JSON, XML, file ZIP (memproses isi secara rekursif)
- **Format Penerbitan**: EPub, notebook Jupyter (.ipynb)
- **Email**: Pesan Outlook (.msg)
- **Lanjutan**: Integrasi Azure Document Intelligence untuk pemrosesan PDF yang lebih baik

**Kemampuan lanjutan**: MarkItDown mendukung deskripsi gambar berbasis LLM (jika disediakan klien OpenAI), Azure Document Intelligence untuk pemrosesan PDF yang ditingkatkan, transkripsi audio untuk konten suara, dan sistem plugin untuk memperluas ke format file tambahan.

**Penggunaan nyata**: "Ubah presentasi PowerPoint ini ke Markdown untuk situs dokumentasi kami", "Ekstrak teks dari PDF ini dengan struktur judul yang tepat", atau "Ubah spreadsheet Excel ini menjadi format tabel yang mudah dibaca"

**Contoh unggulan**: Mengutip dari [dokumentasi MarkItDown](https://github.com/microsoft/markitdown#why-markdown):

> Markdown sangat dekat dengan teks biasa, dengan markup atau format minimal, tapi tetap menyediakan cara untuk merepresentasikan struktur dokumen penting. LLM mainstream, seperti GPT-4o dari OpenAI, secara native "berbicara" Markdown, dan sering memasukkan Markdown dalam respons mereka tanpa diminta. Ini menunjukkan bahwa mereka telah dilatih dengan sejumlah besar teks berformat Markdown, dan memahaminya dengan baik. Sebagai manfaat tambahan, konvensi Markdown juga sangat efisien dalam penggunaan token.

MarkItDown sangat baik dalam menjaga struktur dokumen, yang penting untuk alur kerja AI. Misalnya, saat mengonversi presentasi PowerPoint, ia mempertahankan organisasi slide dengan judul yang tepat, mengekstrak tabel sebagai tabel Markdown, menyertakan teks alternatif untuk gambar, dan bahkan memproses catatan pembicara. Grafik diubah menjadi tabel data yang mudah dibaca, dan Markdown hasilnya mempertahankan alur logis presentasi asli. Ini membuatnya sempurna untuk memasukkan konten presentasi ke dalam sistem AI atau membuat dokumentasi dari slide yang ada.

### 6. 🗃️ SQL Server MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Apa yang dilakukan**: Menyediakan akses percakapan ke database SQL Server (on-premises, Azure SQL, atau Fabric)

**Mengapa ini berguna**: Mirip dengan server PostgreSQL tapi untuk ekosistem Microsoft SQL. Hubungkan dengan string koneksi sederhana dan mulai melakukan query dengan bahasa alami – tidak perlu lagi berganti konteks!

**Penggunaan nyata**: "Cari semua pesanan yang belum dipenuhi dalam 30 hari terakhir" diterjemahkan ke query SQL yang sesuai dan mengembalikan hasil yang diformat

**Contoh unggulan**: Setelah Anda mengatur koneksi database, Anda bisa langsung mulai berinteraksi dengan data Anda. Blog post menampilkan ini dengan pertanyaan sederhana: "database apa yang sedang Anda hubungkan?" MCP server merespons dengan memanggil alat database yang tepat, menghubungkan ke instance SQL Server Anda, dan mengembalikan detail tentang koneksi database saat ini – semua tanpa menulis satu baris SQL pun. Server ini mendukung operasi database lengkap mulai dari manajemen skema hingga manipulasi data, semua melalui perintah bahasa alami. Untuk instruksi pengaturan lengkap dan contoh konfigurasi dengan VS Code dan Claude Desktop, lihat: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).

### 7. 🎭 Playwright MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Apa yang dilakukan**: Memungkinkan agen AI berinteraksi dengan halaman web untuk pengujian dan otomatisasi

> **ℹ️ Mendukung GitHub Copilot**
> 
> Playwright MCP Server mendukung Coding Agent GitHub Copilot, memberikannya kemampuan browsing web! [Pelajari lebih lanjut tentang fitur ini](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Mengapa ini berguna**: Sempurna untuk pengujian otomatis yang didorong oleh deskripsi bahasa alami. AI dapat menavigasi situs web, mengisi formulir, dan mengekstrak data melalui snapshot aksesibilitas terstruktur – ini sangat kuat!

**Penggunaan nyata**: "Uji alur login dan verifikasi bahwa dashboard dimuat dengan benar" atau "Buat tes yang mencari produk dan memvalidasi halaman hasil" – semua tanpa perlu kode sumber aplikasi

**Contoh unggulan**: Rekan saya Debbie O'Brien baru-baru ini melakukan pekerjaan luar biasa dengan Playwright MCP Server! Misalnya, dia menunjukkan bagaimana Anda bisa membuat tes Playwright lengkap tanpa harus memiliki akses ke kode sumber aplikasi. Dalam skenarionya, dia meminta Copilot membuat tes untuk aplikasi pencarian film: buka situs, cari "Garfield," dan verifikasi film muncul di hasil. MCP membuka sesi browser, menjelajahi struktur halaman menggunakan snapshot DOM, menemukan selector yang tepat, dan menghasilkan tes TypeScript yang berfungsi penuh dan lolos pada percobaan pertama.

Yang membuat ini sangat kuat adalah kemampuannya menjembatani instruksi bahasa alami dengan kode tes yang dapat dijalankan. Pendekatan tradisional memerlukan penulisan tes manual atau akses ke kode untuk konteks. Tapi dengan Playwright MCP, Anda bisa menguji situs eksternal, aplikasi klien, atau bekerja dalam skenario pengujian black-box tanpa akses kode.

### 8. 💻 Dev Box MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Apa yang dilakukan**: Mengelola lingkungan Microsoft Dev Box melalui bahasa alami

**Mengapa ini berguna**: Mempermudah pengelolaan lingkungan pengembangan secara signifikan! Buat, konfigurasikan, dan kelola lingkungan pengembangan tanpa harus mengingat perintah spesifik.

**Penggunaan nyata**: "Siapkan Dev Box baru dengan SDK .NET terbaru dan konfigurasikan untuk proyek kami", "Periksa status semua lingkungan pengembangan saya", atau "Buat lingkungan demo standar untuk presentasi tim kami"

**Contoh unggulan**: Saya sangat menyukai penggunaan Dev Box untuk pengembangan pribadi. Momen pencerahan saya adalah saat James Montemagno menjelaskan betapa hebatnya Dev Box untuk demo konferensi, karena koneksi ethernet-nya sangat cepat tanpa tergantung pada wifi konferensi/hotel/pesawat yang saya gunakan saat itu. Bahkan, saya baru-baru ini berlatih demo konferensi sambil laptop saya tethering ke hotspot ponsel saat naik bus dari Bruges ke Antwerp! Langkah saya berikutnya adalah mendalami pengelolaan tim dengan banyak lingkungan pengembangan dan lingkungan demo standar. Dan kasus penggunaan besar lain yang saya dengar dari pelanggan dan rekan kerja adalah menggunakan Dev Box untuk lingkungan pengembangan yang sudah dikonfigurasi sebelumnya. Dalam kedua kasus, menggunakan MCP untuk mengonfigurasi dan mengelola Dev Box memungkinkan interaksi dengan bahasa alami, sambil tetap berada di lingkungan pengembangan Anda.

### 9. 🤖 Azure AI Foundry MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Apa yang dilakukan**: Azure AI Foundry MCP Server memberikan akses lengkap kepada pengembang ke ekosistem AI Azure, termasuk katalog model, manajemen deployment, pengindeksan pengetahuan dengan Azure AI Search, dan alat evaluasi. Server eksperimental ini menjembatani pengembangan AI dengan infrastruktur AI Azure yang kuat, memudahkan pembuatan, deployment, dan evaluasi aplikasi AI.

**Mengapa ini berguna**: Server ini mengubah cara Anda bekerja dengan layanan Azure AI dengan menghadirkan kemampuan AI kelas perusahaan langsung ke alur kerja pengembangan Anda. Alih-alih bolak-balik antara portal Azure, dokumentasi, dan IDE, Anda bisa menemukan model, melakukan deployment layanan, mengelola basis pengetahuan, dan mengevaluasi performa AI melalui perintah bahasa alami. Ini sangat berguna bagi pengembang yang membangun aplikasi RAG (Retrieval-Augmented Generation), mengelola deployment multi-model, atau mengimplementasikan pipeline evaluasi AI yang komprehensif.

**Kemampuan utama untuk pengembang**:
- **🔍 Penemuan & Deployment Model**: Jelajahi katalog model Azure AI Foundry, dapatkan informasi detail model dengan contoh kode, dan deploy model ke Azure AI Services
- **📚 Manajemen Pengetahuan**: Buat dan kelola indeks Azure AI Search, tambahkan dokumen, konfigurasikan indexer, dan bangun sistem RAG yang canggih
- **⚡ Integrasi Agen AI**: Hubungkan dengan Azure AI Agents, query agen yang ada, dan evaluasi performa agen dalam skenario produksi
- **📊 Kerangka Evaluasi**: Jalankan evaluasi teks dan agen secara menyeluruh, buat laporan markdown, dan terapkan jaminan kualitas untuk aplikasi AI
- **🚀 Alat Prototipe**: Dapatkan instruksi setup untuk prototipe berbasis GitHub dan akses Azure AI Foundry Labs untuk model riset terkini

**Penggunaan nyata oleh pengembang**: "Deploy model Phi-4 ke Azure AI Services untuk aplikasi saya", "Buat indeks pencarian baru untuk sistem RAG dokumentasi saya", "Evaluasi respons agen saya berdasarkan metrik kualitas", atau "Temukan model reasoning terbaik untuk tugas analisis kompleks saya"

**Skenario demo lengkap**: Berikut alur kerja pengembangan AI yang kuat:


> "Saya sedang membangun agen dukungan pelanggan. Bantu saya menemukan model reasoning yang bagus dari katalog, deploy ke Azure AI Services, buat basis pengetahuan dari dokumentasi kami, siapkan kerangka evaluasi untuk menguji kualitas respons, dan bantu saya prototipe integrasi dengan token GitHub untuk pengujian."

Azure AI Foundry MCP Server akan:
- Query katalog model untuk merekomendasikan model reasoning optimal berdasarkan kebutuhan Anda
- Memberikan perintah deployment dan informasi kuota untuk wilayah Azure pilihan Anda
- Menyiapkan indeks Azure AI Search dengan skema yang tepat untuk dokumentasi Anda
- Mengonfigurasi pipeline evaluasi dengan metrik kualitas dan pemeriksaan keamanan
- Menghasilkan kode prototipe dengan autentikasi GitHub untuk pengujian langsung
- Menyediakan panduan setup lengkap yang disesuaikan dengan tumpukan teknologi Anda

**Contoh unggulan**: Sebagai pengembang, saya kesulitan mengikuti berbagai model LLM yang tersedia. Saya tahu beberapa model utama, tapi merasa kehilangan potensi produktivitas dan efisiensi. Token dan kuota juga membuat stres dan sulit diatur – saya tidak pernah yakin apakah memilih model yang tepat untuk tugas yang tepat atau malah boros anggaran. Saya baru dengar tentang MCP Server ini dari James Montemagno saat berdiskusi dengan rekan tim untuk rekomendasi MCP Server, dan saya sangat antusias untuk mencobanya! Kemampuan penemuan model terlihat sangat mengesankan bagi saya yang ingin menjelajah lebih jauh dari model-model umum dan menemukan model yang dioptimalkan untuk tugas spesifik. Kerangka evaluasi juga akan membantu saya memastikan hasil yang lebih baik, bukan hanya mencoba hal baru tanpa tujuan.

> **ℹ️ Status Eksperimental**
> 
> MCP server ini bersifat eksperimental dan sedang dalam pengembangan aktif. Fitur dan API dapat berubah. Cocok untuk eksplorasi kemampuan Azure AI dan pembuatan prototipe, tapi pastikan stabilitas untuk penggunaan produksi.

### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Apa yang dilakukan**: Menyediakan alat penting bagi pengembang untuk membangun agen AI dan aplikasi yang terintegrasi dengan Microsoft 365 dan Microsoft 365 Copilot, termasuk validasi skema, pengambilan contoh kode, dan bantuan pemecahan masalah.

**Mengapa ini berguna**: Pengembangan untuk Microsoft 365 dan Copilot melibatkan skema manifest yang kompleks dan pola pengembangan khusus. MCP server ini menghadirkan sumber daya pengembangan penting langsung ke lingkungan pengkodean Anda, membantu memvalidasi skema, menemukan contoh kode, dan memecahkan masalah umum tanpa harus terus merujuk dokumentasi.

**Penggunaan nyata**: "Validasi manifest agen deklaratif saya dan perbaiki kesalahan skema", "Tunjukkan contoh kode untuk mengimplementasikan plugin Microsoft Graph API", atau "Bantu saya memecahkan masalah autentikasi aplikasi Teams saya"

**Contoh unggulan**: Saya menghubungi teman saya John Miller setelah berbincang dengannya di Build tentang M365 Agents, dan dia merekomendasikan MCP ini. Ini bisa sangat membantu pengembang baru di M365 Agents karena menyediakan template, contoh kode, dan scaffolding untuk memulai tanpa harus tenggelam dalam dokumentasi. Fitur validasi skema terlihat sangat berguna untuk menghindari kesalahan struktur manifest yang bisa menyebabkan debugging berjam-jam.

> **💡 Tips Pro**
> 
> Gunakan server ini bersamaan dengan Microsoft Learn Docs MCP Server untuk dukungan pengembangan M365 yang lengkap – satu menyediakan dokumentasi resmi sementara yang ini menawarkan alat pengembangan praktis dan bantuan pemecahan masalah.

## Apa Selanjutnya? 🔮

## 📋 Kesimpulan

Model Context Protocol (MCP) mengubah cara pengembang berinteraksi dengan asisten AI dan alat eksternal. 10 server Microsoft MCP ini menunjukkan kekuatan integrasi AI yang terstandarisasi, memungkinkan alur kerja yang mulus yang menjaga fokus pengembang sambil mengakses kemampuan eksternal yang kuat.

Dari integrasi ekosistem Azure yang komprehensif hingga alat khusus seperti Playwright untuk otomasi browser dan MarkItDown untuk pemrosesan dokumen, server-server ini menunjukkan bagaimana MCP dapat meningkatkan produktivitas di berbagai skenario pengembangan. Protokol yang terstandarisasi memastikan alat-alat ini bekerja bersama dengan lancar, menciptakan pengalaman pengembangan yang kohesif.

Seiring ekosistem MCP terus berkembang, tetap terlibat dengan komunitas, menjelajahi server baru, dan membangun solusi kustom akan menjadi kunci untuk memaksimalkan produktivitas pengembangan Anda. Sifat standar terbuka MCP memungkinkan Anda menggabungkan alat dari berbagai vendor untuk menciptakan alur kerja yang sempurna sesuai kebutuhan spesifik Anda.

## 🔗 Sumber Daya Tambahan

- [Official Microsoft MCP Repository](https://github.com/microsoft/mcp)
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)
- [VS Code MCP Documentation](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP Documentation](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP Documentation](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP Events](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot Customizations](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days Live 29th/30th July or watch on Demand ](https://aka.ms/mcpdevdays)

## 🎯 Latihan

1. **Instal dan Konfigurasi**: Pasang salah satu server MCP di lingkungan VS Code Anda dan uji fungsi dasar.
2. **Integrasi Alur Kerja**: Rancang alur kerja pengembangan yang menggabungkan setidaknya tiga server MCP berbeda.
3. **Perencanaan Server Kustom**: Identifikasi tugas dalam rutinitas pengembangan harian Anda yang bisa diuntungkan dengan server MCP kustom dan buat spesifikasinya.
4. **Analisis Kinerja**: Bandingkan efisiensi penggunaan server MCP dengan pendekatan tradisional untuk tugas pengembangan umum.
5. **Penilaian Keamanan**: Evaluasi implikasi keamanan penggunaan server MCP di lingkungan pengembangan Anda dan usulkan praktik terbaik.

Next:[Best Practices](../08-BestPractices/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.