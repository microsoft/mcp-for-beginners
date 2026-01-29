# Melaksanakan Azure Content Safety dengan MCP

Untuk mengukuhkan keselamatan MCP daripada suntikan arahan, pencemaran alat, dan kerentanan khusus AI lain, integrasi Azure Content Safety sangat disyorkan.

## Integrasi dengan Pelayan MCP

Untuk mengintegrasikan Azure Content Safety dengan pelayan MCP anda, tambahkan penapis keselamatan kandungan sebagai middleware dalam saluran pemprosesan permintaan anda:

1. Inisialisasi penapis semasa pelancaran pelayan  
2. Sahkan semua permintaan alat yang masuk sebelum diproses  
3. Periksa semua respons yang keluar sebelum dihantar kembali kepada klien  
4. Log dan beri amaran mengenai pelanggaran keselamatan  
5. Laksanakan pengendalian ralat yang sesuai untuk pemeriksaan keselamatan kandungan yang gagal  

Ini menyediakan pertahanan kukuh terhadap:  
- Serangan suntikan arahan  
- Cubaan pencemaran alat  
- Eksfiltrasi data melalui input berniat jahat  
- Penjanaan kandungan berbahaya  

## Amalan Terbaik untuk Integrasi Azure Content Safety

1. **Senarai Blok Tersuai**: Cipta senarai blok tersuai khusus untuk corak suntikan MCP  
2. **Penalaan Tahap Keseriusan**: Laraskan ambang keseriusan berdasarkan kes penggunaan dan toleransi risiko anda  
3. **Liputan Menyeluruh**: Terapkan pemeriksaan keselamatan kandungan pada semua input dan output  
4. **Pengoptimuman Prestasi**: Pertimbangkan pelaksanaan caching untuk pemeriksaan keselamatan kandungan yang berulang  
5. **Mekanisme Sandaran**: Tetapkan tingkah laku sandaran yang jelas apabila perkhidmatan keselamatan kandungan tidak tersedia  
6. **Maklum Balas Pengguna**: Berikan maklum balas yang jelas kepada pengguna apabila kandungan disekat kerana kebimbangan keselamatan  
7. **Penambahbaikan Berterusan**: Kemas kini secara berkala senarai blok dan corak berdasarkan ancaman yang muncul

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.