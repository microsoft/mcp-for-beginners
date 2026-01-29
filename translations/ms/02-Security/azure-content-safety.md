# Keselamatan MCP Lanjutan dengan Azure Content Safety

Azure Content Safety menyediakan beberapa alat yang berkuasa untuk meningkatkan keselamatan pelaksanaan MCP anda:

## Prompt Shields

AI Prompt Shields Microsoft memberikan perlindungan kukuh terhadap serangan suntikan prompt secara langsung dan tidak langsung melalui:

1. **Pengesanan Lanjutan**: Menggunakan pembelajaran mesin untuk mengenal pasti arahan berniat jahat yang diselitkan dalam kandungan.
2. **Penyorotan**: Mengubah teks input untuk membantu sistem AI membezakan antara arahan sah dan input luaran.
3. **Pembatas dan Penandaan Data**: Menandakan sempadan antara data yang dipercayai dan tidak dipercayai.
4. **Integrasi Content Safety**: Bekerjasama dengan Azure AI Content Safety untuk mengesan cubaan jailbreak dan kandungan berbahaya.
5. **Kemas Kini Berterusan**: Microsoft sentiasa mengemas kini mekanisme perlindungan terhadap ancaman baru.

## Melaksanakan Azure Content Safety dengan MCP

Pendekatan ini menyediakan perlindungan berlapis-lapis:
- Mengimbas input sebelum pemprosesan
- Mengesahkan output sebelum dipulangkan
- Menggunakan senarai blok untuk corak berbahaya yang diketahui
- Memanfaatkan model keselamatan kandungan Azure yang sentiasa dikemas kini

## Sumber Azure Content Safety

Untuk mengetahui lebih lanjut tentang pelaksanaan Azure Content Safety dengan pelayan MCP anda, rujuk sumber rasmi berikut:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Dokumentasi rasmi untuk Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Pelajari cara mencegah serangan suntikan prompt.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Rujukan API terperinci untuk melaksanakan Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Panduan pelaksanaan cepat menggunakan C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Perpustakaan klien untuk pelbagai bahasa pengaturcaraan.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Panduan khusus untuk mengesan dan mencegah cubaan jailbreak.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Amalan terbaik untuk melaksanakan keselamatan kandungan dengan berkesan.

Untuk pelaksanaan yang lebih mendalam, lihat [panduan Pelaksanaan Azure Content Safety](./azure-content-safety-implementation.md) kami.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.