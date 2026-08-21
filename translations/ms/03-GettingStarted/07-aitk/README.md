# Menggunakan pelayan dari sambungan AI Toolkit untuk Visual Studio Code

Apabila anda membina agen AI, ia bukan sahaja tentang menjana tindak balas pintar; ia juga tentang memberikan kebolehan kepada agen anda untuk bertindak. Di sinilah Model Context Protocol (MCP) memainkan peranan. MCP memudahkan agen mengakses alat dan perkhidmatan luar dengan cara yang konsisten. Fikirkan ia seperti menyambungkan agen anda ke dalam kotak alat yang boleh ia *betul-betul* gunakan.

Katakan anda menyambungkan agen kepada pelayan MCP kalkulator anda. Tiba-tiba, agen anda boleh melakukan operasi matematik dengan menerima arahan seperti “Berapakah 47 darab 89?”—tidak perlu kod keras atau membina API khusus.

## Gambaran Keseluruhan

Pelajaran ini membincangkan bagaimana menyambungkan pelayan MCP kalkulator ke agen dengan sambungan [AI Toolkit](https://aka.ms/AIToolkit) dalam Visual Studio Code, membolehkan agen anda melakukan operasi matematik seperti tambah, tolak, darab, dan bahagi melalui bahasa semula jadi.

AI Toolkit adalah sambungan berkuasa untuk Visual Studio Code yang mempermudah pembangunan agen. Jurutera AI boleh dengan mudah membina aplikasi AI dengan membangunkan dan menguji model AI generatif—secara tempatan atau di awan. Sambungan ini menyokong kebanyakan model generatif utama yang ada hari ini.

*Nota*: AI Toolkit kini menyokong Python dan TypeScript.

## Objektif Pembelajaran

Pada akhir pelajaran ini, anda akan dapat:

- Menggunakan pelayan MCP melalui AI Toolkit.
- Mengkonfigurasi konfigurasi agen untuk membolehkan ia mengesan dan menggunakan alat yang disediakan oleh pelayan MCP.
- Menggunakan alat MCP melalui bahasa semula jadi.

## Pendekatan

Berikut ialah cara kita perlu mendekati ini pada tahap tinggi:

- Cipta agen dan tetapkan prompt sistemnya.
- Cipta pelayan MCP dengan alat kalkulator.
- Sambungkan Pembina Agen ke pelayan MCP.
- Uji panggilan alat agen melalui bahasa semula jadi.

Bagus, sekarang kita faham alirannya, mari kita konfigurasikan agen AI untuk memanfaatkan alat luar melalui MCP, meningkatkan keupayaannya!

## Prasyarat

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit untuk Visual Studio Code](https://aka.ms/AIToolkit)

## Latihan: Menggunakan pelayan

> [!WARNING]
> Nota untuk Pengguna macOS. Kami sedang menyiasat isu yang menjejaskan pemasangan pergantungan pada macOS. Oleh itu, pengguna macOS tidak dapat menyelesaikan tutorial ini buat masa ini. Kami akan mengemas kini arahan sebaik sahaja pembaikan tersedia. Terima kasih atas kesabaran dan kefahaman anda!

Dalam latihan ini, anda akan membina, menjalankan, dan meningkatkan agen AI dengan alat dari pelayan MCP di dalam Visual Studio Code menggunakan AI Toolkit.

### -0- Langkah awal, tambah model OpenAI GPT-4o ke My Models

Latihan ini menggunakan model **GPT-4o**. Model ini perlu ditambah ke **My Models** sebelum mencipta agen.

![Screenshot antara muka pilihan model dalam sambungan AI Toolkit Visual Studio Code. Tajuk utama berbunyi "Find the right model for your AI Solution" dengan sari kata menggalakkan pengguna untuk menemui, menguji, dan menerapkan model AI. Di bawah, di bawah “Popular Models,” enam kad model dipaparkan: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), dan DeepSeek-R1 (Ollama-hosted). Setiap kad termasuk pilihan untuk “Add” model atau “Try in Playground](../../../../translated_images/ms/aitk-model-catalog.2acd38953bb9c119.webp)

1. Buka sambungan **AI Toolkit** dari **Activity Bar**.
1. Dalam bahagian **Catalog**, pilih **Models** untuk membuka **Model Catalog**. Memilih **Models** membuka **Model Catalog** dalam tab editor baru.
1. Dalam bar carian **Model Catalog**, masukkan **OpenAI GPT-4o**.
1. Klik **+ Add** untuk menambah model ke senarai **My Models** anda. Pastikan anda memilih model yang **Hosted by GitHub**.
1. Dalam **Activity Bar**, sahkan bahawa model **OpenAI GPT-4o** muncul dalam senarai.

### -1- Cipta agen

**Agent (Prompt) Builder** membolehkan anda mencipta dan menyesuaikan agen AI anda sendiri. Dalam bahagian ini, anda akan mencipta agen baru dan menetapkan model untuk menguatkuasakan perbualan.

![Screenshot antara muka pembina "Calculator Agent" dalam sambungan AI Toolkit untuk Visual Studio Code. Pada panel kiri, model yang dipilih ialah "OpenAI GPT-4o (via GitHub)." Prompt sistem membaca "You are a professor in university teaching math," dan prompt pengguna berkata, "Explain to me the Fourier equation in simple terms." Pilihan tambahan termasuk butang untuk menambah alat, mengaktifkan MCP Server, dan memilih output berstruktur. Butang biru “Run” di bawah. Pada panel kanan, di bawah "Get Started with Examples," tiga agen contoh disenaraikan: Web Developer (dengan MCP Server, Second-Grade Simplifier, dan Dream Interpreter, setiap satu dengan deskripsi ringkas fungsi mereka.](../../../../translated_images/ms/aitk-agent-builder.901e3a2960c3e477.webp)

1. Buka sambungan **AI Toolkit** dari **Activity Bar**.
1. Dalam bahagian **Tools**, pilih **Agent (Prompt) Builder**. Memilih **Agent (Prompt) Builder** membuka **Agent (Prompt) Builder** dalam tab editor baru.
1. Klik butang **+ New Agent**. Sambungan akan melancarkan wizard tetapan melalui **Command Palette**.
1. Masukkan nama **Calculator Agent** dan tekan **Enter**.
1. Dalam **Agent (Prompt) Builder**, untuk medan **Model**, pilih model **OpenAI GPT-4o (via GitHub)**.

### -2- Cipta prompt sistem untuk agen

Dengan agen telah disediakan, tiba masa untuk menentukan personaliti dan tujuannya. Dalam bahagian ini, anda akan menggunakan ciri **Generate system prompt** untuk menerangkan tingkah laku yang dikehendaki oleh agen—dalam kes ini, agen kalkulator—dan membuat model menulis prompt sistem untuk anda.

![Screenshot antara muka "Calculator Agent" dalam AI Toolkit untuk Visual Studio Code dengan tetingkap mod al atas bertajuk "Generate a prompt." Mod al menerangkan bahawa templat prompt boleh dijana dengan berkongsi butiran asas dan termasuk kotak teks dengan contoh prompt sistem: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Di bawah kotak teks terdapat butang "Close" dan "Generate." Di latar belakang, sebahagian daripada konfigurasi agen kelihatan, termasuk model terpilih "OpenAI GPT-4o (via GitHub)" dan medan untuk prompt sistem dan pengguna.](../../../../translated_images/ms/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. Untuk bahagian **Prompts**, klik butang **Generate system prompt**. Butang ini membuka pembina prompt yang menggunakan AI untuk menjana prompt sistem untuk agen.
1. Dalam tetingkap **Generate a prompt**, masukkan: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. Klik butang **Generate**. Pemberitahuan akan muncul di penjuru bawah kanan mengesahkan bahawa prompt sistem sedang dijana. Setelah penjanaan selesai, prompt akan muncul di medan **System prompt** dalam **Agent (Prompt) Builder**.
1. Semak **System prompt** dan ubah jika perlu.

### -3- Cipta pelayan MCP

Kini anda telah mentakrifkan prompt sistem agen anda—yang membimbing tingkah laku dan tindak balasnya—tiba masa untuk melengkapkan agen dengan keupayaan praktikal. Dalam bahagian ini, anda akan mencipta pelayan MCP kalkulator dengan alat untuk menjalankan pengiraan tambah, tolak, darab, dan bahagi. Pelayan ini akan membolehkan agen anda melakukan operasi matematik masa nyata sebagai tindak balas kepada arahan bahasa semula jadi.

!["Screenshot bahagian bawah antara muka Calculator Agent dalam sambungan AI Toolkit untuk Visual Studio Code. Ia menunjukkan menu yang boleh dikembangkan untuk “Tools” dan “Structure output,” bersama-sama menu lungsur bertanda “Choose output format” yang diset pada “text.” Di sebelah kanan, terdapat butang bertanda “+ MCP Server” untuk menambah pelayan Model Context Protocol. Tataletak ikon gambar ditunjukkan di atas bahagian Tools.](../../../../translated_images/ms/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit dilengkapi dengan templat untuk memudahkan penciptaan pelayan MCP anda sendiri. Kita akan menggunakan templat Python untuk mencipta pelayan MCP kalkulator.

*Nota*: AI Toolkit kini menyokong Python dan TypeScript.

1. Dalam bahagian **Tools** di **Agent (Prompt) Builder**, klik butang **+ MCP Server**. Sambungan akan melancarkan wizard tetapan melalui **Command Palette**.
1. Pilih **+ Add Server**.
1. Pilih **Create a New MCP Server**.
1. Pilih **python-weather** sebagai templat.
1. Pilih **Default folder** untuk menyimpan templat pelayan MCP.
1. Masukkan nama berikut untuk pelayan itu: **Calculator**
1. Tetingkap Visual Studio Code baru akan dibuka. Pilih **Yes, I trust the authors**.
1. Menggunakan terminal (**Terminal** > **New Terminal**), cipta persekitaran maya: `python -m venv .venv`
1. Menggunakan terminal, aktifkan persekitaran maya:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Menggunakan terminal, pasang pergantungan: `pip install -e .[dev]`
1. Dalam pandangan **Explorer** di **Activity Bar**, kembangkan direktori **src** dan pilih **server.py** untuk membuka fail dalam editor.
1. Gantikan kod dalam fail **server.py** dengan yang berikut dan simpan:

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

### -4- Jalankan agen dengan pelayan MCP kalkulator

Kini agen anda mempunyai alat, tiba masa untuk menggunakannya! Dalam bahagian ini, anda akan menghantar arahan kepada agen untuk menguji dan mengesahkan sama ada agen menggunakan alat yang sesuai dari pelayan MCP kalkulator.

![Screenshot antara muka Calculator Agent dalam sambungan AI Toolkit untuk Visual Studio Code. Pada panel kiri, di bawah “Tools,” pelayan MCP bernama local-server-calculator_server ditambah, menunjukkan empat alat tersedia: add, subtract, multiply, dan divide. Lencana menunjukkan bahawa empat alat aktif. Di bawah ialah bahagian “Structure output” yang diruntuhkan dan butang biru “Run.” Pada panel kanan, di bawah “Model Response,” agen memanggil alat multiply dan subtract dengan input {"a": 3, "b": 25} dan {"a": 75, "b": 20} masing-masing. “Tool Response” akhir ditunjukkan sebagai 75.0. Butang “View Code” muncul di bahagian bawah.](../../../../translated_images/ms/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Anda akan menjalankan pelayan MCP kalkulator pada mesin pembangunan tempatan anda melalui **Agent Builder** sebagai klien MCP.

1. Tekan `F5` untuk mula debug pelayan MCP. **Agent (Prompt) Builder** akan dibuka dalam tab editor baru. Status pelayan kelihatan di terminal.
1. Dalam medan **User prompt** **Agent (Prompt) Builder**, masukkan arahan berikut: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Klik butang **Run** untuk menjana tindak balas agen.
1. Semak output agen. Model sepatutnya membuat kesimpulan bahawa anda membayar **$55**.
1. Berikut pecahan apa yang sepatutnya berlaku:
    - Agen memilih alat **multiply** dan **subtract** untuk membantu pengiraan.
    - Nilai `a` dan `b` masing-masing ditetapkan untuk alat **multiply**.
    - Nilai `a` dan `b` masing-masing ditetapkan untuk alat **subtract**.
    - Tindak balas dari setiap alat diberi dalam **Tool Response** masing-masing.
    - Output akhir dari model diberikan dalam **Model Response** akhir.
1. Hantar arahan tambahan untuk menguji lebih lanjut agen. Anda boleh mengubah arahan sedia ada dalam medan **User prompt** dengan mengklik medan tersebut dan menggantikan arahan yang ada.
1. Setelah selesai menguji agen, anda boleh menghentikan pelayan melalui **terminal** dengan menekan **CTRL/CMD+C** untuk keluar.

## Tugasan

Cuba tambah entri alat tambahan ke fail **server.py** anda (contoh: kembalikan punca kuasa dua bagi sesuatu nombor). Hantar arahan tambahan yang memerlukan agen menggunakan alat baru anda (atau alat sedia ada). Pastikan anda mulakan semula pelayan untuk memuatkan alat yang baru ditambah.

## Penyelesaian

[Penyelesaian](./solution/README.md)

## Kajian Utama

Kajian utama dari bab ini adalah seperti berikut:

- Sambungan AI Toolkit adalah klien yang hebat yang membolehkan anda menggunakan Pelayan MCP dan alatnya.
- Anda boleh menambah alat baru ke pelayan MCP, meluaskan keupayaan agen untuk memenuhi keperluan yang berkembang.
- AI Toolkit menyertakan templat (contohnya, templat pelayan MCP Python) untuk memudahkan penciptaan alat tersuai.

## Sumber Tambahan

- [Dokumen AI Toolkit](https://aka.ms/AIToolkit/doc)

## Apa Seterusnya
- Seterusnya: [Ujian & Pengubahsuaian](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->