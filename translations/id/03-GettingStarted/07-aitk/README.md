# Menggunakan server dari ekstensi AI Toolkit untuk Visual Studio Code

Ketika Anda membangun agen AI, ini bukan hanya tentang menghasilkan respons cerdas; ini juga tentang memberi agen Anda kemampuan untuk mengambil tindakan. Di sinilah Model Context Protocol (MCP) berperan. MCP memudahkan agen untuk mengakses alat dan layanan eksternal dengan cara yang konsisten. Anggap saja seperti menghubungkan agen Anda ke kotak alat yang memang *benar-benar* bisa digunakan.

Misalnya, Anda menghubungkan agen ke server MCP kalkulator Anda. Tiba-tiba, agen Anda bisa melakukan operasi matematika hanya dengan menerima perintah seperti "Berapa 47 kali 89?" — tanpa perlu mengkodekan logika secara keras atau membuat API khusus.

## Gambaran Umum

Pelajaran ini menjelaskan cara menghubungkan server MCP kalkulator ke agen dengan ekstensi [AI Toolkit](https://aka.ms/AIToolkit) di Visual Studio Code, memungkinkan agen Anda melakukan operasi matematika seperti penjumlahan, pengurangan, perkalian, dan pembagian melalui bahasa alami.

AI Toolkit adalah ekstensi kuat untuk Visual Studio Code yang mempermudah pengembangan agen. Insinyur AI dapat dengan mudah membangun aplikasi AI dengan mengembangkan dan menguji model AI generatif—secara lokal atau di cloud. Ekstensi ini mendukung sebagian besar model generatif utama yang tersedia saat ini.

*Catatan*: AI Toolkit saat ini mendukung Python dan TypeScript.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Menggunakan server MCP melalui AI Toolkit.
- Mengkonfigurasi konfigurasi agen untuk memungkinkannya menemukan dan menggunakan alat yang disediakan oleh server MCP.
- Memanfaatkan alat MCP melalui bahasa alami.

## Pendekatan

Berikut adalah cara kita perlu mendekatinya secara garis besar:

- Membuat agen dan mendefinisikan prompt sistemnya.
- Membuat server MCP dengan alat kalkulator.
- Menghubungkan Pembuat Agen ke server MCP.
- Menguji pemanggilan alat agen melalui bahasa alami.

Bagus, sekarang setelah kita memahami alurnya, mari kita konfigurasikan agen AI untuk memanfaatkan alat eksternal melalui MCP, meningkatkan kemampuannya!

## Prasyarat

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit untuk Visual Studio Code](https://aka.ms/AIToolkit)

## Latihan: Menggunakan server

> [!WARNING]
> Catatan untuk pengguna macOS. Kami sedang menyelidiki masalah yang memengaruhi instalasi dependensi di macOS. Akibatnya, pengguna macOS tidak dapat menyelesaikan tutorial ini saat ini. Kami akan memperbarui instruksi segera setelah perbaikan tersedia. Terima kasih atas kesabaran dan pengertian Anda!

Dalam latihan ini, Anda akan membangun, menjalankan, dan meningkatkan agen AI dengan alat dari server MCP di dalam Visual Studio Code menggunakan AI Toolkit.

### -0- Langkah awal, tambahkan model OpenAI GPT-4o ke My Models

Latihan ini menggunakan model **GPT-4o**. Model tersebut harus ditambahkan ke **My Models** sebelum membuat agen.

![Screenshot antarmuka pemilihan model di ekstensi AI Toolkit Visual Studio Code. Judul bertuliskan "Find the right model for your AI Solution" dengan subjudul yang mendorong pengguna untuk menemukan, menguji, dan menerapkan model AI. Di bawahnya, di bawah “Popular Models,” ada enam kartu model yang ditampilkan: DeepSeek-R1 (dihosting GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), dan DeepSeek-R1 (dihosting Ollama). Setiap kartu mencakup opsi untuk “Add” model atau “Try in Playground](../../../../translated_images/id/aitk-model-catalog.2acd38953bb9c119.webp)

1. Buka ekstensi **AI Toolkit** dari **Activity Bar**.
1. Di bagian **Catalog**, pilih **Models** untuk membuka **Model Catalog**. Memilih **Models** membuka **Model Catalog** di tab editor baru.
1. Di bilah pencarian **Model Catalog**, masukkan **OpenAI GPT-4o**.
1. Klik **+ Add** untuk menambahkan model ke daftar **My Models** Anda. Pastikan Anda memilih model yang **Dihosting oleh GitHub**.
1. Di **Activity Bar**, pastikan model **OpenAI GPT-4o** muncul dalam daftar.

### -1- Membuat agen

**Agent (Prompt) Builder** memungkinkan Anda membuat dan menyesuaikan agen bertenaga AI Anda sendiri. Pada bagian ini, Anda akan membuat agen baru dan menetapkan model untuk mendukung percakapan.

![Screenshot antarmuka pembuat "Calculator Agent" di ekstensi AI Toolkit untuk Visual Studio Code. Panel kiri menampilkan model yang dipilih "OpenAI GPT-4o (via GitHub)." Prompt sistem berbunyi "You are a professor in university teaching math," dan prompt pengguna berkata, "Explain to me the Fourier equation in simple terms." Opsi tambahan termasuk tombol untuk menambah alat, mengaktifkan MCP Server, dan memilih output terstruktur. Tombol biru “Run” ada di bagian bawah. Panel kanan, di bawah "Get Started with Examples," daftar tiga agen sampel: Web Developer (dengan MCP Server, Second-Grade Simplifier, dan Dream Interpreter, masing-masing dengan deskripsi singkat tentang fungsi mereka.](../../../../translated_images/id/aitk-agent-builder.901e3a2960c3e477.webp)

1. Buka ekstensi **AI Toolkit** dari **Activity Bar**.
1. Di bagian **Tools**, pilih **Agent (Prompt) Builder**. Memilih **Agent (Prompt) Builder** membuka **Agent (Prompt) Builder** di tab editor baru.
1. Klik tombol **+ New Agent**. Ekstensi akan membuka wizard pengaturan melalui **Command Palette**.
1. Masukkan nama **Calculator Agent** dan tekan **Enter**.
1. Di **Agent (Prompt) Builder**, untuk kolom **Model**, pilih model **OpenAI GPT-4o (via GitHub)**.

### -2- Membuat prompt sistem untuk agen

Dengan agen sudah dibuat, saatnya mendefinisikan kepribadian dan tujuannya. Di bagian ini, Anda akan menggunakan fitur **Generate system prompt** untuk menggambarkan perilaku yang diinginkan agen—dalam hal ini, agen kalkulator—dan membiarkan model menulis prompt sistem untuk Anda.

![Screenshot antarmuka "Calculator Agent" di AI Toolkit untuk Visual Studio Code dengan jendela modal terbuka berjudul "Generate a prompt." Modal menjelaskan bahwa template prompt dapat dihasilkan dengan berbagi detail dasar dan termasuk kotak teks dengan contoh prompt sistem: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Di bawah kotak teks ada tombol "Close" dan "Generate". Di latar belakang, bagian konfigurasi agen terlihat termasuk model "OpenAI GPT-4o (via GitHub)" yang dipilih dan kolom untuk prompt sistem dan pengguna.](../../../../translated_images/id/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Untuk bagian **Prompts**, klik tombol **Generate system prompt**. Tombol ini membuka pembangun prompt yang memanfaatkan AI untuk menghasilkan prompt sistem untuk agen.
1. Di jendela **Generate a prompt**, masukkan teks berikut: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. Klik tombol **Generate**. Notifikasi akan muncul di pojok kanan bawah yang mengonfirmasi bahwa prompt sistem sedang dibuat. Setelah proses pembuatan prompt selesai, prompt akan muncul di kolom **System prompt** dari **Agent (Prompt) Builder**.
1. Tinjau **System prompt** dan modifikasi jika perlu.

### -3- Membuat server MCP

Sekarang setelah Anda mendefinisikan prompt sistem agen Anda—yang memandu perilaku dan responsnya—saatnya untuk membekali agen dengan kemampuan praktis. Di bagian ini, Anda akan membuat server MCP kalkulator dengan alat untuk melakukan perhitungan penjumlahan, pengurangan, perkalian, dan pembagian. Server ini akan memungkinkan agen Anda melakukan operasi matematika secara waktu nyata sebagai respons terhadap prompt bahasa alami.

!["Screenshot bagian bawah antarmuka Calculator Agent di ekstensi AI Toolkit untuk Visual Studio Code. Menampilkan menu dapat diperluas untuk “Tools” dan “Structure output,” serta menu dropdown berlabel “Choose output format” yang disetel ke “text.” Di sebelah kanan ada tombol bertuliskan “+ MCP Server” untuk menambah server Model Context Protocol. Tampilkan ikon placeholder gambar di atas bagian Tools.](../../../../translated_images/id/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit dilengkapi dengan template untuk memudahkan pembuatan server MCP Anda sendiri. Kita akan menggunakan template Python untuk membuat server MCP kalkulator.

*Catatan*: AI Toolkit saat ini mendukung Python dan TypeScript.

1. Di bagian **Tools** dari **Agent (Prompt) Builder**, klik tombol **+ MCP Server**. Ekstensi akan membuka wizard pengaturan melalui **Command Palette**.
1. Pilih **+ Add Server**.
1. Pilih **Create a New MCP Server**.
1. Pilih template **python-weather**.
1. Pilih **Default folder** untuk menyimpan template server MCP.
1. Masukkan nama berikut untuk server: **Calculator**
1. Jendela Visual Studio Code baru akan terbuka. Pilih **Yes, I trust the authors**.
1. Menggunakan terminal (**Terminal** > **New Terminal**), buat lingkungan virtual: `python -m venv .venv`
1. Menggunakan terminal, aktifkan lingkungan virtual:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Menggunakan terminal, instal dependensi: `pip install -e .[dev]`
1. Di tampilan **Explorer** pada **Activity Bar**, perluas direktori **src** dan pilih **server.py** untuk membuka file di editor.
1. Ganti kode di file **server.py** dengan berikut ini dan simpan:

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- Menjalankan agen dengan server MCP kalkulator

Sekarang agen Anda memiliki alat, saatnya menggunakannya! Di bagian ini, Anda akan mengajukan prompt ke agen untuk menguji dan memvalidasi apakah agen menggunakan alat yang sesuai dari server MCP kalkulator.

![Screenshot antarmuka Calculator Agent di ekstensi AI Toolkit untuk Visual Studio Code. Di panel kiri, di bawah “Tools,” sebuah server MCP bernama local-server-calculator_server ditambahkan, menampilkan empat alat yang tersedia: add, subtract, multiply, dan divide. Lencana menunjukkan bahwa empat alat aktif. Di bawahnya adalah bagian “Structure output” yang diperkecil dan tombol biru “Run.” Di panel kanan, di bawah “Model Response,” agen memanggil alat multiply dan subtract dengan input {"a": 3, "b": 25} dan {"a": 75, "b": 20} masing-masing. “Tool Response” terakhir ditampilkan sebagai 75.0. Tombol “View Code” muncul di bagian bawah.](../../../../translated_images/id/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Anda akan menjalankan server MCP kalkulator di mesin pengembangan lokal Anda melalui **Agent Builder** sebagai klien MCP.

1. Tekan `F5` untuk memulai debug server MCP. **Agent (Prompt) Builder** akan terbuka di tab editor baru. Status server terlihat di terminal.
1. Di kolom **User prompt** pada **Agent (Prompt) Builder**, masukkan prompt berikut: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Klik tombol **Run** untuk menghasilkan respons agen.
1. Tinjau output agen. Model harus menyimpulkan bahwa Anda membayar **$55**.
1. Berikut ini adalah rincian apa yang seharusnya terjadi:
    - Agen memilih alat **multiply** dan **subtract** untuk membantu perhitungan.
    - Nilai `a` dan `b` yang sesuai ditetapkan untuk alat **multiply**.
    - Nilai `a` dan `b` yang sesuai ditetapkan untuk alat **subtract**.
    - Respons dari setiap alat diberikan pada **Tool Response** masing-masing.
    - Output akhir dari model diberikan pada **Model Response** akhir.
1. Kirimkan prompt tambahan untuk menguji agen lebih lanjut. Anda dapat memodifikasi prompt yang ada di kolom **User prompt** dengan mengklik ke dalam kolom dan mengganti prompt yang ada.
1. Setelah selesai menguji agen, Anda dapat menghentikan server melalui **terminal** dengan menekan **CTRL/CMD+C** untuk keluar.

## Tugas

Cobalah menambahkan entri alat tambahan ke file **server.py** Anda (misalnya: mengembalikan akar kuadrat dari sebuah angka). Kirimkan prompt tambahan yang mengharuskan agen memanfaatkan alat baru Anda (atau alat yang sudah ada). Pastikan untuk me-restart server agar alat baru dimuat.

## Solusi

[Solusi](./solution/README.md)

## Poin Penting

Poin penting dari bab ini adalah sebagai berikut:

- Ekstensi AI Toolkit adalah klien hebat yang memungkinkan Anda menggunakan Server MCP dan alat-alatnya.
- Anda dapat menambahkan alat baru ke server MCP, memperluas kemampuan agen untuk memenuhi kebutuhan yang terus berkembang.
- AI Toolkit mencakup template (misalnya, template server MCP Python) untuk mempermudah pembuatan alat kustom.

## Sumber Daya Tambahan

- [Dokumentasi AI Toolkit](https://aka.ms/AIToolkit/doc)

## Selanjutnya
- Berikutnya: [Testing & Debugging](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->