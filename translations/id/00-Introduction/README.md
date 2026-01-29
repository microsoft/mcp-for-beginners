# Pengantar Model Context Protocol (MCP): Mengapa Penting untuk Aplikasi AI yang Skalabel

[![Pengantar Model Context Protocol](../../../translated_images/id/01.a467036d886b5fb5b9cf7b39bac0e743b6ca0a4a18a492de90061daaf0cc55f0.png)](https://youtu.be/agBbdiOPLQA)

_(Klik gambar di atas untuk menonton video pelajaran ini)_

Aplikasi AI generatif adalah langkah maju yang luar biasa karena sering kali memungkinkan pengguna berinteraksi dengan aplikasi menggunakan perintah bahasa alami. Namun, seiring dengan meningkatnya waktu dan sumber daya yang diinvestasikan dalam aplikasi semacam itu, Anda ingin memastikan bahwa Anda dapat dengan mudah mengintegrasikan fungsi dan sumber daya sehingga mudah untuk diperluas, aplikasi Anda dapat mendukung lebih dari satu model yang digunakan, dan menangani berbagai kompleksitas model. Singkatnya, membangun aplikasi AI generatif mudah untuk memulai, tetapi seiring pertumbuhannya dan menjadi lebih kompleks, Anda perlu mulai mendefinisikan arsitektur dan kemungkinan besar membutuhkan standar untuk memastikan aplikasi Anda dibangun dengan cara yang konsisten. Di sinilah MCP hadir untuk mengatur segalanya dan menyediakan standar.

---

## **🔍 Apa Itu Model Context Protocol (MCP)?**

**Model Context Protocol (MCP)** adalah **antarmuka terbuka dan terstandar** yang memungkinkan Model Bahasa Besar (LLM) berinteraksi dengan alat eksternal, API, dan sumber data secara mulus. MCP menyediakan arsitektur yang konsisten untuk meningkatkan fungsi model AI di luar data pelatihannya, memungkinkan sistem AI yang lebih cerdas, skalabel, dan responsif.

---

## **🎯 Mengapa Standarisasi dalam AI Penting**

Seiring dengan semakin kompleksnya aplikasi AI generatif, penting untuk mengadopsi standar yang memastikan **skalabilitas, ekstensibilitas, pemeliharaan**, dan **menghindari ketergantungan pada vendor tertentu**. MCP menjawab kebutuhan ini dengan:

- Menyatukan integrasi model-alat
- Mengurangi solusi khusus yang rapuh
- Memungkinkan beberapa model dari berbagai vendor untuk hidup berdampingan dalam satu ekosistem

**Catatan:** Meskipun MCP mengklaim dirinya sebagai standar terbuka, tidak ada rencana untuk menstandarkan MCP melalui badan standar yang ada seperti IEEE, IETF, W3C, ISO, atau badan standar lainnya.

---

## **📚 Tujuan Pembelajaran**

Pada akhir artikel ini, Anda akan dapat:

- Mendefinisikan **Model Context Protocol (MCP)** dan kasus penggunaannya
- Memahami bagaimana MCP menstandarkan komunikasi antara model dan alat
- Mengidentifikasi komponen inti dari arsitektur MCP
- Mengeksplorasi aplikasi nyata MCP dalam konteks perusahaan dan pengembangan

---

## **💡 Mengapa Model Context Protocol (MCP) Menjadi Terobosan**

### **🔗 MCP Mengatasi Fragmentasi dalam Interaksi AI**

Sebelum MCP, integrasi model dengan alat membutuhkan:

- Kode khusus untuk setiap pasangan alat-model
- API yang tidak standar untuk setiap vendor
- Sering terjadi kerusakan akibat pembaruan
- Skalabilitas yang buruk dengan lebih banyak alat

### **✅ Manfaat Standarisasi MCP**

| **Manfaat**              | **Deskripsi**                                                                |
|--------------------------|--------------------------------------------------------------------------------|
| Interoperabilitas        | LLM bekerja secara mulus dengan alat dari berbagai vendor                     |
| Konsistensi              | Perilaku yang seragam di berbagai platform dan alat                           |
| Dapat Digunakan Kembali  | Alat yang dibuat sekali dapat digunakan di berbagai proyek dan sistem         |
| Pengembangan Lebih Cepat | Mengurangi waktu pengembangan dengan antarmuka standar yang siap pakai        |

---

## **🧱 Gambaran Arsitektur MCP Tingkat Tinggi**

MCP mengikuti model **klien-server**, di mana:

- **MCP Host** menjalankan model AI
- **MCP Client** memulai permintaan
- **MCP Server** menyediakan konteks, alat, dan kemampuan

### **Komponen Utama:**

- **Sumber Daya** – Data statis atau dinamis untuk model  
- **Prompt** – Alur kerja yang telah ditentukan untuk generasi terarah  
- **Alat** – Fungsi yang dapat dieksekusi seperti pencarian, perhitungan  
- **Sampling** – Perilaku agen melalui interaksi berulang

---

## Cara Kerja MCP Server

Server MCP beroperasi dengan cara berikut:

- **Alur Permintaan**:
    1. Permintaan dimulai oleh pengguna akhir atau perangkat lunak yang bertindak atas nama mereka.
    2. **MCP Client** mengirimkan permintaan ke **MCP Host**, yang mengelola runtime model AI.
    3. **Model AI** menerima prompt pengguna dan mungkin meminta akses ke alat atau data eksternal melalui satu atau lebih panggilan alat.
    4. **MCP Host**, bukan model secara langsung, berkomunikasi dengan **MCP Server** yang sesuai menggunakan protokol standar.
- **Fungsi MCP Host**:
    - **Registri Alat**: Memelihara katalog alat yang tersedia dan kemampuannya.
    - **Otentikasi**: Memverifikasi izin untuk akses alat.
    - **Pengelola Permintaan**: Memproses permintaan alat yang masuk dari model.
    - **Pemformat Respons**: Menyusun keluaran alat dalam format yang dapat dipahami oleh model.
- **Eksekusi MCP Server**:
    - **MCP Host** mengarahkan panggilan alat ke satu atau lebih **MCP Server**, masing-masing menyediakan fungsi khusus (misalnya, pencarian, perhitungan, kueri basis data).
    - **MCP Server** melakukan operasi masing-masing dan mengembalikan hasil ke **MCP Host** dalam format yang konsisten.
    - **MCP Host** memformat dan menyampaikan hasil ini ke **Model AI**.
- **Penyelesaian Respons**:
    - **Model AI** menggabungkan keluaran alat ke dalam respons akhir.
    - **MCP Host** mengirimkan respons ini kembali ke **MCP Client**, yang menyampaikannya kepada pengguna akhir atau perangkat lunak pemanggil.

```mermaid
---
title: MCP Architecture and Component Interactions
description: A diagram showing the flows of the components in MCP.
---
graph TD
    Client[MCP Client/Application] -->|Sends Request| H[MCP Host]
    H -->|Invokes| A[AI Model]
    A -->|Tool Call Request| H
    H -->|MCP Protocol| T1[MCP Server Tool 01: Web Search]
    H -->|MCP Protocol| T2[MCP Server Tool 02: Calculator tool]
    H -->|MCP Protocol| T3[MCP Server Tool 03: Database Access tool]
    H -->|MCP Protocol| T4[MCP Server Tool 04: File System tool]
    H -->|Sends Response| Client

    subgraph "MCP Host Components"
        H
        G[Tool Registry]
        I[Authentication]
        J[Request Handler]
        K[Response Formatter]
    end

    H <--> G
    H <--> I
    H <--> J
    H <--> K

    style A fill:#f9d5e5,stroke:#333,stroke-width:2px
    style H fill:#eeeeee,stroke:#333,stroke-width:2px
    style Client fill:#d5e8f9,stroke:#333,stroke-width:2px
    style G fill:#fffbe6,stroke:#333,stroke-width:1px
    style I fill:#fffbe6,stroke:#333,stroke-width:1px
    style J fill:#fffbe6,stroke:#333,stroke-width:1px
    style K fill:#fffbe6,stroke:#333,stroke-width:1px
    style T1 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T2 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T3 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T4 fill:#c2f0c2,stroke:#333,stroke-width:1px
```

## 👨‍💻 Cara Membuat MCP Server (Dengan Contoh)

Server MCP memungkinkan Anda memperluas kemampuan LLM dengan menyediakan data dan fungsi.

Siap mencobanya? Berikut adalah SDK spesifik bahasa dan/atau stack dengan contoh pembuatan server MCP sederhana dalam berbagai bahasa/stack:

- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk

- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk

- **Java SDK**: https://github.com/modelcontextprotocol/java-sdk

- **C#/.NET SDK**: https://github.com/modelcontextprotocol/csharp-sdk


## 🌍 Kasus Penggunaan MCP di Dunia Nyata

MCP memungkinkan berbagai aplikasi dengan memperluas kemampuan AI:

| **Aplikasi**               | **Deskripsi**                                                                |
|----------------------------|--------------------------------------------------------------------------------|
| Integrasi Data Perusahaan  | Menghubungkan LLM ke basis data, CRM, atau alat internal                      |
| Sistem AI Agen             | Memungkinkan agen otonom dengan akses alat dan alur kerja pengambilan keputusan |
| Aplikasi Multi-modal       | Menggabungkan alat teks, gambar, dan audio dalam satu aplikasi AI yang terpadu |
| Integrasi Data Real-time   | Membawa data langsung ke interaksi AI untuk keluaran yang lebih akurat dan terkini |

### 🧠 MCP = Standar Universal untuk Interaksi AI

Model Context Protocol (MCP) bertindak sebagai standar universal untuk interaksi AI, seperti halnya USB-C menstandarkan koneksi fisik untuk perangkat. Dalam dunia AI, MCP menyediakan antarmuka yang konsisten, memungkinkan model (klien) untuk terintegrasi secara mulus dengan alat eksternal dan penyedia data (server). Ini menghilangkan kebutuhan akan protokol khusus yang beragam untuk setiap API atau sumber data.

Di bawah MCP, alat yang kompatibel dengan MCP (disebut sebagai server MCP) mengikuti standar yang seragam. Server ini dapat mencantumkan alat atau tindakan yang mereka tawarkan dan menjalankan tindakan tersebut saat diminta oleh agen AI. Platform agen AI yang mendukung MCP mampu menemukan alat yang tersedia dari server dan memanggilnya melalui protokol standar ini.

### 💡 Memfasilitasi akses ke pengetahuan

Selain menawarkan alat, MCP juga memfasilitasi akses ke pengetahuan. MCP memungkinkan aplikasi untuk memberikan konteks kepada model bahasa besar (LLM) dengan menghubungkannya ke berbagai sumber data. Misalnya, server MCP dapat mewakili repositori dokumen perusahaan, memungkinkan agen untuk mengambil informasi yang relevan sesuai permintaan. Server lain dapat menangani tindakan spesifik seperti mengirim email atau memperbarui catatan. Dari perspektif agen, ini hanyalah alat yang dapat digunakan—beberapa alat mengembalikan data (konteks pengetahuan), sementara yang lain melakukan tindakan. MCP mengelola keduanya secara efisien.

Agen yang terhubung ke server MCP secara otomatis mempelajari kemampuan yang tersedia dan data yang dapat diakses server melalui format standar. Standarisasi ini memungkinkan ketersediaan alat secara dinamis. Misalnya, menambahkan server MCP baru ke sistem agen membuat fungsinya langsung dapat digunakan tanpa memerlukan penyesuaian lebih lanjut pada instruksi agen.

Integrasi yang efisien ini selaras dengan alur yang digambarkan dalam diagram berikut, di mana server menyediakan alat dan pengetahuan, memastikan kolaborasi yang mulus di seluruh sistem.

### 👉 Contoh: Solusi Agen yang Skalabel

```mermaid
---
title: Scalable Agent Solution with MCP
description: A diagram illustrating how a user interacts with an LLM that connects to multiple MCP servers, with each server providing both knowledge and tools, creating a scalable AI system architecture
---
graph TD
    User -->|Prompt| LLM
    LLM -->|Response| User
    LLM -->|MCP| ServerA
    LLM -->|MCP| ServerB
    ServerA -->|Universal connector| ServerB
    ServerA --> KnowledgeA
    ServerA --> ToolsA
    ServerB --> KnowledgeB
    ServerB --> ToolsB

    subgraph Server A
        KnowledgeA[Knowledge]
        ToolsA[Tools]
    end

    subgraph Server B
        KnowledgeB[Knowledge]
        ToolsB[Tools]
    end
```
Universal Connector memungkinkan server MCP berkomunikasi dan berbagi kemampuan satu sama lain, memungkinkan ServerA mendelegasikan tugas ke ServerB atau mengakses alat dan pengetahuannya. Ini menghubungkan alat dan data di seluruh server, mendukung arsitektur agen yang skalabel dan modular. Karena MCP menstandarkan eksposur alat, agen dapat secara dinamis menemukan dan mengarahkan permintaan antar server tanpa integrasi yang dikodekan secara keras.

Federasi alat dan pengetahuan: Alat dan data dapat diakses di seluruh server, memungkinkan arsitektur agen yang lebih skalabel dan modular.

### 🔄 Skenario MCP Lanjutan dengan Integrasi LLM di Sisi Klien

Selain arsitektur MCP dasar, ada skenario lanjutan di mana baik klien maupun server mengandung LLM, memungkinkan interaksi yang lebih canggih. Dalam diagram berikut, **Client App** bisa menjadi IDE dengan sejumlah alat MCP yang tersedia untuk digunakan oleh LLM:

```mermaid
---
title: Advanced MCP Scenarios with Client-Server LLM Integration
description: A sequence diagram showing the detailed interaction flow between user, client application, client LLM, multiple MCP servers, and server LLM, illustrating tool discovery, user interaction, direct tool calling, and feature negotiation phases
---
sequenceDiagram
    autonumber
    actor User as 👤 User
    participant ClientApp as 🖥️ Client App
    participant ClientLLM as 🧠 Client LLM
    participant Server1 as 🔧 MCP Server 1
    participant Server2 as 📚 MCP Server 2
    participant ServerLLM as 🤖 Server LLM
    
    %% Discovery Phase
    rect rgb(220, 240, 255)
        Note over ClientApp, Server2: TOOL DISCOVERY PHASE
        ClientApp->>+Server1: Request available tools/resources
        Server1-->>-ClientApp: Return tool list (JSON)
        ClientApp->>+Server2: Request available tools/resources
        Server2-->>-ClientApp: Return tool list (JSON)
        Note right of ClientApp: Store combined tool<br/>catalog locally
    end
    
    %% User Interaction
    rect rgb(255, 240, 220)
        Note over User, ClientLLM: USER INTERACTION PHASE
        User->>+ClientApp: Enter natural language prompt
        ClientApp->>+ClientLLM: Forward prompt + tool catalog
        ClientLLM->>-ClientLLM: Analyze prompt & select tools
    end
    
    %% Scenario A: Direct Tool Calling
    alt Direct Tool Calling
        rect rgb(220, 255, 220)
            Note over ClientApp, Server1: SCENARIO A: DIRECT TOOL CALLING
            ClientLLM->>+ClientApp: Request tool execution
            ClientApp->>+Server1: Execute specific tool
            Server1-->>-ClientApp: Return results
            ClientApp->>+ClientLLM: Process results
            ClientLLM-->>-ClientApp: Generate response
            ClientApp-->>-User: Display final answer
        end
    
    %% Scenario B: Feature Negotiation (VS Code style)
    else Feature Negotiation (VS Code style)
        rect rgb(255, 220, 220)
            Note over ClientApp, ServerLLM: SCENARIO B: FEATURE NEGOTIATION
            ClientLLM->>+ClientApp: Identify needed capabilities
            ClientApp->>+Server2: Negotiate features/capabilities
            Server2->>+ServerLLM: Request additional context
            ServerLLM-->>-Server2: Provide context
            Server2-->>-ClientApp: Return available features
            ClientApp->>+Server2: Call negotiated tools
            Server2-->>-ClientApp: Return results
            ClientApp->>+ClientLLM: Process results
            ClientLLM-->>-ClientApp: Generate response
            ClientApp-->>-User: Display final answer
        end
    end
```

## 🔐 Manfaat Praktis MCP

Berikut adalah manfaat praktis menggunakan MCP:

- **Keterkinian**: Model dapat mengakses informasi terkini di luar data pelatihannya
- **Ekstensi Kemampuan**: Model dapat memanfaatkan alat khusus untuk tugas yang tidak dilatihnya
- **Mengurangi Halusinasi**: Sumber data eksternal memberikan dasar fakta
- **Privasi**: Data sensitif dapat tetap berada dalam lingkungan yang aman daripada disematkan dalam prompt

## 📌 Poin Penting

Berikut adalah poin penting untuk menggunakan MCP:

- **MCP** menstandarkan cara model AI berinteraksi dengan alat dan data
- Mendorong **ekstensibilitas, konsistensi, dan interoperabilitas**
- MCP membantu **mengurangi waktu pengembangan, meningkatkan keandalan, dan memperluas kemampuan model**
- Arsitektur klien-server **memungkinkan aplikasi AI yang fleksibel dan dapat diperluas**

## 🧠 Latihan

Pikirkan tentang aplikasi AI yang ingin Anda bangun.

- Alat atau data **eksternal** apa yang dapat meningkatkan kemampuannya?
- Bagaimana MCP dapat membuat integrasi **lebih sederhana dan lebih andal?**

## Sumber Daya Tambahan

- [Repositori GitHub MCP](https://github.com/modelcontextprotocol)


## Apa Selanjutnya

Selanjutnya: [Bab 1: Konsep Inti](../01-CoreConcepts/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.