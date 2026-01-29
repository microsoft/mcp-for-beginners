# Menggunakan pelayan dari sambungan AI Toolkit untuk Visual Studio Code

Apabila anda membina agen AI, ia bukan hanya tentang menghasilkan respons pintar; ia juga tentang memberikan keupayaan kepada agen anda untuk mengambil tindakan. Di sinilah Model Context Protocol (MCP) memainkan peranan. MCP memudahkan agen untuk mengakses alat dan perkhidmatan luaran dengan cara yang konsisten. Anggap ia seperti menyambungkan agen anda kepada kotak alat yang boleh *benar-benar* digunakan.

Sebagai contoh, katakan anda menyambungkan agen kepada pelayan MCP kalkulator anda. Tiba-tiba, agen anda boleh melakukan operasi matematik hanya dengan menerima arahan seperti "Berapakah 47 kali 89?"—tanpa perlu menulis logik secara manual atau membina API tersuai.

## Gambaran Keseluruhan

Pelajaran ini merangkumi cara menyambungkan pelayan MCP kalkulator kepada agen menggunakan sambungan [AI Toolkit](https://aka.ms/AIToolkit) dalam Visual Studio Code, membolehkan agen anda melakukan operasi matematik seperti penambahan, penolakan, pendaraban, dan pembahagian melalui bahasa semula jadi.

AI Toolkit adalah sambungan yang berkuasa untuk Visual Studio Code yang mempermudah pembangunan agen. Jurutera AI boleh dengan mudah membina aplikasi AI dengan membangunkan dan menguji model AI generatif—secara tempatan atau di awan. Sambungan ini menyokong kebanyakan model generatif utama yang tersedia hari ini.

*Nota*: AI Toolkit kini menyokong Python dan TypeScript.

## Objektif Pembelajaran

Pada akhir pelajaran ini, anda akan dapat:

- Menggunakan pelayan MCP melalui AI Toolkit.
- Mengkonfigurasi tetapan agen untuk membolehkan ia menemui dan menggunakan alat yang disediakan oleh pelayan MCP.
- Menggunakan alat MCP melalui bahasa semula jadi.

## Pendekatan

Berikut adalah pendekatan yang perlu kita ambil secara keseluruhan:

- Cipta agen dan tentukan arahan sistemnya.
- Cipta pelayan MCP dengan alat kalkulator.
- Sambungkan Agent Builder kepada pelayan MCP.
- Uji penggunaan alat agen melalui bahasa semula jadi.

Bagus, sekarang kita memahami alirannya, mari kita konfigurasikan agen AI untuk memanfaatkan alat luaran melalui MCP, meningkatkan keupayaannya!

## Prasyarat

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit untuk Visual Studio Code](https://aka.ms/AIToolkit)

## Latihan: Menggunakan pelayan

> [!WARNING]
> Nota untuk Pengguna macOS. Kami sedang menyiasat isu yang menjejaskan pemasangan kebergantungan pada macOS. Akibatnya, pengguna macOS tidak dapat menyelesaikan tutorial ini buat masa ini. Kami akan mengemas kini arahan sebaik sahaja penyelesaian tersedia. Terima kasih atas kesabaran dan pemahaman anda!

Dalam latihan ini, anda akan membina, menjalankan, dan meningkatkan agen AI dengan alat dari pelayan MCP di dalam Visual Studio Code menggunakan AI Toolkit.

### -0- Langkah awal, tambahkan model OpenAI GPT-4o ke My Models

Latihan ini menggunakan model **GPT-4o**. Model ini perlu ditambahkan ke **My Models** sebelum mencipta agen.

1. Buka sambungan **AI Toolkit** dari **Activity Bar**.
1. Dalam bahagian **Catalog**, pilih **Models** untuk membuka **Model Catalog**. Memilih **Models** akan membuka **Model Catalog** dalam tab editor baru.
1. Dalam bar carian **Model Catalog**, masukkan **OpenAI GPT-4o**.
1. Klik **+ Add** untuk menambahkan model ke senarai **My Models** anda. Pastikan anda memilih model yang **Hosted by GitHub**.
1. Dalam **Activity Bar**, pastikan model **OpenAI GPT-4o** muncul dalam senarai.

### -1- Cipta agen

**Agent (Prompt) Builder** membolehkan anda mencipta dan menyesuaikan agen AI anda sendiri. Dalam bahagian ini, anda akan mencipta agen baru dan menetapkan model untuk menggerakkan perbualan.

1. Buka sambungan **AI Toolkit** dari **Activity Bar**.
1. Dalam bahagian **Tools**, pilih **Agent (Prompt) Builder**. Memilih **Agent (Prompt) Builder** akan membuka **Agent (Prompt) Builder** dalam tab editor baru.
1. Klik butang **+ New Agent**. Sambungan akan melancarkan wizard persediaan melalui **Command Palette**.
1. Masukkan nama **Calculator Agent** dan tekan **Enter**.
1. Dalam **Agent (Prompt) Builder**, untuk medan **Model**, pilih model **OpenAI GPT-4o (via GitHub)**.

### -2- Cipta arahan sistem untuk agen

Setelah agen disediakan, tiba masanya untuk menentukan personaliti dan tujuannya. Dalam bahagian ini, anda akan menggunakan ciri **Generate system prompt** untuk menerangkan tingkah laku yang diinginkan untuk agen—dalam kes ini, agen kalkulator—dan membiarkan model menulis arahan sistem untuk anda.

1. Untuk bahagian **Prompts**, klik butang **Generate system prompt**. Butang ini membuka pembina arahan yang menggunakan AI untuk menjana arahan sistem untuk agen.
1. Dalam tetingkap **Generate a prompt**, masukkan: `Anda adalah pembantu matematik yang cekap dan membantu. Apabila diberikan masalah yang melibatkan aritmetik asas, anda memberikan hasil yang betul.`
1. Klik butang **Generate**. Pemberitahuan akan muncul di sudut kanan bawah mengesahkan bahawa arahan sistem sedang dijana. Setelah penjanaan arahan selesai, arahan akan muncul dalam medan **System prompt** di **Agent (Prompt) Builder**.
1. Semak **System prompt** dan ubah jika perlu.

### -3- Cipta pelayan MCP

Setelah anda menentukan arahan sistem agen—membimbing tingkah laku dan responsnya—tiba masanya untuk melengkapkan agen dengan keupayaan praktikal. Dalam bahagian ini, anda akan mencipta pelayan MCP kalkulator dengan alat untuk melaksanakan pengiraan penambahan, penolakan, pendaraban, dan pembahagian. Pelayan ini akan membolehkan agen anda melakukan operasi matematik secara masa nyata sebagai respons kepada arahan bahasa semula jadi.

AI Toolkit dilengkapi dengan templat untuk memudahkan penciptaan pelayan MCP anda sendiri. Kami akan menggunakan templat Python untuk mencipta pelayan MCP kalkulator.

*Nota*: AI Toolkit kini menyokong Python dan TypeScript.

1. Dalam bahagian **Tools** di **Agent (Prompt) Builder**, klik butang **+ MCP Server**. Sambungan akan melancarkan wizard persediaan melalui **Command Palette**.
1. Pilih **+ Add Server**.
1. Pilih **Create a New MCP Server**.
1. Pilih **python-weather** sebagai templat.
1. Pilih **Default folder** untuk menyimpan templat pelayan MCP.
1. Masukkan nama berikut untuk pelayan: **Calculator**
1. Tetingkap Visual Studio Code baru akan dibuka. Pilih **Yes, I trust the authors**.
1. Menggunakan terminal (**Terminal** > **New Terminal**), cipta persekitaran maya: `python -m venv .venv`
1. Menggunakan terminal, aktifkan persekitaran maya:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Menggunakan terminal, pasang kebergantungan: `pip install -e .[dev]`
1. Dalam paparan **Explorer** di **Activity Bar**, kembangkan direktori **src** dan pilih **server.py** untuk membuka fail dalam editor.
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

Sekarang agen anda mempunyai alat, tiba masanya untuk menggunakannya! Dalam bahagian ini, anda akan menghantar arahan kepada agen untuk menguji dan mengesahkan sama ada agen menggunakan alat yang sesuai dari pelayan MCP kalkulator.

Anda akan menjalankan pelayan MCP kalkulator pada mesin pembangunan tempatan anda melalui **Agent Builder** sebagai klien MCP.

1. Tekan `F5` untuk memulakan debugging pelayan MCP. **Agent (Prompt) Builder** akan dibuka dalam tab editor baru. Status pelayan kelihatan dalam terminal.
1. Dalam medan **User prompt** di **Agent (Prompt) Builder**, masukkan arahan berikut: `Saya membeli 3 item berharga $25 setiap satu, dan kemudian menggunakan diskaun $20. Berapakah jumlah yang saya bayar?`
1. Klik butang **Run** untuk menjana respons agen.
1. Semak output agen. Model sepatutnya menyimpulkan bahawa anda membayar **$55**.
1. Berikut adalah pecahan apa yang sepatutnya berlaku:
    - Agen memilih alat **multiply** dan **subtract** untuk membantu dalam pengiraan.
    - Nilai `a` dan `b` masing-masing diberikan untuk alat **multiply**.
    - Nilai `a` dan `b` masing-masing diberikan untuk alat **subtract**.
    - Respons dari setiap alat diberikan dalam **Tool Response** masing-masing.
    - Output akhir dari model diberikan dalam **Model Response** akhir.
1. Hantar arahan tambahan untuk menguji agen lebih lanjut. Anda boleh mengubah arahan yang ada dalam medan **User prompt** dengan mengklik ke dalam medan dan menggantikan arahan yang ada.
1. Setelah selesai menguji agen, anda boleh menghentikan pelayan melalui **terminal** dengan memasukkan **CTRL/CMD+C** untuk keluar.

## Tugasan

Cuba tambahkan entri alat tambahan ke fail **server.py** anda (contohnya: mengembalikan punca kuasa dua nombor). Hantar arahan tambahan yang memerlukan agen menggunakan alat baru anda (atau alat yang sedia ada). Pastikan untuk memulakan semula pelayan untuk memuatkan alat yang baru ditambahkan.

## Penyelesaian

[Penyelesaian](./solution/README.md)

## Poin Penting

Poin penting dari bab ini adalah seperti berikut:

- Sambungan AI Toolkit adalah klien yang hebat yang membolehkan anda menggunakan pelayan MCP dan alatnya.
- Anda boleh menambahkan alat baru ke pelayan MCP, memperluaskan keupayaan agen untuk memenuhi keperluan yang berkembang.
- AI Toolkit termasuk templat (contohnya, templat pelayan MCP Python) untuk mempermudah penciptaan alat tersuai.

## Sumber Tambahan

- [Dokumentasi AI Toolkit](https://aka.ms/AIToolkit/doc)

## Apa Seterusnya
- Seterusnya: [Pengujian & Debugging](../08-testing/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.