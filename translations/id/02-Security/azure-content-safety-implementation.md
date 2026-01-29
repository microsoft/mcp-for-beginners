# Mengimplementasikan Azure Content Safety dengan MCP

Untuk memperkuat keamanan MCP terhadap prompt injection, tool poisoning, dan kerentanan AI spesifik lainnya, sangat disarankan untuk mengintegrasikan Azure Content Safety.

## Integrasi dengan MCP Server

Untuk mengintegrasikan Azure Content Safety dengan server MCP Anda, tambahkan filter content safety sebagai middleware dalam pipeline pemrosesan permintaan:

1. Inisialisasi filter saat server mulai berjalan  
2. Validasi semua permintaan tool yang masuk sebelum diproses  
3. Periksa semua respons yang keluar sebelum dikembalikan ke klien  
4. Catat dan berikan peringatan pada pelanggaran keamanan  
5. Terapkan penanganan error yang tepat untuk pemeriksaan content safety yang gagal  

Ini memberikan perlindungan yang kuat terhadap:  
- Serangan prompt injection  
- Upaya tool poisoning  
- Eksfiltrasi data melalui input berbahaya  
- Pembuatan konten yang merugikan  

## Praktik Terbaik untuk Integrasi Azure Content Safety

1. **Custom Blocklists**: Buat blocklist khusus yang ditujukan untuk pola injeksi MCP  
2. **Severity Tuning**: Sesuaikan ambang tingkat keparahan berdasarkan kasus penggunaan dan toleransi risiko Anda  
3. **Comprehensive Coverage**: Terapkan pemeriksaan content safety pada semua input dan output  
4. **Performance Optimization**: Pertimbangkan penerapan caching untuk pemeriksaan content safety yang berulang  
5. **Fallback Mechanisms**: Tentukan perilaku fallback yang jelas saat layanan content safety tidak tersedia  
6. **User Feedback**: Berikan umpan balik yang jelas kepada pengguna saat konten diblokir karena alasan keamanan  
7. **Continuous Improvement**: Perbarui blocklist dan pola secara berkala berdasarkan ancaman yang muncul

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.