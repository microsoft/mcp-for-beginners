# Studi Kasus: Azure AI Travel Agents – Implementasi Referensi

## Ikhtisar

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) adalah solusi referensi komprehensif yang dikembangkan oleh Microsoft yang menunjukkan cara membangun aplikasi perencanaan perjalanan bertenaga AI dengan multi-agent menggunakan Model Context Protocol (MCP), Azure OpenAI, dan Azure AI Search. Proyek ini menampilkan praktik terbaik untuk mengorkestrasi beberapa agen AI, mengintegrasikan data perusahaan, dan menyediakan platform yang aman serta dapat diperluas untuk skenario dunia nyata.

## Fitur Utama
- **Orkestrasi Multi-Agent:** Memanfaatkan MCP untuk mengoordinasikan agen khusus (misalnya, agen penerbangan, hotel, dan rencana perjalanan) yang bekerja sama untuk menyelesaikan tugas perencanaan perjalanan yang kompleks.
- **Integrasi Data Perusahaan:** Terhubung ke Azure AI Search dan sumber data perusahaan lainnya untuk menyediakan informasi terkini dan relevan bagi rekomendasi perjalanan.
- **Arsitektur Aman dan Skalabel:** Memanfaatkan layanan Azure untuk autentikasi, otorisasi, dan penyebaran yang dapat diskalakan, mengikuti praktik keamanan perusahaan terbaik.
- **Alat yang Dapat Diperluas:** Mengimplementasikan alat MCP yang dapat digunakan ulang dan template prompt, memungkinkan adaptasi cepat ke domain atau kebutuhan bisnis baru.
- **Pengalaman Pengguna:** Menyediakan antarmuka percakapan bagi pengguna untuk berinteraksi dengan agen perjalanan, didukung oleh Azure OpenAI dan MCP.

## Arsitektur
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Deskripsi Diagram Arsitektur

Solusi Azure AI Travel Agents dirancang untuk modularitas, skalabilitas, dan integrasi aman dari beberapa agen AI dan sumber data perusahaan. Komponen utama dan alur data adalah sebagai berikut:

- **User Interface:** Pengguna berinteraksi dengan sistem melalui UI percakapan (seperti chat web atau bot Teams), yang mengirimkan pertanyaan pengguna dan menerima rekomendasi perjalanan.
- **MCP Server:** Berfungsi sebagai pengatur pusat, menerima input pengguna, mengelola konteks, dan mengoordinasikan tindakan agen khusus (misalnya FlightAgent, HotelAgent, ItineraryAgent) melalui Model Context Protocol.
- **AI Agents:** Setiap agen bertanggung jawab pada domain tertentu (penerbangan, hotel, rencana perjalanan) dan diimplementasikan sebagai alat MCP. Agen menggunakan template prompt dan logika untuk memproses permintaan dan menghasilkan respons.
- **Azure OpenAI Service:** Menyediakan pemahaman dan generasi bahasa alami tingkat lanjut, memungkinkan agen memahami maksud pengguna dan menghasilkan respons percakapan.
- **Azure AI Search & Data Perusahaan:** Agen melakukan kueri ke Azure AI Search dan sumber data perusahaan lainnya untuk mengambil informasi terkini tentang penerbangan, hotel, dan opsi perjalanan.
- **Autentikasi & Keamanan:** Terintegrasi dengan Microsoft Entra ID untuk autentikasi yang aman dan menerapkan kontrol akses dengan prinsip least-privilege ke semua sumber daya.
- **Penyebaran:** Dirancang untuk penyebaran di Azure Container Apps, memastikan skalabilitas, pemantauan, dan efisiensi operasional.

Arsitektur ini memungkinkan orkestrasi mulus dari beberapa agen AI, integrasi aman dengan data perusahaan, dan platform yang kuat serta dapat diperluas untuk membangun solusi AI spesifik domain.

## Penjelasan Langkah demi Langkah Diagram Arsitektur
Bayangkan merencanakan perjalanan besar dan memiliki tim asisten ahli yang membantu Anda dengan setiap detail. Sistem Azure AI Travel Agents bekerja dengan cara serupa, menggunakan bagian-bagian berbeda (seperti anggota tim) yang masing-masing memiliki tugas khusus. Berikut cara semuanya bekerja bersama:

### User Interface (UI):
Anggap ini sebagai meja depan agen perjalanan Anda. Di sinilah Anda (pengguna) mengajukan pertanyaan atau permintaan, seperti “Cari penerbangan ke Paris.” Ini bisa berupa jendela chat di situs web atau aplikasi pesan.

### MCP Server (Koordinator):
MCP Server seperti manajer yang mendengarkan permintaan Anda di meja depan dan memutuskan spesialis mana yang harus menangani setiap bagian. Ia melacak percakapan Anda dan memastikan semuanya berjalan lancar.

### AI Agents (Asisten Spesialis):
Setiap agen adalah ahli di bidang tertentu—satu tahu semua tentang penerbangan, yang lain tentang hotel, dan yang lain tentang perencanaan rencana perjalanan. Ketika Anda meminta perjalanan, MCP Server mengirimkan permintaan Anda ke agen yang tepat. Agen-agen ini menggunakan pengetahuan dan alat mereka untuk menemukan opsi terbaik bagi Anda.

### Azure OpenAI Service (Ahli Bahasa):
Ini seperti memiliki ahli bahasa yang memahami dengan tepat apa yang Anda tanyakan, tidak peduli bagaimana Anda mengungkapkannya. Ini membantu agen memahami permintaan Anda dan merespons dengan bahasa percakapan yang alami.

### Azure AI Search & Data Perusahaan (Perpustakaan Informasi):
Bayangkan perpustakaan besar dan terkini dengan semua info perjalanan terbaru—jadwal penerbangan, ketersediaan hotel, dan lainnya. Agen mencari perpustakaan ini untuk mendapatkan jawaban paling akurat untuk Anda.

### Autentikasi & Keamanan (Penjaga Keamanan):
Seperti penjaga keamanan yang memeriksa siapa yang boleh masuk ke area tertentu, bagian ini memastikan hanya orang dan agen yang berwenang yang dapat mengakses informasi sensitif. Ini menjaga data Anda tetap aman dan pribadi.

### Penyebaran di Azure Container Apps (Gedung):
Semua asisten dan alat ini bekerja bersama di dalam gedung yang aman dan dapat diskalakan (cloud). Ini berarti sistem dapat menangani banyak pengguna sekaligus dan selalu tersedia saat Anda membutuhkannya.

## Cara Kerja Keseluruhan:

Anda mulai dengan mengajukan pertanyaan di meja depan (UI).  
Manajer (MCP Server) menentukan spesialis (agen) mana yang akan membantu Anda.  
Spesialis menggunakan ahli bahasa (OpenAI) untuk memahami permintaan Anda dan perpustakaan (AI Search) untuk menemukan jawaban terbaik.  
Penjaga keamanan (Autentikasi) memastikan semuanya aman.  
Semua ini terjadi di dalam gedung yang andal dan dapat diskalakan (Azure Container Apps), sehingga pengalaman Anda lancar dan aman.  
Kerja sama ini memungkinkan sistem dengan cepat dan aman membantu Anda merencanakan perjalanan, seperti tim agen perjalanan ahli yang bekerja bersama di kantor modern!

## Implementasi Teknis
- **MCP Server:** Menyediakan logika orkestrasi inti, mengekspos alat agen, dan mengelola konteks untuk alur kerja perencanaan perjalanan multi-langkah.
- **Agents:** Setiap agen (misalnya FlightAgent, HotelAgent) diimplementasikan sebagai alat MCP dengan template prompt dan logika sendiri.
- **Integrasi Azure:** Menggunakan Azure OpenAI untuk pemahaman bahasa alami dan Azure AI Search untuk pengambilan data.
- **Keamanan:** Terintegrasi dengan Microsoft Entra ID untuk autentikasi dan menerapkan kontrol akses least-privilege ke semua sumber daya.
- **Penyebaran:** Mendukung penyebaran ke Azure Container Apps untuk skalabilitas dan efisiensi operasional.

## Hasil dan Dampak
- Menunjukkan bagaimana MCP dapat digunakan untuk mengorkestrasi beberapa agen AI dalam skenario dunia nyata yang siap produksi.
- Mempercepat pengembangan solusi dengan menyediakan pola yang dapat digunakan ulang untuk koordinasi agen, integrasi data, dan penyebaran aman.
- Berfungsi sebagai cetak biru untuk membangun aplikasi bertenaga AI spesifik domain menggunakan MCP dan layanan Azure.

## Referensi
- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.