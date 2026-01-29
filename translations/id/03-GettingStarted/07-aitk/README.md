# Menggunakan Server dari Ekstensi AI Toolkit untuk Visual Studio Code

Ketika Anda membangun agen AI, tujuannya bukan hanya menghasilkan respons cerdas, tetapi juga memberikan kemampuan kepada agen untuk mengambil tindakan. Di sinilah Model Context Protocol (MCP) berperan. MCP memudahkan agen untuk mengakses alat dan layanan eksternal dengan cara yang konsisten. Anggap saja seperti menyambungkan agen Anda ke kotak peralatan yang benar-benar bisa digunakan.

Misalnya, Anda menghubungkan agen ke server MCP kalkulator Anda. Tiba-tiba, agen Anda dapat melakukan operasi matematika hanya dengan menerima perintah seperti "Berapa hasil 47 kali 89?"—tanpa perlu menulis logika secara manual atau membangun API khusus.

## Gambaran Umum

Pelajaran ini membahas cara menghubungkan server MCP kalkulator ke agen menggunakan ekstensi [AI Toolkit](https://aka.ms/AIToolkit) di Visual Studio Code, memungkinkan agen Anda melakukan operasi matematika seperti penjumlahan, pengurangan, perkalian, dan pembagian melalui bahasa alami.

AI Toolkit adalah ekstensi yang kuat untuk Visual Studio Code yang menyederhanakan pengembangan agen. Insinyur AI dapat dengan mudah membangun aplikasi AI dengan mengembangkan dan menguji model AI generatif—secara lokal atau di cloud. Ekstensi ini mendukung sebagian besar model generatif utama yang tersedia saat ini.

*Catatan*: AI Toolkit saat ini mendukung Python dan TypeScript.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Menggunakan server MCP melalui AI Toolkit.
- Mengonfigurasi agen agar dapat menemukan dan menggunakan alat yang disediakan oleh server MCP.
- Menggunakan alat MCP melalui bahasa alami.

## Pendekatan

Berikut adalah pendekatan yang perlu kita lakukan secara garis besar:

- Membuat agen dan mendefinisikan prompt sistemnya.
- Membuat server MCP dengan alat kalkulator.
- Menghubungkan Agent Builder ke server MCP.
- Menguji pemanggilan alat agen melalui bahasa alami.

Bagus, sekarang setelah kita memahami alurnya, mari kita konfigurasikan agen AI untuk memanfaatkan alat eksternal melalui MCP, meningkatkan kemampuannya!

## Prasyarat

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit untuk Visual Studio Code](https://aka.ms/AIToolkit)

## Latihan: Menggunakan Server

> [!WARNING]
> Catatan untuk Pengguna macOS. Kami saat ini sedang menyelidiki masalah yang memengaruhi instalasi dependensi di macOS. Akibatnya, pengguna macOS tidak dapat menyelesaikan tutorial ini untuk saat ini. Kami akan memperbarui instruksi segera setelah perbaikan tersedia. Terima kasih atas kesabaran dan pengertian Anda!

Dalam latihan ini, Anda akan membangun, menjalankan, dan meningkatkan agen AI dengan alat dari server MCP di dalam Visual Studio Code menggunakan AI Toolkit.

### -0- Langkah Awal, tambahkan model OpenAI GPT-4o ke My Models

Latihan ini menggunakan model **GPT-4o**. Model ini harus ditambahkan ke **My Models** sebelum membuat agen.

1. Buka ekstensi **AI Toolkit** dari **Activity Bar**.
1. Di bagian **Catalog**, pilih **Models** untuk membuka **Model Catalog**. Memilih **Models** akan membuka **Model Catalog** di tab editor baru.
1. Di bilah pencarian **Model Catalog**, masukkan **OpenAI GPT-4o**.
1. Klik **+ Add** untuk menambahkan model ke daftar **My Models** Anda. Pastikan Anda memilih model yang **Hosted by GitHub**.
1. Di **Activity Bar**, pastikan model **OpenAI GPT-4o** muncul di daftar.

### -1- Membuat Agen

**Agent (Prompt) Builder** memungkinkan Anda membuat dan menyesuaikan agen bertenaga AI Anda sendiri. Di bagian ini, Anda akan membuat agen baru dan menetapkan model untuk mendukung percakapan.

1. Buka ekstensi **AI Toolkit** dari **Activity Bar**.
1. Di bagian **Tools**, pilih **Agent (Prompt) Builder**. Memilih **Agent (Prompt) Builder** akan membuka **Agent (Prompt) Builder** di tab editor baru.
1. Klik tombol **+ New Agent**. Ekstensi akan meluncurkan wizard pengaturan melalui **Command Palette**.
1. Masukkan nama **Calculator Agent** dan tekan **Enter**.
1. Di **Agent (Prompt) Builder**, untuk bidang **Model**, pilih model **OpenAI GPT-4o (via GitHub)**.

### -2- Membuat Prompt Sistem untuk Agen

Setelah agen dibuat, saatnya mendefinisikan kepribadian dan tujuannya. Di bagian ini, Anda akan menggunakan fitur **Generate system prompt** untuk mendeskripsikan perilaku yang diinginkan dari agen—dalam hal ini, agen kalkulator—dan meminta model menulis prompt sistem untuk Anda.

1. Untuk bagian **Prompts**, klik tombol **Generate system prompt**. Tombol ini membuka pembuat prompt yang memanfaatkan AI untuk menghasilkan prompt sistem untuk agen.
1. Di jendela **Generate a prompt**, masukkan: `Anda adalah asisten matematika yang membantu dan efisien. Ketika diberikan masalah yang melibatkan aritmatika dasar, Anda merespons dengan hasil yang benar.`
1. Klik tombol **Generate**. Notifikasi akan muncul di sudut kanan bawah yang mengonfirmasi bahwa prompt sistem sedang dibuat. Setelah pembuatan prompt selesai, prompt akan muncul di bidang **System prompt** dari **Agent (Prompt) Builder**.
1. Tinjau **System prompt** dan modifikasi jika diperlukan.

### -3- Membuat Server MCP

Setelah Anda mendefinisikan prompt sistem agen—yang membimbing perilaku dan responsnya—saatnya melengkapi agen dengan kemampuan praktis. Di bagian ini, Anda akan membuat server MCP kalkulator dengan alat untuk melakukan perhitungan penjumlahan, pengurangan, perkalian, dan pembagian. Server ini akan memungkinkan agen Anda melakukan operasi matematika secara real-time sebagai respons terhadap perintah bahasa alami.

AI Toolkit dilengkapi dengan template untuk mempermudah pembuatan server MCP Anda sendiri. Kita akan menggunakan template Python untuk membuat server MCP kalkulator.

*Catatan*: AI Toolkit saat ini mendukung Python dan TypeScript.

1. Di bagian **Tools** dari **Agent (Prompt) Builder**, klik tombol **+ MCP Server**. Ekstensi akan meluncurkan wizard pengaturan melalui **Command Palette**.
1. Pilih **+ Add Server**.
1. Pilih **Create a New MCP Server**.
1. Pilih **python-weather** sebagai template.
1. Pilih **Default folder** untuk menyimpan template server MCP.
1. Masukkan nama berikut untuk server: **Calculator**
1. Jendela Visual Studio Code baru akan terbuka. Pilih **Yes, I trust the authors**.
1. Menggunakan terminal (**Terminal** > **New Terminal**), buat lingkungan virtual: `python -m venv .venv`
1. Menggunakan terminal, aktifkan lingkungan virtual:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Menggunakan terminal, instal dependensi: `pip install -e .[dev]`
1. Di tampilan **Explorer** dari **Activity Bar**, perluas direktori **src** dan pilih **server.py** untuk membuka file di editor.
1. Ganti kode di file **server.py** dengan yang berikut dan simpan:

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

### -4- Menjalankan Agen dengan Server MCP Kalkulator

Sekarang agen Anda memiliki alat, saatnya menggunakannya! Di bagian ini, Anda akan mengirimkan perintah ke agen untuk menguji dan memvalidasi apakah agen menggunakan alat yang sesuai dari server MCP kalkulator.

1. Tekan `F5` untuk memulai debugging server MCP. **Agent (Prompt) Builder** akan terbuka di tab editor baru. Status server terlihat di terminal.
1. Di bidang **User prompt** dari **Agent (Prompt) Builder**, masukkan perintah berikut: `Saya membeli 3 barang seharga $25 masing-masing, lalu menggunakan diskon $20. Berapa yang saya bayar?`
1. Klik tombol **Run** untuk menghasilkan respons agen.
1. Tinjau output agen. Model seharusnya menyimpulkan bahwa Anda membayar **$55**.
1. Berikut adalah rincian yang seharusnya terjadi:
    - Agen memilih alat **multiply** dan **subtract** untuk membantu perhitungan.
    - Nilai `a` dan `b` masing-masing ditetapkan untuk alat **multiply**.
    - Nilai `a` dan `b` masing-masing ditetapkan untuk alat **subtract**.
    - Respons dari setiap alat diberikan di **Tool Response** masing-masing.
    - Output akhir dari model diberikan di **Model Response** akhir.
1. Kirimkan perintah tambahan untuk menguji agen lebih lanjut. Anda dapat memodifikasi perintah yang ada di bidang **User prompt** dengan mengklik bidang tersebut dan mengganti perintah yang ada.
1. Setelah selesai menguji agen, Anda dapat menghentikan server melalui **terminal** dengan memasukkan **CTRL/CMD+C** untuk keluar.

## Tugas

Cobalah menambahkan entri alat tambahan ke file **server.py** Anda (misalnya: mengembalikan akar kuadrat dari sebuah angka). Kirimkan perintah tambahan yang memerlukan agen untuk menggunakan alat baru Anda (atau alat yang sudah ada). Pastikan untuk memulai ulang server untuk memuat alat yang baru ditambahkan.

## Solusi

[Solusi](./solution/README.md)

## Poin Penting

Poin-poin penting dari bab ini adalah sebagai berikut:

- Ekstensi AI Toolkit adalah klien yang hebat yang memungkinkan Anda menggunakan Server MCP dan alat-alatnya.
- Anda dapat menambahkan alat baru ke server MCP, memperluas kemampuan agen untuk memenuhi kebutuhan yang terus berkembang.
- AI Toolkit mencakup template (misalnya, template server MCP Python) untuk menyederhanakan pembuatan alat khusus.

## Sumber Daya Tambahan

- [Dokumentasi AI Toolkit](https://aka.ms/AIToolkit/doc)

## Selanjutnya
- Selanjutnya: [Pengujian & Debugging](../08-testing/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.