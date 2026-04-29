# Topik Lanjutan dalam MCP

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/id/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Klik gambar di atas untuk menonton video pelajaran ini)_

Bab ini membahas serangkaian topik lanjutan dalam implementasi Model Context Protocol (MCP), termasuk integrasi multi-modal, skalabilitas, praktik terbaik keamanan, dan integrasi perusahaan. Topik-topik ini penting untuk membangun aplikasi MCP yang kuat dan siap produksi yang dapat memenuhi tuntutan sistem AI modern.

## Ikhtisar

Pelajaran ini mengeksplorasi konsep lanjutan dalam implementasi Model Context Protocol, dengan fokus pada integrasi multi-modal, skalabilitas, praktik terbaik keamanan, dan integrasi perusahaan. Topik-topik ini penting untuk membangun aplikasi MCP kelas produksi yang dapat menangani kebutuhan kompleks di lingkungan perusahaan.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Menerapkan kemampuan multi-modal dalam kerangka kerja MCP
- Merancang arsitektur MCP yang skalabel untuk situasi permintaan tinggi
- Menerapkan praktik terbaik keamanan sesuai dengan prinsip keamanan MCP
- Mengintegrasikan MCP dengan sistem dan kerangka kerja AI perusahaan
- Mengoptimalkan kinerja dan keandalan di lingkungan produksi

## Pelajaran dan Proyek Contoh

| Link | Judul | Deskripsi |
|------|-------|-----------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Integrasi dengan Azure | Pelajari cara mengintegrasikan Server MCP Anda di Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | Contoh Multi modal MCP | Contoh untuk respons audio, gambar, dan multi modal |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | Demo MCP OAuth2 | Aplikasi Spring Boot minimal yang menunjukkan OAuth2 dengan MCP, baik sebagai Authorization maupun Resource Server. Menampilkan penerbitan token yang aman, endpoint terlindungi, deployment Azure Container Apps, dan integrasi API Management. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Root contexts | Pelajari lebih lanjut tentang root context dan cara mengimplementasikannya |
| [5.5 Routing](./mcp-routing/README.md) | Routing | Pelajari berbagai jenis routing |
| [5.6 Sampling](./mcp-sampling/README.md) | Sampling | Pelajari cara bekerja dengan sampling |
| [5.7 Scaling](./mcp-scaling/README.md) | Scaling | Pelajari tentang scaling |
| [5.8 Security](./mcp-security/README.md) | Security | Amankan Server MCP Anda |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Web Search MCP | Server dan klien Python MCP yang mengintegrasikan dengan SerpAPI untuk pencarian web, berita, produk, dan Q&A secara real-time. Menampilkan orkestrasi multi-alat, integrasi API eksternal, dan penanganan kesalahan yang tangguh. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming | Streaming data real-time telah menjadi esensial di dunia yang digerakkan data saat ini, di mana bisnis dan aplikasi memerlukan akses informasi segera untuk membuat keputusan tepat waktu. |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Web Search | Pencarian web real-time bagaimana MCP mengubah pencarian web real-time dengan menyediakan pendekatan standar untuk manajemen konteks di antara model AI, mesin pencari, dan aplikasi. |
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Autentikasi Entra ID | Microsoft Entra ID menyediakan solusi manajemen identitas dan akses berbasis cloud yang tangguh, membantu memastikan hanya pengguna dan aplikasi yang berwenang yang dapat berinteraksi dengan server MCP Anda. |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Integrasi Azure AI Foundry | Pelajari cara mengintegrasikan server Model Context Protocol dengan agen Azure AI Foundry, memungkinkan orkestrasi alat yang kuat dan kemampuan AI perusahaan dengan koneksi standar ke sumber data eksternal. |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Context Engineering | Peluang masa depan teknik rekayasa konteks untuk server MCP, termasuk optimasi konteks, manajemen konteks dinamis, dan strategi rekayasa prompt yang efektif dalam kerangka MCP. |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Custom Transport | Pelajari cara mengimplementasikan mekanisme transportasi khusus untuk skenario komunikasi MCP yang spesial. |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Fitur Protokol | Kuasai fitur protokol lanjutan termasuk notifikasi kemajuan, pembatalan permintaan, template sumber daya, dan pola penanganan kesalahan. |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Agen Adversarial | Gunakan dua agen dengan posisi berlawanan, berbagi satu set alat MCP, untuk menangkap halusinasi, menampilkan kasus tepi, dan menghasilkan output yang lebih terkalibrasi melalui debat terstruktur. |

> **Baru dalam Spesifikasi MCP 2025-11-25**: Spesifikasi kini mencakup dukungan eksperimental untuk **Tasks** (operasi jangka panjang dengan pelacakan kemajuan), **Anotasi Alat** (metadata tentang perilaku alat untuk keamanan), **URL Mode Elicitation** (meminta konten URL spesifik dari klien), dan **Roots** yang ditingkatkan (untuk manajemen konteks workspace). Lihat [changelog Spesifikasi MCP](https://spec.modelcontextprotocol.io/) untuk detail lengkap.

## Referensi Tambahan

Untuk informasi terbaru tentang topik lanjutan MCP, lihat:
- [Dokumentasi MCP](https://modelcontextprotocol.io/)
- [Spesifikasi MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Repositori GitHub](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Risiko keamanan dan mitigasinya
- [Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Pelatihan keamanan praktis

## Poin Penting

- Implementasi MCP multi-modal memperluas kemampuan AI di luar pemrosesan teks
- Skalabilitas esensial untuk penerapan di perusahaan dan dapat diatasi melalui scaling horizontal dan vertikal
- Langkah keamanan komprehensif melindungi data dan menjamin kontrol akses yang tepat
- Integrasi perusahaan dengan platform seperti Azure OpenAI dan Microsoft AI Foundry meningkatkan kemampuan MCP
- Implementasi MCP lanjutan mendapat manfaat dari arsitektur yang dioptimalkan dan manajemen sumber daya yang cermat

## Latihan

Rancang implementasi MCP kelas perusahaan untuk kasus penggunaan tertentu:

1. Identifikasi kebutuhan multi-modal untuk kasus penggunaan Anda
2. Rancang kontrol keamanan yang diperlukan untuk melindungi data sensitif
3. Rancang arsitektur yang skalabel yang dapat menangani beban bervariasi
4. Rencanakan titik integrasi dengan sistem AI perusahaan
5. Dokumentasikan potensi hambatan kinerja dan strategi mitigasi

## Sumber Daya Tambahan

- [Dokumentasi Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Dokumentasi Microsoft AI Foundry](https://learn.microsoft.com/en-us/ai-services/)

---

## Selanjutnya

Jelajahi pelajaran dalam modul ini mulai dari: [5.1 MCP Integration](./mcp-integration/README.md)

Setelah menyelesaikan modul ini, lanjutkan ke: [Modul 6: Kontribusi Komunitas](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidaktepatan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->