# Solusi Server MCP stdio

> **⚠️ Penting**: Solusi ini telah diperbarui untuk menggunakan **transport stdio** sesuai rekomendasi Spesifikasi MCP 2025-06-18. Transport SSE (Server-Sent Events) yang lama telah dihentikan penggunaannya.

Berikut adalah solusi lengkap untuk membangun server MCP menggunakan transport stdio di setiap runtime:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Implementasi server stdio lengkap
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Server stdio Python dengan asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - Server stdio .NET dengan dependency injection

Setiap solusi mencakup:
- Pengaturan transport stdio
- Mendefinisikan alat server
- Penanganan pesan JSON-RPC yang benar
- Integrasi dengan klien MCP seperti Claude

Semua solusi mengikuti spesifikasi MCP terkini dan menggunakan transport stdio yang direkomendasikan untuk kinerja dan keamanan yang optimal.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.