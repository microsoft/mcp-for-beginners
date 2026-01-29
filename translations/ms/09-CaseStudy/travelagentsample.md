# Kajian Kes: Azure AI Travel Agents – Pelaksanaan Rujukan

## Gambaran Keseluruhan

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) adalah penyelesaian rujukan menyeluruh yang dibangunkan oleh Microsoft yang menunjukkan cara membina aplikasi perancangan perjalanan berkuasa AI dengan pelbagai ejen menggunakan Model Context Protocol (MCP), Azure OpenAI, dan Azure AI Search. Projek ini mempamerkan amalan terbaik untuk mengatur pelbagai ejen AI, mengintegrasikan data perusahaan, dan menyediakan platform yang selamat serta boleh dikembangkan untuk senario dunia sebenar.

## Ciri-ciri Utama
- **Pengurusan Pelbagai Ejen:** Menggunakan MCP untuk menyelaraskan ejen khusus (contohnya, ejen penerbangan, hotel, dan jadual perjalanan) yang bekerjasama untuk melaksanakan tugasan perancangan perjalanan yang kompleks.
- **Integrasi Data Perusahaan:** Berhubung dengan Azure AI Search dan sumber data perusahaan lain untuk menyediakan maklumat terkini dan relevan bagi cadangan perjalanan.
- **Seni Bina Selamat dan Boleh Skala:** Memanfaatkan perkhidmatan Azure untuk pengesahan, kebenaran, dan penyebaran yang boleh diskalakan, mengikut amalan keselamatan perusahaan terbaik.
- **Alat Boleh Dikembangkan:** Melaksanakan alat MCP yang boleh digunakan semula dan templat arahan, membolehkan penyesuaian pantas kepada domain atau keperluan perniagaan baru.
- **Pengalaman Pengguna:** Menyediakan antara muka perbualan untuk pengguna berinteraksi dengan ejen perjalanan, dikuasakan oleh Azure OpenAI dan MCP.

## Seni Bina
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Penerangan Rajah Seni Bina

Penyelesaian Azure AI Travel Agents direka untuk modulariti, kebolehsuaian, dan integrasi selamat pelbagai ejen AI serta sumber data perusahaan. Komponen utama dan aliran data adalah seperti berikut:

- **Antara Muka Pengguna:** Pengguna berinteraksi dengan sistem melalui UI perbualan (seperti chat web atau bot Teams), yang menghantar pertanyaan pengguna dan menerima cadangan perjalanan.
- **MCP Server:** Berfungsi sebagai pengatur pusat, menerima input pengguna, mengurus konteks, dan menyelaraskan tindakan ejen khusus (contohnya, FlightAgent, HotelAgent, ItineraryAgent) melalui Model Context Protocol.
- **Ejen AI:** Setiap ejen bertanggungjawab untuk domain tertentu (penerbangan, hotel, jadual perjalanan) dan dilaksanakan sebagai alat MCP. Ejen menggunakan templat arahan dan logik untuk memproses permintaan dan menghasilkan respons.
- **Azure OpenAI Service:** Menyediakan kefahaman dan penjanaan bahasa semula jadi yang canggih, membolehkan ejen mentafsir niat pengguna dan menghasilkan respons perbualan.
- **Azure AI Search & Data Perusahaan:** Ejen membuat pertanyaan kepada Azure AI Search dan sumber data perusahaan lain untuk mendapatkan maklumat terkini mengenai penerbangan, hotel, dan pilihan perjalanan.
- **Pengesahan & Keselamatan:** Berintegrasi dengan Microsoft Entra ID untuk pengesahan selamat dan menggunakan kawalan akses keistimewaan minimum ke atas semua sumber.
- **Penyebaran:** Direka untuk penyebaran pada Azure Container Apps, memastikan kebolehsuaian, pemantauan, dan kecekapan operasi.

Seni bina ini membolehkan pengurusan lancar pelbagai ejen AI, integrasi selamat dengan data perusahaan, dan platform yang kukuh serta boleh dikembangkan untuk membina penyelesaian AI khusus domain.

## Penjelasan Langkah demi Langkah Rajah Seni Bina
Bayangkan merancang perjalanan besar dan mempunyai pasukan pembantu pakar yang membantu anda dengan setiap butiran. Sistem Azure AI Travel Agents berfungsi dengan cara yang sama, menggunakan bahagian berbeza (seperti ahli pasukan) yang masing-masing mempunyai tugas khusus. Berikut adalah bagaimana semuanya bersatu:

### Antara Muka Pengguna (UI):
Fikirkan ini sebagai kaunter hadapan ejen perjalanan anda. Di sinilah anda (pengguna) mengemukakan soalan atau membuat permintaan, seperti “Cari penerbangan ke Paris.” Ini boleh menjadi tetingkap chat di laman web atau aplikasi mesej.

### MCP Server (Pengaturcara):
MCP Server adalah seperti pengurus yang mendengar permintaan anda di kaunter hadapan dan memutuskan pakar mana yang harus mengendalikan setiap bahagian. Ia menjejaki perbualan anda dan memastikan semuanya berjalan lancar.

### Ejen AI (Pembantu Pakar):
Setiap ejen adalah pakar dalam bidang tertentu—satu tahu semua tentang penerbangan, satu lagi tentang hotel, dan satu lagi tentang merancang jadual perjalanan anda. Apabila anda membuat permintaan perjalanan, MCP Server menghantar permintaan anda kepada ejen yang sesuai. Ejen ini menggunakan pengetahuan dan alat mereka untuk mencari pilihan terbaik untuk anda.

### Azure OpenAI Service (Pakar Bahasa):
Ini seperti mempunyai pakar bahasa yang memahami dengan tepat apa yang anda minta, tidak kira bagaimana anda menyatakannya. Ia membantu ejen memahami permintaan anda dan memberi respons dalam bahasa perbualan yang semula jadi.

### Azure AI Search & Data Perusahaan (Perpustakaan Maklumat):
Bayangkan sebuah perpustakaan besar dan terkini dengan semua maklumat perjalanan terkini—jadual penerbangan, ketersediaan hotel, dan banyak lagi. Ejen mencari perpustakaan ini untuk mendapatkan jawapan paling tepat untuk anda.

### Pengesahan & Keselamatan (Pengawal Keselamatan):
Seperti pengawal keselamatan yang memeriksa siapa yang boleh masuk ke kawasan tertentu, bahagian ini memastikan hanya orang dan ejen yang dibenarkan boleh mengakses maklumat sensitif. Ia menjaga data anda selamat dan peribadi.

### Penyebaran pada Azure Container Apps (Bangunan):
Semua pembantu dan alat ini bekerja bersama dalam sebuah bangunan yang selamat dan boleh diskalakan (awan). Ini bermakna sistem boleh mengendalikan ramai pengguna serentak dan sentiasa tersedia apabila anda memerlukannya.

## Cara semuanya berfungsi bersama:

Anda mula dengan mengemukakan soalan di kaunter hadapan (UI).  
Pengurus (MCP Server) menentukan pakar (ejen) yang akan membantu anda.  
Pakar menggunakan pakar bahasa (OpenAI) untuk memahami permintaan anda dan perpustakaan (AI Search) untuk mencari jawapan terbaik.  
Pengawal keselamatan (Pengesahan) memastikan semuanya selamat.  
Semua ini berlaku dalam bangunan yang boleh dipercayai dan boleh diskalakan (Azure Container Apps), supaya pengalaman anda lancar dan selamat.  
Kerjasama ini membolehkan sistem membantu anda merancang perjalanan dengan cepat dan selamat, seperti pasukan ejen perjalanan pakar yang bekerja bersama dalam pejabat moden!

## Pelaksanaan Teknikal
- **MCP Server:** Menempatkan logik pengurusan teras, mendedahkan alat ejen, dan mengurus konteks untuk aliran kerja perancangan perjalanan berbilang langkah.
- **Ejen:** Setiap ejen (contohnya, FlightAgent, HotelAgent) dilaksanakan sebagai alat MCP dengan templat arahan dan logik tersendiri.
- **Integrasi Azure:** Menggunakan Azure OpenAI untuk kefahaman bahasa semula jadi dan Azure AI Search untuk pengambilan data.
- **Keselamatan:** Berintegrasi dengan Microsoft Entra ID untuk pengesahan dan menggunakan kawalan akses keistimewaan minimum ke atas semua sumber.
- **Penyebaran:** Menyokong penyebaran ke Azure Container Apps untuk kebolehsuaian dan kecekapan operasi.

## Keputusan dan Impak
- Menunjukkan bagaimana MCP boleh digunakan untuk mengatur pelbagai ejen AI dalam senario dunia sebenar yang berskala pengeluaran.
- Mempercepat pembangunan penyelesaian dengan menyediakan corak boleh guna semula untuk penyelarasan ejen, integrasi data, dan penyebaran selamat.
- Berfungsi sebagai cetak biru untuk membina aplikasi berkuasa AI khusus domain menggunakan MCP dan perkhidmatan Azure.

## Rujukan
- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.