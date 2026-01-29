# Keamanan MCP Lanjutan dengan Azure Content Safety

Azure Content Safety menyediakan beberapa alat kuat yang dapat meningkatkan keamanan implementasi MCP Anda:

## Prompt Shields

AI Prompt Shields dari Microsoft memberikan perlindungan kuat terhadap serangan injeksi prompt baik secara langsung maupun tidak langsung melalui:

1. **Deteksi Lanjutan**: Menggunakan machine learning untuk mengidentifikasi instruksi berbahaya yang tersembunyi dalam konten.
2. **Spotlighting**: Mengubah teks input agar sistem AI dapat membedakan antara instruksi yang valid dan input eksternal.
3. **Delimiters dan Datamarking**: Menandai batas antara data yang dipercaya dan yang tidak dipercaya.
4. **Integrasi Content Safety**: Bekerja sama dengan Azure AI Content Safety untuk mendeteksi upaya jailbreak dan konten berbahaya.
5. **Pembaruan Berkelanjutan**: Microsoft secara rutin memperbarui mekanisme perlindungan terhadap ancaman yang muncul.

## Mengimplementasikan Azure Content Safety dengan MCP

Pendekatan ini memberikan perlindungan berlapis:
- Memindai input sebelum diproses
- Memvalidasi output sebelum dikembalikan
- Menggunakan blocklist untuk pola berbahaya yang sudah dikenal
- Memanfaatkan model content safety Azure yang terus diperbarui

## Sumber Daya Azure Content Safety

Untuk mempelajari lebih lanjut tentang implementasi Azure Content Safety dengan server MCP Anda, lihat sumber resmi berikut:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Dokumentasi resmi untuk Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Pelajari cara mencegah serangan injeksi prompt.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Referensi API terperinci untuk mengimplementasikan Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Panduan cepat implementasi menggunakan C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Perpustakaan klien untuk berbagai bahasa pemrograman.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Panduan khusus untuk mendeteksi dan mencegah upaya jailbreak.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Praktik terbaik untuk mengimplementasikan content safety secara efektif.

Untuk implementasi yang lebih mendalam, lihat [panduan Implementasi Azure Content Safety](./azure-content-safety-implementation.md) kami.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.