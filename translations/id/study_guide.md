# Protokol Konteks Model (MCP) untuk Pemula - Panduan Belajar

Panduan belajar ini memberikan gambaran umum tentang struktur dan konten repositori untuk kurikulum "Protokol Konteks Model (MCP) untuk Pemula". Gunakan panduan ini untuk menavigasi repositori dengan efisien dan memanfaatkan sumber daya yang tersedia secara maksimal.

## Gambaran Umum Repositori

Protokol Konteks Model (MCP) adalah kerangka kerja standar untuk interaksi antara model AI dan aplikasi klien. Awalnya dibuat oleh Anthropic, MCP kini dikelola oleh komunitas MCP yang lebih luas melalui organisasi GitHub resmi. Repositori ini menyediakan kurikulum komprehensif dengan contoh kode langsung dalam C#, Java, JavaScript, Python, dan TypeScript, yang dirancang untuk pengembang AI, arsitek sistem, dan insinyur perangkat lunak.

## Peta Kurikulum Visual

```mermaid
mindmap
  root((MCP for Beginners))
    00. Introduction
      ::icon(fa fa-book)
      (Protocol Overview)
      (Standardization Benefits)
      (Real-world Use Cases)
      (AI Integration Fundamentals)
    01. Core Concepts
      ::icon(fa fa-puzzle-piece)
      (Client-Server Architecture)
      (Protocol Components)
      (Messaging Patterns)
      (Transport Mechanisms)
    02. Security
      ::icon(fa fa-shield)
      (AI-Specific Threats)
      (Best Practices 2025)
      (Azure Content Safety)
      (Auth & Authorization)
      (Microsoft Prompt Shields)
    03. Getting Started
      ::icon(fa fa-rocket)
      (First Server Implementation)
      (Client Development)
      (LLM Client Integration)
      (VS Code Extensions)
      (SSE Server Setup)
      (HTTP Streaming)
      (AI Toolkit Integration)
      (Testing Frameworks)
      (Advanced Server Usage)
      (Simple Auth)
      (Deployment Strategies)
    04. Practical Implementation
      ::icon(fa fa-code)
      (Multi-Language SDKs)
      (Testing & Debugging)
      (Prompt Templates)
      (Sample Projects)
      (Production Patterns)
    05. Advanced Topics
      ::icon(fa fa-graduation-cap)
      (Context Engineering)
      (Foundry Agent Integration)
      (Multi-modal AI Workflows)
      (OAuth2 Authentication)
      (Real-time Search)
      (Streaming Protocols)
      (Root Contexts)
      (Routing Strategies)
      (Sampling Techniques)
      (Scaling Solutions)
      (Security Hardening)
      (Entra ID Integration)
      (Web Search MCP)
      
    06. Community
      ::icon(fa fa-users)
      (Code Contributions)
      (Documentation)
      (MCP Client Ecosystem)
      (MCP Server Registry)
      (Image Generation Tools)
      (GitHub Collaboration)
    07. Early Adoption
      ::icon(fa fa-lightbulb)
      (Production Deployments)
      (Microsoft MCP Servers)
      (Azure MCP Service)
      (Enterprise Case Studies)
      (Future Roadmap)
    08. Best Practices
      ::icon(fa fa-check)
      (Performance Optimization)
      (Fault Tolerance)
      (System Resilience)
      (Monitoring & Observability)
    09. Case Studies
      ::icon(fa fa-file-text)
      (Azure API Management)
      (AI Travel Agent)
      (Azure DevOps Integration)
      (Documentation MCP)
      (GitHub MCP Registry)
      (VS Code Integration)
      (Real-world Implementations)
    10. Hands-on Workshop
      ::icon(fa fa-laptop)
      (MCP Server Fundamentals)
      (Advanced Development)
      (AI Toolkit Integration)
      (Production Deployment)
      (4-Lab Structure)
    11. Database Integration Labs
      ::icon(fa fa-database)
      (PostgreSQL Integration)
      (Retail Analytics Use Case)
      (Row Level Security)
      (Semantic Search)
      (Production Deployment)
      (13-Lab Structure)
      (Hands-on Learning)
```

## Struktur Repositori

Repositori ini diorganisasikan ke dalam sebelas bagian utama, masing-masing berfokus pada aspek berbeda dari MCP:

1. **Pendahuluan (00-Introduction/)**
   - Gambaran umum tentang Protokol Konteks Model
   - Mengapa standarisasi penting dalam pipeline AI
   - Kasus penggunaan praktis dan manfaatnya

2. **Konsep Inti (01-CoreConcepts/)**
   - Arsitektur klien-server
   - Komponen utama protokol
   - Pola pesan dalam MCP

3. **Keamanan (02-Security/)**
   - Ancaman keamanan dalam sistem berbasis MCP
   - Praktik terbaik untuk mengamankan implementasi
   - Strategi autentikasi dan otorisasi
   - **Dokumentasi Keamanan Komprehensif**:
     - Praktik Terbaik Keamanan MCP 2025
     - Panduan Implementasi Keamanan Konten Azure
     - Kontrol dan Teknik Keamanan MCP
     - Referensi Cepat Praktik Terbaik MCP
   - **Topik Keamanan Utama**:
     - Serangan injeksi prompt dan peracunan alat
     - Pembajakan sesi dan masalah deputi bingung
     - Kerentanan token passthrough
     - Izin berlebihan dan kontrol akses
     - Keamanan rantai pasokan untuk komponen AI
     - Integrasi Microsoft Prompt Shields

4. **Memulai (03-GettingStarted/)**
   - Pengaturan dan konfigurasi lingkungan
   - Membuat server dan klien MCP dasar
   - Integrasi dengan aplikasi yang ada
   - Termasuk bagian untuk:
     - Implementasi server pertama
     - Pengembangan klien
     - Integrasi klien LLM
     - Integrasi VS Code
     - Server Server-Sent Events (SSE)
     - Penggunaan server tingkat lanjut
     - Streaming HTTP
     - Integrasi AI Toolkit
     - Strategi pengujian
     - Panduan penerapan

5. **Implementasi Praktis (04-PracticalImplementation/)**
   - Menggunakan SDK di berbagai bahasa pemrograman
   - Teknik debugging, pengujian, dan validasi
   - Membuat template prompt dan alur kerja yang dapat digunakan kembali
   - Proyek contoh dengan contoh implementasi

6. **Topik Lanjutan (05-AdvancedTopics/)**
   - Teknik rekayasa konteks
   - Integrasi agen Foundry
   - Alur kerja AI multi-modal
   - Demo autentikasi OAuth2
   - Kemampuan pencarian real-time
   - Streaming real-time
   - Implementasi konteks root
   - Strategi routing
   - Teknik sampling
   - Pendekatan skalabilitas
   - Pertimbangan keamanan
   - Integrasi keamanan Entra ID
   - Integrasi pencarian web

7. **Kontribusi Komunitas (06-CommunityContributions/)**
   - Cara berkontribusi kode dan dokumentasi
   - Kolaborasi melalui GitHub
   - Peningkatan dan umpan balik yang didorong oleh komunitas
   - Menggunakan berbagai klien MCP (Claude Desktop, Cline, VSCode)
   - Bekerja dengan server MCP populer termasuk generasi gambar

8. **Pelajaran dari Adopsi Awal (07-LessonsfromEarlyAdoption/)**
   - Implementasi dunia nyata dan kisah sukses
   - Membangun dan menerapkan solusi berbasis MCP
   - Tren dan peta jalan masa depan
   - **Panduan Server MCP Microsoft**: Panduan komprehensif untuk 10 server MCP Microsoft siap produksi termasuk:
     - Server MCP Microsoft Learn Docs
     - Server MCP Azure (15+ konektor khusus)
     - Server MCP GitHub
     - Server MCP Azure DevOps
     - Server MCP MarkItDown
     - Server MCP SQL Server
     - Server MCP Playwright
     - Server MCP Dev Box
     - Server MCP Azure AI Foundry
     - Server MCP Microsoft 365 Agents Toolkit

9. **Praktik Terbaik (08-BestPractices/)**
   - Penyempurnaan dan optimasi kinerja
   - Merancang sistem MCP yang tahan terhadap kegagalan
   - Strategi pengujian dan ketahanan

10. **Studi Kasus (09-CaseStudy/)**
    - **Tujuh studi kasus komprehensif** yang menunjukkan fleksibilitas MCP dalam berbagai skenario:
    - **Azure AI Travel Agents**: Orkestrasi multi-agen dengan Azure OpenAI dan AI Search
    - **Integrasi Azure DevOps**: Mengotomatisasi proses alur kerja dengan pembaruan data YouTube
    - **Pengambilan Dokumentasi Real-Time**: Klien konsol Python dengan streaming HTTP
    - **Generator Rencana Studi Interaktif**: Aplikasi web Chainlit dengan AI percakapan
    - **Dokumentasi Dalam Editor**: Integrasi VS Code dengan alur kerja GitHub Copilot
    - **Manajemen API Azure**: Integrasi API perusahaan dengan pembuatan server MCP
    - **Registri MCP GitHub**: Pengembangan ekosistem dan platform integrasi agen
    - Contoh implementasi mencakup integrasi perusahaan, produktivitas pengembang, dan pengembangan ekosistem

11. **Lokakarya Praktis (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - Lokakarya praktis komprehensif yang menggabungkan MCP dengan AI Toolkit
    - Membangun aplikasi cerdas yang menjembatani model AI dengan alat dunia nyata
    - Modul praktis yang mencakup dasar-dasar, pengembangan server khusus, dan strategi penerapan produksi
    - **Struktur Lab**:
      - Lab 1: Dasar-Dasar Server MCP
      - Lab 2: Pengembangan Server MCP Lanjutan
      - Lab 3: Integrasi AI Toolkit
      - Lab 4: Penerapan dan Skalabilitas Produksi
    - Pendekatan pembelajaran berbasis lab dengan instruksi langkah demi langkah

12. **Lab Integrasi Database Server MCP (11-MCPServerHandsOnLabs/)**
    - **Jalur pembelajaran 13-lab komprehensif** untuk membangun server MCP siap produksi dengan integrasi PostgreSQL
    - **Implementasi analitik ritel dunia nyata** menggunakan kasus penggunaan Zava Retail
    - **Pola tingkat perusahaan** termasuk Keamanan Tingkat Baris (RLS), pencarian semantik, dan akses data multi-tenant
    - **Struktur Lab Lengkap**:
      - **Lab 00-03: Dasar-Dasar** - Pendahuluan, Arsitektur, Keamanan, Pengaturan Lingkungan
      - **Lab 04-06: Membangun Server MCP** - Desain Database, Implementasi Server MCP, Pengembangan Alat
      - **Lab 07-09: Fitur Lanjutan** - Pencarian Semantik, Pengujian & Debugging, Integrasi VS Code
      - **Lab 10-12: Produksi & Praktik Terbaik** - Penerapan, Pemantauan, Optimasi
    - **Teknologi yang Dibahas**: Kerangka kerja FastMCP, PostgreSQL, Azure OpenAI, Azure Container Apps, Application Insights
    - **Hasil Pembelajaran**: Server MCP siap produksi, pola integrasi database, analitik bertenaga AI, keamanan tingkat perusahaan

## Sumber Daya Tambahan

Repositori ini mencakup sumber daya pendukung:

- **Folder gambar**: Berisi diagram dan ilustrasi yang digunakan di seluruh kurikulum
- **Terjemahan**: Dukungan multi-bahasa dengan terjemahan dokumentasi otomatis
- **Sumber Daya Resmi MCP**:
  - [Dokumentasi MCP](https://modelcontextprotocol.io/)
  - [Spesifikasi MCP](https://spec.modelcontextprotocol.io/)
  - [Repositori GitHub MCP](https://github.com/modelcontextprotocol)

## Cara Menggunakan Repositori Ini

1. **Pembelajaran Berurutan**: Ikuti bab-bab secara berurutan (00 hingga 11) untuk pengalaman belajar yang terstruktur.
2. **Fokus Bahasa Spesifik**: Jika Anda tertarik pada bahasa pemrograman tertentu, jelajahi direktori sampel untuk implementasi dalam bahasa pilihan Anda.
3. **Implementasi Praktis**: Mulailah dengan bagian "Memulai" untuk mengatur lingkungan Anda dan membuat server dan klien MCP pertama Anda.
4. **Eksplorasi Lanjutan**: Setelah merasa nyaman dengan dasar-dasarnya, selami topik lanjutan untuk memperluas pengetahuan Anda.
5. **Keterlibatan Komunitas**: Bergabunglah dengan komunitas MCP melalui diskusi GitHub dan saluran Discord untuk terhubung dengan para ahli dan pengembang lainnya.

## Klien dan Alat MCP

Kurikulum ini mencakup berbagai klien dan alat MCP:

1. **Klien Resmi**:
   - Visual Studio Code 
   - MCP di Visual Studio Code
   - Claude Desktop
   - Claude di VSCode 
   - Claude API

2. **Klien Komunitas**:
   - Cline (berbasis terminal)
   - Cursor (editor kode)
   - ChatMCP
   - Windsurf

3. **Alat Manajemen MCP**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## Server MCP Populer

Repositori ini memperkenalkan berbagai server MCP, termasuk:

1. **Server MCP Microsoft Resmi**:
   - Server MCP Microsoft Learn Docs
   - Server MCP Azure (15+ konektor khusus)
   - Server MCP GitHub
   - Server MCP Azure DevOps
   - Server MCP MarkItDown
   - Server MCP SQL Server
   - Server MCP Playwright
   - Server MCP Dev Box
   - Server MCP Azure AI Foundry
   - Server MCP Microsoft 365 Agents Toolkit

2. **Server Referensi Resmi**:
   - Filesystem
   - Fetch
   - Memory
   - Sequential Thinking

3. **Generasi Gambar**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **Alat Pengembangan**:
   - Git MCP
   - Terminal Control
   - Code Assistant

5. **Server Khusus**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## Kontribusi

Repositori ini menyambut kontribusi dari komunitas. Lihat bagian Kontribusi Komunitas untuk panduan tentang cara berkontribusi secara efektif ke ekosistem MCP.

----

*Panduan belajar ini diperbarui pada 6 Oktober 2025, dan memberikan gambaran umum tentang repositori hingga tanggal tersebut. Konten repositori dapat diperbarui setelah tanggal ini.*

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.