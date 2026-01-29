# Penyelesaian Pelayan MCP stdio

> **⚠️ Penting**: Penyelesaian ini telah dikemas kini untuk menggunakan **pengangkutan stdio** seperti yang disyorkan oleh Spesifikasi MCP 2025-06-18. Pengangkutan SSE (Server-Sent Events) asal telah dihentikan.

Berikut adalah penyelesaian lengkap untuk membina pelayan MCP menggunakan pengangkutan stdio dalam setiap runtime:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Pelaksanaan pelayan stdio lengkap
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Pelayan stdio Python dengan asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - Pelayan stdio .NET dengan suntikan kebergantungan

Setiap penyelesaian menunjukkan:
- Menyediakan pengangkutan stdio
- Mendefinisikan alat pelayan
- Pengendalian mesej JSON-RPC yang betul
- Integrasi dengan klien MCP seperti Claude

Semua penyelesaian mematuhi spesifikasi MCP semasa dan menggunakan pengangkutan stdio yang disyorkan untuk prestasi dan keselamatan yang optimum.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.