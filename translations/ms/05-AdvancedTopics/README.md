# Topik Lanjutan dalam MCP

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/ms/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Klik gambar di atas untuk menonton video pelajaran ini)_

Bab ini merangkumi siri topik lanjutan dalam pelaksanaan Model Context Protocol (MCP), termasuk integrasi multi-modal, skala, amalan terbaik keselamatan, dan integrasi perusahaan. Topik-topik ini penting untuk membina aplikasi MCP yang kukuh dan sedia untuk pengeluaran yang dapat memenuhi keperluan sistem AI moden.

## Gambaran Keseluruhan

Pelajaran ini meneroka konsep lanjutan dalam pelaksanaan Model Context Protocol, menumpukan pada integrasi multi-modal, skala, amalan terbaik keselamatan, dan integrasi perusahaan. Topik-topik ini penting untuk membina aplikasi MCP bertaraf pengeluaran yang boleh menangani keperluan kompleks dalam persekitaran perusahaan.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Melaksanakan kemampuan multi-modal dalam kerangka MCP
- Mereka bentuk seni bina MCP yang boleh diskalakan untuk senario permintaan tinggi
- Memohon amalan terbaik keselamatan yang selaras dengan prinsip keselamatan MCP
- Mengintegrasikan MCP dengan sistem dan kerangka AI perusahaan
- Mengoptimumkan prestasi dan kebolehpercayaan dalam persekitaran pengeluaran

## Pelajaran dan Projek Contoh

| Pautan | Tajuk | Penerangan |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Integrasi dengan Azure | Pelajari cara mengintegrasikan Server MCP anda di Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | Contoh Multi modal MCP | Contoh untuk audio, imej dan tindak balas multi modal |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | Demo MCP OAuth2 | Aplikasi Spring Boot minimal yang menunjukkan OAuth2 dengan MCP, kedua-duanya sebagai Authorization dan Resource Server. Memperagakan pengeluaran token yang selamat, titik akhir terlindung, penyebaran Azure Container Apps, dan integrasi Pengurusan API. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Konteks Root | Pelajari lebih lanjut mengenai konteks root dan cara melaksanakannya |
| [5.5 Routing](./mcp-routing/README.md) | Routing | Pelajari jenis routing yang berbeza |
| [5.6 Sampling](./mcp-sampling/README.md) | Sampling | Pelajari cara bekerja dengan sampling |
| [5.7 Scaling](./mcp-scaling/README.md) | Skala | Pelajari mengenai skala |
| [5.8 Security](./mcp-security/README.md) | Keselamatan | Lindungi Server MCP anda |
| [5.9 Web Search sample](./web-search-mcp/README.md) | MCP Carian Web | Server dan klien MCP Python yang mengintegrasikan dengan SerpAPI untuk carian web masa nyata, berita, produk, dan soal jawab. Memperagakan orkestrasi pelbagai alat, integrasi API luaran, dan pengendalian ralat yang kukuh. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Penstriman | Penstriman data masa nyata telah menjadi penting dalam dunia berasaskan data hari ini, di mana perniagaan dan aplikasi memerlukan akses segera kepada maklumat untuk membuat keputusan tepat pada masanya.|
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Carian Web | Carian web masa nyata bagaimana MCP mengubah carian web masa nyata dengan menyediakan pendekatan standard kepada pengurusan konteks merentas model AI, enjin carian, dan aplikasi.| 
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Pengesahan Entra ID | Microsoft Entra ID menyediakan penyelesaian pengurusan identiti dan akses berasaskan awan yang mantap, membantu memastikan hanya pengguna dan aplikasi yang dibenarkan boleh berinteraksi dengan server MCP anda.|
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Integrasi Azure AI Foundry | Pelajari cara mengintegrasikan server Model Context Protocol dengan agen Azure AI Foundry, membolehkan orkestrasi alat yang berkuasa dan keupayaan AI perusahaan dengan sambungan sumber data luaran yang standard.|
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Kejuruteraan Konteks | Peluang masa depan teknik kejuruteraan konteks untuk server MCP, termasuk pengoptimuman konteks, pengurusan konteks dinamik, dan strategi kejuruteraan arahan yang berkesan dalam kerangka MCP.|
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Pengangkutan Tersuai | Pelajari cara melaksanakan mekanisme pengangkutan tersuai untuk senario komunikasi MCP yang khusus.|
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Ciri-ciri Protokol | Kuasai ciri protokol lanjutan termasuk notifikasi kemajuan, pembatalan permintaan, templat sumber, dan corak pengendalian ralat.|
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Ejen Adversarial | Gunakan dua ejen dengan posisi bertentangan, berkongsi satu set alat MCP untuk mengesan halusinasi, membangkitkan kes tepi, dan menghasilkan output yang lebih baik melalui perdebatan tersusun.|

> **Baru dalam Spesifikasi MCP 2025-11-25**: Spesifikasi kini termasuk sokongan eksperimen untuk **Tugas** (operasi jangka panjang dengan penjejakan kemajuan), **Anotasi Alat** (metadata tentang tingkah laku alat untuk keselamatan), **URL Mode Elicitation** (meminta kandungan URL tertentu dari klien), dan **Roots** yang dipertingkatkan (untuk pengurusan konteks ruang kerja). Lihat [log perubahan Spesifikasi MCP](https://spec.modelcontextprotocol.io/) untuk butiran penuh.

## Rujukan Tambahan

Untuk maklumat terkini mengenai topik MCP lanjutan, rujuk:
- [Dokumentasi MCP](https://modelcontextprotocol.io/)
- [Spesifikasi MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Repositori GitHub](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Risiko keselamatan dan mitigasi
- [Bengkel Sidang Kemuncak Keselamatan MCP (Sherpa)](https://azure-samples.github.io/sherpa/) - Latihan keselamatan secara praktikal

## Perkara Penting

- Pelaksanaan MCP multi-modal meluaskan keupayaan AI melebihi pemprosesan teks
- Skala adalah penting untuk penyebaran perusahaan dan boleh ditangani melalui skala mendatar dan menegak
- Langkah keselamatan menyeluruh melindungi data dan memastikan kawalan akses yang betul
- Integrasi perusahaan dengan platform seperti Azure OpenAI dan Microsoft AI Foundry meningkatkan keupayaan MCP
- Pelaksanaan MCP lanjutan mendapat manfaat daripada seni bina yang dioptimumkan dan pengurusan sumber yang berhati-hati

## Latihan

Reka pelaksanaan MCP bertaraf perusahaan untuk kes penggunaan tertentu:

1. Kenal pasti keperluan multi-modal untuk kes penggunaan anda
2. Gariskan kawalan keselamatan yang diperlukan untuk melindungi data sensitif
3. Reka seni bina skala yang boleh mengendalikan beban pelbagai
4. Rancang titik integrasi dengan sistem AI perusahaan
5. Dokumentasikan potensi kesesakan prestasi dan strategi mitigasi

## Sumber Tambahan

- [Dokumentasi Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Dokumentasi Microsoft AI Foundry](https://learn.microsoft.com/en-us/ai-services/)

---

## Apa seterusnya

Terokai pelajaran dalam modul ini bermula dengan: [5.1 Integrasi MCP](./mcp-integration/README.md)

Setelah anda menyiapkan modul ini, teruskan ke: [Modul 6: Sumbangan Komuniti](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat kritikal, terjemahan oleh manusia profesional digalakkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->